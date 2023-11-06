import os

import Moduli.SharedData as Shared
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def selezionacolore(numero,*args):
    print("tag")
    if numero == "vuoto":
        Dati.immagine_per_casella = f"{Shared.path_art}/hexes/vuoto.png"
    else:
        listanomihex = ["hexviola","hexarancione","hexblu","hexceleste","hexbianco","hexnero","hexrosso","hexrosso1",
                    "hexrosso2","hexrosso3","hexrosso4","hexverde","hexverdescuro","hexverdino","hexverdissimo",
                        "hexviolascuro","hexgiallo","hexmagenta"]
        Dati.immagine_per_casella = f"{Shared.path_art}/hexes/{listanomihex[numero-1]}{Dati.orientamento_griglia}.png"


def openmappa(*args, hex = False):
    from Moduli.Grafica import KivyInput
    box = FloatLayout()
    popup = Popup(title=f"", title_size=(30),
                  title_align='center',content = box,
                  size_hint=(None, None), size=(2000, 1100),
                  auto_dismiss=True)

    box_polonia = FloatLayout()

    boximg = KivyInput.Zoom(size_hint=(4, 4))
    if not hex:
        notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/megamappa.jpg',
                        pos_hint={"center_x": 0.5, "center_y": 0.5})
    else:
        notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/megamappa_hex.jpg',
                        pos_hint={"center_x": 0.5, "center_y": 0.5})
    boximg.add_widget(notepic)

    box.add_widget(box_polonia)
    bg_pop = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/bg_mappa_del_mondo.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(bg_pop)

    box_polonia.add_widget(boximg)
    popup.open()

class Dati:
    immagine_per_casella = f"{Shared.path_art}/hexes/hexrosso.png"
    dimensione_griglia = "l"
    dimensione_griglia_attuale = ""
    click_tutte_le_caselle = False
    orientamento_griglia = "a"


def show_griglia():
    grandezza = "XS"
    self = Shared.finestra
    for numero in range(1,10000):
        try:
            self.remove_widget(eval(f"self.casella{numero}kv"))
            self.remove_widget(eval(f"self.immaginal1{numero}kv"))
        except:
            Dati.immagine_per_casella = f"{Shared.path_art}/hexes/vuoto.png"
            break
    step_per_y = True

    if grandezza in ["m","s","xs"]: #per s e xs non vale la pena, ma per non far buggare le griglie glieli faccio creare lostesso come m
        Dati.dimensione_griglia_attuale = "m"
        x = 0.365
        y = 0.7755
        x_base = 0.365
        larghezza =0.02375
        altezza = 0.0372
        numero = 331
        step_x = 0.0113
        limite_x = 0.878
        x_offset_immagine = -0.0027
        y_offset_immagine = +0.004
        x_molt_immagine = 1
        y_molt_immagine = 1.0035

    if grandezza == "l":
        Dati.dimensione_griglia_attuale = "l"
        x = 0.365
        y = 0.77
        x_base = 0.365
        larghezza =0.0348
        altezza = 0.0545
        numero = 151
        step_x = 0.0175
        limite_x = 0.875
        x_offset_immagine = -0.0040
        y_offset_immagine = +0.0077
        x_molt_immagine = 0.998
        y_molt_immagine = 1.00062
    elif grandezza == "xl":
        Dati.dimensione_griglia_attuale = "xl"
        x = 0.368
        y = 0.76
        x_base = 0.368
        larghezza =0.0555
        altezza = 0.087
        numero = 55
        step_x = 0.0294
        limite_x = 0.85
        x_offset_immagine = -0.009
        y_offset_immagine = 0.01
        x_molt_immagine = 1
        y_molt_immagine = 1

    path = os.getcwd()
    for item in range(1, numero):
        exec(f"""self.casella{item}kv = Button(disabled=False, size_hint=(larghezza, altezza),
         on_release=partial(gestisci_casella,{item}),
                               background_color = (1,1,0.3,0),pos_hint={{"x": {x}, "top": {y}}})""")
        exec(f"""self.immaginel1{item}kv = Image(size_hint=(larghezza*1.257, altezza*1.257), source=Dati.immagine_per_casella,pos_hint={{"x": {(x+x_offset_immagine)*x_molt_immagine}, "top": {(y+y_offset_immagine)*y_molt_immagine}}})""")
        exec(f"""self.add_widget(self.immaginel1{item}kv)""")
        exec(f"""self.add_widget(self.casella{item}kv)""")
        x += larghezza
        if x >= limite_x:
            x = x_base
            if step_per_y == True:
                x+=step_x
                step_per_y = False
            else:
                step_per_y = True
            y -= altezza
