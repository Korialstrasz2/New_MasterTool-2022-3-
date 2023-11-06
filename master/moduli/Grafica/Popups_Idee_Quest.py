import Moduli.SharedData as Shared

import os

from Moduli.Grafica import Popups_Notifiche, FinestraPrincipaleMain, Popups_Alchimia
from Moduli.Logica import Oggetti, EquipAttore, Salvataggio
from kivy.lang import Builder
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

def idee_quest_open(*args):
    box = FloatLayout()
    popup = Popup(title=f'Idee Quest', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(550, 800),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/note.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)

    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    y_layout_1 = 0.2


    for linea in Shared.tipi_missione:
        layout1.add_widget(
            TextInput(text=linea,
                  size_hint=(0.1, 0.05), font_size=20, background_color=(1, 1, 1, 0.05)))
        y_layout_1 += 0.1
    layout1.size_hint_y = y_layout_1
    scroller.add_widget(layout1)

    popup.open()