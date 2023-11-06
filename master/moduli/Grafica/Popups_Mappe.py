import os

import Moduli.SharedData as Shared
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

def seleziona_immagine(*args, nome):
    self1 = Shared.finestra
    if nome.startswith("D-"):
        self1.ids.immaginemain.source = f'{Shared.path_art}//license/folder_lic_t/{nome}'
    elif nome.startswith("N-") or nome.startswith("M-"):
        self1.ids.immaginemain.source = f'{Shared.path_art}/immagini/mostri_npc/{nome}'
    else:
        self1.ids.immaginemain.source = f'{Shared.path_art}/immagini/{nome}'

def aprimappecitta():
    layout1 = GridLayout(cols=4, spacing=0, size_hint_y=None, height=100)
    scroller = ScrollView(size_hint=(1, None), size=(400, 350), effect_cls="ScrollEffect")
    popup = Popup(title="", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 400),
                  auto_dismiss=True)
    path = os.getcwd()
    pathrisorse = f"{Shared.path_art}/immagini/thumbs"
    for file in os.listdir(pathrisorse):
        if file.startswith(f"C-"):
            layout1.add_widget(Image(source=f"{pathrisorse}/{file}"))
            layout1.add_widget(Button(text = file.split(".")[0], on_release=partial(seleziona_immagine,nome = file)))
            layout1.height += 100
    scroller.add_widget(layout1)
    popup.open()
def aprimapperistrette():
    layout1 = GridLayout(cols=4, spacing=0, size_hint_y=None, height=100)
    scroller = ScrollView(size_hint=(1, None), size=(400, 350), effect_cls="ScrollEffect")
    popup = Popup(title="", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 400),
                  auto_dismiss=True)
    path = os.getcwd()

    pathrisorsedungeon = f"{Shared.path_art}/license/folder_lic_t/thumbs"
    for file in os.listdir(pathrisorsedungeon):
        if file.startswith(f"D-"):
            layout1.add_widget(Image(source=f"{pathrisorsedungeon}/{file}"))
            layout1.add_widget(Button(text = file.split(".")[0], on_release=partial(seleziona_immagine,nome = file)))
            layout1.height += 100
    scroller.add_widget(layout1)
    popup.open()

def aprimappelocale():
    layout1 = GridLayout(cols=4, spacing=0, size_hint_y=None, height=100)
    scroller = ScrollView(size_hint=(1, None), size=(400, 350), effect_cls="ScrollEffect")
    popup = Popup(title="", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 400),
                  auto_dismiss=True)
    path = os.getcwd()
    pathrisorse = f"{Shared.path_art}/immagini/thumbs"
    for file in os.listdir(pathrisorse):
        if file.startswith(f"L-"):
            layout1.add_widget(Image(source=f"{pathrisorse}/{file}"))
            layout1.add_widget(Button(text = file.split(".")[0], on_release=partial(seleziona_immagine,nome = file)))
            layout1.height += 100
    scroller.add_widget(layout1)
    popup.open()

def aprimapperegione():
    layout1 = GridLayout(cols=4, spacing=0, size_hint_y=None, height=100)
    scroller = ScrollView(size_hint=(1, None), size=(400, 350), effect_cls="ScrollEffect")
    popup = Popup(title="", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 400),
                  auto_dismiss=True)
    path = os.getcwd()
    pathrisorse = f"{Shared.path_art}/immagini/thumbs"
    for file in os.listdir(pathrisorse):
        if file.startswith(f"R-"):
            layout1.add_widget(Image(source=f"{pathrisorse}/{file}"))
            layout1.add_widget(Button(text = file.split(".")[0], on_release=partial(seleziona_immagine,nome = file)))
            layout1.height += 100
    scroller.add_widget(layout1)
    popup.open()

def apriimgnpc():
    layout1 = GridLayout(cols=6, spacing=0, size_hint_y=None, height=100)
    scroller = ScrollView(size_hint=(1, None), size=(550, 500), effect_cls="ScrollEffect")
    popup = Popup(title="", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(900, 550),
                  auto_dismiss=True)
    path = os.getcwd()
    pathrisorse = f"{Shared.path_art}/immagini/thumbs"
    gruppofilealfabetico = []
    for filepre in os.listdir(pathrisorse):
        if filepre.startswith("N-") or filepre.startswith("M-"):
            gruppofilealfabetico.append(str(filepre))

    for file in sorted(gruppofilealfabetico):
        layout1.add_widget(Image(source=f"{pathrisorse}/{file}"))
        layout1.add_widget(Button(text = file.split(".")[0], on_release=partial(seleziona_immagine,nome = file)))
        layout1.height += 60
    scroller.add_widget(layout1)
    popup.open()
