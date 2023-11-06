from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout

from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def calcolatrice(self, *args):
    box = GridLayout(cols=1, padding=(10))
    popup = Popup(title='Calcolatrice', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(400, 200),
                  auto_dismiss=True)

    boxcalcolo = TextInput(text="2 * 5", multiline=False)
    box.add_widget(boxcalcolo)
    boxrisultato = TextInput(text="10")

    def calcolof(*args):
        boxrisultato.text = str(eval(boxcalcolo.text))

    box.add_widget(Button(text="CALCOLA", on_release=calcolof))
    box.add_widget(boxrisultato)
    popup.open()
