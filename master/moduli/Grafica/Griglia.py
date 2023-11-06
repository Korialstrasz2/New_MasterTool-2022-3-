import os
from kivy.uix.button import Button
from kivy.properties import partial
from kivy.uix.image import Image
import Moduli.SharedData as Shared
path = os.getcwd()

class Dati:
    immagine_per_casella = f"{Shared.path_art}/hexes/vuoto.png"
    dimensione_griglia = "l"
    dimensione_griglia_attuale = ""
    click_tutte_le_caselle = False
    orientamento_griglia = "a"

def gestisci_casella(numero_casella,*args):
    self = Shared.finestra
    exec(f"self.immaginel1{numero_casella}kv.source = Dati.immagine_per_casella")

def tutte_le_caselle(*args):
    if Dati.click_tutte_le_caselle == False:
        Dati.click_tutte_le_caselle = True
    else:
        Dati.click_tutte_le_caselle = False
        for numero in range(1, 10000):
            try:
                gestisci_casella(numero)
            except:
                break

def show_griglia():
    grandezza = Dati.dimensione_griglia
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

def selezionacolore(numero,*args):
    path = os.getcwd()
    if numero == "vuoto":
        Dati.immagine_per_casella = f"{Shared.path_art}/hexes/vuoto.png"
    else:
        listanomihex = ["hexviola","hexarancione","hexblu","hexceleste","hexbianco","hexnero","hexrosso","hexrosso1",
                    "hexrosso2","hexrosso3","hexrosso4","hexverde","hexverdescuro","hexverdino","hexverdissimo",
                        "hexviolascuro","hexgiallo","hexmagenta"]
        Dati.immagine_per_casella = f"{Shared.path_art}/hexes/{listanomihex[numero-1]}{Dati.orientamento_griglia}.png"

def rimuovibottonicolori():
    self = Shared.finestra
    for item in range(1,19):
        self.remove_widget(eval(f"self.colori{item}kv"))
    self.remove_widget(self.colotututtihexkv)


def bottonicolorihex():
    self = Shared.finestra
    step_per_y = True
    x = 0.901
    y = 0.4965
    x_base = 0.902
    larghezza =0.0245
    altezza = 0.039
    step_x = 0.01
    limite_x = 0.985
    path = os.getcwd()
    for item in range(1, 19):
        exec(f"""self.colori{item}kv = Button(disabled=False, size_hint=(larghezza, altezza),
         on_release=partial(selezionacolore,{item}),
                               background_color = (1,1,0.3,0),pos_hint={{"x": {x}, "top": {y}}})""")
        exec(f"""self.add_widget(self.colori{item}kv)""")
        x += larghezza
        if x >= limite_x:
            x = x_base
            if step_per_y == True:
                x+=step_x
                step_per_y = False
            else:
                step_per_y = True
            y -= altezza
    self.colotututtihexkv =  Button(size_hint=(0.033, 0.059), on_release=tutte_le_caselle,
                               background_color = (1,1,0.3,0),pos_hint={"x": 0.9332, "top": 0.299})
    self.add_widget(self.colotututtihexkv)
    self.nocolorihexkv = Button(size_hint=(0.03, 0.05), on_release=partial(selezionacolore,"vuoto"),
                               background_color = (1,1,0.3,0),pos_hint={"x": 0.97, "top": 0.292})
    self.add_widget(self.nocolorihexkv)

def bottonehex():
    self = Shared.finestra
    path = os.getcwd()
    immaginegruppohex = f"{Shared.path_art}/barracolorihex.png"
    try:
        if self.immaginegruppohexkv.pos_hint == {"x": 0.8, "top": 0.515}:
            self.immaginegruppohexkv.pos_hint = {"x": 3.8, "top": 0.515}
            rimuovibottonicolori()
            for btnimg in ["btnreg","imgreg","btncit","imgcit","btnloc","imgloc","btnris","imgris","btnnpc","imgnpc"]:
                exec(f"self.ids.{btnimg}.pos_hint['x'] -= 3")
            for numero in range(1, 10000):
                try:
                    exec(f"self.casella{numero}kv.pos_hint['x'] += 3")
                    exec(f"self.immaginel1{numero}kv.pos_hint['x'] += 3")
                except:
                    break
        else:
            self.immaginegruppohexkv.pos_hint = {"x": 0.8, "top": 0.515}
            bottonicolorihex()
            for btnimg in ["btnreg","imgreg","btncit","imgcit","btnloc","imgloc","btnris","imgris","btnnpc","imgnpc"]:
                exec(f"self.ids.{btnimg}.pos_hint['x'] += 3")
            if Dati.dimensione_griglia == Dati.dimensione_griglia_attuale:
                for numero in range(1, 10000):
                    try:
                        exec(f"self.casella{numero}kv.pos_hint['x'] -= 3")
                        exec(f"self.immaginel1{numero}kv.pos_hint['x'] -= 3")
                    except:
                        break
            else:
                show_griglia()
    except:
        self.immaginegruppohexkv = Image(size_hint=(0.3, 0.3), source=immaginegruppohex,
                                         pos_hint={"x": 0.8, "top": 0.515})
        self.add_widget(self.immaginegruppohexkv)

        for btnimg in ["btnreg", "imgreg", "btncit", "imgcit", "btnloc", "imgloc", "btnris", "imgris", "btnnpc",
                       "imgnpc"]:
            exec(f"self.ids.{btnimg}.pos_hint['x'] += 3")
        show_griglia()
        bottonicolorihex()

def giragriglia():
    self1 = Shared.finestra
    parte_1 = self1.ids.immeginegriglia.source.split(".")[0]
    if parte_1[-1] == "a":
        replace = parte_1[:-1] + "b.png"
        Dati.orientamento_griglia = "b"
    else:
        replace = parte_1[:-1] + "a.png"
        Dati.orientamento_griglia = "a"
    self1.ids.immeginegriglia.source = replace

def grigliasino():
    self1 = Shared.finestra
    if self1.ids.boxgriglia.pos_hint == {"x": 0.365, "top": 0.785}:
        self1.ids.boxgriglia.pos_hint = {"x": 4, "top": 4}
    else:
        self1.ids.boxgriglia.pos_hint = {"x": 0.365, "top": 0.785}


def grigliaxs():
    self1 = Shared.finestra
    self1.ids.immeginegriglia.source = 'Art/immagini/grigliaxsmalla.png'
    Dati.dimensione_griglia = "xs"

def griglias():
    self1 = Shared.finestra
    self1.ids.immeginegriglia.source = 'Art/immagini/grigliasmalla.png'
    Dati.dimensione_griglia = "s"

def grigliam():
    self1 = Shared.finestra
    self1.ids.immeginegriglia.source = 'Art/immagini/grigliamediuma.png'
    Dati.dimensione_griglia = "m"

def griglial():
    self1 = Shared.finestra
    self1.ids.immeginegriglia.source = 'Art/immagini/griglialargea.png'
    Dati.dimensione_griglia = "l"

def grigliaxl():
    self1 = Shared.finestra
    self1.ids.immeginegriglia.source = 'Art/immagini/grigliaxlargea.png'
    Dati.dimensione_griglia = "xl"