import Moduli.SharedData as Shared
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

def master_mode_check():
    layout = GridLayout(cols=1, spacing=0, size_hint_y=1, height=200)
    popup = Popup(title='Cambia mode', title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(400, 300),
                  auto_dismiss=True)

    def accettafuoo(*args):
        if Shared.tentativiPassowrdMastermode < 3:
            if "-" in textinputverifica.text[:-1] and textinputverifica.text.endswith("-"):
                Shared.mastermode = True
                Shared.tentativiPassowrdMastermode = 0
        else:
            if textinputverifica.text == "-stefanostaibarando-":
                Shared.mastermode = True
                Shared.tentativiPassowrdMastermode = 0

        Shared.tentativiPassowrdMastermode += 1
        popup.dismiss()

    if Shared.tentativiPassowrdMastermode < 3:
        layout.add_widget(Label(text="Inserisci qui la password"))
    else:
        layout.add_widget(Label(text="TROPPI TENTATIVI. Inserisci PUK"))
    accetta = Button(text="V Accetta", color=(1, 1, 1, 1), font_size=19, on_release=accettafuoo)
    rifiuta = Button(text="X Rifiuta", color=(1, 1, 1, 1), font_size=19, on_release=popup.dismiss)

    textinputverifica = TextInput()
    layout.add_widget(textinputverifica)
    layout.add_widget(rifiuta)
    layout.add_widget(accetta)

    popup.open()
