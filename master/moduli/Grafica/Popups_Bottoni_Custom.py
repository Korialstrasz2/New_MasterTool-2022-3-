import ast
import json
import os

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain
from Moduli.Logica import EquipAttore, Salvataggio
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def find_most_recent_file(path1, path2):
    # Check if the first file exists
    if not os.path.exists(path1):
        if os.path.exists(path2):
            return path2
        else:
            return "inesistenti"
    # Check if the second file exists
    if not os.path.exists(path2):
        return path1

    # Get the last modified timestamps of the files
    path1_modified = os.path.getmtime(path1)
    path2_modified = os.path.getmtime(path2)

    # Compare the timestamps to determine the most recent file
    if path1_modified > path2_modified:
        return path1
    else:
        return path2


def apri(*args):
    nome_pg = Shared.pg_selezionato["nome_in_uso"]
    pathcompleto_shared = Shared.path_cartella_shared + f"/{nome_pg}/bottoni/{nome_pg}bottoni.json"
    pathcompleto_dati = Shared.path_PG_e_Unici + f"/bottoni/{nome_pg}bottoni.json"
    recente = find_most_recent_file(pathcompleto_shared, pathcompleto_dati)
    if recente != "inesistenti":
        with open(recente, "r") as json_file:
            dati = ast.literal_eval(json_file.read())
    else:
        dati = Salvataggio.crea_bottoni_base()

    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=None, height=400)
    scroller = ScrollView(size_hint=(1, None), size=(400, 400), effect_cls="ScrollEffect")
    popup = Popup(title="EFFETTI", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 500),
                  auto_dismiss=True)

    def apribottone(*args, numero, dati):
        layout_effetto = BoxLayout(orientation='vertical', spacing=2, size_hint=(1, 1))
        layout_popup = BoxLayout(orientation='vertical', spacing=2, size_hint=(1, 1))
        layout_campi = BoxLayout(orientation='vertical', spacing=2, size_hint=(1, 1))
        layout_link = BoxLayout(orientation='vertical', spacing=2, size_hint=(1, 1))
        big_box_effetti = GridLayout(cols=1, spacing=0, size_hint=(1, 0.5), pos_hint={"x": 0, "y": 0.43})
        big_box_popup = GridLayout(cols=1, spacing=0, size_hint=(1, 0.13), pos_hint={"x": 0, "y": 0.27})
        big_box_campi = GridLayout(cols=1, spacing=0, size_hint=(1, 0.15), pos_hint={"x": 0, "y": 0.15})
        big_box_link = GridLayout(cols=1, spacing=0, size_hint=(1, 0.115), pos_hint={"x": 0, "y": 0.035})
        master_layout = FloatLayout()
        nome_bottone = "bottone_" + str(numero)
        dati_locali = dati[nome_bottone]





        popup = Popup(title=f"Bottone {numero}", title_size=(30),
                      title_align='center', content=master_layout,
                      size_hint=(None, None), size=(800, 930),
                      auto_dismiss=True)
        ############ Inizio effetto ###################
        titolo_bottone = TextInput(text = dati_locali['nome'],size_hint=(1, 0.035), pos_hint={"x": 0, "y": 0.93})
        master_layout.add_widget(Label(text = "POPUP" ,size_hint=(1, 0.035), pos_hint={"x": 0, "y": 0.4}))
        master_layout.add_widget(Label(text = "NOME BOTTONE" ,size_hint=(1, 0.035), pos_hint={"x": 0, "y": 0.965}))
        master_layout.add_widget(titolo_bottone)
        master_layout.add_widget(big_box_effetti)
        master_layout.add_widget(big_box_popup)
        master_layout.add_widget(big_box_campi)
        master_layout.add_widget(big_box_link)
        Shared.flag_aggiungi_popup_effetti = False

        def popup_extra(*args, tipo = "malattie"):
            widget_list = list(big_box_effetti.children)
            nonlocal inserisci_codice
            nonlocal inserisci_codice_descrizione
            nonlocal popup
            if len(widget_list) == 1:
                lvpg = Shared.pg_selezionato['livello']
                big_box_effetti.cols = 2
                box_extra = GridLayout(padding=5, cols=5)
                lista_malattie = {
                    "M-Atassia": ["","Non fai frasi di senso compiuto."],
                    "M-Brividi": ["","15% di fallire azioni."],
                    "M-Vermi Infetti": ["","1 stanchezza ogni 12 ore."],
                    "M-Artic. di\nRoccia": ["","-1 mod. gen."],
                    "M-Artic. \nInfernali": ["","-2 mod. gen."],
                    "M-Demenza": ["","Ogni turno, se fallisci tiro conc. 5, non fai azione."],
                    "M-Febbre \nPesante": ["","raddoppia il costo in energia."],
                    "M-Sfuggimente":
                        ["Shared.pg_selezionato['intelligenza_bonus_extra'] -= 4$$Shared.pg_selezionato["
                         "'concentrazione_bonus_extra'] -= 4","-4 int e conc."],
                    "M-Tick Giallo": ["","-1 a tutte le abilità."],
                    "M-Spasmi": ["","-1 a tutti i tiri."],
                    "S-Scosso": ["Shared.pg_selezionato['attacco_extra'] -= 3","-3 atk 10 % sbagliare cast"],
                    "S-Impaurito": ["Shared.pg_selezionato['attacco_extra'] -= 6$$Shared.pg_selezionato['difesa_extra'] "
                                    "+= 2","+2 def -6 atk, 20% sbagliare cast"],
                    "S-Sanguinante": ["","-1pf/t. per 5t minimo 0pf"],
                    "S-Abbagliato/\nPenombra": ["","puoi attaccare solo entro 1m, oltre, -20% miss a casella."],
                    "S-Nauseato": ["","spendi il doppio di en."],
                    "S-Rallentato": ["","dimezza i pa disponibili."],
                    "S-Terrorizzato": ["","fuggi, se non puoi combatti usando tutto quello che hai."],
                    "S-Accecato/\nBuio": ["","50% di fallire colpi o cast entro 1m. Oltre 100%."],
                    "S-Muto": ["","non puoi parlare, dare comandi agli animali etc..."],
                    "S-Stordito": ["","50% di fallire qualsiasi azione non di movimento."],
                    "S-Paralizzato": ["","azzera i pa disponibili."],
                    "S-Comandato": ["","fa quello che decide l'autore dell'incantesimo."],
                    "S-Frenetico": ["","attacca con tutte le risorse il pg o npc piu' vicino."],
                    "S-Mindscaped": ["","Mindscaped"]

                }
                lista_bagno = {
                    "C-Stufato di \nCarne(lv1)": ["Shared.pg_selezionato['pf_extra'] += int(Shared.pg_selezionato['livello'])+4",
                                                  f"PF+ ({int(lvpg)+4})"],
                    "C-Spezzatino(lv2)": ["Shared.pg_selezionato['pf_extra'] += int(Shared.pg_selezionato["
                                          "'livello'])*2+5$$Shared.pg_selezionato['pa_extra'] += floor(int("
                                          "Shared.pg_selezionato['livello'])/5)+1",f"PF++({int(lvpg)*2+5}), PA+({int(int(lvpg)/5+1)})"],
                    "C-Taglio\nScelto(lv3)": ["Shared.pg_selezionato['pf_extra'] += int(Shared.pg_selezionato["
                                              "'livello'])*3+7$$Shared.pg_selezionato['pa_extra'] += floor(int("
                                              "Shared.pg_selezionato['livello'])/4)+2",f"PF+++({int(lvpg)*3+7}),PA++({int(int(lvpg)/4+2)})"],
                    "C-Zuppa di\nPesce(lv1)": ["Shared.pg_selezionato['mana_extra'] += int(Shared.pg_selezionato['livello'])+4",f"Mana+({int(lvpg)+4})"],
                    "C-Pesce al\nForno(lv2)": ["Shared.pg_selezionato['mana_extra'] += int(Shared.pg_selezionato["
                                               "'livello'])*2+5$$Shared.pg_selezionato['pa_extra'] += floor(int("
                                               "Shared.pg_selezionato['livello'])/5)+1",f"Mana++({int(lvpg)*2+5}),PA+({int(int(lvpg)/5+1)})"],
                    "C-Trancio \ndi Pesce(lv3)": ["Shared.pg_selezionato['mana_extra'] += int(Shared.pg_selezionato["
                                                  "'livello'])*3+7$$Shared.pg_selezionato['pa_extra'] += floor(int("
                                                  "Shared.pg_selezionato['livello'])/4)+2",f"Mana+++({int(lvpg)*3+7}),PA++({int(int(lvpg)/4+2)})"],
                    "C-Stufato di \nVerdure(lv1)": ["Shared.pg_selezionato['energia_extra'] += int(int(Shared.pg_selezionato["
                                                    "'livello'])/3)+2",f"EN+({int(int(lvpg)/3+2)})"],
                    "C-Zuppa di \nLegumi(lv2)": ["Shared.pg_selezionato['energia_extra'] += int(int(Shared.pg_selezionato["
                                                 "'livello'])/2)+3$$Shared.pg_selezionato['pa_extra'] += floor(int("
                                                 "Shared.pg_selezionato['livello'])/5)+1",f"EN++({int(int(lvpg)/2+3)}),PA+({int(int(lvpg)/5+1)})"],
                    "C-Ratauille(lv3)": ["Shared.pg_selezionato['energia_extra'] += int(int(Shared.pg_selezionato["
                                         "'livello'])/1.5)+4$$Shared.pg_selezionato['pa_extra'] += floor(int("
                                         "Shared.pg_selezionato['livello'])/4)+2",f"EN+++({int(int(lvpg)/1.5+4)}),PA++({int(int(lvpg)/4+2)})"],
                    "B-Bagno con \nSali": ["Shared.pg_selezionato['energia_extra'] += int(int(Shared.pg_selezionato["
                                           "'livello'])/3)+2",f"EN+({int(int(lvpg)/3+2)})"],
                    "B-Bagno \nLussuoso": ["Shared.pg_selezionato['energia_extra'] += int(int(Shared.pg_selezionato["
                                           "'livello'])/2)+3",f"EN++({int(int(lvpg)/2+3)})"]

                }
                lista_extra = []
                if tipo == "malattie":
                    lista_extra = lista_malattie
                elif tipo == "cibo":
                    lista_extra = lista_bagno
                for item in lista_extra:
                    c = (0.7, 0.7, 0.7, 1)
                    if item[:2] == "M-":
                        c = (0.7, 1, 0.7, 1)
                    elif item[:2] == "S-":
                        c = (1.5, 1.5, 0, 1)
                    elif item[:2] == "C-":
                        c = (1.5, 1, 0, 0.8)
                    elif item[:2] == "B-":
                        c = (0.3, 0.3, 1.5, 0.8)
                    item_totale = [item,lista_extra[item]]
                    exec(f"box_extra.add_widget(Button(text = item,background_color=c,"
                         f"color = (1,1,1,1),"
                         f" on_release=partial(inserisci_codice_descrizione, item2 = item_totale)))")
                big_box_effetti.add_widget(box_extra)
            else:
                big_box_effetti.cols = 1
                big_box_effetti.remove_widget(widget_list[0])

        def inserisci_codice_descrizione(*args, item2):
            nomeeffetto.text = item2[0].replace("\n", "")
            descrizioneeffetto.text = item2[1][1].replace("\n", "")
            barracodice.text = item2[1][0]
            aggiungi_temp()

        def inserisci_codice(*args, item2):
            flag_ignora = ["M-", "S-", "C-", "B-"]
            if nomeeffetto.text in ["Vuoto",""] or nomeeffetto.text[:2] in ["M-", "S-", "C-", "B-"]:
                nomeeffetto.text = item2[0].replace("\n", "")
            if item2[0][:2] in flag_ignora:
                barracodice.text = item2[1]
                aggiungi_temp()

                return

            if not Shared.flag_aggiungi_popup_effetti:
                barracodice.text = item2[1] + " += 0"
            else:
                barracodice.text += item2[1] + " += 0"

        def aggiungi_codice(*args):
            barracodice.text += "$$"
            Shared.flag_aggiungi_popup_effetti = True

        def aggiungi_temp(*args):
            if not descrizioneeffetto.text.endswith("(t)"):
                descrizioneeffetto.text += "(t)"


        barranome = Label(size_hint=(1, 0.11), text="Nome Effetto")
        nomeeffetto = TextInput(size_hint=(1, 0.11), text=f"{dati_locali['nome_effetto']}")
        barraeffetto = Label(size_hint=(1, 0.11), text="Descrizione")
        descrizioneeffetto = TextInput(size_hint=(1, 0.11),
                                       text=f"{dati_locali['descrizione_effetto']}")
        barracodice = TextInput(size_hint=(1, 0.25), text=f"{dati_locali['codice_effetto']}")
        box = GridLayout(padding=5, cols=5)

        lista = {"Attacco": "Shared.pg_selezionato['attacco_extra']",
                 "Difesa": "Shared.pg_selezionato['difesa_extra']",
                 "Tier Danno": "Shared.pg_selezionato['tier_extra']", "PF": "Shared.pg_selezionato['pf_extra']",
                 "Mana": "Shared.pg_selezionato['mana_extra']",
                 "Energia": "Shared.pg_selezionato['energia_extra']",
                 "Punti Azione": "Shared.pg_selezionato['pa_extra']",
                 "Potere": "Shared.pg_selezionato['potere_extra']",
                 "RD fis.": "Shared.pg_selezionato['rd_fis_extra']",
                 "Res. Contundente": "Shared.pg_selezionato['res_contundente_extra']",
                 "Res. Perforante": "Shared.pg_selezionato['res_perforante_extra']",
                 "Res. Taglio": "Shared.pg_selezionato['res_taglio_extra']",
                 "RD Fuoco": "Shared.pg_selezionato['rd_fuoco_extra']",
                 "RD Gelo": "Shared.pg_selezionato['rd_gelo_extra']",
                 "RD Elettro": "Shared.pg_selezionato['rd_elettro_extra']",
                 "Res. Fuoco": "Shared.pg_selezionato['res_fuoco_extra']",
                 "Res. Gelo": "Shared.pg_selezionato['res_gelo_extra']",
                 "Res. Elettro": "Shared.pg_selezionato['res_elettro_extra']",
                 "Forza": "Shared.pg_selezionato['forza_bonus_extra']",
                 "Resistenza": "Shared.pg_selezionato['resistenza_bonus_extra']",
                 "Velocita": "Shared.pg_selezionato['velocita_bonus_extra']",
                 "Agilità": "Shared.pg_selezionato['agilita_bonus_extra']",
                 "Intelligenza": "Shared.pg_selezionato['intelligenza_bonus_extra']",
                 "Concentrazione": "Shared.pg_selezionato['concentrazione_bonus_extra']",
                 "Personalità": "Shared.pg_selezionato['personalita_bonus_extra']",
                 "Saggezza": "Shared.pg_selezionato['saggezza_bonus_extra']",
                 "Fortuna": "Shared.pg_selezionato['fortuna_bonus_extra']",
                 "Mod. Generale": "Shared.pg_selezionato['modificatore_generale_extra']",
                 "Mod. Carico": "Shared.pg_selezionato['mod_carico']"
                 }

        for item in lista:
            c = (0.7, 0.7, 0.7, 1)
            if item[:2] == "M-":
                c = (0.7, 1, 0.7, 1)
            elif item[:2] == "S-":
                c = (1.5, 1.5, 0, 1)
            elif item[:2] == "C-":
                c = (1.5, 1, 0, 0.8)
            elif item[:2] == "B-":
                c = (0.3, 0.3, 1.5, 0.8)
            item_totale = [item, lista[item]]
            exec(f"box.add_widget(Button(text = item,background_color=c,"
                 f"color = (1,1,1,1),"
                 f" on_release=partial(inserisci_codice, item2 = item_totale)))")
        box.add_widget(Button(text="MALATTIE\nSTATUS", background_color=(0.7, 1, 0.7, 1), on_release=partial(popup_extra, tipo = "malattie")))
        box.add_widget(Button(text="CIBO\nBAGNO", background_color=(1.3, 1.3, 2, 0.8), on_release=partial(popup_extra, tipo = "cibo")))
        box.add_widget(Button(text="AGGIUNGI", background_color=(2, 1.3, 0.5, 0.8), on_release=aggiungi_codice))
        box.add_widget(Button(text="TEMPORANEO", background_color=(2, 1.3, 0.5, 0.8), on_release=aggiungi_temp))

        layout_effetto.add_widget(barranome)
        layout_effetto.add_widget(nomeeffetto)
        layout_effetto.add_widget(barraeffetto)
        layout_effetto.add_widget(descrizioneeffetto)
        layout_effetto.add_widget(barracodice)
        layout_effetto.add_widget(box)

        big_box_effetti.add_widget(layout_effetto)

        ############ fine effetto ################
        ############ inizio popup ################


        nuovo_testo_titolo_popup = TextInput(size_hint=(1, 0.35),text = dati_locali['titolo_popup'])
        nuovo_testo_contenuto_popup = TextInput(size_hint=(1, 0.65),text = dati_locali['contenuto_popup'])
        layout_popup.add_widget(nuovo_testo_titolo_popup)
        layout_popup.add_widget(nuovo_testo_contenuto_popup)
        big_box_popup.add_widget(layout_popup)

        ############ fine popup ################
        ############ inizio campi ################
        box_campi = GridLayout(padding=5, cols=8)
        layout_campi.add_widget(box_campi)
        big_box_campi.add_widget(Label(text = "Nome campo -> Valore desiderato"))
        box_campi.add_widget(Label(text = "PF", size_hint=(0.25, 0.25)))
        box_campi_pf = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_PF'] if 'campo_PF' in dati_locali else "0")
        box_campi.add_widget(box_campi_pf)
        box_campi.add_widget(Label(text = "Mana", size_hint=(0.25, 0.25)))
        box_campi_mana = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Mana'] if 'campo_Mana' in dati_locali else "0")
        box_campi.add_widget(box_campi_mana)
        box_campi.add_widget(Label(text = "Energia", size_hint=(0.25, 0.25)))
        box_campi_energia = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Energia'] if 'campo_Energia' in dati_locali else "0")
        box_campi.add_widget(box_campi_energia)
        box_campi.add_widget(Label(text = "Potere", size_hint=(0.25, 0.25)))
        box_campi_potere = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Potere'] if 'campo_Potere' in dati_locali else "0")
        box_campi.add_widget(box_campi_potere)
        box_campi.add_widget(Label(text = "Punti Azione", size_hint=(0.25, 0.25)))
        box_campi_pa = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Punti_Azione'] if 'campo_Punti_Azione' in dati_locali else "0")
        box_campi.add_widget(box_campi_pa)
        box_campi.add_widget(Label(text = "Bonus Atk", size_hint=(0.25, 0.25)))
        box_campi_bonus_atk = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Bonus_Atk'] if 'campo_Bonus_Atk' in dati_locali else "0")
        box_campi.add_widget(box_campi_bonus_atk)
        box_campi.add_widget(Label(text = "Bonus Tier", size_hint=(0.25, 0.25)))
        box_campi_bonus_tier = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Bonus_Tier'] if 'campo_Bonus_Tier' in dati_locali else "0")
        box_campi.add_widget(box_campi_bonus_tier)
        box_campi.add_widget(Label(text = "Bonus DMG", size_hint=(0.25, 0.25)))
        box_campi_dmg = TextInput(size_hint=(0.15, 0.25),text = dati_locali['campo_Bonus_DMG'] if 'campo_Bonus_DMG' in dati_locali else "0")
        box_campi.add_widget(box_campi_dmg)

        big_box_campi.add_widget(layout_campi)

        ############ fine campi ################
        ############ inizio link ################
        def sostituisci_link(*args, valore_link):
            dati_locali['link'] = valore_link
            Shared.label_apre_finestra.text = "Apre Finestra -> " + dati_locali['link']

        Shared.label_apre_finestra = Label(text = "Apre Finestra -> " + dati_locali['link'], size_hint=(0.25, 0.35))
        big_box_link.add_widget(Shared.label_apre_finestra)
        box_link = GridLayout(padding=5, cols=8, size_hint=(1, 0.65))
        box_link.add_widget(Button(text= "Bottoni", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Bottoni")))
        box_link.add_widget(Button(text= "Sblocca\nSkill", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Sblocca\nSkill")))
        box_link.add_widget(Button(text= "Zaino", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Zaino")))
        box_link.add_widget(Button(text= "Mappa\nGlobale", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Mappa\nGlobale")))
        box_link.add_widget(Button(text= "Mappa\nGlobale\nHex", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Mappa\nGlobale Hex")))
        box_link.add_widget(Button(text= "Alchimia", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Alchimia")))
        box_link.add_widget(Button(text= "Calcolat.", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "Calcolatrice")))
        box_link.add_widget(Button(text= "Vuoto", color = (1,1,1,1),on_release=partial(sostituisci_link, valore_link = "")))

        layout_link.add_widget(box_link)


        big_box_link.add_widget(layout_link)


        def salva_bottone(*args,dati):
            dati[f"bottone_{numero}"] = {"nome": str(titolo_bottone.text), "nome_effetto": str(nomeeffetto.text),
                                         "descrizione_effetto": str(descrizioneeffetto.text),
                                         "codice_effetto": str(barracodice.text),
                                         "titolo_popup": str(nuovo_testo_titolo_popup.text),
                                         "contenuto_popup": str(nuovo_testo_contenuto_popup.text),
                                         "link": str(dati_locali['link']),"campo_PF":str(box_campi_pf.text),
                                         "campo_Mana":str(box_campi_mana.text),
                                         "campo_Energia":str(box_campi_energia.text),
                                         "campo_Potere":str(box_campi_potere.text),
                                         "campo_Punti_Azione":str(box_campi_pa.text),
                                         "campo_Bonus_Atk":str(box_campi_bonus_atk.text),
                                         "campo_Bonus_Tier":str(box_campi_bonus_tier.text),
                                         "campo_Bonus_DMG":str(box_campi_dmg.text)}
            pathcompleto_shared = Shared.path_cartella_shared + f"/{nome_pg}/bottoni/{nome_pg}bottoni.json"
            pathcompleto_dati = Shared.path_PG_e_Unici + f"/bottoni/{nome_pg}bottoni.json"

            try:
                with open(pathcompleto_shared, 'w') as json_file:
                    json.dump(dati, json_file, indent=4)
            except FileNotFoundError:
                os.makedirs(pathcompleto_shared)
                with open(pathcompleto_shared, 'w') as json_file:
                    json.dump(dati, json_file, indent=4)

            with open(pathcompleto_dati, "w") as json_file:
                json.dump(dati, json_file, indent=4)
            Shared.dati_bottoni = dati


        master_layout.add_widget(Button(text = "Salva",size_hint=(0.2, 0.035),
                                        on_release = partial(salva_bottone,dati = dati), pos_hint={"x": 0.8, "y": 0}))
        popup.open()



    def elimina(*args, numero):
        dati[f"bottone_{numero}"] = {"nome":"", "nome_effetto": "", "descrizione_effetto":"","codice_effetto":"","titolo_popup":"",
                          "contenuto_popup":"","link":"","campo_PF":"","campo_Mana":"","campo_Energia":"","campo_Potere":"",
                          "campo_Punti_Azione":"","campo_Bonus_Atk":"","campo_Bonus_Tier":"","campo_Bonus_DMG":""}
        pathcompleto_shared = Shared.path_cartella_shared + f"/{nome_pg}/bottoni/{nome_pg}bottoni.json"
        pathcompleto_dati = Shared.path_PG_e_Unici + f"/bottoni/{nome_pg}bottoni.json"
        with open(pathcompleto_shared, "w") as json_file:
            json.dump(dati, json_file, indent=4)
        with open(pathcompleto_dati, "w") as json_file:
            json.dump(dati, json_file, indent=4)
        Shared.dati_bottoni = dati


    for bottone in range(1, 7):
        exec(f"linea{bottone} = BoxLayout(orientation='horizontal')")
        exec(f"linea{bottone}.add_widget(Button(size_hint=(0.12,1), color=(1,1,1,1),text = 'Bottone {bottone}', on_release=partial(apribottone, numero={bottone}, dati = dati)))")
        exec(f"linea{bottone}.add_widget(Label(text = str(dati['bottone_{bottone}']['nome']), color=(1,1,1,1)))")
        exec(f"linea{bottone}.add_widget(Button(size_hint=(0.1,1),text = 'Elimina', color=(1,1,1,1), on_release=partial(elimina, numero={bottone})))")
        exec(f"layout1.add_widget(linea{bottone})")




    scroller.add_widget(layout1)
    popup.open()




