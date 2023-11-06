from random import randrange

import Moduli.SharedData as Shared
from Moduli.Logica import Salvataggio
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def viaggioopen(*args):
    box = FloatLayout()
    popup = Popup(title='Viaggio', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(650, 700),
                  auto_dismiss=True)
    bg = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/viaggiopop.png',
               pos_hint={"center_x": 0.5, "center_y": 0.5})
    box.add_widget(bg)

    def salvanoteviaggio(*args):
        Shared.pg_selezionato['diario19'] = noteviaggio.text
        Salvataggio.salva_pgnpc(Shared.pg_selezionato['nome_in_uso'])


    noteviaggio = (
        TextInput(text=Shared.pg_selezionato['diario19'], background_color=(1, 1, 1, 0.25), font_size="14", padding=(1, 1, 1, 1),
                  size_hint=(0.8, 0.05), pos_hint={"x": 0.07, "top": 0.975}))
    box.add_widget(noteviaggio)
    box.add_widget(Button(text="salva", pos_hint={"x": 0.9, "top": 0.975}, size_hint=(0.05, 0.05),
                          on_release=salvanoteviaggio))
    tilenum = Label(text="0", pos_hint={"center_x": 0.7, "center_y": 0.7}, size_hint=(0.1, 0.06),
                    background_color=(1, 1, 1, 0.1), font_size=(25))
    box.add_widget(tilenum)

    box.add_widget((Label(text="ORE:", pos_hint={"center_x": 0.22, "center_y": 0.5}, size_hint=(0.15, 0.7),
                          font_size=(25))))
    ore = TextInput(text="0", pos_hint={"center_x": 0.22, "center_y": 0.45}, size_hint=(0.1, 0.06),
                    background_color=(1, 1, 1, 0.1), font_size=(25))
    box.add_widget(ore)
    box.add_widget((Label(text="MOD\ntiro:", pos_hint={"center_x": 0.095, "center_y": 0.35},
                          size_hint=(0.15, 0.7), font_size=(23))))
    modtiro = TextInput(text="0", pos_hint={"center_x": 0.22, "center_y": 0.35}, size_hint=(0.1, 0.06),
                        background_color=(1, 1, 1, 0.1), font_size=(25))
    box.add_widget(modtiro)

    box.add_widget((Label(text="n. TIRI:", pos_hint={"center_x": 0.35, "center_y": 0.5}, size_hint=(0.15, 0.7),
                          font_size=(25))))
    tiri = TextInput(text="0", pos_hint={"center_x": 0.35, "center_y": 0.45}, size_hint=(0.1, 0.06),
                     background_color=(1, 1, 1, 0.1), font_size=(25))
    box.add_widget(tiri)
    box.add_widget((Label(text="TIRO:", pos_hint={"center_x": 0.35, "center_y": 0.4}, size_hint=(0.15, 0.7),
                          font_size=(25))))
    tiro = TextInput(text="0", pos_hint={"center_x": 0.35, "center_y": 0.35}, size_hint=(0.12, 0.06),
                     background_color=(1, 1, 1, 0.1), font_size=(23))
    box.add_widget(tiro)

    d100 = Label(text="d100:", pos_hint={"center_x": 0.3, "center_y": 0.15}, size_hint=(0.15, 0.7),
                 font_size=(25))
    box.add_widget(d100)
    labelrisultato = Label(text="Incontro:", pos_hint={"center_x": 0.3, "center_y": 0.05}, size_hint=(0.15, 0.7),
                 font_size=(25))
    box.add_widget(labelrisultato)
    barratiro = Button(pos_hint={"center_x": 0.85, "center_y": 0.15}, background_color=(0, 1, 0, 0.7),
                       size_hint=(0.15, 0.15))
    box.add_widget(barratiro)

    class lontananza():
        malus = 0
        tiro = 0

    class zona():
        malus = 0
        tiro = 0
        zona = ""

    class esagono():
        malus = 0

    def popuptiro(*args):
        popup = Popup(title='Incontri casuali!', title_size=(30),
                      title_align='center',
                      size_hint=(None, None), size=(400, 200),
                      auto_dismiss=True)
        popup.open()

    def bloccaviaggio(*args):
        if float(tiri.text) >= 1:
            popuptiro()

    def calcoloviaggio(*args):
        dadotiro = randrange(1, 101, 1)
        d100.text = "d100: " + str(dadotiro)
        tirotiro1 = int(round(float(lontananza.tiro + zona.tiro + dadotiro + int(modtiro.text)), 1))
        if tirotiro1 > 100:
            tirotiro1 = 100
        elif tirotiro1 < 1:
            tirotiro1 = 1
        elif tirotiro1 < 50:
            tirotiro1 -= int(modtiro.text)
        tiro.text = str(tirotiro1)
        effetti = Shared.dati_incontri_casuali[str(tirotiro1)]
        testorisultato = ""
        for x in effetti:
            if x != "":
                testorisultato += str(x) + "\n"
        labelrisultato.text = testorisultato
        altezzabrra = tirotiro1 / 120
        basebarra = 0.075 + (altezzabrra / 2)
        barratiro.size_hint = (0.15, altezzabrra)
        barratiro.pos_hint = {"center_x": 0.85, "center_y": basebarra}
        if tirotiro1 >= 61 and tirotiro1 <= 70:
            barratiro.background_color = (0.7, 1, 0, 0.7)
        if tirotiro1 >= 71 and tirotiro1 <= 80:
            barratiro.background_color = (1, 1, 0, 0.7)
        if tirotiro1 >= 81 and tirotiro1 <= 90:
            barratiro.background_color = (1, 0.7, 0, 0.7)
        if tirotiro1 >= 91 and tirotiro1 <= 100:
            barratiro.background_color = (1, 0, 0, 0.7)
        if tirotiro1 <= 60:
            barratiro.background_color = (0, 1, 0, 0.7)


    def lontananzabreve(*args):
        lontananza.tiro = -4

    lontananzabreveb = Button(on_release=lontananzabreve, size_hint=(0.1, 0.1),
                              pos_hint={"center_x": 0.25, "center_y": 0.58},
                              background_color=(0, 1, 0, 0.5), text="breve\ndistanza")
    box.add_widget(lontananzabreveb)

    def lontananzamediaimg(*args):
        lontananza.tiro = 0

    lontananzamediaimgb = Button(on_release=lontananzamediaimg, size_hint=(0.1, 0.1),
                                 pos_hint={"center_x": 0.4, "center_y": 0.58},
                                 background_color=(1, 1, 0, 0.5), text="media\ndistanza")
    box.add_widget(lontananzamediaimgb)

    def lontananzalunga(*args):
        lontananza.tiro = 4

    lontananzalungab = Button(on_release=lontananzalunga, size_hint=(0.1, 0.1),
                              pos_hint={"center_x": 0.55, "center_y": 0.58},
                              background_color=(1, 0, 0, 0.5), text="lunga\ndistanza")
    box.add_widget(lontananzalungab)

    calcolab = Button(on_release=calcoloviaggio, size_hint=(0.1, 0.1),
                      pos_hint={"center_x": 0.7, "center_y": 0.58},
                      background_color=(1, 1, 1, 0.7), text="VAI!")
    box.add_widget(calcolab)

    def regionesicura(*args):
        zona.tiro = 0
        zona.zona = "sicura"

    regionesicurab = Button(on_release=regionesicura, size_hint=(0.12, 0.055),
                            pos_hint={"center_x": 0.15, "center_y": 0.9},
                            background_color=(1, 0.5, 0.5, 0.5), text="Regione\nSicura")
    box.add_widget(regionesicurab)

    def regionecomune(*args):
        zona.tiro = 3
        zona.zona = "comune"

    regionecomuneb = Button(on_release=regionecomune, size_hint=(0.12, 0.055),
                          pos_hint={"center_x": 0.28, "center_y": 0.9},
                          background_color=(1, 0.5, 0.5, 0.5), text="Regione\nComune")
    box.add_widget(regionecomuneb)

    def regioneselvaggia(*args):
        zona.tiro = 6
        zona.zona = "fjalding"

    regioneselvaggiab = Button(on_release=regioneselvaggia, size_hint=(0.12, 0.055),
                           pos_hint={"center_x": 0.41, "center_y": 0.9},
                           background_color=(1, 0.5, 0.5, 0.5), text="Regione\nSelvaggia")
    box.add_widget(regioneselvaggiab)

    def regionepericolosa(*args):
        zona.tiro = 10
        zona.zona = "isinfier"

    regionepericolosab = Button(on_release=regionepericolosa, size_hint=(0.12, 0.055),
                           pos_hint={"center_x": 0.54, "center_y": 0.9},
                           background_color=(1, 0.5, 0.5, 0.5), text="Regione\nPericolosa")
    box.add_widget(regionepericolosab)

    def regionemortale(*args):
        zona.tiro = 15
        zona.zona = "moesring"

    regionemortaleb = Button(on_release=regionemortale, size_hint=(0.12, 0.055),
                           pos_hint={"center_x": 0.67, "center_y": 0.9},
                           background_color=(1, 0.5, 0.5, 0.5), text="Regione\nMortale")
    box.add_widget(regionemortaleb)

    def adderba(*args):
        ore.text = str(round(float(float(ore.text) + 0.5), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.25), 1))
        esagono.malus += 0.5
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    erba = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/erba.png',
                 pos_hint={"center_x": 0.1, "center_y": 0.8})
    box.add_widget(erba)
    box.add_widget(Button(on_release=adderba, pos_hint={"center_x": 0.1, "center_y": 0.8}, size_hint=(0.1, 0.1),
                          background_color=(0, 0, 0, 0)))

    def addneve(*args):
        ore.text = str(round(float(float(ore.text) + 0.75), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.3), 1))
        esagono.malus += 0.7
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    neve = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/neve.png',
                 pos_hint={"center_x": 0.2, "center_y": 0.8})
    box.add_widget(neve)
    box.add_widget(Button(on_release=addneve, pos_hint={"center_x": 0.2, "center_y": 0.8}, size_hint=(0.1, 0.1),
                          background_color=(0, 0, 0, 0)))

    def addforesta(*args):
        ore.text = str(round(float(float(ore.text) + 0.65), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.35), 1))
        esagono.malus += 1
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    foresta = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/foresta.png',
                    pos_hint={"center_x": 0.3, "center_y": 0.8})
    box.add_widget(foresta)
    box.add_widget(
        Button(on_release=addforesta, pos_hint={"center_x": 0.3, "center_y": 0.8}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addforestaneve(*args):
        ore.text = str(round(float(float(ore.text) + 0.85), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.4), 1))
        esagono.malus += 1.5
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    forestaneve = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/forestaneve.png',
                        pos_hint={"center_x": 0.4, "center_y": 0.8})
    box.add_widget(forestaneve)
    box.add_widget(
        Button(on_release=addforestaneve, pos_hint={"center_x": 0.4, "center_y": 0.8}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addstradaerba(*args):
        ore.text = str(round(float(float(ore.text) + 0.35), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.2), 1))
        esagono.malus += 0
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    stradaerba = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/stradaerba.png',
                       pos_hint={"center_x": 0.5, "center_y": 0.8})
    box.add_widget(stradaerba)
    box.add_widget(
        Button(on_release=addstradaerba, pos_hint={"center_x": 0.5, "center_y": 0.8}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addstradaneve(*args):
        ore.text = str(round(float(float(ore.text) + 0.4), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.2), 1))
        esagono.malus += 0.35
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    stradaneve = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/stradaneve.png',
                       pos_hint={"center_x": 0.6, "center_y": 0.8})
    box.add_widget(stradaneve)
    box.add_widget(
        Button(on_release=addstradaneve, pos_hint={"center_x": 0.6, "center_y": 0.8}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def adderbam(*args):
        ore.text = str(round(float(float(ore.text) + 0.65), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.35), 1))
        esagono.malus += 0.5
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    erbam = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/erbam.png',
                  pos_hint={"center_x": 0.1, "center_y": 0.7})
    box.add_widget(erbam)
    box.add_widget(
        Button(on_release=adderbam, pos_hint={"center_x": 0.1, "center_y": 0.7}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addnevem(*args):
        ore.text = str(round(float(float(ore.text) + 0.9), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.4), 1))
        esagono.malus += 0.7
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    nevem = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/nevem.png',
                  pos_hint={"center_x": 0.2, "center_y": 0.7})
    box.add_widget(nevem)
    box.add_widget(
        Button(on_release=addnevem, pos_hint={"center_x": 0.2, "center_y": 0.7}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addforestam(*args):
        tilenum.text = str(int(int(tilenum.text) + 1))
        ore.text = str(round(float(float(ore.text) + 0.75), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.45), 1))
        esagono.malus += 1
        bloccaviaggio()

    forestam = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/forestam.png',
                     pos_hint={"center_x": 0.3, "center_y": 0.7})
    box.add_widget(forestam)
    box.add_widget(
        Button(on_release=addforestam, pos_hint={"center_x": 0.3, "center_y": 0.7}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addforestanevem(*args):
        ore.text = str(round(float(float(ore.text) + 1.2), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.5), 1))
        esagono.malus += 1.5
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    forestanevem = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/forestanevem.png',
                         pos_hint={"center_x": 0.4, "center_y": 0.7})
    box.add_widget(forestanevem)
    box.add_widget(
        Button(on_release=addforestanevem, pos_hint={"center_x": 0.4, "center_y": 0.7}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addstradaerbam(*args):
        ore.text = str(round(float(float(ore.text) + 0.4), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.3), 1))
        esagono.malus += 0
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    stradaerbam = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/stradaerbam.png',
                        pos_hint={"center_x": 0.5, "center_y": 0.7})
    box.add_widget(stradaerbam)
    box.add_widget(
        Button(on_release=addstradaerbam, pos_hint={"center_x": 0.5, "center_y": 0.7}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addstradanevem(*args):
        ore.text = str(round(float(float(ore.text) + 0.5), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.3), 1))
        esagono.malus += 0.35
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    stradanevem = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/stradanevem.png',
                        pos_hint={"center_x": 0.6, "center_y": 0.7})
    box.add_widget(stradanevem)
    box.add_widget(
        Button(on_release=addstradanevem, pos_hint={"center_x": 0.6, "center_y": 0.7}, size_hint=(0.1, 0.1),
               background_color=(0, 0, 0, 0)))

    def addmare(*args):
        ore.text = str(round(float(float(ore.text) + 0.3), 1))
        tiri.text = str(round(float(float(tiri.text) + 0.15), 1))
        esagono.malus += 0.5
        tilenum.text = str(int(int(tilenum.text) + 1))
        bloccaviaggio()

    mare = Image(allow_stretch=True, size_hint=(0.1, 0.1), source=f'{Shared.path_art}/mare.png',
                 pos_hint={"center_x": 0.7, "center_y": 0.8})
    box.add_widget(mare)
    box.add_widget(Button(on_release=addmare, pos_hint={"center_x": 0.7, "center_y": 0.8}, size_hint=(0.1, 0.1),
                          background_color=(0, 0, 0, 0)))
    statocavalloviaggio = False
    def cavallo(*args):
        nonlocal  statocavalloviaggio
        if statocavalloviaggio == False:
            cavallob.text = "Cavallo\n (si)"
            statocavalloviaggio = True
            cavallob.background_color = (0.5, 1, 0.5, 0.5)
            ore.text = str(round(float(float(ore.text) / 2), 1))
        elif statocavalloviaggio == True:
            cavallob.text = "Cavallo\n (no)"
            statocavalloviaggio = False
            cavallob.background_color = (1, 0.5, 0.5, 0.5)
            ore.text = ore.text = str(round(float(float(ore.text) * 2), 1))

    cavallob = Button(on_release=cavallo, size_hint=(0.1, 0.1), pos_hint={"center_x": 0.1, "center_y": 0.58},
                      background_color=(1, 0.5, 0.5, 0.5), text="Cavallo\n (no)")
    box.add_widget(cavallob)
    popup.open()
