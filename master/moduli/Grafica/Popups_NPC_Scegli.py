import copy
import json
import os
import shutil
from random import randrange

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


def apri(*args):
    Builder.load_string("""
<Label>:
    color: 0,0,0,1
<TextInput>:
    background_color: 1,1,1,0.7""")

    layout = FloatLayout()
    popup = Popup(title=f"Seleziona Nemico", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(800, 750),
                  auto_dismiss=True)


    notepic = Image(allow_stretch=True, size_hint=(1, 1), source='Art/NPCbg.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    layout.add_widget(notepic)

    def seleziona_livello(totale,*args):
        Shared.box_id_per_eventuale_import_da_selezionato.text = totale

    def seleziona_npc(nome, *args):
        layout.clear_widgets()
        layout.add_widget(notepic)
        layout.add_widget(Button(size_hint=(0.25, 0.05), pos_hint={"x": 0, "y": 0.95}, text="Seleziona\nNPC",
                                 on_release=popola_bottoni))
        x_base = 0
        y_base = 0.9
        for livello in range(1,21):
            totale = nome.split("_lv_")[0] + "_lv_" + str(livello)
            layout.add_widget(Button(size_hint=(0.25, 0.05), pos_hint={"x": x_base, "y": y_base}, text=str(livello), on_release=partial(seleziona_livello,totale)))
            x_base += 0.25
            if x_base > 0.75:
                x_base = 0
                y_base -= 0.05


    def popola_bottoni(*args):
        layout.clear_widgets()
        layout.add_widget(notepic)
        x_base = 0
        y_base = 0.95
        gia_presi = []
        dictnomi = {}

        for npc in Shared.pgnpc_importati_base:
            if "__pg__" not in npc and "__" in npc:
                nomepre = npc.split("__")[2]
                nome = nomepre.split("_lv")[0]
                if nome not in gia_presi:
                    gia_presi.append(nome)
                    dictnomi[nome] = [npc,npc.split("__")[1]]

        for preso in sorted(gia_presi):
            nome = f"({dictnomi[preso][1][:3]}) {preso}"
            layout.add_widget(Button(size_hint=(0.25, 0.05), pos_hint={"x": x_base, "y": y_base}, text=nome,
                                     on_release=partial(seleziona_npc, dictnomi[preso][0])))
            x_base += 0.25
            if x_base > 0.75:
                x_base = 0
                y_base -= 0.05

    popola_bottoni()
    popup.open()
