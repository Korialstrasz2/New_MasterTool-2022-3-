import random

import Moduli.SharedData as Shared

import os

from Moduli.Grafica import Popups_Notifiche, FinestraPrincipaleMain, Popups_Alchimia
from Moduli.Logica import Oggetti, EquipAttore, Salvataggio
from kivy.lang import Builder
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

def apri(*args):
    layout = FloatLayout()
    popup = Popup(title="Crea Nomi", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(700, 400),
                  auto_dismiss=True)

    def crea_nome(tipo,*args):
        nuovo_nome = ""
        nuovo_nome += Shared.razze_nomi_npc[tipo][random.randrange(1,len(Shared.razze_nomi_npc[tipo]))]
        if tipo.startswith("Altmer"):
            nuovo_nome += " "
            nuovo_nome += Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")][random.randrange(1,len(Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")]))]
            nuovo_nome += " "
            nuovo_nome += Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")][random.randrange(1,len(Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")]))]
            nuovo_nome += " "
            nuovo_nome += Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")][random.randrange(1,len(Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")]))]

        elif not tipo.startswith("Argoniani"):
            nuovo_nome += " "
            nuovo_nome += Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")][random.randrange(1,len(Shared.razze_nomi_npc[tipo.replace("maschi","famiglia").replace("femmine","famiglia")]))]

        box_risultato.text = nuovo_nome

    n_riga = 0
    n_colonna = 1
    for tipo in Shared.razze_nomi_npc:
        if not tipo.endswith("famiglia"):
            n_riga += 1
            layout.add_widget(
                Button(size_hint=(0.25, 0.15), pos_hint={"x": (n_riga*0.25)-0.25, "y": 1-(n_colonna*0.15)}, text=tipo,
                       on_release=partial(crea_nome,tipo)))
        if n_riga == 4:
            n_riga = 0
            n_colonna += 1
    box_risultato = TextInput(size_hint=(0.5, 0.15), pos_hint={"x": 0.25, "y": 0.0})
    layout.add_widget(box_risultato)
    popup.open()
