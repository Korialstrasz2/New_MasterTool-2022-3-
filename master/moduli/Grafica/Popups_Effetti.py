import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain
from Moduli.Logica import EquipAttore
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

def gestisci_effetti_open(*args,numero_open=False):
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=None, height=1040)
    scroller = ScrollView(size_hint=(1, None), size=(400, 400), effect_cls="ScrollEffect")
    popup = Popup(title="EFFETTI", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 500),
                  auto_dismiss=True)

    def aprieffetto(*args, numero):
        layout2 = BoxLayout(orientation='vertical', spacing=2)
        big_box = GridLayout(cols=1, spacing=0)
        popup = Popup(title=f"Effetto {numero}", title_size=(30),
                      title_align='center', content=big_box,
                      size_hint=(None, None), size=(590, 700),
                      auto_dismiss=True)

        Shared.flag_aggiungi_popup_effetti = False
        sezione_extra_selezionata = ""
        def popup_extra(*args, tipo = "malattie"):
            widget_list = list(big_box.children)
            nonlocal inserisci_codice
            nonlocal inserisci_codice_descrizione
            nonlocal popup
            nonlocal sezione_extra_selezionata
            if len(widget_list) == 1 :
                lvpg = Shared.pg_selezionato['livello']
                temporaneo = True
                big_box.cols = 2
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
                lista_attacco = {
                    "Attacco Base": ["Shared.pg_selezionato['attacco_extra'] += 0",""],
                    "Armi \nLunghe": ["Shared.pg_selezionato['atk_skill_lunghe'] += 0",""],
                    "Armi \nMedie\n(lunghezza)": ["Shared.pg_selezionato['atk_skill_medie1'] += 0",""],
                    "Armi \nCorte": ["Shared.pg_selezionato['atk_skill_corte'] += 0",""],
                    "Armi \nPotenti": ["Shared.pg_selezionato['atk_skill_potenti'] += 0",""],
                    "Armi \nMedie\n(potenza)": ["Shared.pg_selezionato['atk_skill_medie2'] += 0",""],
                    "Armi \nPrecise": ["Shared.pg_selezionato['atk_skill_precise'] += 0",""],
                    "Armi \nTaglio": ["Shared.pg_selezionato['atk_skill_taglio'] += 0",""],
                    "Armi \nContundenti": ["Shared.pg_selezionato['atk_skill_contundente'] += 0",""],
                    "Armi \nPerforanti": ["Shared.pg_selezionato['atk_skill_perforante'] += 0",""],
                    "Attacco \nMani Nude": ["Shared.pg_selezionato['atk_skill_maninude'] += 0",""],
                    "Tier \nMani Nude": ["Shared.pg_selezionato['tier_skill_maninude'] += 0",""]
                }
                lista_difesa = {
                    "Difesa Base": ["Shared.pg_selezionato['difesa_extra'] += 0",""],
                    "Set Leggeri": ["Shared.pg_selezionato['def_skill_leggera'] += 0",""],
                    "Set Pesanti": ["Shared.pg_selezionato['def_skill_pesante'] += 0",""],
                    "Senza Armatura": ["Shared.pg_selezionato['def_skill_noarmatura'] += 0",""],
                    "Scudi": ["Shared.pg_selezionato['def_skill_scudo'] += 0",""]
                }
                lista_resistenze = {
                    "RD Fisica": ["Shared.pg_selezionato['rd_fis_base'] += 0",""],
                    "Res Contundente": ["Shared.pg_selezionato['res_contundente_base'] += 0",""],
                    "Res Taglio": ["Shared.pg_selezionato['res_taglio_base'] += 0",""],
                    "Res Perforante": ["Shared.pg_selezionato['res_perforante_base'] += 0",""],
                    "Res Fuoco": ["Shared.pg_selezionato['res_fuoco_base'] += 0",""],
                    "Res Gelo": ["Shared.pg_selezionato['res_gelo_base'] += 0",""],
                    "Res Elettro": ["Shared.pg_selezionato['res_elettro_base'] += 0",""],
                    "RD Fuoco": ["Shared.pg_selezionato['rd_fuoco_base'] += 0",""],
                    "RD Gelo": ["Shared.pg_selezionato['rd_gelo_base'] += 0",""],
                    "RD Elettro": ["Shared.pg_selezionato['rd_elettro_base'] += 0",""]
                }
                lista_caratteristiche = {
                    "Forza": ["Shared.pg_selezionato['forza_bonus_extra'] += 0",""],
                    "Resistenza": ["Shared.pg_selezionato['resistenza_bonus_extra'] += 0",""],
                    "Velocità": ["Shared.pg_selezionato['velocita_bonus_extra'] += 0",""],
                    "Agilità": ["Shared.pg_selezionato['agilita_bonus_extra'] += 0",""],
                    "Intelligenza": ["Shared.pg_selezionato['intelligenza_bonus_extra'] += 0",""],
                    "Concentrazione": ["Shared.pg_selezionato['concentrazione_bonus_extra'] += 0",""],
                    "Personalità": ["Shared.pg_selezionato['personalita_bonus_extra'] += 0",""],
                    "Saggezza": ["Shared.pg_selezionato['saggezza_bonus_extra'] += 0",""],
                    "Fortuna": ["Shared.pg_selezionato['fortuna_bonus_extra'] += 0",""]
                }
                lista_stat_magie = {
                    "En per (X/10) Mana\nMagia Ordine": ["Shared.pg_selezionato['enpermanaordine_extra'] += 0",""],
                    "En per (X/10) Mana\nMagia Caos": ["Shared.pg_selezionato['enpermanacaos_extra'] += 0",""],
                    "PA per (X/10) Mana\nMagia Ordine": ["Shared.pg_selezionato['papermanaordine_extra'] += 0",""],
                    "PA per (X/10) Mana\nMagia Caos": ["Shared.pg_selezionato['papermanacaos_extra'] += 0",""],
                    "Sconto Mana per\nogni punto Potere": ["Shared.pg_selezionato['sconto_mana_per_potere_extra'] += 0",""],
                    "Sconto PA per\nogni punto Potere": ["Shared.pg_selezionato['sconto_pa_per_potere_extra'] += 0",""]
                }
                lista_extra = []
                if tipo == "malattie":
                    lista_extra = lista_malattie
                elif tipo == "cibo":
                    lista_extra = lista_bagno
                elif tipo == "Attacco":
                    lista_extra = lista_attacco
                    temporaneo = False
                elif tipo == "Difesa":
                    lista_extra = lista_difesa
                    temporaneo = False
                elif tipo == "Resistenze":
                    lista_extra = lista_resistenze
                    temporaneo = False
                elif tipo == "Caratteristiche":
                    lista_extra = lista_caratteristiche
                    temporaneo = False
                elif tipo == "Stat Magie":
                    lista_extra = lista_stat_magie
                    temporaneo = False
                if len(lista_extra) < 15:
                    box_extra.cols = 2
                if len(lista_extra) < 10:
                    box_extra.cols = 1
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
                         f" on_release=partial(inserisci_codice_descrizione, item2 = item_totale, temp = temporaneo)))")
                popup.size = (1200, 700)
                big_box.add_widget(box_extra)
            elif sezione_extra_selezionata != tipo:
                popup.size = (590, 700)
                big_box.cols = 1
                big_box.remove_widget(widget_list[0])
                popup_extra(tipo = tipo)
            else:
                popup.size = (590, 700)
                big_box.cols = 1
                big_box.remove_widget(widget_list[0])
            sezione_extra_selezionata = tipo

        def inserisci_codice_descrizione(*args, item2, temp = True):
            if not Shared.flag_aggiungi_popup_effetti:
                nomeeffetto.text = item2[0].replace("\n", "")
                descrizioneeffetto.text = item2[1][1].replace("\n", "")
                barracodice.text = item2[1][0]
            else:
                barracodice.text += item2[1][0]
            if temp:
                aggiungi_temp()


        def inserisci_codice(*args, item2):
            if item2[1] == "Attacco":
                popup_extra(tipo="Attacco")
            elif item2[1] == "Difesa":
                popup_extra(tipo="Difesa")
            elif item2[1] == "Resistenze":
                popup_extra(tipo="Resistenze")
            elif item2[1] == "Caratteristiche":
                popup_extra(tipo="Caratteristiche")
            else:
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

        def accetta(*args, numero_effetto):
            nonlocal nomeeffetto
            nonlocal descrizioneeffetto
            nonlocal barracodice
            exec(f"Shared.pg_selezionato['nome_effetto_{numero}'] = nomeeffetto.text")
            exec(f"Shared.pg_selezionato['descrizione_effetto_{numero}'] = descrizioneeffetto.text")
            exec(f"Shared.pg_selezionato['codice_effetto_{numero}'] = barracodice.text")

            EquipAttore.equip_npc(nome_NPC_Attori=Shared.pg_selezionato['nome_valore_excel'])
            FinestraPrincipaleMain.FunzioniFinestra.show_all()

        barranome = Label(size_hint=(1, 0.07), text=f"Nome Effetto {numero}")
        nomeeffetto = TextInput(size_hint=(1, 0.07), text=eval(f"Shared.pg_selezionato['nome_effetto_{numero}']"))
        barraeffetto = Label(size_hint=(1, 0.07), text="Descrizione Effetto")
        descrizioneeffetto = TextInput(size_hint=(1, 0.07),
                                       text=eval(f"Shared.pg_selezionato['descrizione_effetto_{numero}']"))
        barracodice = TextInput(size_hint=(1, 0.25), text=eval(f"Shared.pg_selezionato['codice_effetto_{numero}']"))
        box = GridLayout(padding=5, cols=5)

        lista = {"Attacco": "Attacco",
                 "Difesa": "Difesa",
                 "Tier Danno": "Shared.pg_selezionato['tier_extra']", "PF": "Shared.pg_selezionato['pf_extra']",
                 "Mana": "Shared.pg_selezionato['mana_extra']",
                 "Energia": "Shared.pg_selezionato['energia_extra']",
                 "Punti Azione": "Shared.pg_selezionato['pa_extra']",
                 "Potere": "Shared.pg_selezionato['potere_extra']",
                 "Resistenze/RD.": "Resistenze",
                 "Caratteristiche": "Caratteristiche",
                 "Mod. Generale": "Shared.pg_selezionato['modificatore_generale_extra']",
                 "Mod. Carico": "Shared.pg_selezionato['mod_carico']"
                 }

        # colore bottono m s c b
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
        box.add_widget(Button(text="Modificatori\nMagie", background_color=(0, 0, 1, 1), on_release=partial(popup_extra, tipo = "Stat Magie")))
        box.add_widget(Button(text="MALATTIE\nSTATUS", background_color=(0.7, 1, 0.7, 1), on_release=partial(popup_extra, tipo = "malattie")))
        box.add_widget(Button(text="CIBO\nBAGNO", background_color=(1.3, 1.3, 2, 0.8), on_release=partial(popup_extra, tipo = "cibo")))
        box.add_widget(Button(text="AGGIUNGI", background_color=(2, 1.3, 0.5, 0.8), on_release=aggiungi_codice))
        box.add_widget(Button(text="TEMPORANEO", background_color=(2, 1.3, 0.5, 0.8), on_release=aggiungi_temp))
        box.add_widget(
            Button(text="ACCETTA", background_color=(0, 1, 0, 1), on_release=partial(accetta, numero_effetto=numero)))
        box.add_widget(
            Button(text="ELIMINA", background_color=(1.5, 0, 0, 1), on_release=partial(elimina, numero=numero)))

        layout2.add_widget(barranome)
        layout2.add_widget(nomeeffetto)
        layout2.add_widget(barraeffetto)
        layout2.add_widget(descrizioneeffetto)
        layout2.add_widget(barracodice)
        layout2.add_widget(box)
        big_box.add_widget(layout2)
        popup.open()

    def elimina(*args, numero):
        exec(f"Shared.pg_selezionato['nome_effetto_{numero}'] = 'Vuoto'")
        exec(f"Shared.pg_selezionato['descrizione_effetto_{numero}'] = 'Vuoto'")
        exec(f"Shared.pg_selezionato['codice_effetto_{numero}'] = 'Vuoto'")
        EquipAttore.equip_npc(nome_NPC_Attori=Shared.pg_selezionato['nome_valore_excel'])
        FinestraPrincipaleMain.FunzioniFinestra.show_all()

    for effetto in range(1, 32):
        exec(f"""linea{effetto} = BoxLayout(orientation='horizontal')
linea{effetto}.add_widget(Label(size_hint=(0.3,1), color=(1,1,1,1), text = "Effetto {effetto}"))
linea{effetto}.add_widget(Button(size_hint=(0.5,1), color=(1,1,1,1),text = str(Shared.pg_selezionato['nome_effetto_{effetto}']), on_release=partial(aprieffetto, numero={effetto})))
linea{effetto}.add_widget(Label(text = str(Shared.pg_selezionato['descrizione_effetto_{effetto}']), color=(1,1,1,1)))
linea{effetto}.add_widget(Button(size_hint=(0.3,1),text = "Elimina", color=(1,1,1,1), on_release=partial(elimina, numero={effetto})))
layout1.add_widget(linea{effetto})
""")

    scroller.add_widget(layout1)
    popup.open()
    if numero_open:
        aprieffetto(numero=numero_open)
