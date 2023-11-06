import Moduli.SharedData as Shared

import os
from Moduli.Grafica import Popups_Notifiche, FinestraPrincipaleMain, Popups_Alchimia, Popups_NomePG_Oggetti_Tutti, \
    Popups_Negozio, Popups_Calcolatrice
from Moduli.Logica import Oggetti, EquipAttore, Salvataggio
from kivy.clock import Clock
from kivy.compat import string_types
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import partial, StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
# from Moduli.Grafica.KivyInput import InfoTextInput




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
    boxid = ""

def zainoopen():
    from Moduli.Grafica.KivyInput import InfoTextInput
    Builder.load_string("""
<Label>:
    color: 0,0,0,1
<TextInput>:
    background_color: 1,1,1,0.7""")

    Builder.load_string("""
<InfoTextInput>:
    background_color: 1,1,1,0.7
<Tooltip>:
    size_hint: None, None
    size: self.texture_size[0]+5, self.texture_size[1]+5
    color: 0,0,0,1
    canvas.before:
        Color:
            rgba: (1, 1, 1, 0.83)
        Rectangle:
            size: self.size
            pos: self.pos

    """)


    layout = FloatLayout()
    popup = Popup(title=f"Zaino", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1730, 850),
                  auto_dismiss=False)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/zainobg.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    layout.add_widget(notepic)

    layout.add_widget(
        Image(size_hint=(0.4, 0.4), pos_hint={"x": 0.03, "y": 0.32}, source=f"{Shared.path_art}/omino.png"))

    sourceritratto = ""
    pathrisorse = f'{Shared.path_art}/bgeritrattipg'
    nome = Shared.pg_selezionato["nomepg"]
    for file in os.listdir(pathrisorse):
        if file.startswith(f"ritratto{nome}"):
            sourceritratto = f'{pathrisorse}/ritratto{nome}.png'
            break
        else:
            nome = Shared.pg_selezionato["nome_valore_excel"][6:]
            cartella = os.listdir(Shared.path_art + f"/bgeritrattipg")
            if f"miniritratto{nome}.png" in cartella:
                sourceritratto = Shared.path_art + f"/bgeritrattipg/ritratto{nome}.png"
            else:
                sourceritratto = Shared.path_art + f"/empty.png"

    layout.add_widget(
        Image(size_hint=(0.4, 0.4), pos_hint={"x": 0.17, "y": 0.32}, source=sourceritratto))



    def cerca(*args):
        nomes = ""
        ids = ""
        boxtipo1s = ""
        boxtipo2s = ""
        boxtipo3s = ""
        if len(Zaino.boxid.text) > 0:
            ids = str(Zaino.boxid.text)
        else:
            if len(boxnome.text) > 0:
                nomes = str(boxnome.text)
            if len(boxtipo1.text) > 0:
                boxtipo1s = str(boxtipo1.text)
            if len(boxtipo2.text) > 0:
                boxtipo2s = str(boxtipo2.text)

        risultato = Oggetti.trova_oggetto(ids=ids, nome=nomes, boxtipo1=boxtipo1s, boxtipo2=boxtipo2s)

        if type(risultato) == dict:
            Zaino.boxid.text = str(risultato["ID"])
            boxnome.text = str(risultato["NOME"])
            boxtipo1.text = str(risultato["TIPO1"])
            boxtipo2.text = str(risultato["TIPO2"])
            boxtipo3.text = str(risultato["TIPO3"])
            boxdescrizione.text = str(risultato["DESCRIZIONE"])
            boxvalore.text = str(risultato["VALORE"])
            boxslot.text = str(risultato["SLOT"])
            boxeff1.text = str(risultato["EFFETTO1"])
            boxeff2.text = str(risultato["EFFETTO2"])
            boxeff3.text = str(risultato["EFFETTO3"])
            boxeff4.text = str(risultato["EFFETTO4"])
            boxeff5.text = str(risultato["EFFETTO5"])
            boxeff6.text = str(risultato["EFFETTO6"])
            boxeff7.text = str(risultato["EFFETTO7"])
        elif type(risultato) == list:
            if len(risultato) == 1:
                risultato = risultato[0]
                Zaino.boxid.text = str(risultato["ID"])
                boxnome.text = str(risultato["NOME"])
                boxtipo1.text = str(risultato["TIPO1"])
                boxtipo2.text = str(risultato["TIPO2"])
                boxtipo3.text = str(risultato["TIPO3"])
                boxdescrizione.text = str(risultato["DESCRIZIONE"])
                boxvalore.text = str(risultato["VALORE"])
                boxslot.text = str(risultato["SLOT"])
                boxeff1.text = str(risultato["EFFETTO1"])
                boxeff2.text = str(risultato["EFFETTO2"])
                boxeff3.text = str(risultato["EFFETTO3"])
                boxeff4.text = str(risultato["EFFETTO4"])
                boxeff5.text = str(risultato["EFFETTO5"])
                boxeff6.text = str(risultato["EFFETTO6"])
                boxeff7.text = str(risultato["EFFETTO7"])
            else:
                barraricerca.text = ""

                for singolo in risultato:
                    barraricerca.text += "\n"
                    stringa = f"{singolo['ID']} - {singolo['NOME']} - {singolo['DESCRIZIONE'][:20]}"
                    barraricerca.text += stringa
                if Temp.showbarraricercazaino == False:
                    showbarraricerca()

    def showbarraricerca(*args):
        if Temp.showbarraricercazaino == True:
            barraricerca.pos_hint={"x": 1.84, "y": 1.85}
            Temp.showbarraricercazaino = False
        else:
            barraricerca.pos_hint={"x": 0, "y": 0.59}
            Temp.showbarraricercazaino = True
    def libera(*args):
        Zaino.boxid.text = ""
        boxnome.text = ""
        boxtipo1.text = ""
        boxtipo2.text = ""
        boxtipo3.text = ""
        boxdescrizione.text = ""
        boxvalore.text = ""
        boxslot.text = ""
        boxeff1.text = ""
        boxeff2.text = ""
        boxeff3.text = ""
        boxeff4.text = ""
        boxeff5.text = ""
        boxeff6.text = ""
        boxeff7.text = ""

    def bevi(*args):
        pozioneid = boxbevi.text
        try:
            pozione = Oggetti.trova_oggetto(pozioneid)
            exec(pozione[8])
            boxbevi.text = "BEVUTA"
        except:
            pass

    def aggiungi(*args):
        if Zaino.selezionato == "00":
            Popups_Notifiche.noslotselezionato()

        elif Zaino.boxid.text == "":
            exec(f"""Zaino.boxidslot{Zaino.selezionato}.text = '{Zaino.boxid.text}'""")
            exec(f"""Zaino.boxnomeslot{Zaino.selezionato}.text = '{boxnome.text}'""")
        else:
            cerca()
            exec(f"""Zaino.boxidslot{Zaino.selezionato}.text = '{Zaino.boxid.text}'""")
            exec(f"""Zaino.boxnomeslot{Zaino.selezionato}.text = '{boxnome.text}'""")

    def apritutti(*args):
        Popups_NomePG_Oggetti_Tutti.oggetti_tutti_open()

    def importa(*args):
        Zaino.da_mettere = []
        ignora = ["Vuoto", "", " ", "None", None, "Slot1", "1", 1]
        for item in range(1, 41):
            if eval(f"Shared.pg_selezionato['zaino_slot_{item}']") not in ignora:
                Zaino.da_mettere.append(eval(f"Shared.pg_selezionato['zaino_slot_{item}']"))

        for slot_m in range(int(Shared.pg_selezionato['slot_zaino_magici'])):
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

        for slot_n in range(int(Shared.pg_selezionato['slot_zaino_non_magici'])):
            if len(Zaino.da_mettere) > 0:
                if str(Zaino.da_mettere[0])[:3] == "id:":
                    oggetto = Oggetti.trova_oggetto(ids=str(eval(Zaino.da_mettere[0][3:])))
                    nome = oggetto['NOME']
                    ids = oggetto['ID']
                    exec(f"Zaino.boxidslot{slot_n + 1}n.text = str(ids)")
                    exec(f"Zaino.boxnomeslot{slot_n + 1}n.text = nome")
                else:
                    exec(f"Zaino.boxnomeslot{slot_n + 1}n.text = str(Zaino.da_mettere[0])")
                    if len(str(Zaino.da_mettere[0])) > 15:
                        exec(f"Zaino.boxnomeslot{slot_n + 1}n.font_size = 12")
                    if len(str(Zaino.da_mettere[0])) > 22:
                        exec(f"Zaino.boxnomeslot{slot_n + 1}n.font_size = 10")
                Zaino.da_mettere.pop(0)

        for note in range(1, 5):
            exec(f"""Zaino.boxnote{note}.text = str(Shared.pg_selezionato['note_zaino_{note}'])""")

        arma1 = Oggetti.trova_oggetto(ids=str(Shared.pg_selezionato['id_arma_1']))
        Zaino.boxidslotar1.text = str(arma1['ID'])
        Zaino.boxnomeslotar1.text = arma1['NOME']
        arma2 = Oggetti.trova_oggetto(ids=str(Shared.pg_selezionato['id_arma_2']))
        Zaino.boxidslotar2.text = str(arma2['ID'])
        Zaino.boxnomeslotar2.text = arma2['NOME']
        armatura = Oggetti.trova_oggetto(ids=str(Shared.pg_selezionato['id_armatura']))
        Zaino.boxidslotse1.text = str(armatura['ID'])
        Zaino.boxnomeslotse1.text = armatura['NOME']
        scudo = Oggetti.trova_oggetto(ids=str(Shared.pg_selezionato['id_scudo']))
        Zaino.boxidslotse2.text = str(scudo['ID'])
        Zaino.boxnomeslotse2.text = scudo['NOME']
        chainmail = Oggetti.trova_oggetto(ids=str(Shared.pg_selezionato['id_chainmail']))
        Zaino.boxidslotse3.text = str(chainmail['ID'])
        Zaino.boxnomeslotse3.text = chainmail['NOME']
        veste = Oggetti.trova_oggetto(ids=str(Shared.pg_selezionato['id_veste']))
        Zaino.boxidslotse4.text = str(veste['ID'])
        Zaino.boxnomeslotse4.text = veste['NOME']
        numeroeq = 1
        for item in Oggetti.equipaggiabili:
            exec(f"""{item} = Oggetti.trova_oggetto(ids = int(Shared.pg_selezionato['equip_{item}']))""")
            exec(f"""Zaino.boxidsloteq{numeroeq}.text = str({item}['ID'])""")
            exec(f"""Zaino.boxnomesloteq{numeroeq}.text = {item}['NOME']""")
            numeroeq += 1

    Zaino.selezionato = "00"

    y1 = 0.755

    for slotn in range(1, 21):
        exec(
            f"""Zaino.boxidslot{slotn}n = InfoTextInput(size_hint = (0.02,0.04), pos_hint={{"x": 0.48, "y":{y1}}}, padding = (3,3,0,0), font_size = 12)""")
        exec(f"Zaino.boxidslot{slotn}n.tooltip_txt = 'Zaino.boxidslot{slotn}n'")
        exec(
            f"""Zaino.boxnomeslot{slotn}n = TextInput(size_hint = (0.15,0.04), pos_hint={{"x": 0.5, "y":{y1}}}, padding = (3,3,0,0), font_size = 15)""")
        y1 -= 0.04

    for slot_nm in range(int(Shared.pg_selezionato['slot_zaino_non_magici'])):
        exec(f"layout.add_widget(Zaino.boxidslot{slot_nm + 1}n)")
        exec(f"layout.add_widget(Zaino.boxnomeslot{slot_nm + 1}n)")

    layout.add_widget(Label(size_hint=(0.15, 0.04), pos_hint={"x": 0.5, "y": 0.8}, text="Non Magici"))

    y1 = 0.755

    for slotn in range(1, 21):
        exec(
            f"""Zaino.boxidslot{slotn}m = InfoTextInput(size_hint = (0.02,0.04), pos_hint={{"x": 0.660, "y":{y1}}}, padding = (3,3,0,0), font_size = 12)""")
        exec(f"Zaino.boxidslot{slotn}m.tooltip_txt = 'Zaino.boxidslot{slotn}m'")
        exec(
            f"""Zaino.boxnomeslot{slotn}m = TextInput(size_hint = (0.15,0.04), pos_hint={{"x": 0.680, "y":{y1}}}, padding = (3,3,0,0), font_size = 15)""")
        y1 -= 0.04

    for slot_nm in range(int(Shared.pg_selezionato['slot_zaino_magici'])):
        exec(f"layout.add_widget(Zaino.boxidslot{slot_nm + 1}m)")
        exec(f"layout.add_widget(Zaino.boxnomeslot{slot_nm + 1}m)")

    layout.add_widget(Label(size_hint=(0.15, 0.04), pos_hint={"x": 0.66, "y": 0.8}, text="Magici"))

    layout.add_widget(Label(size_hint=(0.03, 0.05), pos_hint={"x": 0, "y": 0.95}, text="ID"))
    Zaino.boxid = InfoTextInput(size_hint=(0.03, 0.05), pos_hint={"x": 0, "y": 0.9})
    Zaino.boxid.tooltip_txt = "Zaino.boxid"
    layout.add_widget(Label(size_hint=(0.05, 0.05), pos_hint={"x": 0.025, "y": 0.95}, text="Nome"))
    boxnome = TextInput(size_hint=(0.15, 0.05), pos_hint={"x": 0.03, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.18, "y": 0.95}, text="Tipo 1(daga,pozione...)"))
    boxtipo1 = TextInput(size_hint=(0.1, 0.05), pos_hint={"x": 0.18, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.28, "y": 0.95}, text="Tipo 2(materiale, livello)"))
    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.38, "y": 0.95}, text="Tipo 3(contundente,...)"))
    boxtipo2 = TextInput(size_hint=(0.1, 0.05), pos_hint={"x": 0.28, "y": 0.90})
    boxtipo3 = TextInput(size_hint=(0.1, 0.05), pos_hint={"x": 0.38, "y": 0.90})
    layout.add_widget(Label(size_hint=(0.42, 0.05), pos_hint={"x": 0.48, "y": 0.95}, text="Descrizione"))
    boxdescrizione = TextInput(size_hint=(0.42, 0.05), font_size=13, pos_hint={"x": 0.48, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.05, 0.05), pos_hint={"x": 0.9, "y": 0.95}, text="Valore"))
    boxvalore = TextInput(size_hint=(0.05, 0.05), pos_hint={"x": 0.9, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.03, 0.05), pos_hint={"x": 0.95, "y": 0.95}, text="Peso"))
    boxslot = TextInput(size_hint=(0.03, 0.05), pos_hint={"x": 0.95, "y": 0.9})
    boxeff1 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.0, "y": 0.85}, font_size=12)
    boxeff2 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.14, "y": 0.85}, font_size=12)
    boxeff3 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.28, "y": 0.85}, font_size=12)
    boxeff4 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.42, "y": 0.85}, font_size=12)
    boxeff5 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.56, "y": 0.85}, font_size=12)
    boxeff6 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.70, "y": 0.85}, font_size=12)
    boxeff7 = TextInput(size_hint=(0.14, 0.05), pos_hint={"x": 0.84, "y": 0.85}, font_size=12)
    barraricerca = TextInput(size_hint=(0.3, 0.25), pos_hint={"x": 1.84, "y": 1.85}, font_size=15)
    layout.add_widget(Zaino.boxid)
    layout.add_widget(boxnome)
    layout.add_widget(boxtipo1)
    layout.add_widget(boxtipo2)
    layout.add_widget(boxtipo3)
    layout.add_widget(boxeff1)
    layout.add_widget(boxeff2)
    layout.add_widget(boxeff3)
    layout.add_widget(boxeff4)
    layout.add_widget(boxeff5)
    layout.add_widget(boxeff6)
    layout.add_widget(boxeff7)
    layout.add_widget(boxdescrizione)
    layout.add_widget(boxvalore)
    layout.add_widget(boxslot)

    layout.add_widget(Button(size_hint=(0.035, 0.035), pos_hint={"x": 0.07, "y": 0.985}, text="Tutti", on_release=apritutti))
    layout.add_widget(Button(size_hint=(0.035, 0.035), pos_hint={"x": 0.07, "y": 0.95}, text="Cerca", on_release=cerca))
    layout.add_widget(Button(size_hint=(0.035, 0.035), pos_hint={"x": 0.105, "y": 0.95}, text="Libera", on_release=libera))
    layout.add_widget(Button(size_hint=(0.035, 0.035), pos_hint={"x": 0.14, "y": 0.95}, text="Barra", on_release=showbarraricerca))
    layout.add_widget(Button(size_hint=(0.10, 0.05), pos_hint={"x": 0.88, "y": 0.8}, text="Aggiungi/Rimuovi",
                             on_release=partial(aggiungi)))
    layout.add_widget(Button(size_hint=(0.035, 0.04), pos_hint={"x": 0.39, "y": 0.695}, text="Bevi",
                             on_release=bevi))
    boxbevi = TextInput(size_hint=(0.04, 0.04), pos_hint={"x": 0.425, "y": 0.695}, font_size=12)
    layout.add_widget(boxbevi)
    layout.add_widget(
        Button(size_hint=(0.05, 0.05), pos_hint={"x": 0.85, "y": 0.0}, text="Salva", on_release=Salvataggio.salvazaino))
    layout.add_widget(
        Button(size_hint=(0.10, 0.05), pos_hint={"x": 0.9, "y": 0.0}, text="Salva e Esci",
               on_press=Salvataggio.salvazaino, on_release=popup.dismiss))


    def aggiungiadesegui(*args, dati):
        Zaino.boxesegui.text = dati

    def esegui(*args):
        testo = Zaino.boxesegui.text
        if testo[:11] == "slot magici":
            if "+=" in testo:
                parte2 = testo.split("+=")[1]
                testo = f"Shared.pg_selezionato['slot_zaino_magici'] = int(Shared.pg_selezionato['slot_zaino_magici']) + {str(parte2)}"
            elif "-=" in testo:
                parte2 = testo.split("-=")[1]
                testo = f"Shared.pg_selezionato['slot_zaino_magici'] = int(Shared.pg_selezionato['slot_zaino_magici']) - {str(parte2)}"
        elif testo[:11] == "slot non ma":
            if "+=" in testo:
                parte2 = testo.split("+=")[1]
                testo = f"Shared.pg_selezionato['slot_zaino_non_magici'] = int(Shared.pg_selezionato['slot_zaino_non_magici']) + {str(parte2)}"
            elif "-=" in testo:
                parte2 = testo.split("-=")[1]
                testo = f"Shared.pg_selezionato['slot_zaino_non_magici'] = int(Shared.pg_selezionato['slot_zaino_non_magici']) - {str(parte2)}"

        try:
            exec(testo)
        except:
            Popups_Notifiche.nodigit(stringa=testo)

        FinestraPrincipaleMain.FunzioniFinestra.show_all()

    def equipnpc(*args):
        for slot_m in range(0, 20):
            if eval(f"Zaino.boxidslot{slot_m + 1}m.text") != "":
                exec(f"Shared.pg_selezionato['zaino_slot_{slot_m + 1}'] = 'id:'+Zaino.boxidslot{slot_m + 1}m.text")
            else:
                exec(f"Shared.pg_selezionato['zaino_slot_{slot_m + 1}'] = Zaino.boxnomeslot{slot_m + 1}m.text")

        for slot_n in range(0, 20):
            if eval(f"Zaino.boxidslot{slot_n + 1}n.text") != "":
                exec(f"Shared.pg_selezionato['zaino_slot_{slot_n + 21}'] = 'id:'+Zaino.boxidslot{slot_n + 1}n.text")
            else:
                exec(f"Shared.pg_selezionato['zaino_slot_{slot_n + 21}'] = Zaino.boxnomeslot{slot_n + 1}n.text")

        Shared.pg_selezionato['id_arma_1'] = Zaino.boxidslotar1.text
        Shared.pg_selezionato['id_arma_2'] = Zaino.boxidslotar2.text
        Shared.pg_selezionato['id_armatura'] = Zaino.boxidslotse1.text
        Shared.pg_selezionato['id_scudo'] = Zaino.boxidslotse2.text
        Shared.pg_selezionato['id_chainmail'] = Zaino.boxidslotse3.text
        Shared.pg_selezionato['id_veste'] = Zaino.boxidslotse4.text
        Shared.pg_selezionato['monete'] = Zaino.boxmonete.text
        for note in range(1, 5):
            exec(f"Shared.pg_selezionato['note_zaino_{note}'] = Zaino.boxnote{note}.text")
        numeroeq = 1
        for item in Oggetti.equipaggiabili:
            exec(f"Shared.pg_selezionato['equip_{item}'] = Zaino.boxidsloteq{numeroeq}.text")
            numeroeq += 1
        EquipAttore.equip_npc(Shared.pg_selezionato['nome_in_uso'])
        FinestraPrincipaleMain.FunzioniFinestra.show_all()

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

    Zaino.boxesegui = TextInput(size_hint=(0.17, 0.05), font_size=11, pos_hint={"x": 0.83, "y": 0.75})
    layout.add_widget(Zaino.boxesegui)
    layout.add_widget(Button(size_hint=(0.10, 0.05), pos_hint={"x": 0.87, "y": 0.7}, text="Esegui", on_release=esegui))
    layout.add_widget(Button(size_hint=(0.075, 0.05), pos_hint={"x": 0.85, "y": 0.65}, text="Alchimia",
                             on_release=Popups_Alchimia.alchimiaopen))
    layout.add_widget(Button(size_hint=(0.075, 0.05), pos_hint={"x": 0.925, "y": 0.65}, text="Negozio",
                             on_release=Popups_Negozio.negozio_open))
    layout.add_widget(Button(size_hint=(0.075, 0.05), pos_hint={"x": 0.925, "y": 0.6}, text="Slot Magici",
                             on_release=partial(aggiungiadesegui,
                                                dati="slot magici += ")))
    layout.add_widget(Button(size_hint=(0.075, 0.05), pos_hint={"x": 0.85, "y": 0.6}, text="Slot Normali",
                             on_release=partial(aggiungiadesegui,
                                                dati="slot non magici += ")))
    layout.add_widget(Button(size_hint=(0.03, 0.05), pos_hint={"x": 0.97, "y": 0.7}, text="print", font_size=12,
                             on_release=partial(aggiungiadesegui,
                                                dati=r"print(Shared.pg_selezionato['inserisciqui'])")))
    layout.add_widget(Label(size_hint=(0.07, 0.05), pos_hint={"x": 0.84, "y": 0.55}, text="Monete:"))
    Zaino.boxmonete = TextInput(size_hint=(0.055, 0.05), pos_hint={"x": 0.9, "y": 0.55}, font_size=17,
                                text=str(Shared.pg_selezionato['monete']))
    layout.add_widget(Button(size_hint=(0.045, 0.05), pos_hint={"x": 0.955, "y": 0.55}, text="+-x/", font_size=15,
                             on_release=partial(Popups_Calcolatrice.calcolatrice)))
    Zaino.boxnote1 = TextInput(size_hint=(0.14, 0.08), pos_hint={"x": 0.85, "y": 0.47}, font_size=12)
    Zaino.boxnote2 = TextInput(size_hint=(0.14, 0.14), pos_hint={"x": 0.85, "y": 0.33}, font_size=12)
    Zaino.boxnote3 = TextInput(size_hint=(0.14, 0.14), pos_hint={"x": 0.85, "y": 0.19}, font_size=12)
    Zaino.boxnote4 = TextInput(size_hint=(0.14, 0.14), pos_hint={"x": 0.85, "y": 0.05}, font_size=12)
    layout.add_widget(Zaino.boxmonete)
    layout.add_widget(Zaino.boxnote1)
    layout.add_widget(Zaino.boxnote2)
    layout.add_widget(Zaino.boxnote3)
    layout.add_widget(Zaino.boxnote4)

    layout.add_widget(Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.0, "y": 0.8}, text="Armi:"))
    Zaino.boxidslotar1 = InfoTextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.0095, "y": 0.77}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotar1.tooltip_txt = "Zaino.boxidslotar1"

    Zaino.boxidslotar2 = InfoTextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.0095, "y": 0.735}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotar2.tooltip_txt = "Zaino.boxidslotar2"
    Zaino.boxnomeslotar1 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.031, "y": 0.77}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.boxnomeslotar2 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.031, "y": 0.735}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.bottooneeqar1 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.13, "y": 0.77}, text="EQ", font_size=12,
                                 on_release=equipnpc)
    Zaino.bottooneXXar1 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.145, "y": 0.77}, text="X", font_size=12,
                                 on_release=partial(fooXX, "ar1"))
    Zaino.bottooneXXar2 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.145, "y": 0.735}, text="X", font_size=12,
                                 on_release=partial(fooXX, "ar2"))
    layout.add_widget(Zaino.boxidslotar1)
    layout.add_widget(Zaino.boxidslotar2)
    layout.add_widget(Zaino.boxnomeslotar1)
    layout.add_widget(Zaino.boxnomeslotar2)
    layout.add_widget(Zaino.bottooneeqar1)
    layout.add_widget(Zaino.bottooneXXar1)
    layout.add_widget(Zaino.bottooneXXar2)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.18, "y": 0.805}, font_size=14, text="  Set: \n Scudo:"))

    Zaino.boxidslotse1 = InfoTextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.1655, "y": 0.77}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotse1.tooltip_txt = "Zaino.boxidslotse1"
    Zaino.boxidslotse2 = InfoTextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.1655, "y": 0.735}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotse2.tooltip_txt = "Zaino.boxidslotse2"
    Zaino.boxnomeslotse1 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.19, "y": 0.77}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.boxnomeslotse2 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.19, "y": 0.735}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.bottooneeqse1 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.29, "y": 0.77}, text="EQ", font_size=12,
                                 on_release=equipnpc)
    Zaino.bottooneeqse2 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.29, "y": 0.735}, text="EQ", font_size=12,
                                 on_release=equipnpc)
    Zaino.bottooneXXse1 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.305, "y": 0.77}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se1"))
    Zaino.bottooneXXse2 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.305, "y": 0.735}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se2"))

    layout.add_widget(Zaino.boxidslotse1)
    layout.add_widget(Zaino.boxidslotse2)
    layout.add_widget(Zaino.boxnomeslotse1)
    layout.add_widget(Zaino.boxnomeslotse2)
    layout.add_widget(Zaino.bottooneeqse1)
    layout.add_widget(Zaino.bottooneeqse2)
    layout.add_widget(Zaino.bottooneXXse1)
    layout.add_widget(Zaino.bottooneXXse2)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0.32, "y": 0.805}, font_size=14, text="Chainmail: \n Veste:"))
    Zaino.boxidslotse3 = InfoTextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.3255, "y": 0.77}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotse3.tooltip_txt = "Zaino.boxidslotse3"
    Zaino.boxidslotse4 = InfoTextInput(size_hint=(0.025, 0.035), pos_hint={"x": 0.3255, "y": 0.735}, font_size=12,
                                   padding=(3, 3, 3, 3))
    Zaino.boxidslotse4.tooltip_txt = "Zaino.boxidslotse4"
    Zaino.boxnomeslotse3 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.35, "y": 0.77}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.boxnomeslotse4 = TextInput(size_hint=(0.1, 0.035), pos_hint={"x": 0.35, "y": 0.735}, font_size=12,
                                     padding=(3, 3, 3, 3))
    Zaino.bottooneeqse3 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.45, "y": 0.77}, text="EQ", font_size=12,
                                 on_release=equipnpc)
    Zaino.bottooneeqse4 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.45, "y": 0.735}, text="EQ", font_size=12,
                                 on_release=equipnpc)
    Zaino.bottooneXXse3 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.465, "y": 0.77}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se3"))
    Zaino.bottooneXXse4 = Button(size_hint=(0.015, 0.035), pos_hint={"x": 0.465, "y": 0.735}, text="X", font_size=12,
                                 on_release=partial(fooXX, "se4"))

    layout.add_widget(Zaino.boxidslotse3)
    layout.add_widget(Zaino.boxidslotse4)
    layout.add_widget(Zaino.boxnomeslotse3)
    layout.add_widget(Zaino.boxnomeslotse4)
    layout.add_widget(Zaino.bottooneeqse3)
    layout.add_widget(Zaino.bottooneeqse4)
    layout.add_widget(Zaino.bottooneXXse3)
    layout.add_widget(Zaino.bottooneXXse4)

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0, "y": 0.69}, font_size=14, text="Anelli:"))

    yanelli = 0.67
    for item in range(1, 9):
        exec(
            f"""Zaino.boxidsloteq{item} = InfoTextInput(size_hint=(0.025, 0.03), pos_hint={{"x": 0.0095, "y": {yanelli}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(f"Zaino.boxidsloteq{item}.tooltip_txt = 'Zaino.boxidsloteq{item}'")
        exec(
            f"""Zaino.boxnomesloteq{item} = TextInput(size_hint=(0.1, 0.03), pos_hint={{"x": 0.031, "y":{yanelli}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(
            f"""Zaino.bottooneeqeq{item} = Button(size_hint=(0.015, 0.03), pos_hint={{"x": 0.13, "y": {yanelli}}}, text="EQ", font_size=12,on_release=equipnpc)""")
        exec(
            f"""Zaino.bottooneXXeq{item} = Button(size_hint=(0.015, 0.03), pos_hint={{"x": 0.145, "y": {yanelli}}}, text="X", font_size=12,on_release=partial(fooXX,'eq{item}'))""")
        exec(f"""layout.add_widget(Zaino.boxidsloteq{item})""")
        exec(f"""layout.add_widget(Zaino.boxnomesloteq{item})""")
        exec(f"""layout.add_widget(Zaino.bottooneeqeq{item})""")
        exec(f"""layout.add_widget(Zaino.bottooneXXeq{item})""")
        yanelli -= 0.03

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0, "y": 0.42}, font_size=14, text="Orecchini:"))
    yorecchini = 0.4
    for item in range(9, 20):
        exec(
            f"""Zaino.boxidsloteq{item} = InfoTextInput(size_hint=(0.025, 0.03), pos_hint={{"x": 0.0095, "y": {yorecchini}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(f"Zaino.boxidsloteq{item}.tooltip_txt = 'Zaino.boxidsloteq{item}'")
        exec(
            f"""Zaino.boxnomesloteq{item} = TextInput(size_hint=(0.1, 0.03), pos_hint={{"x": 0.031, "y":{yorecchini}}}, font_size=12, padding=(3, 3, 0, 3))""")
        exec(
            f"""Zaino.bottooneeqeq{item} = Button(size_hint=(0.015, 0.03), pos_hint={{"x": 0.13, "y": {yorecchini}}}, text="EQ", font_size=12,on_release=equipnpc)""")
        exec(
            f"""Zaino.bottooneXXeq{item} = Button(size_hint=(0.015, 0.03), pos_hint={{"x": 0.145, "y": {yorecchini}}}, text="X", font_size=12,on_release=partial(fooXX,'eq{item}'))""")
        exec(f"""layout.add_widget(Zaino.boxidsloteq{item})""")
        exec(f"""layout.add_widget(Zaino.boxnomesloteq{item})""")
        exec(f"""layout.add_widget(Zaino.bottooneeqeq{item})""")
        exec(f"""layout.add_widget(Zaino.bottooneXXeq{item})""")
        yorecchini -= 0.03
        a = yorecchini * 100
        if 19 < a < 22:
            yorecchini -= 0.05

    layout.add_widget(
        Label(size_hint=(0.14, 0.05), pos_hint={"x": 0, "y": 0.2}, font_size=14,
              text="Spilla/Fascia/Mantello/\nAmuleto/Cintura:"))



    layout.add_widget(Button(text="Esci", pos_hint={"x": 0.9, "y": 1}, color=(1, 1, 1, 1),
                             size_hint=(0.05, 0.05), on_release=popup.dismiss))

    def estrai(*args):
        if Zaino.tipoloot.text == "":
            Zaino.tipoloot.text = "casuale"
        if Zaino.livelloloot.text == "":
            Zaino.livelloloot.text = "casuale"
        if Zaino.fortunaloot.text == "":
            Zaino.fortunaloot.text = "10"

        Zaino.boxid.text = str(Oggetti.estrai_oggetto(tipo=Zaino.tipoloot.text, livello=Zaino.livelloloot.text,
                                                fortuna=Zaino.fortunaloot.text))
        cerca()
        try:
            pass
        except:
            return

    def selarmi(*args):
        Zaino.helperloot.text = testo_loot_helper

    def selaltro(*args):
        Zaino.helperloot.text = testo_generale


    Zaino.bottooneselarmi = Button(size_hint=(0.043, 0.05), pos_hint={"x": 0.16, "y": 0.245}, text="armi", font_size=15,
                                   on_release=partial(selarmi))
    layout.add_widget(Zaino.bottooneselarmi)
    Zaino.bottooneselaltro = Button(size_hint=(0.043, 0.05), pos_hint={"x": 0.203, "y": 0.245}, text="altro",
                                    font_size=15,
                                    on_release=partial(selaltro))
    layout.add_widget(Zaino.bottooneselaltro)
    Zaino.bottooneestrai = Button(size_hint=(0.043, 0.05), pos_hint={"x": 0.4, "y": 0.245}, text="estrai", font_size=15,
                                  on_release=partial(estrai))

    layout.add_widget(Zaino.bottooneestrai)

    testo_loot_helper = "arma martello tirapugni nunchaku mazza mazzafrusta kusarigama bastone martellodaguerra bastoneconpesi " \
                        "tonfa coltello daga armblade spadalunga sciabola katana asciaaduemani spadone zweihander accettadalancio" \
                        " accetta ascia stiletto shiv kriss fioretto estoc lancia picca beccodicorvo tridente coltellodalancio" \
                        " shuriken balestra balestraaripetizione arcocorto arcolungo arcocomposito chukonu"

    testo_generale = "armatura armaturaanimale scudo chainmail veste anello orecchino spilla fascia mantello amuleto cintura pozione" \
                     " faretra borsa reagenti freccia sacca portapozioni borsello portapergamene lingotto setalchemico" \
                     " altareincantamento bastonemagico oggettivari gemma vestiti trappola pergamena pietrapreziosa usabile"

    layout.add_widget(Label(text="Loot: tipo(copia o scrivi), livello (1-10), fortuna", size_hint=(0.5, 0.1),
                            pos_hint={"x": 0.08, "y": 0.255}))
    Zaino.tipoloot = TextInput(size_hint=(0.09, 0.05), pos_hint={"x": 0.25, "y": 0.245}, font_size=12)
    layout.add_widget(Zaino.tipoloot)
    Zaino.livelloloot = TextInput(size_hint=(0.03, 0.05), pos_hint={"x": 0.34, "y": 0.245}, font_size=12)
    layout.add_widget(Zaino.livelloloot)
    Zaino.fortunaloot = TextInput(size_hint=(0.03, 0.05), pos_hint={"x": 0.37, "y": 0.245}, font_size=12)
    layout.add_widget(Zaino.fortunaloot)
    Zaino.fortunaloot.text = str(Shared.pg_selezionato["fortuna_tot"])
    Zaino.helperloot = TextInput(text=testo_loot_helper, size_hint=(0.32, 0.25), pos_hint={"x": 0.158, "y": 0.0},
                                 font_size=17)
    layout.add_widget(Zaino.helperloot)
    layout.add_widget(barraricerca)
    importa()
    popup.open()

