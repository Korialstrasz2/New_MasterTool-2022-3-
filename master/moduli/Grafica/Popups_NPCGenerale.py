import copy
import json
import os
import shutil
from random import randrange

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, FinestraPrincipaleCombat, Popups_ScreenPGImportato, \
    Popups_NPC_Scegli, Popups_Notifiche, Popups_NPC_Dettagli
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

class Temp:
    showbarraricercazaino = False

class Zaino():
    slot_1 = ""
    slot_2 = ""
    slot_3 = ""
    slot_4 = ""
    slot_5 = ""
    slot_6 = ""
    slot_7 = ""
    slot_8 = ""
    slot_9 = ""
    slot_10 = ""
    pagina_negozio_attuale = 0
    negozio_tipo_attuale = ""

def NPCopen(numeronpc):
    Builder.load_string("""
<Label>:
    color: 0,0,0,1
<TextInput>:
    background_color: 1,1,1,0.7""")
    Shared.npc_selezionato = Shared.npc_numeri_assegnati[numeronpc]

    layout = FloatLayout()
    popup = Popup(title=f"NPC {numeronpc}", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1500, 750),
                  auto_dismiss=False)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source='Art/NPCbg.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    layout.add_widget(notepic)

    def cerca(*args):
        nomes = ""
        ids = ""
        livellos = ""
        razzas = ""
        if len(boxid.text) > 0:
            ids = str(boxid.text)
        if len(boxnome.text) > 0:
            nomes = str(boxnome.text)
        if len(boxlivello.text) > 0:
            livellos = str(boxlivello.text)
        if len(boxrazza.text) > 0:
            razzas = str(boxrazza.text)
        risultato = Inizializza.trova_pgnpc(ids=ids, nome=nomes, livello=livellos)

        if type(risultato) == dict:
            for item in range(1, 11):
                oggetto_in_slot = eval(f"risultato['zaino_slot_{item}']")
                if type(oggetto_in_slot) == str \
                        and len(oggetto_in_slot) > 3 \
                        and oggetto_in_slot[:3] == "id:":
                    scritta_1 = Oggetti.trova_oggetto(oggetto_in_slot[3:])['ID']
                    scritta_2 = Oggetti.trova_oggetto(oggetto_in_slot[3:])['NOME']
                    exec(f"Zaino.slot_{item} = f'({scritta_1}) {scritta_2}'")
                else:
                    exec(f"Zaino.slot_{item} = oggetto_in_slot")
            boxid.text = str(risultato["nome_valore_excel"])
            boxnome.text = str(risultato["nomepg"])
            boxlivello.text = str(risultato["livello"])
            boxrazza.text = str(risultato["razza1"] + " - " + risultato["razza2"] + " - " + risultato["razza3"])
            boxzaino1.text = str(risultato["zaino_slot_1"])
            boxzaino2.text = str(risultato["zaino_slot_2"])
            boxzaino3.text = str(risultato["zaino_slot_3"])
            boxzaino4.text = str(risultato["zaino_slot_4"])
            boxzaino5.text = str(risultato["zaino_slot_5"])
            boxzaino6.text = str(risultato["zaino_slot_6"])
            boxzaino7.text = str(risultato["zaino_slot_7"])
            boxzaino8.text = str(risultato["zaino_slot_8"])
            boxzaino9.text = str(risultato["zaino_slot_9"])
            boxzaino10.text = str(risultato["zaino_slot_10"])

        if type(risultato) == list:
            if len(risultato) == 1:
                for item in range(1, 11):
                    oggetto_in_slot = eval(f"risultato[0]['zaino_slot_{item}']")
                    if type(oggetto_in_slot) == str \
                            and len(oggetto_in_slot) > 3 \
                            and oggetto_in_slot[:3] == "id:":
                        scritta_1 = Oggetti.trova_oggetto(oggetto_in_slot[3:])['ID']
                        scritta_2 = Oggetti.trova_oggetto(oggetto_in_slot[3:])['NOME']
                        exec(f"Zaino.slot_{item} = f'({scritta_1}) {scritta_2}'")
                    else:
                        exec(f"Zaino.slot_{item} = oggetto_in_slot")
                boxid.text = str(risultato[0]["nome_valore_excel"])
                boxnome.text = str(risultato[0]["nomepg"])
                boxlivello.text = str(risultato[0]["livello"])
                boxrazza.text = str(
                    risultato[0]["razza1"] + " - " + risultato[0]["razza2"] + " - " + risultato[0]["razza3"])
                boxzaino1.text = str(risultato[0]["zaino_slot_1"])
                boxzaino2.text = str(risultato[0]["zaino_slot_2"])
                boxzaino3.text = str(risultato[0]["zaino_slot_3"])
                boxzaino4.text = str(risultato[0]["zaino_slot_4"])
                boxzaino5.text = str(risultato[0]["zaino_slot_5"])
                boxzaino6.text = str(risultato[0]["zaino_slot_6"])
                boxzaino7.text = str(risultato[0]["zaino_slot_7"])
                boxzaino8.text = str(risultato[0]["zaino_slot_8"])
                boxzaino9.text = str(risultato[0]["zaino_slot_9"])
                boxzaino10.text = str(risultato[0]["zaino_slot_10"])
            else:
                layout5 = GridLayout(pos_hint={"center_x": 0.5, "center_y": 0.5}, cols=5, spacing=0,
                                     size_hint_y=0.4, height=200)
                bglayout5 = FloatLayout()
                popup = Popup(title=f"Cerca NPC", title_size=(30),
                              title_align='center', content=bglayout5,
                              size_hint=(None, None), size=(1400, 750),
                              auto_dismiss=True)

                bglayout5.add_widget(Image(allow_stretch=True, size_hint=(1, 1), source='risorse/art/npcselectbg.jpg',
                                           pos_hint={"center_x": 0.5, "center_y": 0.5}))
                bglayout5.add_widget(layout5)
                layout5.add_widget(Label(size_hint=(0.01, 0.01), text="nome excel"))
                layout5.add_widget(Label(size_hint=(0.1, 0.01), text="Nome"))
                layout5.add_widget(Label(size_hint=(0.03, 0.01), text="Livello"))
                layout5.add_widget(Label(size_hint=(0.03, 0.01), text="Razza 1"))
                layout5.add_widget(Label(size_hint=(0.03, 0.01), text="Razza 2"))
                da_mostrare = ["nome_valore_excel", "nomepg", "livello", "razza1", "razza2"]
                for singolo in risultato:
                    for item in da_mostrare:
                        layout5.size_hint_y += 0.0018
                        layout5.add_widget(
                            TextInput(text=str(singolo[item]), padding=(0, 0, 0, 0), background_color=(1, 1, 1, 0.1)))
                popup.open()

    def sleziona_adv_npc(*args):
        layout = FloatLayout()
        popup = Popup(title='Pg e NPC - Seleziona', title_size=(30),
                      title_align='center', content=layout,
                      size_hint=(None, None), size=(1500, 800),
                      auto_dismiss=True)

        def seleziona_npc(numeronpc, *args):
            FinestraPrincipaleMain.FunzioniFinestra.conferma()
            ImportazioneAttori.assegna_npc(eval(f"Temp.bottone_npc_{str(numeronpc)}.text"), numeronpc)

            FinestraPrincipaleMain.FunzioniFinestra.conferma()
            FinestraPrincipaleCombat.invertiattaccante()
            FinestraPrincipaleCombat.invertiattaccante()

        Temp.bottone_npc_1 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0, "y": 0.9}, on_release=partial(seleziona_npc, 1))
        Temp.bottone_npc_2 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.2, "y": 0.9}, on_release=partial(seleziona_npc, 2))
        Temp.bottone_npc_3 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.4, "y": 0.9}, on_release=partial(seleziona_npc, 3))
        Temp.bottone_npc_4 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.6, "y": 0.9}, on_release=partial(seleziona_npc, 4))
        Temp.bottone_npc_5 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.8, "y": 0.9}, on_release=partial(seleziona_npc, 5))
        Temp.bottone_npc_6 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0, "y": 0.8}, on_release=partial(seleziona_npc, 6))
        Temp.bottone_npc_7 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.2, "y": 0.8}, on_release=partial(seleziona_npc, 7))
        Temp.bottone_npc_8 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.4, "y": 0.8}, on_release=partial(seleziona_npc, 8))
        Temp.bottone_npc_9 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.6, "y": 0.8}, on_release=partial(seleziona_npc, 9))
        Temp.bottone_npc_10 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.8, "y": 0.8}, on_release=partial(seleziona_npc, 10))
        Temp.bottone_npc_11 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0, "y": 0.7}, on_release=partial(seleziona_npc, 11))
        Temp.bottone_npc_12 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.2, "y": 0.7}, on_release=partial(seleziona_npc, 12))
        Temp.bottone_npc_13 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.4, "y": 0.7}, on_release=partial(seleziona_npc, 13))
        Temp.bottone_npc_14 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.6, "y": 0.7}, on_release=partial(seleziona_npc, 14))
        Temp.bottone_npc_15 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.8, "y": 0.7}, on_release=partial(seleziona_npc, 15))
        Temp.bottone_npc_16 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0, "y": 0.6}, on_release=partial(seleziona_npc, 16))
        Temp.bottone_npc_17 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.2, "y": 0.6}, on_release=partial(seleziona_npc, 17))
        Temp.bottone_npc_18 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.4, "y": 0.6}, on_release=partial(seleziona_npc, 18))
        Temp.bottone_npc_19 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.6, "y": 0.6}, on_release=partial(seleziona_npc, 19))
        Temp.bottone_npc_20 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.8, "y": 0.6}, on_release=partial(seleziona_npc, 20))
        Temp.bottone_npc_21 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0, "y": 0.5}, on_release=partial(seleziona_npc, 21))
        Temp.bottone_npc_22 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.2, "y": 0.5}, on_release=partial(seleziona_npc, 22))
        Temp.bottone_npc_23 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.4, "y": 0.5}, on_release=partial(seleziona_npc, 23))
        Temp.bottone_npc_24 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.6, "y": 0.5}, on_release=partial(seleziona_npc, 24))
        Temp.bottone_npc_25 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.8, "y": 0.5}, on_release=partial(seleziona_npc, 25))
        Temp.bottone_npc_26 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0, "y": 0.4}, on_release=partial(seleziona_npc, 26))
        Temp.bottone_npc_27 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.2, "y": 0.4}, on_release=partial(seleziona_npc, 27))
        Temp.bottone_npc_28 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.4, "y": 0.4}, on_release=partial(seleziona_npc, 28))
        Temp.bottone_npc_29 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.6, "y": 0.4}, on_release=partial(seleziona_npc, 29))
        Temp.bottone_npc_30 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.8, "y": 0.4}, on_release=partial(seleziona_npc, 30))
        Temp.bottone_npc_31 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0, "y": 0.3}, on_release=partial(seleziona_npc, 31))
        Temp.bottone_npc_32 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.2, "y": 0.3}, on_release=partial(seleziona_npc, 32))
        Temp.bottone_npc_33 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.4, "y": 0.3}, on_release=partial(seleziona_npc, 33))
        Temp.bottone_npc_34 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.6, "y": 0.3}, on_release=partial(seleziona_npc, 34))
        Temp.bottone_npc_35 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                    pos_hint={"x": 0.8, "y": 0.3}, on_release=partial(seleziona_npc, 35))

        indice_per_bottoni = 1
        for NPC_box in Shared.pg_png_inizializzati:
            if not NPC_box.startswith("__natura__Null"):
                if indice_per_bottoni < 36:
                    exec(f"Temp.bottone_npc_{indice_per_bottoni}.text = NPC_box")
                    exec(f"layout.add_widget(Temp.bottone_npc_{indice_per_bottoni})")
                    indice_per_bottoni += 1

        popup.open()

    def scegli_npc(*args):
        Popups_NPC_Scegli.apri()

    def impcartella(*args):
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory(title='Select a folder')
        filenpc = ImportazioneAttori.json_piu_recente_no_skill(folder_selected)
        if filenpc != 'no file':
            percorso = os.path.join(folder_selected,filenpc)
            with open(percorso, 'r') as json_file:
                data = json.load(json_file)
            data["numero_npc"] = numeronpc
            Shared.pg_png_inizializzati[data["nome_in_uso"]] = data
            EquipAttore.equip_npc(data["nome_in_uso"])
            ImportazioneAttori.assegna_npc(data["nome_in_uso"], numeronpc)
            FinestraPrincipaleCombat.invertiattaccante()
            FinestraPrincipaleCombat.invertiattaccante()

    def libera(*args):
        boxid.text = ""
        boxnome.text = ""
        boxlivello.text = ""
        boxrazza.text = ""
        boxzaino1.text = ""
        boxzaino2.text = ""
        boxzaino3.text = ""
        boxzaino4.text = ""
        boxzaino5.text = ""
        boxzaino6.text = ""
        boxzaino7.text = ""
        boxzaino8.text = ""
        boxzaino9.text = ""
        boxzaino10.text = ""

    def aggiungi(*args):
        if boxid.text in Shared.pgnpc_importati_base:
            FinestraPrincipaleMain.FunzioniFinestra.conferma()
            nomenpc = ImportazioneAttori.crea_attore_attivo(boxid.text)
            EquipAttore.equip_npc(nomenpc)
            ImportazioneAttori.assegna_npc(nomenpc, numeronpc)
            FinestraPrincipaleCombat.invertiattaccante()
            FinestraPrincipaleCombat.invertiattaccante()
        popup.dismiss()
        NPCopen(numeronpc)

    def crea_e_salva_nuovo_npc(*args):
        Popups_Notifiche.guida_crea_pg_da_npc()
        if "__" in boxid.text:
            tipo = f'{boxid.text.split("__")[1]}'
            if tipo == "pg":
                nomenpc = boxid.text
                da_clonare = copy.deepcopy(Shared.npc_selezionato)
                da_clonare["nome_in_uso"] = boxid.text
                da_clonare["nome_valore_excel"] = boxid.text
                da_clonare["nomepg"] = boxnome.text
                ImportazioneAttori.inizializza_pg_esterno(da_clonare)
                Shared.pg_png_inizializzati[nomenpc] = da_clonare
                EquipAttore.equip_npc(nomenpc)
                shutil.copy(Shared.path_dati + "/dbNeo.json",
                            Shared.path_PG_e_Unici + f"/__pg__{boxnome.text}.json")
                shutil.copy(Shared.path_dati + "/skillvuoto.json",
                            Shared.path_PG_e_Unici + f"/__pg__{boxnome.text}skill.json")
                pathcompleto = Shared.path_PG_e_Unici + f"//__pg__{boxnome.text}.json"
                with open(pathcompleto, "w") as json_file:
                    json.dump(da_clonare, json_file, indent=4)
                Popups_ScreenPGImportato.popup_check_differenze_pgnpc(da_clonare)
                Salvataggio.salva_pgnpc(nomenpc)
                Popups_Notifiche.custom_popup("PG crato!", f"id: {nomenpc}, nome: {da_clonare['nomepg']}")
                boxid.text = ""

    def rieqequip(*args):
        if len(boxlivello.text) > 0:
            livello = int(int(boxlivello.text) / 2) + 2
            minimo = int(livello) - 2
            if minimo < 1:
                minimo = 1
            if minimo > 9:
                minimo = 9
            massimo = int(livello) + 2
            if massimo > 10:
                massimo = 10
            livello = randrange(minimo, massimo + 1)
            Zaino.boxidslotse1.text = str(Oggetti.estrai_oggetto(tipo="armatura", livello=int(int(livello))))
            Zaino.boxnomeslotse1.text = str(Oggetti.trova_oggetto(ids=int(Zaino.boxidslotse1.text))["NOME"])
            Zaino.boxidslotse2.text = str(Oggetti.estrai_oggetto(tipo="scudo", livello=int(int(livello))))
            Zaino.boxnomeslotse2.text = str(Oggetti.trova_oggetto(ids=int(Zaino.boxidslotse2.text))["NOME"])
            Zaino.boxidslotse3.text = str(Oggetti.estrai_oggetto(tipo="chainmail", livello=int(int(livello))))
            Zaino.boxnomeslotse3.text = str(Oggetti.trova_oggetto(ids=int(Zaino.boxidslotse3.text))["NOME"])
            Zaino.boxidslotse4.text = str(Oggetti.estrai_oggetto(tipo="veste", livello=int(int(livello))))
            Zaino.boxnomeslotse4.text = str(Oggetti.trova_oggetto(ids=int(Zaino.boxidslotse4.text))["NOME"])
            Zaino.boxnomeslotar2.text = "PREMI RIEQ PER EQUIP"

    def rieqarma(*args):
        if len(boxlivello.text) > 0:
            livello = int(int(boxlivello.text) / 2) + 2
            minimo = int(livello) - 2
            if minimo < 1:
                minimo = 1
            if minimo > 9:
                minimo = 9
            massimo = int(livello) + 2
            if massimo > 10:
                massimo = 10
            livello = randrange(minimo, massimo + 1)
            Zaino.boxidslotar1.text = str(Oggetti.estrai_oggetto(tipo="arma", livello=int(int(livello))))
            Zaino.boxnomeslotar1.text = str(Oggetti.trova_oggetto(ids=int(Zaino.boxidslotar1.text))["NOME"])
            Zaino.boxnomeslotar2.text = "PREMI RIEQ PER EQUIP"

    def rieqaccess(*args):
        if len(boxlivello.text) > 0:
            livello = int(int(boxlivello.text) / 2) + 2
            minimo = int(livello) - 2
            if minimo < 1:
                minimo = 1
            if minimo > 9:
                minimo = 9
            massimo = int(livello) + 2
            if massimo > 10:
                massimo = 10
            livello = randrange(minimo, massimo + 1)
            numeroeq = 1

            for item in Oggetti.equipaggiabili:
                exec(
                    f"""Zaino.boxidsloteq{numeroeq}.text = str(Oggetti.estrai_oggetto(tipo='{item.split("_")[0]}', livello=int(int(livello)/2)))""")
                exec(
                    f"""Zaino.boxnomesloteq{numeroeq}.text = str(Oggetti.trova_oggetto(ids=int(Zaino.boxidsloteq{numeroeq}.text))["NOME"])""")
                numeroeq += 1
            Zaino.boxnomeslotar2.text = "PREMI RIEQ PER EQUIP"

    def rieq(*args):
        for slot_m in range(0, 20):
            if eval(f"Zaino.boxidslot{slot_m + 1}m.text") != "":
                exec(f"Shared.npc_selezionato['zaino_slot_{slot_m + 1}'] = 'id:'+Zaino.boxidslot{slot_m + 1}m.text")
            else:
                exec(f"Shared.npc_selezionato['zaino_slot_{slot_m + 1}'] = Zaino.boxnomeslot{slot_m + 1}m.text")

        for slot_n in range(0, 20):
            if eval(f"Zaino.boxidslot{slot_n + 1}n.text") != "":
                exec(f"Shared.npc_selezionato['zaino_slot_{slot_n + 21}'] = 'id:'+Zaino.boxidslot{slot_n + 1}n.text")
            else:
                exec(f"Shared.npc_selezionato['zaino_slot_{slot_n + 21}'] = Zaino.boxnomeslot{slot_n + 1}n.text")

        Shared.npc_selezionato['id_arma_1'] = Zaino.boxidslotar1.text
        Shared.npc_selezionato['id_arma_2'] = Zaino.boxidslotar2.text
        Shared.npc_selezionato['id_armatura'] = Zaino.boxidslotse1.text
        Shared.npc_selezionato['id_scudo'] = Zaino.boxidslotse2.text
        Shared.npc_selezionato['id_chainmail'] = Zaino.boxidslotse3.text
        Shared.npc_selezionato['id_veste'] = Zaino.boxidslotse4.text

        numeroeq = 1
        for item in Oggetti.equipaggiabili:
            exec(f"Shared.npc_selezionato['equip_{item}'] = Zaino.boxidsloteq{numeroeq}.text")
            numeroeq += 1
        EquipAttore.equip_npc(Shared.npc_selezionato['nome_in_uso'])
        FinestraPrincipaleMain.FunzioniFinestra.show_all()

    def importa(*args):
        Zaino.da_mettere = []
        ignora = ["Vuoto", "", " ", "None", None, "Slot1", "1", 1]
        for item in range(1, 41):
            if eval(f"Shared.npc_selezionato['zaino_slot_{item}']") not in ignora:
                Zaino.da_mettere.append(eval(f"Shared.npc_selezionato['zaino_slot_{item}']"))

        for slot_m in range(int(Shared.npc_selezionato['slot_zaino_magici'])):
            if len(Zaino.da_mettere) > 0:
                if str(Zaino.da_mettere[0])[:3] == "id:":
                    oggetto = Oggetti.trova_oggetto(ids=str(eval(Zaino.da_mettere[0][3:])))
                    nome = oggetto['NOME']
                    ids = oggetto['ID']
                    exec(f"Zaino.boxidslot{slot_m + 1}m.text = str(ids)")
                    exec(f"Zaino.boxnomeslot{slot_m + 1}m.text = nome")
                else:
                    exec(f"Zaino.boxnomeslot{slot_m + 1}m.text = str(Zaino.da_mettere[0])")
                Zaino.da_mettere.pop(0)

        for slot_n in range(int(Shared.npc_selezionato['slot_zaino_non_magici'])):
            if len(Zaino.da_mettere) > 0:
                if str(Zaino.da_mettere[0])[:3] == "id:":
                    oggetto = Oggetti.trova_oggetto(ids=str(eval(Zaino.da_mettere[0][3:])))
                    nome = oggetto['NOME']
                    ids = oggetto['ID']
                    exec(f"Zaino.boxidslot{slot_n + 1}n.text = str(ids)")
                    exec(f"Zaino.boxnomeslot{slot_n + 1}n.text = nome")
                else:
                    exec(f"Zaino.boxnomeslot{slot_n + 1}n.text = str(Zaino.da_mettere[0])")
                Zaino.da_mettere.pop(0)


        arma1 = Oggetti.trova_oggetto(ids=str(Shared.npc_selezionato['id_arma_1']))
        Zaino.boxidslotar1.text = str(arma1['ID'])
        Zaino.boxnomeslotar1.text = arma1['NOME']
        arma2 = Oggetti.trova_oggetto(ids=str(Shared.npc_selezionato['id_arma_2']))
        Zaino.boxidslotar2.text = str(arma2['ID'])
        Zaino.boxnomeslotar2.text = arma2['NOME']
        armatura = Oggetti.trova_oggetto(ids=str(Shared.npc_selezionato['id_armatura']))
        Zaino.boxidslotse1.text = str(armatura['ID'])
        Zaino.boxnomeslotse1.text = armatura['NOME']
        scudo = Oggetti.trova_oggetto(ids=str(Shared.npc_selezionato['id_scudo']))
        Zaino.boxidslotse2.text = str(scudo['ID'])
        Zaino.boxnomeslotse2.text = scudo['NOME']
        chainmail = Oggetti.trova_oggetto(ids=str(Shared.npc_selezionato['id_chainmail']))
        Zaino.boxidslotse3.text = str(chainmail['ID'])
        Zaino.boxnomeslotse3.text = chainmail['NOME']
        veste = Oggetti.trova_oggetto(ids=str(Shared.npc_selezionato['id_veste']))
        Zaino.boxidslotse4.text = str(veste['ID'])
        Zaino.boxnomeslotse4.text = veste['NOME']
        numeroeq = 1

    y1 = 0.755

    for slotn in range(1, 21):
        exec(
            f"""Zaino.boxidslot{slotn}n = TextInput(size_hint = (0.02,0.04), pos_hint={{"x": 0.48, "y":{y1}}}, padding = (3,3,0,0), font_size = 12)""")
        exec(
            f"""Zaino.boxnomeslot{slotn}n = TextInput(size_hint = (0.15,0.04), pos_hint={{"x": 0.5, "y":{y1}}}, padding = (3,3,0,0), font_size = 15)""")
        y1 -= 0.04

    for slot_nm in range(int(Shared.npc_selezionato['slot_zaino_non_magici'])):
        exec(f"layout.add_widget(Zaino.boxidslot{slot_nm + 1}n)")
        exec(f"layout.add_widget(Zaino.boxnomeslot{slot_nm + 1}n)")

    layout.add_widget(Label(size_hint=(0.15, 0.04), pos_hint={"x": 0.5, "y": 0.8}, text="Non Magici"))

    y1 = 0.755

    for slotn in range(1, 21):
        exec(
            f"""Zaino.boxidslot{slotn}m = TextInput(size_hint = (0.02,0.04), pos_hint={{"x": 0.675, "y":{y1}}}, padding = (3,3,0,0), font_size = 12)""")
        exec(
            f"""Zaino.boxnomeslot{slotn}m = TextInput(size_hint = (0.15,0.04), pos_hint={{"x": 0.695, "y":{y1}}}, padding = (3,3,0,0), font_size = 15)""")
        y1 -= 0.04

    for slot_nm in range(int(Shared.npc_selezionato['slot_zaino_magici'])):
        exec(f"layout.add_widget(Zaino.boxidslot{slot_nm + 1}m)")
        exec(f"layout.add_widget(Zaino.boxnomeslot{slot_nm + 1}m)")

    layout.add_widget(Label(size_hint=(0.15, 0.04), pos_hint={"x": 0.66, "y": 0.8}, text="Magici"))

    layout.add_widget(Label(size_hint=(0.03, 0.05), pos_hint={"x": 0, "y": 0.95}, text="ID"))
    boxid = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.11, 0.05), pos_hint={"x": 0.15, "y": 0.95}, text="Nome"))
    boxnome = TextInput(size_hint=(0.11, 0.05), pos_hint={"x": 0.15, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.03, 0.05), pos_hint={"x": 0.26, "y": 0.95}, text="Livello"))
    boxlivello = TextInput(size_hint=(0.03, 0.05), pos_hint={"x": 0.26, "y": 0.9})
    layout.add_widget(Button(size_hint=(0.12, 0.05), pos_hint={"x": 0.29, "y": 0.95}, text="Razza", on_release=partial(Popups_NPC_Dettagli.apri, Shared.npc_selezionato, numeronpc)))
    boxrazza = TextInput(size_hint=(0.12, 0.05), pos_hint={"x": 0.29, "y": 0.90})
    boxzaino1 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.41, "y": 0.9}, font_size=12)
    boxzaino2 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.55, "y": 0.9}, font_size=12)
    boxzaino3 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.69, "y": 0.9}, font_size=12)
    boxzaino4 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.0, "y": 0.85}, font_size=12)
    boxzaino5 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.14, "y": 0.85}, font_size=12)
    boxzaino6 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.28, "y": 0.85}, font_size=12)
    boxzaino7 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.42, "y": 0.85}, font_size=12)
    boxzaino8 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.56, "y": 0.85}, font_size=12)
    boxzaino9 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.70, "y": 0.85}, font_size=12)
    boxzaino10 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.84, "y": 0.85}, font_size=12)


    Shared.box_id_per_eventuale_import_da_selezionato = boxid
    layout.add_widget(boxid)
    layout.add_widget(boxnome)
    layout.add_widget(boxlivello)
    layout.add_widget(boxrazza)
    layout.add_widget(boxzaino1)
    layout.add_widget(boxzaino2)
    layout.add_widget(boxzaino3)
    layout.add_widget(boxzaino4)
    layout.add_widget(boxzaino5)
    layout.add_widget(boxzaino6)
    layout.add_widget(boxzaino7)
    layout.add_widget(boxzaino8)
    layout.add_widget(boxzaino9)
    layout.add_widget(boxzaino10)

    def fooXX(slot, *args):
        if slot == "ar1":
            ids = str(548)
            txt = "Mani Nude"
        elif slot == "ar2":
            ids = str(548)
            txt = "Mani Nude"
        elif slot == "se1":
            ids = str(549)
            txt = "No Armatura"
        elif slot == "se2":
            ids = str(564)
            txt = "No Scudo"
        elif slot == "se3":
            ids = str(579)
            txt = "No Chain"
        elif slot == "se4":
            ids = str(594)
            txt = "No Vesti"
        elif slot[:2] == "eq":
            if int(slot[2:]) < 9:
                ids = str(643)
                txt = "No Anello"
            elif int(slot[2:]) < 15:
                ids = str(1242)
                txt = "No Orecchino"
            elif int(slot[2:]) < 16:
                ids = str(1841)
                txt = "No Spilla"
            elif int(slot[2:]) < 17:
                ids = str(2440)
                txt = "No Fascia"
            elif int(slot[2:]) < 18:
                ids = str(3039)
                txt = "No Mantello"
            elif int(slot[2:]) < 19:
                ids = str(3638)
                txt = "No Amuleto"
            elif int(slot[2:]) < 20:
                ids = str(4237)
                txt = "No Cintura"

        exec(f"Zaino.boxidslot{slot}.text = ids")
        exec(f"Zaino.boxnomeslot{slot}.text = txt")

    if Shared.mastermode:
        layout.add_widget(
            Button(size_hint=(0.07, 0.05), pos_hint={"x": 0.79, "y": 0.95}, text="Adv. Sel.",
                   on_release=sleziona_adv_npc))

    layout.add_widget(Button(size_hint=(0.07, 0.05), pos_hint={"x": 0.86, "y": 0.9}, text="Cerca", on_release=cerca))
    layout.add_widget(Button(size_hint=(0.07, 0.05), pos_hint={"x": 0.93, "y": 0.9}, text="Libera", on_release=libera))
    layout.add_widget(Button(size_hint=(0.07, 0.05), pos_hint={"x": 0.86, "y": 0.95}, text="Scegli", on_release=scegli_npc))
    layout.add_widget(Button(size_hint=(0.07, 0.05), pos_hint={"x": 0.93, "y": 0.95}, text="Imp. Cartella", on_release=impcartella))
    layout.add_widget(Button(size_hint=(0.035, 0.05), pos_hint={"x": 0.810, "y": 0.8}, text="Rand.\nDifen.",
                             on_release=rieqequip))
    layout.add_widget(Button(size_hint=(0.035, 0.05), pos_hint={"x": 0.845, "y": 0.8}, text="Rand.\nAcces.",
                             on_release=rieqaccess))
    layout.add_widget(Button(size_hint=(0.035, 0.05), pos_hint={"x": 0.810, "y": 0.75}, text="Rand.\nArma",
                             on_release=rieqarma))
    layout.add_widget(Button(size_hint=(0.095, 0.05), pos_hint={"x": 0.88, "y": 0.8}, text="Importa",
                             on_release=partial(aggiungi)))
    layout.add_widget(Button(size_hint=(0.05, 0.05), pos_hint={"x": 0.948, "y": 0.75}, text="  SALVA\n(solo pg)",
                             on_release=crea_e_salva_nuovo_npc))
    layout.add_widget(Button(size_hint=(0.023, 0.05), pos_hint={"x": 0.975, "y": 0.8}, text="Rieq",
                             on_release=partial(rieq)))
    layout.add_widget(Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.0, "y": 0.8}, text="Armi:"))
    Zaino.boxidslotar1 = TextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.0095, "y": 0.77}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotar2 = TextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.0095, "y": 0.735}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxnomeslotar1 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.031, "y": 0.77}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.boxnomeslotar2 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.031, "y": 0.735}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.bottooneXXar1 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.13, "y": 0.77}, text="X", font_size=12,
                                 on_release=partial(fooXX, "ar1"))
    Zaino.bottooneXXar2 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.13, "y": 0.735}, text="X", font_size=12,
                                 on_release=partial(fooXX, "ar2"))

    layout.add_widget(Zaino.boxidslotar1)
    layout.add_widget(Zaino.boxidslotar2)
    layout.add_widget(Zaino.boxnomeslotar1)
    layout.add_widget(Zaino.boxnomeslotar2)
    layout.add_widget(Zaino.bottooneXXar1)
    layout.add_widget(Zaino.bottooneXXar2)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.18, "y": 0.805}, font_size=14, text="  Set: \n Scudo:"))
    Zaino.boxidslotse1 = TextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.1655, "y": 0.77}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotse2 = TextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.1655, "y": 0.735}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxnomeslotse1 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.19, "y": 0.77}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.boxnomeslotse2 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.19, "y": 0.735}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.bottooneXXse1 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.29, "y": 0.77}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se1"))
    Zaino.bottooneXXse2 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.29, "y": 0.735}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se2"))

    layout.add_widget(Zaino.boxidslotse1)
    layout.add_widget(Zaino.boxidslotse2)
    layout.add_widget(Zaino.boxnomeslotse1)
    layout.add_widget(Zaino.boxnomeslotse2)
    layout.add_widget(Zaino.bottooneXXse1)
    layout.add_widget(Zaino.bottooneXXse2)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.32, "y": 0.805}, font_size=14, text="Chainmail: \n Veste:"))
    Zaino.boxidslotse3 = TextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.3255, "y": 0.77}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotse4 = TextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.3255, "y": 0.735}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxnomeslotse3 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.35, "y": 0.77}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.boxnomeslotse4 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.35, "y": 0.735}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.bottooneXXse3 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.45, "y": 0.77}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se3"))
    Zaino.bottooneXXse4 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.45, "y": 0.735}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se4"))

    layout.add_widget(Zaino.boxidslotse3)
    layout.add_widget(Zaino.boxidslotse4)
    layout.add_widget(Zaino.boxnomeslotse3)
    layout.add_widget(Zaino.boxnomeslotse4)
    layout.add_widget(Zaino.bottooneXXse3)
    layout.add_widget(Zaino.bottooneXXse4)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.85, "y": 0.735}, font_size=14, text="Extra:"))
    boxextra1 = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0.852, "y": 0.7}, font_size=12,
                          padding=(3, 3, 3, 3))
    boxextra2 = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0.852, "y": 0.65}, font_size=12,
                          padding=(3, 3, 3, 3))
    boxextra3 = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0.852, "y": 0.6}, font_size=12,
                          padding=(3, 3, 3, 3))
    boxextra4 = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0.852, "y": 0.55}, font_size=12,
                          padding=(3, 3, 3, 3))
    boxextra5 = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0.852, "y": 0.5}, font_size=12,
                          padding=(3, 3, 3, 3))
    layout.add_widget(boxextra1)
    layout.add_widget(boxextra2)
    layout.add_widget(boxextra3)
    layout.add_widget(boxextra4)
    layout.add_widget(boxextra5)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0, "y": 0.69}, font_size=14, text="Anelli:"))

    yanelli = 0.67
    for item in range(1, 9):
        exec(
            f"""Zaino.boxidsloteq{item} = TextInput(size_hint=(0.025, 0.03), pos_hint={{"x": 0.0095, "y": {yanelli}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(
            f"""Zaino.boxnomesloteq{item} = TextInput(size_hint=(0.1, 0.03), pos_hint={{"x": 0.031, "y":{yanelli}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(
            f"""Zaino.bottooneXXeq{item} = Button(size_hint=(0.015, 0.03), pos_hint={{"x": 0.13, "y": {yanelli}}}, text="X", font_size=12,on_release=partial(fooXX,'eq{item}'))""")

        exec(f"""layout.add_widget(Zaino.boxidsloteq{item})""")
        exec(f"""layout.add_widget(Zaino.boxnomesloteq{item})""")
        exec(f"""layout.add_widget(Zaino.bottooneXXeq{item})""")
        yanelli -= 0.03

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0, "y": 0.42}, font_size=14, text="Orecchini:"))
    yorecchini = 0.4
    for item in range(9, 20):
        exec(
            f"""Zaino.boxidsloteq{item} = TextInput(size_hint=(0.025, 0.03), pos_hint={{"x": 0.0095, "y": {yorecchini}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(
            f"""Zaino.boxnomesloteq{item} = TextInput(size_hint=(0.1, 0.03), pos_hint={{"x": 0.031, "y":{yorecchini}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(
            f"""Zaino.bottooneXXeq{item} = Button(size_hint=(0.015, 0.03), pos_hint={{"x": 0.13, "y": {yorecchini}}}, text="X", font_size=12,on_release=partial(fooXX,'eq{item}'))""")

        exec(f"""layout.add_widget(Zaino.boxidsloteq{item})""")
        exec(f"""layout.add_widget(Zaino.boxnomesloteq{item})""")
        exec(f"""layout.add_widget(Zaino.bottooneXXeq{item})""")
        yorecchini -= 0.03
        a = yorecchini * 100
        if 19 < a < 22:
            yorecchini -= 0.05

    def copri(*args, bottone):
        if Shared.mastermode:
            exec(f"""
if Zaino.{bottone}.background_color == [0,0,0,1]:
    exec(f"Zaino.{bottone}.background_color=0,0,0,0")
elif Zaino.{bottone}.background_color == [0,0,0,0]:
    exec(f"Zaino.{bottone}.background_color=0,0,0,1")
""")

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.8, "y": 0.435}, font_size=14, text="PF tot:"))
    boxpftot = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.4}, font_size=15,
                         padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['pf_tot']))
    Zaino.boxpftotcover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.4}, background_color=(0, 0, 0, 1),
                                 on_release=partial(copri, bottone="boxpftotcover"))
    layout.add_widget(boxpftot)
    layout.add_widget(Zaino.boxpftotcover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.84, "y": 0.435}, font_size=14, text="Danno:"))
    boxdanno = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.4}, font_size=15,
                         padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['danno']))
    Zaino.boxdannocover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.4}, background_color=(0, 0, 0, 1),
                                 on_release=partial(copri, bottone="boxdannocover"))
    layout.add_widget(boxdanno)
    layout.add_widget(Zaino.boxdannocover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.88, "y": 0.435}, font_size=14, text="Disp.:"))
    boxpfdis = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.4}, font_size=15,
                         padding=(3, 3, 3, 3), text=str(int(Shared.npc_selezionato['pf_tot']) - int(Shared.npc_selezionato['danno'])))
    Zaino.boxpfdiscover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.4}, background_color=(0, 0, 0, 1),
                                 on_release=partial(copri, bottone="boxpfdiscover"))
    layout.add_widget(boxpfdis)
    layout.add_widget(Zaino.boxpfdiscover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.8, "y": 0.35}, font_size=14, text="Att.:"))
    boxattacco = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.315}, font_size=15,
                           padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['attacco_tot']))
    Zaino.boxattaccocover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.315},
                                   background_color=(0, 0, 0, 1),
                                   on_release=partial(copri, bottone="boxattaccocover"))
    layout.add_widget(boxattacco)
    layout.add_widget(Zaino.boxattaccocover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.84, "y": 0.35}, font_size=14, text="Def.:"))
    boxdifesa = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.315}, font_size=15,
                          padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['difesa_tot']))
    Zaino.boxdifesacover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.315},
                                  background_color=(0, 0, 0, 1),
                                  on_release=partial(copri, bottone="boxdifesacover"))
    layout.add_widget(boxdifesa)
    layout.add_widget(Zaino.boxdifesacover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.88, "y": 0.35}, font_size=14, text="Vel.:"))
    boxvelocita = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.315}, font_size=15,
                            padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['velocita_tot']))
    Zaino.boxvelocitacover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.315},
                                    background_color=(0, 0, 0, 1),
                                    on_release=partial(copri, bottone="boxvelocitacover"))
    layout.add_widget(boxvelocita)
    layout.add_widget(Zaino.boxvelocitacover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.8, "y": 0.265}, font_size=14, text="Res. Con.:"))
    boxrescon = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.23}, font_size=15,
                          padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['res_contundente']))
    Zaino.boxresconcover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.23},
                                  background_color=(0, 0, 0, 1),
                                  on_release=partial(copri, bottone="boxresconcover"))
    layout.add_widget(boxrescon)
    layout.add_widget(Zaino.boxresconcover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.84, "y": 0.265}, font_size=14, text="Res. Tag.:"))
    boxrestag = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.23}, font_size=15,
                          padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['res_taglio']))
    Zaino.boxrestagcover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.23},
                                  background_color=(0, 0, 0, 1),
                                  on_release=partial(copri, bottone="boxrestagcover"))
    layout.add_widget(boxrestag)
    layout.add_widget(Zaino.boxrestagcover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.88, "y": 0.265}, font_size=14, text="Res. Per.:"))
    boxresper = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.23}, font_size=15,
                          padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['res_perforante']))
    Zaino.boxrespercover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.23},
                                  background_color=(0, 0, 0, 1),
                                  on_release=partial(copri, bottone="boxrespercover"))
    layout.add_widget(boxresper)
    layout.add_widget(Zaino.boxrespercover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.8, "y": 0.18}, font_size=14, text="Res F/G/E"))
    boxresmag = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.145}, font_size=15,
                          padding=(3, 3, 3, 3), text=f"{str(Shared.npc_selezionato['res_fuoco'])}/"
                                                     f"{str(Shared.npc_selezionato['res_gelo'])}"
                                                     f"/{str(Shared.npc_selezionato['res_elettro'])}")
    Zaino.boxresmagcover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.85, "y": 0.145},
                                  background_color=(0, 0, 0, 1),
                                  on_release=partial(copri, bottone="boxresmagcover"))
    layout.add_widget(boxresmag)
    layout.add_widget(Zaino.boxresmagcover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.84, "y": 0.18}, font_size=14, text="Forza"))
    boxresforza = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.145}, font_size=15,
                            padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['forza_tot']))
    Zaino.boxresforzacover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.89, "y": 0.145},
                                    background_color=(0, 0, 0, 1),
                                    on_release=partial(copri, bottone="boxresforzacover"))
    layout.add_widget(boxresforza)
    layout.add_widget(Zaino.boxresforzacover)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.88, "y": 0.18}, font_size=14, text="Livello"))
    boxlivello2 = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.145}, font_size=15,
                            padding=(3, 3, 3, 3), text=str(Shared.npc_selezionato['livello']))
    Zaino.boxlivello2cover = Button(size_hint=(0.04, 0.05), pos_hint={"x": 0.93, "y": 0.145},
                                    background_color=(0, 0, 0, 1),
                                    on_release=partial(copri, bottone="boxlivello2cover"))
    layout.add_widget(boxlivello2)
    layout.add_widget(Zaino.boxlivello2cover)

    ids = Shared.npc_numeri_assegnati[numeronpc]['nome_valore_excel']
    risultato0 = Inizializza.trova_pgnpc(ids=ids)
    boxid.text = str(Shared.npc_selezionato['nome_valore_excel'])
    boxnome.text = str(Shared.npc_selezionato["nomepg"])
    boxlivello.text = str(Shared.npc_selezionato["livello"])
    boxrazza.text = str(Shared.npc_selezionato["razza1"] + " - " + Shared.npc_selezionato["razza2"] + " - " + Shared.npc_selezionato["razza3"])
    boxzaino1.text = str(Shared.npc_selezionato["zaino_slot_1"])
    boxzaino2.text = str(Shared.npc_selezionato["zaino_slot_2"])
    boxzaino3.text = str(Shared.npc_selezionato["zaino_slot_3"])
    boxzaino4.text = str(Shared.npc_selezionato["zaino_slot_4"])
    boxzaino5.text = str(Shared.npc_selezionato["zaino_slot_5"])
    boxzaino6.text = str(Shared.npc_selezionato["zaino_slot_6"])
    boxzaino7.text = str(Shared.npc_selezionato["zaino_slot_7"])
    boxzaino8.text = str(Shared.npc_selezionato["zaino_slot_8"])
    boxzaino9.text = str(Shared.npc_selezionato["zaino_slot_9"])
    boxzaino10.text = str(Shared.npc_selezionato["zaino_slot_10"])
    boxextra1.text = str(Shared.npc_selezionato["extra1"])
    boxextra2.text = str(Shared.npc_selezionato["extra2"])
    boxextra3.text = str(Shared.npc_selezionato["extra3"])
    boxextra4.text = str(Shared.npc_selezionato["extra4"])
    boxextra5.text = str(Shared.npc_selezionato["extra5"])

    numeroeq = 1
    for item in Oggetti.equipaggiabili:
        exec(f"""{item} = Oggetti.trova_oggetto(ids = str(Shared.npc_selezionato['equip_{item}']))""")
        exec(f"""Zaino.boxidsloteq{numeroeq}.text = str({item}['ID'])""")
        exec(f"""Zaino.boxnomesloteq{numeroeq}.text = {item}['NOME']""")
        numeroeq += 1
    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0, "y": 0.2}, font_size=14,
              text="Spilla/Fascia/Mantello/\nAmuleto/Cintura:"))

    layout.add_widget(
        Image(size_hint=(0.5, 0.5), pos_hint={"x": 0.08, "y": 0.15}, source="Art\omino.png"))

    layout.add_widget(Button(text="Esci", pos_hint={"x": 0.9, "y": 1}, color=(1, 1, 1, 1),
                             size_hint=(0.05, 0.05), on_release=popup.dismiss))
    importa()
    popup.open()
