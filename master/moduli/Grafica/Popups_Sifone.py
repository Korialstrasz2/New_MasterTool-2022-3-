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


def sifoneopen():
    layout = FloatLayout()
    popup = Popup(title="SIFONE", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(350, 200),
                  auto_dismiss=True)
    testo_s_d_m = f"Base: {Shared.pg_selezionato['sifone_di_mana_base']} Tot: {Shared.pg_selezionato['sifone_di_mana']}"
    layout.add_widget(Label(size_hint=(0.35, 0.3), pos_hint={"x": 0.05, "y": 0.7}, text="Sifone"))
    layout.add_widget(Label(size_hint=(0.5, 0.25), pos_hint={"x": 0.3, "y": 0.8}, text=testo_s_d_m))
    valoresifone = TextInput(size_hint=(0.5, 0.25), pos_hint={"x": 0.3, "y": 0.55},
                             text=str(Shared.pg_selezionato['sifone_di_mana_base']))

    layout.add_widget(valoresifone)

    def salva(*args):
        Shared.pg_selezionato['sifone_di_mana_base'] = int(valoresifone.text)
        FinestraPrincipaleMain.FunzioniFinestra.conferma()

    layout.add_widget(
        Button(size_hint=(0.4, 0.2), pos_hint={"x": 0.1, "y": 0.2}, text="Salva", on_release=salva))

    popup.open()
