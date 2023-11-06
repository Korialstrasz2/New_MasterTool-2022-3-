import json
import shutil
import Moduli.SharedData as Shared
from Moduli import SharedData
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

def nuovo_pg_open():
    layout = GridLayout(cols=1, spacing=0, size_hint_y=1, height=200)
    popup = Popup(title='Nuovo PG', title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(400, 500),
                  auto_dismiss=True)

    def accettafuoo(*args):
        from Moduli.Grafica import FinestraLogin
        nuovonome = box_nome.text.split(" ")[0]
        shutil.copy(SharedData.path_dati + "/dbNeo.json",
                    SharedData.path_PG_e_Unici + f"/__pg__{nuovonome}.json")
        shutil.copy(SharedData.path_dati + "/skillvuoto.json",
                    SharedData.path_PG_e_Unici + f"/__pg__{nuovonome}skill.json")

        pathcompleto = Shared.path_PG_e_Unici + f"//__pg__{nuovonome}.json"
        with open(pathcompleto, 'r') as json_file:
            data = json.load(json_file)

        data["numero_npc"] = 0
        data["nome_in_uso"] = "__pg__" + nuovonome
        data["nome_valore_excel"] = "__pg__" + nuovonome
        data["nomepg"] = box_nome.text
        data["sesso"] = box_sesso.text
        data["razza1"] = box_razza_1.text
        data["razza2"] = box_razza_2.text
        data["eta"] = box_eta.text

        with open(pathcompleto, "w") as json_file:
            json.dump(data, json_file, indent=4)

        FinestraLogin.FinestraLogin.namebutton(self = Shared.finestra_login, nomepg = nuovonome, master=False)
        popup.dismiss()

    box_nome = TextInput()
    box_sesso = TextInput()
    box_razza_1 = TextInput()
    box_razza_2 = TextInput()
    box_eta = TextInput()
    accetta = Button(text="V Accetta", color=(1, 1, 1, 1), font_size=19, on_release=accettafuoo)
    rifiuta = Button(text="X Rifiuta", color=(1, 1, 1, 1), font_size=19, on_release=popup.dismiss)
    layout.add_widget(Label(text="Nome nuovo PG"))
    layout.add_widget(box_nome)
    layout.add_widget(Label(text="Sesso nuovo PG (m/f)"))
    layout.add_widget(box_sesso)
    layout.add_widget(Label(text="Raza principale nuovo PG"))
    layout.add_widget(box_razza_1)
    layout.add_widget(Label(text="Sottorazza nuovo PG"))
    layout.add_widget(box_razza_2)
    layout.add_widget(Label(text="Età nuovo PG"))
    layout.add_widget(box_eta)

    layout.add_widget(accetta)
    layout.add_widget(rifiuta)

    popup.open()
