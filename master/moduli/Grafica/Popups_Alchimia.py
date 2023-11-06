from random import randrange

import Moduli.SharedData as Shared
from Moduli.Grafica import Popups_Negozio, Popups_NomePG_Oggetti_Tutti
from Moduli.Logica import Salvataggio
from kivy.properties import partial
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def unpack_alchimia(nome_NPC_Attori):
    attore_attivo = Shared.pg_selezionato
    attore_attivo["alchimia_ingredienti_rossi_1"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[0]
    attore_attivo["alchimia_ingredienti_rossi_2"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[1]
    attore_attivo["alchimia_ingredienti_rossi_3"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[2]
    attore_attivo["alchimia_ingredienti_rossi_4"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[3]
    attore_attivo["alchimia_ingredienti_verdi_1"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[0]
    attore_attivo["alchimia_ingredienti_verdi_2"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[1]
    attore_attivo["alchimia_ingredienti_verdi_3"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[2]
    attore_attivo["alchimia_ingredienti_verdi_4"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[3]
    attore_attivo["alchimia_ingredienti_blu_1"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[0]
    attore_attivo["alchimia_ingredienti_blu_2"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[1]
    attore_attivo["alchimia_ingredienti_blu_3"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[2]
    attore_attivo["alchimia_ingredienti_blu_4"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[3]
    attore_attivo["alchimia_effetto_ingredienti_1"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        0]
    attore_attivo["alchimia_effetto_ingredienti_2"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        1]
    attore_attivo["alchimia_effetto_ingredienti_3"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        2]
    attore_attivo["alchimia_effetto_ingredienti_4"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        3]


def salva_alchimia():
    stringa_totale = ""
    stringa_alchimia_ingredienti_rossi_1_2_3_4 = f'{Shared.pg_selezionato["alchimia_ingredienti_rossi_1"]}$$' \
                                                 f'{Shared.pg_selezionato["alchimia_ingredienti_rossi_2"]}$$' \
                                                 f'{Shared.pg_selezionato["alchimia_ingredienti_rossi_3"]}$$' \
                                                 f'{Shared.pg_selezionato["alchimia_ingredienti_rossi_4"]}'
    stringa_alchimia_ingredienti_verdi_1_2_3_4 = f'{Shared.pg_selezionato["alchimia_ingredienti_verdi_1"]}$$' \
                                                 f'{Shared.pg_selezionato["alchimia_ingredienti_verdi_2"]}$$' \
                                                 f'{Shared.pg_selezionato["alchimia_ingredienti_verdi_3"]}$$' \
                                                 f'{Shared.pg_selezionato["alchimia_ingredienti_verdi_4"]}'
    stringa_alchimia_ingredienti_blu_1_2_3_4 = f'{Shared.pg_selezionato["alchimia_ingredienti_blu_1"]}$$' \
                                               f'{Shared.pg_selezionato["alchimia_ingredienti_blu_2"]}$$' \
                                               f'{Shared.pg_selezionato["alchimia_ingredienti_blu_3"]}$$' \
                                               f'{Shared.pg_selezionato["alchimia_ingredienti_blu_4"]}'
    stringa_alchimia_effetto_ingredienti_1_2_3_4 = f'{Shared.pg_selezionato["alchimia_effetto_ingredienti_1"]}$$' \
                                                   f'{Shared.pg_selezionato["alchimia_effetto_ingredienti_2"]}$$' \
                                                   f'{Shared.pg_selezionato["alchimia_effetto_ingredienti_3"]}$$' \
                                                   f'{Shared.pg_selezionato["alchimia_effetto_ingredienti_4"]}'

    Shared.pg_selezionato["alchimia_ingredienti_rossi_1_2_3_4"] = stringa_alchimia_ingredienti_rossi_1_2_3_4
    Shared.pg_selezionato["alchimia_ingredienti_verdi_1_2_3_4"] = stringa_alchimia_ingredienti_verdi_1_2_3_4
    Shared.pg_selezionato["alchimia_ingredienti_blu_1_2_3_4"] = stringa_alchimia_ingredienti_blu_1_2_3_4
    Shared.pg_selezionato["alchimia_effetto_ingredienti_1_2_3_4"] = stringa_alchimia_effetto_ingredienti_1_2_3_4

def alchimiaopen(*args):
    box = FloatLayout(size_hint=(0.7, 0.07))
    box_laterale = GridLayout(padding=5, cols=1,size_hint=(0.3, 0.07))
    testo_poz_rosse = """Pozioni Rosse:
    Cura
    Difesa
    Attacco
    -PA
    Danneggia Vita
    Vita Temporanea
    Energia Spesa
    """
    testo_poz_verdi = """Pozioni Verdi:
    +PA
    Visione
    Cura Effetti
    Esplosione
    Stanchezza Spesa
    Fumogeno
    """
    testo_poz_blu = """Pozioni Blu:
    Mana
    Danneggia Mana
    Potere Speso
    Resistenza Magica
    Volo
    Invisibilità
    Intangibilità
    """
    box_laterale.add_widget(TextInput(size_hint=(1, 0.07), text=testo_poz_rosse, font_size = 20))
    box_laterale.add_widget(TextInput(size_hint=(1, 0.07), text=testo_poz_verdi, font_size = 20))
    box_laterale.add_widget(TextInput(size_hint=(1, 0.07), text=testo_poz_blu, font_size = 20))

    box_master = GridLayout(padding=5, cols=1)

    box_master.add_widget(box)
    popup = Popup(title='Alchimia', title_size=(30),
                  title_align='center', content=box_master,
                  size_hint=(None, None), size=(700, 900),
                  auto_dismiss=True)

    def mostra_pozioni(*args):
        if box_master.cols == 1:
            popup.size = (1000,900)
            box_master.cols = 2
            box_master.add_widget(box_laterale)
        else:
            popup.size = (700,900)
            box_master.cols = 1
            box_master.remove_widget(box_laterale)

    def salvaalchimia(*args):
        Shared.pg_selezionato['alchimia_note_1'] = alchimia_note_1kv.text
        Shared.pg_selezionato['alchimia_note_2'] = alchimia_note_2kv.text
        Shared.pg_selezionato['alchimia_note_3'] = alchimia_note_3kv.text
        Shared.pg_selezionato['alchimia_ingredienti_rossi_1'] = alchimia_ingredienti_rossi_1kv.text
        Shared.pg_selezionato['alchimia_ingredienti_rossi_2'] = alchimia_ingredienti_rossi_2kv.text
        Shared.pg_selezionato['alchimia_ingredienti_rossi_3'] = alchimia_ingredienti_rossi_3kv.text
        Shared.pg_selezionato['alchimia_ingredienti_rossi_4'] = alchimia_ingredienti_rossi_4kv.text
        Shared.pg_selezionato['alchimia_ingredienti_verdi_1'] = alchimia_ingredienti_verdi_1kv.text
        Shared.pg_selezionato['alchimia_ingredienti_verdi_2'] = alchimia_ingredienti_verdi_2kv.text
        Shared.pg_selezionato['alchimia_ingredienti_verdi_3'] = alchimia_ingredienti_verdi_3kv.text
        Shared.pg_selezionato['alchimia_ingredienti_verdi_4'] = alchimia_ingredienti_verdi_4kv.text
        Shared.pg_selezionato['alchimia_ingredienti_blu_1'] = alchimia_ingredienti_blu_1kv.text
        Shared.pg_selezionato['alchimia_ingredienti_blu_2'] = alchimia_ingredienti_blu_2kv.text
        Shared.pg_selezionato['alchimia_ingredienti_blu_3'] = alchimia_ingredienti_blu_3kv.text
        Shared.pg_selezionato['alchimia_ingredienti_blu_4'] = alchimia_ingredienti_blu_4kv.text
        Shared.pg_selezionato['alchimia_effetto_ingredienti_1'] = alchimia_effetto_ingredienti_1kv.text
        Shared.pg_selezionato['alchimia_effetto_ingredienti_2'] = alchimia_effetto_ingredienti_2kv.text
        Shared.pg_selezionato['alchimia_effetto_ingredienti_3'] = alchimia_effetto_ingredienti_3kv.text
        Shared.pg_selezionato['alchimia_effetto_ingredienti_4'] = alchimia_effetto_ingredienti_4kv.text
        Shared.pg_selezionato['alchimia_moltiplicatore_blu'] = alchimia_moltiplicatore_blukv.text
        Shared.pg_selezionato['alchimia_moltiplicatore_verdi'] = alchimia_moltiplicatore_verdikv.text
        Shared.pg_selezionato['alchimia_moltiplicatore_rossi'] = alchimia_moltiplicatore_rossikv.text
        salva_alchimia()
        Salvataggio.salva_pgnpc(Shared.pg_selezionato["nome_in_uso"])

    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/tavoloalchemico.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    box.add_widget(notepic)
    notepic = Image(allow_stretch=True, size_hint=(0.5, 0.5), source=f'{Shared.path_art}/tavoloalchemico2.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.25})
    box.add_widget(notepic)

    alchimia_note_1kv = TextInput(text=str(Shared.pg_selezionato['alchimia_note_1']),
                                  pos_hint={"center_x": 0.5, "center_y": 0.95},
                                  size_hint=(0.9, 0.051), background_color=(1, 1, 1, 0.1), padding=(2, 2, 2, 2))
    box.add_widget(alchimia_note_1kv)
    alchimia_note_2kv = TextInput(text=str(Shared.pg_selezionato['alchimia_note_2']),
                                  pos_hint={"center_x": 0.5, "center_y": 0.90},
                                  size_hint=(0.9, 0.051), background_color=(1, 1, 1, 0.1), padding=(2, 2, 2, 2))
    box.add_widget(alchimia_note_2kv)
    alchimia_note_3kv = TextInput(text=str(Shared.pg_selezionato['alchimia_note_3']),
                                  pos_hint={"center_x": 0.5, "center_y": 0.85},
                                  size_hint=(0.9, 0.051), background_color=(1, 1, 1, 0.1), padding=(2, 2, 2, 2))
    box.add_widget(alchimia_note_3kv)

    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Raegenti:", pos_hint={"center_x": 0.3, "center_y": 0.8}, size_hint=(0.1, 0.5),
               font_size=(30))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 1:", pos_hint={"center_x": 0.2, "center_y": 0.75}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 2:", pos_hint={"center_x": 0.3, "center_y": 0.75}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 3:", pos_hint={"center_x": 0.4, "center_y": 0.75}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 4:", pos_hint={"center_x": 0.5, "center_y": 0.75}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Rossi:", pos_hint={"center_x": 0.1, "center_y": 0.7}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Verdi:", pos_hint={"center_x": 0.1, "center_y": 0.65}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Blu:", pos_hint={"center_x": 0.115, "center_y": 0.6}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="TOT:", pos_hint={"center_x": 0.1, "center_y": 0.8}, size_hint=(0.1, 0.5),
               font_size=(25))))

    alchimia_ingredienti_rossi_1kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_rossi_1']),
                                               pos_hint={"center_x": 0.2, "center_y": 0.7},
                                               padding=(2, 2, 2, 2),
                                               size_hint=(0.07, 0.04), background_color=(1, 0, 0, 0.1),
                                               font_size=(23))
    box.add_widget(alchimia_ingredienti_rossi_1kv)
    alchimia_ingredienti_rossi_2kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_rossi_2']),
                                               pos_hint={"center_x": 0.3, "center_y": 0.7},
                                               size_hint=(0.07, 0.04), background_color=(1, 0, 0, 0.2),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_rossi_2kv)
    alchimia_ingredienti_rossi_3kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_rossi_3']),
                                               pos_hint={"center_x": 0.4, "center_y": 0.7},
                                               size_hint=(0.07, 0.04), background_color=(1, 0, 0, 0.3),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_rossi_3kv)
    alchimia_ingredienti_rossi_4kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_rossi_4']),
                                               pos_hint={"center_x": 0.5, "center_y": 0.7},
                                               size_hint=(0.07, 0.04), background_color=(1, 0, 0, 0.4),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_rossi_4kv)
    alchimia_ingredienti_verdi_1kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_verdi_1']),
                                               pos_hint={"center_x": 0.2, "center_y": 0.65},
                                               size_hint=(0.07, 0.04), background_color=(0, 1, 0, 0.1),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_verdi_1kv)
    alchimia_ingredienti_verdi_2kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_verdi_2']),
                                               pos_hint={"center_x": 0.3, "center_y": 0.65},
                                               size_hint=(0.07, 0.04), background_color=(0, 1, 0, 0.2),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_verdi_2kv)
    alchimia_ingredienti_verdi_3kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_verdi_3']),
                                               pos_hint={"center_x": 0.4, "center_y": 0.65},
                                               size_hint=(0.07, 0.04), background_color=(0, 1, 0, 0.3),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_verdi_3kv)
    alchimia_ingredienti_verdi_4kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_verdi_4']),
                                               pos_hint={"center_x": 0.5, "center_y": 0.65},
                                               size_hint=(0.07, 0.04), background_color=(0, 1, 0, 0.4),
                                               padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_verdi_4kv)
    alchimia_ingredienti_blu_1kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_blu_1']),
                                             pos_hint={"center_x": 0.2, "center_y": 0.6},
                                             size_hint=(0.07, 0.04), background_color=(0, 0, 1, 0.1),
                                             padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_blu_1kv)
    alchimia_ingredienti_blu_2kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_blu_2']),
                                             pos_hint={"center_x": 0.3, "center_y": 0.6},
                                             size_hint=(0.07, 0.04), background_color=(0, 0, 1, 0.2),
                                             padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_blu_2kv)
    alchimia_ingredienti_blu_3kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_blu_3']),
                                             pos_hint={"center_x": 0.4, "center_y": 0.6},
                                             size_hint=(0.07, 0.04), background_color=(0, 0, 1, 0.3),
                                             padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_blu_3kv)
    alchimia_ingredienti_blu_4kv = TextInput(text=str(Shared.pg_selezionato['alchimia_ingredienti_blu_4']),
                                             pos_hint={"center_x": 0.5, "center_y": 0.6},
                                             size_hint=(0.07, 0.04), background_color=(0, 0, 1, 0.4),
                                             padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_ingredienti_blu_4kv)
    box.add_widget((Label(color=(0, 0, 0, 1), text=str(
        int(alchimia_ingredienti_rossi_1kv.text) + int(alchimia_ingredienti_rossi_2kv.text) + int(
            alchimia_ingredienti_rossi_3kv.text) +
        int(alchimia_ingredienti_rossi_4kv.text) + int(alchimia_ingredienti_verdi_1kv.text) + int(
            alchimia_ingredienti_verdi_2kv.text) +
        int(alchimia_ingredienti_verdi_3kv.text) + int(alchimia_ingredienti_verdi_4kv.text) + int(
            alchimia_ingredienti_blu_1kv.text)
        + int(alchimia_ingredienti_blu_2kv.text) + int(alchimia_ingredienti_blu_3kv.text) + int(
            alchimia_ingredienti_blu_4kv.text)),
                          pos_hint={"center_x": 0.1, "center_y": 0.75}, size_hint=(0.1, 0.5), font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Effetto:", pos_hint={"center_x": 0.1, "center_y": 0.50}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 1:", pos_hint={"center_x": 0.2, "center_y": 0.55}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 2:", pos_hint={"center_x": 0.3, "center_y": 0.55}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 3:", pos_hint={"center_x": 0.4, "center_y": 0.55}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Lv. 4:", pos_hint={"center_x": 0.5, "center_y": 0.55}, size_hint=(0.1, 0.5),
               font_size=(25))))
    alchimia_effetto_ingredienti_1kv = TextInput(text=str(Shared.pg_selezionato['alchimia_effetto_ingredienti_1']),
                                                 pos_hint={"center_x": 0.2, "center_y": 0.5},
                                                 size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2),
                                                 padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_effetto_ingredienti_1kv)
    alchimia_effetto_ingredienti_2kv = TextInput(text=str(Shared.pg_selezionato['alchimia_effetto_ingredienti_2']),
                                                 pos_hint={"center_x": 0.3, "center_y": 0.5},
                                                 size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2),
                                                 padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_effetto_ingredienti_2kv)
    alchimia_effetto_ingredienti_3kv = TextInput(text=str(Shared.pg_selezionato['alchimia_effetto_ingredienti_3']),
                                                 pos_hint={"center_x": 0.4, "center_y": 0.5},
                                                 size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2),
                                                 padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_effetto_ingredienti_3kv)
    alchimia_effetto_ingredienti_4kv = TextInput(text=str(Shared.pg_selezionato['alchimia_effetto_ingredienti_4']),
                                                 pos_hint={"center_x": 0.5, "center_y": 0.5},
                                                 size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2),
                                                 padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_effetto_ingredienti_4kv)

    box.add_widget((Label(color=(0, 0, 0, 1), text="Moltiplicatori:", pos_hint={"center_x": 0.6, "center_y": 0.8},
                          size_hint=(0.1, 0.5), font_size=(25))))
    alchimia_moltiplicatore_rossikv = TextInput(text=str(Shared.pg_selezionato['alchimia_moltiplicatore_rossi']),
                                                pos_hint={"center_x": 0.6, "center_y": 0.7},
                                                size_hint=(0.07, 0.04), background_color=(1, 0, 0, 0.5),
                                                padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_moltiplicatore_rossikv)
    alchimia_moltiplicatore_verdikv = TextInput(text=str(Shared.pg_selezionato['alchimia_moltiplicatore_verdi']),
                                                pos_hint={"center_x": 0.6, "center_y": 0.65},
                                                size_hint=(0.07, 0.04), background_color=(0, 1, 0, 0.5),
                                                padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_moltiplicatore_verdikv)
    alchimia_moltiplicatore_blukv = TextInput(text=str(Shared.pg_selezionato['alchimia_moltiplicatore_blu']),
                                              pos_hint={"center_x": 0.6, "center_y": 0.6},
                                              size_hint=(0.07, 0.04), background_color=(0, 0, 1, 0.5),
                                              padding=(2, 2, 2, 2), font_size=(23))
    box.add_widget(alchimia_moltiplicatore_blukv)

    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Slot 1:", pos_hint={"center_x": 0.45, "center_y": 0.35}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Slot 2:", pos_hint={"center_x": 0.55, "center_y": 0.35}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Slot 3:", pos_hint={"center_x": 0.45, "center_y": 0.25}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Slot 4:", pos_hint={"center_x": 0.55, "center_y": 0.25}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Skill:", pos_hint={"center_x": 0.8, "center_y": 0.45}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        Button(color=(0, 0, 0, 1), text="Pozioni", pos_hint={'center_x': 0.89, 'center_y': 0.4},
               on_release=mostra_pozioni,
               size_hint=(0.08, 0.04), background_color=(0.8, 1, 0.8, 0.4)))
    box.add_widget(
        Button(color=(0, 0, 0, 1), text="Tutti\nOggetti", pos_hint={'center_x': 0.89, 'center_y': 0.35},
               on_release=partial(Popups_NomePG_Oggetti_Tutti.oggetti_tutti_open,auto_select = "pozione"),
               size_hint=(0.08, 0.04), background_color=(0.8, 1, 0.8, 0.4)))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="Set:", pos_hint={"center_x": 0.8, "center_y": 0.35}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="TOT:", pos_hint={"center_x": 0.8, "center_y": 0.25}, size_hint=(0.1, 0.5),
               font_size=(25))))
    box.add_widget(
        (Label(color=(0, 0, 0, 1), text="FAIL:", pos_hint={"center_x": 0.91, "center_y": 0.25}, size_hint=(0.1, 0.5),
               font_size=(25))))
    ingrediente_1 = TextInput(text="0", pos_hint={"center_x": 0.45, "center_y": 0.3},
                              size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    ingrediente_2 = TextInput(text="0", pos_hint={"center_x": 0.55, "center_y": 0.3},
                              size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    ingrediente_3 = TextInput(text="0", pos_hint={"center_x": 0.45, "center_y": 0.2},
                              size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    ingrediente_4 = TextInput(text="0", pos_hint={"center_x": 0.55, "center_y": 0.2},
                              size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    moltiplicatore = TextInput(text="0", pos_hint={"center_x": 0.8, "center_y": 0.4},
                               size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    set = TextInput(text="0", pos_hint={"center_x": 0.8, "center_y": 0.3},
                    size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    effetto = TextInput(text="0", pos_hint={"center_x": 0.8, "center_y": 0.2},
                        size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    fail = TextInput(text="0", pos_hint={"center_x": 0.91, "center_y": 0.2},
                     size_hint=(0.07, 0.04), background_color=(1, 1, 1, 0.2))
    box.add_widget(ingrediente_1)
    box.add_widget(ingrediente_2)
    box.add_widget(ingrediente_3)
    box.add_widget(ingrediente_4)
    box.add_widget(moltiplicatore)
    box.add_widget(set)
    box.add_widget(effetto)
    box.add_widget(fail)
    lista_reagenti = ['Residuo magico', 'Bacca Shein', 'Ape', 'Spine di Heather', "Polvere d'ossa",
                      'Foglia azzurra', 'Fungo di cenere', 'fiore del deserto', 'Polvere vulcanica',
                      'Radice di Trama', 'Gold Kanet', 'Marshmerrow', 'Coppa elfica', 'muschio rosso',
                      'fiore di belladonna', 'campanula mortale', 'fiori di montagna', 'farfalla blu',
                      'fungo di palude', 'Semi bianchi', 'Lingua di drago', 'libellula', 'fiore della rugiada',
                      'jazabay', 'Scarabeo magico', 'Porcino topazio', 'insetto blu', 'fungo nero ',
                      'insetto rosso', 'Radice di Mandragora', 'Rosa spinosa', 'fungo luminoso',
                      'fiore del sangue', 'fiore luminoso', 'radice di nirn', 'Smeraldo', 'Rubino', 'Zaffiro ',
                      'Ape Regina', 'Diamante', 'Ambrosia', 'Fiore di metallo']
    tipo_reagenti = ['B1', 'V1', 'R1', 'R1', 'V1', 'B1', 'V1', 'R1', 'R1', 'V1', 'B1', 'R1', 'B1', 'R1', 'V1',
                     'R1', 'B1', 'B1', 'B1', 'V1', 'V1', 'V1', 'B1', 'R1', 'B2', 'V2', 'B2', 'V2', 'R2', 'V2',
                     'R2', 'B2', 'R2', 'B3', 'V3', 'V3', 'R3', 'B3', 'R3', 'V4', 'B4', 'R4']
    reagenteestrattokv = TextInput(size_hint=(0.15, 0.04), text=f"",
                                   pos_hint={"center_x": 0.85, "center_y": 0.75}, padding=(1, 1, 1, 1))
    tiporeagenteestrattokv = TextInput(size_hint=(0.05, 0.04), text=f"",
                                       pos_hint={"center_x": 0.95, "center_y": 0.75}, padding=(1, 1, 1, 1))
    box.add_widget(reagenteestrattokv)
    box.add_widget(tiporeagenteestrattokv)

    def estrai_reagente(*args):
        numero = randrange(0, 42)
        reagenteestrattokv.text = lista_reagenti[numero]
        tiporeagenteestrattokv.text = tipo_reagenti[numero]

    box.add_widget(
        Button(color=(0, 0, 0, 1), text="Estrai \nReagente", pos_hint={'center_x': 0.85, 'center_y': 0.8},
               on_release=estrai_reagente,
               size_hint=(0.1, 0.04), background_color=(0.8, 1, 0.8, 0.4)))
    popup.open()

    def creapozione(*args):
        effetto.text = str(int((float(ingrediente_1.text) + float(ingrediente_2.text) + float(
            ingrediente_3.text) + float(ingrediente_4.text)) * (float(set.text) + float(moltiplicatore.text))))
        fail.text = str(randrange(0, 100))

    box.add_widget(
        Label(color=(0, 0, 0, 1),
              text="LV 1\nPolvere d'ossa    V\nGelatina di Scrib V\nCoda di Ratto      R\nOcchio di Cane   B"
                   "\n \nLV 3\nFittone                      V\noc. tig. denti sciab. R\nartigli di orso           R\ngrasso di troll          V\n"
                   "sali di gelo               B\nsali di fuoco             V\nsali del vuoto           R",
              font_size=12, pos_hint={"center_x": 0.725, "center_y": 0.6}))

    box.add_widget(
        Label(color=(0, 0, 0, 1), text="LV 2\nGel di Netch         V\nZucchero Lunare B\nCuore di Lupo      R"
                                       "\n \n \nLV 4\nDente di Gigante      R\nPolvere di Vampiro V\nAcqua di Sinderion  V\nSeta di Daedra          B\n"
                                       "Cuore di Daedra       R\nEctoplasma               B",
              font_size=12, pos_hint={"center_x": 0.91, "center_y": 0.608}))
    box.add_widget(Label(color=(0, 0, 0, 1), text="LV.1 LV.2 LV.3 LV.4 LV.5 LV.6 LV.7 LV.8 LV.9 LV.10 ", font_size=15,
                         pos_hint={"center_x": 0.3, "center_y": 0.459}))
    box.add_widget(
        Label(color=(0, 0, 0, 1), text="3+   6+    9+    12+   15+   18+   21+  24+   27+  30+ ", font_size=15,
              pos_hint={"center_x": 0.295, "center_y": 0.439}))
    box.add_widget(
        Label(color=(0, 0, 0, 1), text="fail   0%    10%   20%   30%   40%   50%   60%   70%   80%   90%", font_size=14,
              pos_hint={"center_x": 0.27, "center_y": 0.419}))
    box.add_widget(Button(color=(0, 0, 0, 1), text="SALVA E CHIUDI", on_press=salvaalchimia, on_release=popup.dismiss,
                          pos_hint={"center_x": 0.2, "center_y": 0.06}, size_hint=(0.25, 0.12),
                          background_color=(0, 0, 0, 0.15)))
    box.add_widget(Button(color=(0, 0, 0, 1), text="CREA", on_press=creapozione,
                          pos_hint={"center_x": 0.7, "center_y": 0.06}, size_hint=(0.25, 0.12),
                          background_color=(0, 0, 0, 0.15)))

