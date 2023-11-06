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

def magiaopen(numero):
    nome_magia = str(eval(f"Shared.pg_selezionato['magia_{numero}_nome']"))
    descrizione_magia = str(eval(f"Shared.pg_selezionato['magia_{numero}_descrizione']"))
    scuola_magia = str(eval(f"Shared.pg_selezionato['magia_{numero}_scuola']"))
    formula_magia = str(eval(f"Shared.pg_selezionato['magia_{numero}_formula']"))
    costo_in_mana_magia = str(eval(f"Shared.pg_selezionato['magia_{numero}_costo_in_mana']"))
    raggio_magia = str(eval(f"Shared.pg_selezionato['magia_{numero}_raggio']"))

    layout = FloatLayout()
    popup = Popup(title=nome_magia, title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(700, 400),
                  auto_dismiss=True)

    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.02, "y": 0.9}, text="Nome Magia"))
    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.02, "y": 0.75}, text="Descrizione"))
    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.04, "y": 0.6}, text="Formula Magia"))
    textscoula = scuola_magia + " - " + raggio_magia
    nomemagia = TextInput(size_hint=(0.35, 0.1), pos_hint={"x": 0.15, "y": 0.875}, text=nome_magia)
    scuolamagia = TextInput(size_hint=(0.5, 0.1), pos_hint={"x": 0.5, "y": 0.875}, text=textscoula)
    descrizionemagia = TextInput(size_hint=(0.8, 0.2), pos_hint={"x": 0.17, "y": 0.675}, text=descrizione_magia)
    formulamagia = TextInput(size_hint=(0.5, 0.1), pos_hint={"x": 0.3, "y": 0.575}, text=formula_magia)

    layout.add_widget(
        Label(size_hint=(0.15, 0.05), pos_hint={"x": 0.12, "y": 0.45}, text="1 Energia per (X/10) Mana Magia Ordine"))
    en_mana_ordine = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "y": 0.45},
                               text=str(Shared.pg_selezionato['enpermanaordine']))
    layout.add_widget(
        Label(size_hint=(0.15, 0.05), pos_hint={"x": 0.12, "y": 0.37}, text="1 Energia per (X/10) Mana Magia Caos"))
    en_mana_caos = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "y": 0.37},
                             text=str(Shared.pg_selezionato['enpermanacaos']))
    layout.add_widget(Label(size_hint=(0.15, 0.05), pos_hint={"x": 0.12, "y": 0.29},
                            text="1 Punto Azione per (X/10) Mana Magia Ordine"))
    pa_mana_ordine = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "y": 0.29},
                               text=str(Shared.pg_selezionato['papermanaordine']))
    layout.add_widget(
        Label(size_hint=(0.15, 0.05), pos_hint={"x": 0.12, "y": 0.21},
              text="1 Punto Azione per (X/10) Mana magia Caos"))
    pa_mana_caos = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "y": 0.21},
                             text=str(Shared.pg_selezionato['papermanacaos']))
    layout.add_widget(Label(size_hint=(0.15, 0.05), pos_hint={"x": 0.12, "y": 0.13}, text="Sconto Mana per 1 Potere"))
    mana_per_potere = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "y": 0.13},
                                text=str(Shared.pg_selezionato['sconto_mana_per_potere']))
    layout.add_widget(
        Label(size_hint=(0.15, 0.05), pos_hint={"x": 0.12, "y": 0.05}, text="Sconto Punti Azione per 1 Potere"))
    pa_per_potere = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "y": 0.05},
                              text=str(Shared.pg_selezionato['sconto_pa_per_potere']))

    layout.add_widget(nomemagia)
    layout.add_widget(scuolamagia)
    layout.add_widget(descrizionemagia)
    layout.add_widget(formulamagia)
    layout.add_widget(en_mana_ordine)
    layout.add_widget(en_mana_caos)
    layout.add_widget(pa_mana_ordine)
    layout.add_widget(pa_mana_caos)
    layout.add_widget(mana_per_potere)
    layout.add_widget(pa_per_potere)

    popup.open()
