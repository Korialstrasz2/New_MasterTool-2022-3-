import copy
import json
import os
import shutil
from random import randrange

from kivy.uix.spinner import Spinner

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, FinestraPrincipaleCombat, Popups_ScreenPGImportato
from Moduli.Logica import EquipAttore, ImportazioneAttori, Oggetti, Inizializza, Salvataggio
from kivy.lang import Builder
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput



def apri_archetipi(*args):
    Builder.load_string("""
<Label>:
    color: 0,0,0,1
<TextInput>:
    background_color: 1,1,1,0.7""")

    layout = FloatLayout()
    popup = Popup(title=f"Seleziona Archetipo", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(800, 750),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source='Art/NPCbg.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    layout.add_widget(notepic)

    print(os.listdir(Shared.path_dati+"//Esempi"))
    nomi = {}
    def seleziona_npc(nome, *args):
        layout.clear_widgets()
        layout.add_widget(notepic)
        layout.add_widget(Button(size_hint=(0.25, 0.05), pos_hint={"x": 0, "y": 0.95}, text="Seleziona\nNPC",
                                 on_release=popola_bottoni))

        y_base = 0.9
        for nome_completo in nomi[nome]:
            livello = nome_completo.split(".")[1].replace("lv","")
            layout.add_widget(Button(size_hint=(1, 0.05), pos_hint={"x": 0, "y": y_base}, text=str(livello), on_release=partial(seleziona_livello,nome_completo, nome)))
            y_base -= 0.05

    def popola_bottoni(*args):
        nonlocal nomi
        layout.clear_widgets()
        layout.add_widget(notepic)
        nomi = {}
        for nome in os.listdir(Shared.path_dati+"//Esempi"):
            nuovonome = nome.split(".")[0].replace("__pg__","")
            if not nuovonome.endswith("skill"):
                if nuovonome not in nomi:
                    nomi[nuovonome] = [nome]
                else:
                    nomi[nuovonome].append(nome)

        y_base = 0.95
        for archetipo in nomi:
            layout.add_widget(Button(size_hint=(1, 0.15), pos_hint={"x": 0, "y": y_base}, text=archetipo,
                                     on_release=partial(seleziona_npc, archetipo)))
            y_base -= 0.15

    def seleziona_livello(totale,nome,*args):
        with open(Shared.path_dati+"//Esempi//"+totale, "r") as dati_json:
            data = json.load(dati_json)
            nome_nuovo = ImportazioneAttori.crea_attore_attivo_da_dati(data,nome)
            Shared.npc_archetipo_selezionato = Shared.pg_png_inizializzati[nome_nuovo]
        # prendi i dati delll'archetipo corrispondente. sostituisci il suo nome_valore_excel e nomepg.
        # a quel punti importalo con i nuovi dati.
        # fai in modo che, se hai importato un png così, quando clicchi calcola non importa un nuovo blob, ma va a lavorare sul pg archetipo

    popola_bottoni()
    popup.open()

def apri(npc, numero_npc,*args):
    Builder.load_string("""
<Label>:
    color: 0,0,0,1
<TextInput>:
    background_color: 1,1,1,0.7""")
    Shared.npc_archetipo_selezionato = ""
    layout = FloatLayout()
    popup = Popup(title=f"Dettagli NPC", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(800, 450),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source='Art/NPCbg.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    layout.add_widget(notepic)

    bottone_archetipi = Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.2, "y": 0.3}, text="Archetipi",on_release=apri_archetipi)


    def check_int(numero):
        try:
            int(numero)
            return int(numero)
        except:
            return 0

    def calc_new(crea,*args):
        if Shared.npc_archetipo_selezionato != "":
            nomenpc = ImportazioneAttori.crea_attore_attivo(Shared.npc_archetipo_selezionato["nome_valore_excel"])
            box_livello.text = str(Shared.npc_archetipo_selezionato["livello"])
        else:
            nomenpc = ImportazioneAttori.crea_attore_attivo("__umani__Blob")
        nuovo_temp = Shared.pg_png_inizializzati[nomenpc]
        conferma_e_import(nuovo_temp)
        nuovo_temp['livello'] = check_int(box_livello.text) if box_livello.text != "" else 1
        nuovo_temp['forza_base'] = 10 + check_int(box_forza.text)
        nuovo_temp['resistenza_base'] = 10 + check_int(box_resistenza.text)
        nuovo_temp['velocita_base'] = 10 + check_int(box_velocita.text)
        nuovo_temp['agilita_base'] = 10 + check_int(box_agilita.text)
        nuovo_temp['intelligenza_base'] = 10 + check_int(box_intelligenza.text)
        nuovo_temp['concentrazione_base'] = 10 + check_int(box_concentrazione.text)
        nuovo_temp['personalita_base'] = 10 + check_int(box_personalita.text)
        nuovo_temp['saggezza_base'] = 10 + check_int(box_saggezza.text)
        nuovo_temp['fortuna_base'] = 10 + check_int(box_fortuna.text)
        EquipAttore.equip_npc(nomenpc)
        box_pf.text = "PF : " + str(nuovo_temp['pf_tot'])
        box_mana.text = "Mana : " + str(nuovo_temp['mana_tot'])
        box_energia.text = "EN : " + str(nuovo_temp['energia_tot'])
        box_potere.text = "POW : " + str(nuovo_temp['potere_tot'])
        box_pa.text = "PA : " + str(nuovo_temp['pa_tot'])
        box_attacco.text = "ATK : " + str(nuovo_temp['attacco_tot'])
        box_difesa.text = "DEF : " + str(nuovo_temp['difesa_tot'])

        if crea:
            ImportazioneAttori.assegna_npc(nomenpc, numero_npc)
        else:
            Shared.pg_png_inizializzati.pop(nomenpc)
            Shared.pg_png_creati_dal_pc.remove(nomenpc)

    def popola_campi(gruppo, npc_input):
        for indice, oggetto in enumerate(gruppo_oggetti):
            npc_input[oggetto] = gruppo[indice] if gruppo[indice] != 0 else npc_input[oggetto]

    def conferma_e_import(npc_input, *args):
        npc_input['razza1'] = spinner_razzze.text
        if spinner_equip.text == "Soldato\nImperiale":
            popola_campi([178,5600,5758,0,0,648,687,0,0,0,0,0,0,0,0,0,0,0,0,0,2646,3253,0,0],npc_input)
        elif spinner_equip.text == "Ufficiale\nImperiale":
            popola_campi([179,5600,5758,0,0,648,687,0,0,0,0,0,0,0,0,0,0,0,0,0,2648,3255,0,0],npc_input)
        elif spinner_equip.text == "Redoran":
            popola_campi([5692,5742,568,0,0,648,687,676,667,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],npc_input)
        elif spinner_equip.text == "Confraternita\nOscura":
            popola_campi([5684,5735,0,0,0,0,0,0,883,0,0,0,0,0,1309,1247,1348,0,0,0,0,0,0,0],npc_input)
        elif spinner_equip.text == "Blade(Combat)":
            popola_campi([5702,5753,0,582,0,650,650,677,713,0,0,0,0,1286,1350,0,0,0,0,0,0,3716,3966,4445],npc_input)
        elif spinner_equip.text == "Blade(Leggero)":
            popola_campi([5702,5733,0,0,0,648,687,676,667,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],npc_input)
        elif spinner_equip.text == "Ordinatore":
            popola_campi([5687,5754,577,592,0,753,713,677,651,648,0,0,0,1305,1484,1492,0,0,0,1887,2658,3371,3904,4511],npc_input)
        elif spinner_equip.text == "Alto\nOrdinatore":
            popola_campi([5687,5754,577,0,0,752,712,676,650,648,0,0,0,1304,1483,1491,0,0,0,1886,2657,3370,3903,4510],npc_input)
        elif spinner_equip.text == "Alikr":
            popola_campi([5699,5734,0,0,0,650,885,909,0,0,0,0,0,1269,1279,1297,1350,0,0,1902,2714,3255,0,4445],npc_input)
        elif spinner_equip.text == "Cavaliere\nHigh Rock":
            popola_campi([328,5750,568,582,0,648,687,0,0,0,0,0,0,0,0,0,0,0,0,0,2646,3255,0,0],npc_input)
        elif spinner_equip.text == "Vuoto":
            popola_campi([548,549,564,579,594,643,643,643,643,643,643,643,643,1242,1242,1242,1242,1242,1242,1841,2440,3039,3638,4237],npc_input)


        EquipAttore.equip_npc(npc['nome_in_uso'])
        FinestraPrincipaleMain.FunzioniFinestra.show_all()

    def show_hide_new(*args):
        nonlocal new_pg
        if not new_pg:
            new_pg = True
            layout.add_widget(box_new)
            layout.add_widget(bottone_archetipi)
        else:
            new_pg = False
            layout.remove_widget(box_new)
            layout.remove_widget(bottone_archetipi)

    new_pg = False
    gruppo_oggetti = ['id_arma_1','id_armatura','id_scudo','id_chainmail','id_veste','equip_anello_1','equip_anello_2',
                      'equip_anello_3','equip_anello_4','equip_anello_5','equip_anello_6','equip_anello_7',
                      'equip_anello_8','equip_orecchino_1','equip_orecchino_2','equip_orecchino_3',
                      'equip_orecchino_4','equip_orecchino_5','equip_orecchino_6','equip_spilla','equip_fascia',
                      'equip_mantello','equip_amuleto','equip_cintura']
    box_new = GridLayout(cols=3, spacing=0, size_hint = (0.6,1), pos_hint ={"x": 0.4, "y": 0} )
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.9}, text="Livello"))
    box_livello = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_livello)
    box_pf = Label(size_hint = (0.33,0.1), text = "PF :")
    box_new.add_widget(box_pf)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.8}, text="FORZ bonus"))
    box_forza = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_forza)
    box_mana = Label(size_hint = (0.33,0.1), text = "Mana :")
    box_new.add_widget(box_mana)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.7}, text="RES bonus"))
    box_resistenza = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_resistenza)
    box_energia = Label(size_hint = (0.33,0.1), text = "EN :")
    box_new.add_widget(box_energia)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.6}, text="VEL bonus"))
    box_velocita = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_velocita)
    box_potere = Label(size_hint = (0.33,0.1), text = "POW :")
    box_new.add_widget(box_potere)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.5}, text="AGI bonus"))
    box_agilita = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_agilita)
    box_pa = Label(size_hint = (0.33,0.1), text = "PA :")
    box_new.add_widget(box_pa)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.4}, text="INT bonus"))
    box_intelligenza = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_intelligenza)
    box_attacco = Label(size_hint = (0.33,0.1), text = "ATK :")
    box_new.add_widget(box_attacco)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.3}, text="CONC bonus"))
    box_concentrazione = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_concentrazione)
    box_difesa = Label(size_hint = (0.33,0.1), text = "DEF :")
    box_new.add_widget(box_difesa)
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.2}, text="PER bonus"))
    box_personalita = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_personalita)
    box_new.add_widget(Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.2, "y": 0.0}, text="Crea e Assegna",
                              on_release=partial(calc_new, True)))
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.1}, text="SAG bonus"))
    box_saggezza = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_saggezza)
    box_new.add_widget(Label(size_hint = (0.33,0.1), text = ""))
    box_new.add_widget(Label(size_hint=(0.33, 0.1), pos_hint={"x": 0.8, "y": 0.1}, text="FORT bonus"))
    box_fortuna = TextInput(size_hint=(0.33, 0.1))
    box_new.add_widget(box_fortuna)
    box_new.add_widget(Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.2, "y": 0.0}, text="Calcola", on_release=partial(calc_new, False)))



    spinner_razzze = Spinner(
        text=npc['razza1'],
        values=('Bosmer','Dunmer','Orsimer','Altmer','Imperiale','Bretone','Argoniano','Khajiit','Nord','Orco','Falmer'),
        size_hint=(0.2, 0.1),
        pos_hint={"x": 0, "y": 0.9}
    )
    spinner_equip = Spinner(
        text="Fast Equip",
        values=('Soldato\nImperiale','Ufficiale\nImperiale','Redoran','Confraternita\nOscura','Blade(Combat)','Blade(Leggero)','Ordinatore','Alto\nOrdinatore','Alikr','Cavaliere\nHigh Rock',"Vuoto"),
        size_hint=(0.2, 0.1),
        pos_hint={"x": 0.2, "y": 0.9}
    )

    layout.add_widget(Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.2, "y": 0.0}, text="Nuovo",on_release=show_hide_new))

    layout.add_widget(spinner_razzze)
    layout.add_widget(spinner_equip)
    layout.add_widget(Button(size_hint=(0.2, 0.1), pos_hint={"x": 0, "y": 0.0}, text="Conferma",on_release=partial(conferma_e_import, npc)))

    popup.open()
