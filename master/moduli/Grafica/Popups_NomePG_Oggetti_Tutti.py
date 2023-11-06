from math import floor

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, Popups_Notifiche, Popups_Effetti
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori, GestioneSkill, Oggetti
from kivy.lang import Builder
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
pgselezionato = Shared.pg_selezionato





def oggetti_tutti_open(*args, auto_select = None):
    from kivy.uix.recycleview import RecycleView
    box = FloatLayout()
    popup = Popup(title=f'Tutti Gli Oggetti', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(1600, 1000),
                  auto_dismiss=True)
    notepic = AsyncImage(allow_stretch=True, size_hint=(1, 1), source='Art/NPCbgshort.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)



    layoutmenu = GridLayout(cols=7, spacing=0, size_hint_x=0.85, size_hint_y=0.2, pos_hint={"x": 0, "y": 0.8})
    layout_submenu = GridLayout(cols=2, spacing=0, size_hint_x=0.15, size_hint_y=1, pos_hint={"x": 0.85, "y": 0})
    box.add_widget(layoutmenu)
    box.add_widget(layout_submenu)


    def updatescroller(gruppo, *args):
        def scroll_to_item(*args, scroller,text_target):
            grid_layout = scroller.children[0]
            flag_trovato = False
            for index, item in enumerate(grid_layout.children):
                if "TIPO2" in item.text:
                    if text_target in item.text.split("TIPO2")[1][:35]:
                        flag_trovato = index / len(grid_layout.children)

            if flag_trovato != False:
                flag_trovato_negativo = 1 - flag_trovato

                scroller.scroll_y = flag_trovato - (flag_trovato_negativo / 95)

        scroller = RecycleView(size_hint=(0.85, 0.8), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
        layout1 = GridLayout(cols=1, spacing=0, size_hint_x=1, size_hint_y=1.2, height=200)
        widget_interni = list(box.children)
        for wid_interno in widget_interni:
            if str(wid_interno).startswith("<kivy.uix.recycleview"):
                box.remove_widget(wid_interno)
        box.add_widget(scroller)
        scroller.add_widget(layout1)

        y = 0.9
        l1sh = 0.8
        numero = 0
        layout_submenu.clear_widgets()
        subgroup_tipi = []
        for ogg in gruppo:
            flag_nuovo_tipo_2 = False
            testo = ""
            nome = ""
            tipo_2 = ""
            for colonna in ogg:
                testocheck = str(ogg[colonna])
                if colonna == "NOME":
                    nome = testocheck
                    continue
                if colonna == "TIPO2":
                    if testocheck not in subgroup_tipi:
                        tipo_2 = testocheck
                        subgroup_tipi.append(testocheck)
                        flag_nuovo_tipo_2 = True
                if testocheck not in ["Vuoto",None, "None","none", "NA"]:
                    testo += colonna + ": " + testocheck + "  ||  "
                    numero += 1
                    l1sh += 0.0045*2
                    if numero > 20:
                        l1sh += 0.0045*2
            if len(testo) > 2:
                layout1.add_widget(
                    TextInput(text=nome, pos_hint={"center_x": 0.5, "center_y": y}, hint_text_color=(0, 0, 0, 1),
                              size_hint=(0.1, 0.3), padding=(2, 2, 2, 2), font_size=20, background_color= (0.5,1,0.5,1)))
                layout1.add_widget(
                    TextInput(text=testo, pos_hint={"center_x": 0.5, "center_y": y}, hint_text_color=(0, 0, 0, 1),
                              size_hint=(0.1, 0.7), padding=(2, 2, 2, 2), font_size=20))
                if flag_nuovo_tipo_2:
                    layout_submenu.add_widget(Button(text=tipo_2, on_release = partial(scroll_to_item, scroller = scroller,text_target = tipo_2)))

        layout1.size_hint_y = l1sh

    gruppi = {}
    for ogg_da_checkare in Shared.db_oggetti:
        oggetto = Shared.db_oggetti[ogg_da_checkare]
        if oggetto["TIPO1"] not in gruppi:
            gruppi[oggetto["TIPO1"]] = [oggetto]
        else:
            gruppi[oggetto["TIPO1"]].append(oggetto)

    for cluster_oggetti in gruppi:
        nome = cluster_oggetti
        if nome not in ["natura1","natura2","natura3","NA"]:
            if nome == "amuleto(tutte)":
                colore = (0, 0, 1, 1)
                nome = "amuleto(tutte le scuole)"
            elif nome in Shared.categorie_armi:
                colore = (1, 0, 0, 1)
            elif nome == "pozione":
                colore = (0, 1, 0, 1)
            elif nome in Oggetti.gruppoequip:
                colore = (0, 0, 1, 1)
            else:
                colore = (1, 1, 1, 1)
            layoutmenu.add_widget(Button(text=nome, size_hint=(0.1, 0.05), pos_hint={"x": 0.9, "y": 0.9}, color = (1,1,1,1),
                         background_color=colore,on_release=partial(updatescroller, gruppi[cluster_oggetti])))

    if auto_select != None:
        updatescroller(gruppi[auto_select])
    if Shared.bloccaskill == False:
        popup.open()


def popup_oggetto_esistente(*args, dati_nuovo_oggetto):
    layout = GridLayout(cols=1, spacing=0, size_hint_y=1, height=200)
    popup = Popup(title='ID oggetto già presente, sovrascrivere?', title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(700, 300),
                  auto_dismiss=False)

    def accettafuoo(*args):
        Oggetti.aggiungi_oggetto_in_posizione(id_precedente=str(int(dati_nuovo_oggetto[0])-1), dati=dati_nuovo_oggetto)
        # GestioneSkill.salva_db_skill()
        popup.dismiss()

    accetta = Button(text="V Accetta", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                     pos_hint={"x": 0, "y": 0}, on_release=accettafuoo)
    rifiuta = Button(text="X Rifiuta", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                     pos_hint={"x": 0.8, "y": 0}, on_release=popup.dismiss)

    layout.add_widget(accetta)
    layout.add_widget(rifiuta)
    popup.open()

def crea_nuovo_oggetto(*args):
    Builder.load_string("""
<Label>:
    color: 1,1,1,1""")
    layout = FloatLayout()
    popup = Popup(title=f"Nuovo oggetto", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1400, 520),
                  auto_dismiss=True)

    def cerca_ultimo_indice(*args):
        risultato = Oggetti.trova_ultimo_popolato()
        boxid.text = str(risultato)
        cerca()

    def cerca(*args):
        risultato = Oggetti.trova_oggetto(boxid.text)
        if type(risultato) == dict:
            boxnome.text = str(risultato["NOME"])
            boxtipo1.text = str(risultato["TIPO1"])
            boxtipo2.text = str(risultato["TIPO2"])
            boxtipo3.text = str(risultato["TIPO3"])
            boxdescrizione.text = str(risultato["DESCRIZIONE"])
            boxvalore.text = str(risultato["VALORE"])
            boxslot.text = str(risultato["SLOT"])
            boxeffetto1.text = str(risultato["EFFETTO1"])
            boxeffetto2.text = str(risultato["EFFETTO2"])
            boxeffetto3.text = str(risultato["EFFETTO3"])
            boxeffetto4.text = str(risultato["EFFETTO4"])
            boxeffetto5.text = str(risultato["EFFETTO5"])
            boxeffetto6.text = str(risultato["EFFETTO6"])
            boxeffetto7.text = str(risultato["EFFETTO7"])
            boxlivloot.text = str(risultato["LV_LOOT"])
            boxrarita.text = str(risultato["RARITA"])
        else:
            boxnome.text = "Non Trovato"
            boxtipo1.text = "Non Trovato"
            boxtipo2.text = "Non Trovato"
            boxtipo3.text = "Non Trovato"
            boxdescrizione.text = "Non Trovato"
            boxvalore.text = "Non Trovato"
            boxslot.text = "Non Trovato"
            boxeffetto1.text = "Non Trovato"
            boxeffetto2.text = "Non Trovato"
            boxeffetto3.text = "Non Trovato"
            boxeffetto4.text = "Non Trovato"
            boxeffetto5.text = "Non Trovato"
            boxeffetto6.text = "Non Trovato"
            boxeffetto7.text = "Non Trovato"
            boxlivloot.text = "Non Trovato"
            boxrarita.text = "Non Trovato"

    def crea(*args):
        stringapre = []
        stringapre.append(int(boxid.text))
        stringapre.append(boxnome.text)
        stringapre.append(boxtipo1.text)
        stringapre.append(boxtipo2.text)
        stringapre.append(boxtipo3.text)
        stringapre.append(boxdescrizione.text)
        stringapre.append(boxvalore.text)
        stringapre.append(boxslot.text)
        stringapre.append(boxeffetto1.text)
        stringapre.append(boxeffetto2.text)
        stringapre.append(boxeffetto3.text)
        stringapre.append(boxeffetto4.text)
        stringapre.append(boxeffetto5.text)
        stringapre.append(boxeffetto6.text)
        stringapre.append(boxeffetto7.text)
        stringapre.append(boxlivloot.text)
        stringapre.append(boxrarita.text)
        stringa = []
        for x in stringapre:
            if x != "":
                stringa.append(x)
            else:
                stringa.append("Vuoto")
        if (type(Oggetti.trova_oggetto(boxid.text)) == dict and str(Oggetti.trova_oggetto(boxid.text)["ID"]) == "9999999") or (len(Oggetti.trova_oggetto(boxid.text)) == 1 and str(Oggetti.trova_oggetto(boxid.text)[0]["ID"]) == "9999999"):
            try:
                Oggetti.aggiungi_oggetto_in_posizione(id_precedente=str(int(stringa[0])-1), dati=stringa)
                pass
                # GestioneSkill.salva_db_oggetti()
            except:
                Popups_Notifiche.nosave()
        elif type(Oggetti.trova_oggetto(boxid.text)) == dict:
            popup_oggetto_esistente(dati_nuovo_oggetto=stringa)

        else:
            print("NOOOO")

    layout.add_widget(Label(size_hint=(0.05, 0.03), pos_hint={"x": 0, "y": 0.95}, text="Numero ID"))
    boxid = TextInput(size_hint=(0.05, 0.07), pos_hint={"x": 0, "y": 0.85})
    layout.add_widget(Label(size_hint=(0.2, 0.03), pos_hint={"x": 0.05, "y": 0.95}, text="Nome"))
    boxnome = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.05, "y": 0.85})
    layout.add_widget(Label(size_hint=(0.25, 0.03), pos_hint={"x": 0.25, "y": 0.95}, text="Tipo 1"))
    boxtipo1 = TextInput(size_hint=(0.25, 0.07), pos_hint={"x": 0.25, "y": 0.85})
    layout.add_widget(Label(size_hint=(0.25, 0.03), pos_hint={"x": 0.5, "y": 0.95}, text="Tipo 2"))
    boxtipo2 = TextInput(size_hint=(0.25, 0.07), pos_hint={"x": 0.5, "y": 0.85})
    layout.add_widget(Label(size_hint=(0.25, 0.03), pos_hint={"x": 0.75, "y": 0.95}, text="Tipo 3"))
    boxtipo3 = TextInput(size_hint=(0.25, 0.07), pos_hint={"x": 0.75, "y": 0.85})

    layout.add_widget(Label(size_hint=(0.7, 0.03), pos_hint={"x": 0.0, "y": 0.75}, text="Descrizione"))
    boxdescrizione = TextInput(size_hint=(0.7, 0.07), pos_hint={"x": 0.0, "y": 0.65})
    layout.add_widget(Label(size_hint=(0.15, 0.03), pos_hint={"x": 0.7, "y": 0.75}, text="Valore"))
    boxvalore = TextInput(size_hint=(0.15, 0.07), pos_hint={"x": 0.7, "y": 0.65})
    layout.add_widget(Label(size_hint=(0.15, 0.03), pos_hint={"x": 0.85, "y": 0.75}, text="Slot(peso)"))
    boxslot = TextInput(size_hint=(0.15, 0.07), pos_hint={"x": 0.85, "y": 0.65})

    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.0, "y": 0.55}, text="Effetto 1\n(atk/def)"))
    boxeffetto1 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.00, "y": 0.45})
    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.33, "y": 0.55}, text="Effetto 2\n(bonus tier/malus pa)"))
    boxeffetto2 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.33, "y": 0.45})
    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.66, "y": 0.55}, text="Effetto 3\n(pa per atk)"))
    boxeffetto3 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.66, "y": 0.45})

    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.0, "y": 0.35}, text="Effetto 4"))
    boxeffetto4 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.0, "y": 0.25})
    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.33, "y": 0.35}, text="Effetto 5"))
    boxeffetto5 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.33, "y": 0.25})
    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.66, "y": 0.35}, text="Effetto 6"))
    boxeffetto6 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.66, "y": 0.25})

    layout.add_widget(Label(size_hint=(0.33, 0.03), pos_hint={"x": 0.0, "y": 0.15}, text="Effetto 7"))
    boxeffetto7 = TextInput(size_hint=(0.33, 0.07), pos_hint={"x": 0.0, "y": 0.05})
    layout.add_widget(Label(size_hint=(0.15, 0.03), pos_hint={"x": 0.33, "y": 0.15}, text="Liv. loot(1-10)"))
    boxlivloot = TextInput(size_hint=(0.15, 0.07), pos_hint={"x": 0.33, "y": 0.05})
    layout.add_widget(Label(size_hint=(0.15, 0.03), pos_hint={"x": 0.48, "y": 0.15}, text="Rarità (1-5)"))
    boxrarita = TextInput(size_hint=(0.15, 0.07), pos_hint={"x": 0.48, "y": 0.05})
    layout.add_widget(
        Button(size_hint=(0.15, 0.07), pos_hint={"x": 0.63, "y": 0.05}, text="Cerca", on_release=cerca))
    layout.add_widget(
        Button(size_hint=(0.15, 0.07), pos_hint={"x": 0.85, "y": 0.12}, text="Cerca Ultimo Indice Usato", on_release=cerca_ultimo_indice))
    layout.add_widget(
        Button(size_hint=(0.15, 0.07), pos_hint={"x": 0.85, "y": 0.05}, text="Crea Nuovo Oggetto", on_release=crea))

    layout.add_widget(boxid)
    layout.add_widget(boxnome)
    layout.add_widget(boxtipo1)
    layout.add_widget(boxtipo2)
    layout.add_widget(boxtipo3)
    layout.add_widget(boxdescrizione)
    layout.add_widget(boxvalore)
    layout.add_widget(boxslot)
    layout.add_widget(boxeffetto1)
    layout.add_widget(boxeffetto2)
    layout.add_widget(boxeffetto3)
    layout.add_widget(boxeffetto4)
    layout.add_widget(boxeffetto5)
    layout.add_widget(boxeffetto6)
    layout.add_widget(boxeffetto7)
    layout.add_widget(boxlivloot)
    layout.add_widget(boxrarita)

    popup.open()
