import os

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import Moduli.SharedData as Shared
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


def citta_info_open(*args):
    layout1 = GridLayout(cols=3, spacing=0)
    popup = Popup(title="Città", title_size=(30),
                  title_align='center', content=layout1,
                  size_hint=(None, None), size=(900, 500),
                  auto_dismiss=True)

    with open(f"{Shared.path_dati}/info-citta.txt", "r", encoding='utf-8') as listacondizioni:
        linee = (listacondizioni.readlines())

    lineelistadict = []
    buffer = {}
    for linea in linee:
        if "°" in linea:
            if buffer != {}:
                lineelistadict.append(buffer)
            buffer = {}
            buffer["titolo"] = linea.split("**")[1]
            buffer["contenuto"] = []
        else:
            buffer["contenuto"].append(linea)

    lineelistadict.append(buffer)



    for citta in lineelistadict:
        from kivy.properties import partial
        layout1.add_widget(Button(text = citta["titolo"], on_release = partial(citta_selezionata_info_open,dati = citta)))

    popup.open()

def citta_selezionata_info_open(*args, dati):
    box = FloatLayout()
    popup = Popup(title=dati["titolo"], title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(1550, 800),
                  auto_dismiss=True)

    immagine = f"{Shared.path_art}/immagini/città/C-D_{dati['titolo']}.jpg"
    if not os.path.isfile(immagine):
        immagine = f"{Shared.path_art}/immagini/città/C-D_default.jpg"

    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=immagine,
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)
    linee = dati["contenuto"]

    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    y = 0.9
    l1sh = 1.2
    import textwrap
    for linea in linee:

        if len(linea) > 150:
            wrapper = textwrap.TextWrapper(width=140)
            word_list = wrapper.wrap(text=linea)
            linea = '\n'.join(word_list)

        layout1.add_widget(
            Label(text=linea, pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                  size_hint=(0.1, 0.05), font_size=20, background_color=(1, 1, 1, 0.5)))
        y -= 0.1
        l1sh += 0.05
    layout1.add_widget(Label(pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                  size_hint=(0.1, 0.05), background_color=(1, 1, 1, 0.5)))


    layout1.size_hint_y = l1sh
    popup.open()



def malattie_status_open():
    box = FloatLayout()
    popup = Popup(title=f'Malattie e Status', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(800, 800),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/bgeffetti.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)
    with open(f"{Shared.path_dati}/lista-condizioni.txt", "r") as listacondizioni:
        linee = (listacondizioni.readlines())

    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    y = 0.9
    l1sh = 1.2
    for linea in linee:
        layout1.add_widget(
            Label(text=linea, pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                  size_hint=(0.1, 0.05), font_size=20, background_color=(1, 1, 1, 0.5)))
        y -= 0.1
        l1sh += 0.05
    layout1.size_hint_y = l1sh
    popup.open()

def razze_info_open():
    box = FloatLayout()
    popup = Popup(title=f'Info razze', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(800, 800),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/bgeffetti.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)
    with open(f"{Shared.path_dati}/lista-info-razze.txt", "r") as listainforazze:
        linee = (listainforazze.readlines())

    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    y = 0.9
    l1sh = 1.2
    for linea in linee:
        layout1.add_widget(
            Label(text=linea, pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                  size_hint=(0.1, 0.05), font_size=20, background_color=(1, 1, 1, 0.5)))
        y -= 0.1
        l1sh += 0.05

    layout1.size_hint_y = l1sh
    popup.open()

def notecondivise():
    box = FloatLayout()
    popup = Popup(title=f'Note condivise', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(550, 800),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/note.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)
    percorsofile = Shared.path_cartella_shared + f"/notecondivise.txt"

    if not os.path.exists(percorsofile):
        with open(percorsofile, "x") as f:
            pass
    with open(percorsofile, "r") as f:
        notecondivisetesto = f.readlines()
    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    y_layout_1 = 0.2


    for linea in notecondivisetesto:
        layout1.add_widget(
            TextInput(text=linea,
                  size_hint=(0.1, 0.05), font_size=20, background_color=(1, 1, 1, 0.05)))
        y_layout_1 += 0.1
    layout1.size_hint_y = y_layout_1
    scroller.add_widget(layout1)

    popup.open()

def meteo_info_open():
    box = FloatLayout()
    popup = Popup(title=f'Info meteo', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(800, 800),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/bgeffetti.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)
    with open(f"{Shared.path_dati}/lista-info-meteo.txt", "r") as listainfometeo:
        linee = (listainfometeo.readlines())

    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    y = 0.9
    l1sh = 1.2
    for linea in linee:
        layout1.add_widget(
            Label(text=linea, pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                  size_hint=(0.1, 0.05), font_size=20, background_color=(1, 1, 1, 0.5)))
        y -= 0.1
        l1sh += 0.05

    layout1.size_hint_y = l1sh
    popup.open()

