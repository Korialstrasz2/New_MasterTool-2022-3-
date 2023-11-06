from math import floor
from random import randrange

import Moduli.SharedData as Shared
from Moduli.Grafica import Popups_NomePG_Skill
from Moduli.Logica import Salvataggio

from kivy.lang import Builder
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class Temp:
    bottoneskill = ""

def skillopen(*args):
    box = FloatLayout()
    Temp.bottoneskill = ""
    popup = Popup(title='Skill', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(1230, 1000),
                  auto_dismiss=True)

    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/skillbg.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
    Builder.load_string("""
<Label>:
    color: 1,1,1,1
""")

    box.add_widget(notepic)
    skill_lista = {"scalare": ["Scalare", "forza"],
                   "manovrare_veicoli": ["Manovrare Veicoli", "forza"],
                   "nuotare": ["Nuotare", "resistenza"],
                   "rapidita_di_mano": ["Rapidita Di Mano", "velocita"],
                   "suonare": ["Suonare", "agilita"],
                   "cavalcare": ["Cavalcare", "agilita"],
                   "furtivita": ["Furtivita", "agilita"],
                   "sapienza_magica": ["Sapienza Magica", "intelligenza"],
                   "ingegneria": ["Ingegneria", "intelligenza"],
                   "strategia_militare": ["Strategia Militare", "intelligenza"],
                   "conoscenze_naturaegeografia": ["Conoscenze Nat/Geo", "concentrazione"],
                   "conoscenze_religioni": ["Conoscenze Religioni", "concentrazione"],
                   "conoscenze_storiaenobilta": ["Conoscenze Sto/Nob", "concentrazione"],
                   "percezione": ["Percezione", "concentrazione"],
                   "diplomazia": ["Diplomazia", "personalita"],
                   "intimidire": ["Intimidire", "personalita"],
                   "cammuffare": ["Cammuffare", "personalita"],
                   "raggirare": ["Raggirare", "personalita"],
                   "sopravvivenza": ["Sopravvivenza", "saggezza"],
                   "gestione_risorse": ["Gestione Risorse", "saggezza"],
                   "intuizione": ["Intuizione", "saggezza"]
                   }
    box.add_widget(
        Button(text="Punti Esperienza", pos_hint={"x": 0.52, "top": 1}, size_hint=(0.1, 0.05), on_release=Popups_NomePG_Skill.skill_excel_open))
    ybarra = 0.978
    for item in skill_lista:
        exec(f"Temp.yscritta{item} = {ybarra}")
        ybarra += 0.0075
        exec(f"Temp.ybarra1{item} = {ybarra}")
        ybarra -= 0.0215
        exec(f"Temp.ybarra2{item} = {ybarra}")
        ybarra -= 0.0335

    for abilita in skill_lista:
        exec(
            f"""if str(Shared.pg_selezionato['skill_{abilita}']) == '0': Shared.pg_selezionato['skill_{abilita}'] = '123' """)
        exec(
            f"Shared.pg_selezionato['barra1{abilita}'] = int(str(Shared.pg_selezionato['skill_{abilita}'])[0])")
        exec(
            f"Shared.pg_selezionato['barra2{abilita}'] = int(str(Shared.pg_selezionato['skill_{abilita}'])[1])")
        exec(f"Shared.pg_selezionato['extra{abilita}'] = int(str(Shared.pg_selezionato['skill_{abilita}'])[2])")

    def salvaabilita(*args):
        for abilitasalva in skill_lista:
            a = eval(f"Shared.pg_selezionato['barra1{abilitasalva}']")
            b = eval(f"Shared.pg_selezionato['barra2{abilitasalva}']")
            c = eval(f"Shared.pg_selezionato['extra{abilitasalva}']")
            exec(f"Shared.pg_selezionato['skill_{abilitasalva}'] = '{a}{b}{c}'")
        Salvataggio.salva_pgnpc(Shared.pg_selezionato['nome_in_uso'])

    guida = Image(allow_stretch=True, size_hint=(0.5, 0.5), source=f'{Shared.path_art}/guidaabilita.png',
                  pos_hint={"center_x": 0.8, "center_y": 0.74})
    box.add_widget(guida)

    Temp.dadod6 = Image(allow_stretch=True, size_hint=(0.2, 0.2), source=f'{Shared.path_art}/d6img.png',
                        pos_hint={"center_x": 0.8, "center_y": 0.4})
    Temp.dadod8 = Image(allow_stretch=True, size_hint=(0.2, 0.2), source=f'{Shared.path_art}/d8img.png',
                        pos_hint={"center_x": 0.8, "center_y": 0.4})
    Temp.dadod10 = Image(allow_stretch=True, size_hint=(0.2, 0.2), source=f'{Shared.path_art}/d10img.png',
                         pos_hint={"center_x": 0.8, "center_y": 0.4})
    Temp.dadod12 = Image(allow_stretch=True, size_hint=(0.2, 0.2), source=f'{Shared.path_art}/d12img.png',
                         pos_hint={"center_x": 0.8, "center_y": 0.4})
    tirodado = Label(text="", pos_hint={"center_x": 0.7, "center_y": 0.47}, font_size=15)

    noteskill = TextInput(text=Shared.pg_selezionato["diario20"], pos_hint={"x": 0.65, "top": 0.45},
                          size_hint=(0.25, 0.1))

    def salvanoteskill(*args):
        Shared.pg_selezionato["diario20"] = noteskill.text

    box.add_widget(
        Button(text="Salva", pos_hint={"x": 0.9, "top": 0.45}, size_hint=(0.05, 0.1), on_release=salvanoteskill))
    nomeskilltirobox = TextInput(text="Nome Skill", pos_hint={"x": 0.65, "top": 0.30}, size_hint=(0.2, 0.05))
    dadoskilltirobox = TextInput(text="dado", pos_hint={"x": 0.85, "top": 0.30},
                                 size_hint=(0.05, 0.05), font_size="12")
    baseskilltirobox = TextInput(text="base", pos_hint={"x": 0.9, "top": 0.30}, size_hint=(0.07, 0.05),
                                 font_size="15")
    box.add_widget(noteskill)
    box.add_widget(nomeskilltirobox)
    box.add_widget(dadoskilltirobox)
    box.add_widget(baseskilltirobox)

    Temp.d6status = False
    Temp.d8status = False
    Temp.d10status = False
    Temp.d12status = False

    def selezionaabilita(nome_skill, nome_skill_originale, *args):
        if Temp.bottoneskill != nome_skill:
            Temp.bottoneskill = nome_skill
            nonlocal tirodado
            tirodado.pos_hint = {"center_x": 5.78, "center_y": 0.45}
            if Temp.d6status == True:
                Temp.d6status = False
                box.remove_widget(Temp.dadod6)
            if Temp.d8status == True:
                Temp.d8status = False
                box.remove_widget(Temp.dadod8)
            if Temp.d10status == True:
                Temp.d10status = False
                box.remove_widget(Temp.dadod10)
            if Temp.d12status == True:
                Temp.d12status = False
                box.remove_widget(Temp.dadod12)

            nomeskilltirobox.text = nome_skill
            skill1temp = int(eval(f"Shared.pg_selezionato['barra1{nome_skill_originale}']"))
            skill3temp = int(eval(f"Shared.pg_selezionato['extra{nome_skill_originale}']"))
            exec(f"""if 0 <= float(Shared.pg_selezionato['barra2{nome_skill_originale}']) < 2:
            dadoskilltirobox.text = 'd6'
            Temp.d6status = True
            box.add_widget(Temp.dadod6)""")
            exec(f"""if 2 <= float(Shared.pg_selezionato['barra2{nome_skill_originale}']) < 4:
            dadoskilltirobox.text = 'd8'
            Temp.d8status = True
            box.add_widget(Temp.dadod8)""")
            exec(f"""if 4 <= float(Shared.pg_selezionato['barra2{nome_skill_originale}']) < 6:
            dadoskilltirobox.text = 'd10'
            Temp.d10status = True
            box.add_widget(Temp.dadod10)""")
            dadoskilltirobox.font_size = "15"
            exec(f"""if 6 <= float(Shared.pg_selezionato['barra2{nome_skill_originale}']) < 8:
            dadoskilltirobox.text = 'd12'
            Temp.d12status = True
            box.add_widget(Temp.dadod12)""")
            exec(f"""baseskilltirobox.text = "base: {int(skill1temp + skill3temp)}" """)
            baseskilltirobox.font_size = "14"
        else:
            abilitaopenpop(nome_abilita=nome_skill_originale)
            Temp.bottoneskill = ""

    colori = {"forza": "(1,0,0,1)", "resistenza": "(0.85,0,0,1)", "velocita": "(0,1,0,1)", "agilita": "(0,0.85,0,1)",
              "intelligenza": "(0,0,1,1)", "concentrazione": "(0,0,0.85,1)", "personalita": "(0.9,0.9,0,1)",
              "saggezza": "(0.82,0.82,0,1)"}

    for abilita in skill_lista:
        bonus = 0
        if skill_lista[abilita][1] == "personalita":
            bonus = int(
                eval(f"str(int(floor(int(Shared.pg_selezionato['{skill_lista[abilita][1]}_tot']) - 10) / 4))"))
        bonus += int(eval(f"Shared.pg_selezionato['extra{abilita}']"))
        exec(f"""

barra{abilita}nome = Label(text="{skill_lista[abilita][0]}", pos_hint={{"center_x": 0.059, "center_y":Temp.yscritta{abilita}}},
                            halign= 'left', size_hint=(0.2, 0.05), background_color=(0, 0, 0, 0))
box.add_widget(barra{abilita}nome)
box.add_widget(
    Image(source=f"Art/skill{abilita}img.png", size_hint=(0.05, 0.05), pos_hint={{"x": 0.45, "center_y":Temp.yscritta{abilita}-0.005}}))
box.add_widget(Button(pos_hint={{"x": 0.45, "center_y":Temp.yscritta{abilita}-0.005}},
           size_hint=(0.05, 0.05), background_normal='',
            on_release=partial(selezionaabilita, skill_lista["{abilita}"][0], '{abilita}'), background_color=(0, 0, 1, 0)))

box.add_widget(Label(text=f"(+{bonus})",
                     pos_hint={{"center_x": 0.135, "center_y": Temp.ybarra1{abilita}-0.009}}))
Temp.{abilita}1_barra_lunghezza = ((float(Shared.pg_selezionato['barra1{abilita}']) + 1) / 8 * 3 / 10)
Temp.{abilita}1_basebarra = 0.15 + (Temp.{abilita}1_barra_lunghezza / 2)
Temp.{abilita}1_barra = (
    Button(pos_hint={{"center_x": Temp.{abilita}1_basebarra, "center_y": Temp.ybarra1{abilita}}},
           size_hint=(Temp.{abilita}1_barra_lunghezza, 0.02), background_normal='',
           background_color={colori[skill_lista[abilita][1]]}))
box.add_widget(Temp.{abilita}1_barra)

Temp.{abilita}2_barra_lunghezza = ((float(Shared.pg_selezionato['barra2{abilita}']) + 1) / 8 * 3 / 10)
Temp.{abilita}2_basebarra = 0.15 + (Temp.{abilita}2_barra_lunghezza / 2)
Temp.{abilita}2_barra = (
    Button(pos_hint={{"center_x": Temp.{abilita}2_basebarra, "center_y": Temp.ybarra2{abilita}}},
           size_hint=(Temp.{abilita}2_barra_lunghezza, 0.02), background_normal='',
           background_color={colori[skill_lista[abilita][1]]}))
box.add_widget(Temp.{abilita}2_barra)

box.add_widget(Image(source="Art/barraskillv2.png",
                     pos_hint={{"center_x": 0.3, "center_y":  Temp.ybarra1{abilita}}},
                     size_hint=(0.3, 0.07)))
box.add_widget(Image(source="Art/barraskillv2.png",
                     pos_hint={{"center_x": 0.3, "center_y":  Temp.ybarra2{abilita}}},
                     size_hint=(0.3, 0.07)))
""")


        def abilitaopenpop(nome_abilita, *args):
            box = GridLayout(padding=(5), cols=1, rows=12)
            popup = Popup(title='', title_size=(50),
                          title_align='center', content=box,
                          size_hint=(None, None), size=(300, 400),
                          auto_dismiss=True)
            box.add_widget(Label(text = nome_abilita, size_hint = (1,0.2)))
            box.add_widget(Label(text = "Inserisci il numero\ncon il valore finale.", size_hint = (1,0.2)))
            box_interno = GridLayout(padding=(5), cols=2, rows=12)
            box_dettagli = GridLayout(padding=(5), cols=1, rows=12)
            box_titolo = GridLayout(padding=(5), cols=2, rows=12)
            a = eval(f"Shared.pg_selezionato['barra1{nome_abilita}']")
            b = eval(f"Shared.pg_selezionato['barra2{nome_abilita}']")
            c = eval(f"Shared.pg_selezionato['extra{nome_abilita}']")
            exec(f"""box_titolo.add_widget(Label(text=f"Colonna 1: {a}", size_hint = (0.7,0.33)))""")
            colonna_1_box = TextInput(text=str(a), input_type='number', font_size=15, size_hint = (0.3,33))
            box_titolo.add_widget(colonna_1_box)
            if nome_abilita != "sopravvivenza":
                exec(f"""box_titolo.add_widget(Label(text=f"Colonna 2: {b}", size_hint = (0.7,0.33)))""")
                colonna_2_box = TextInput(text=str(b), input_type='number', font_size=15, size_hint = (0.3,33))
                box_titolo.add_widget(colonna_2_box)
            exec(f"""box_titolo.add_widget(Label(text=f"Extra: {c}", size_hint = (0.7,0.33)))""")
            colonna_3_box = TextInput(text=str(c), input_type='number', font_size=15, size_hint = (0.3,33))
            box_titolo.add_widget(colonna_3_box)

            def confermaabilita2(nome_abilita, *args):
                nonlocal colonna_1_box, colonna_2_box, colonna_3_box
                exec(
                    f"Shared.pg_selezionato['barra1{nome_abilita}'] = str(int(colonna_1_box.text))")
                if nome_abilita != "sopravvivenza":
                    exec(
                        f"Shared.pg_selezionato['barra2{nome_abilita}'] = str(int(colonna_2_box.text))")
                exec(
                    f"Shared.pg_selezionato['extra{nome_abilita}'] = str(int(colonna_3_box.text))")
                salvaabilita()
                Salvataggio.salva_pgnpc(Shared.pg_selezionato['nome_in_uso'])


            box_interno.add_widget(box_titolo)
            if nome_abilita == "sopravvivenza":
                popup.size = (600, 550)
                box_dettagli.add_widget(Label(text = "1-50% di trovare cibo in 1h.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "2-Abbassa un poco i malus\npercezione mentre si dorme.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "3- -1 incontri casuali.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "4-Senza sacco a pelo\nrecuperi fino a -1 stanc.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "5-100% di trovare cibo in 30m.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "6- -1 uncontri casuali.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "7-Senza sacco a pelo\nrecuperi fino a 0 stanc.", size_hint = (1,0.2)))
                box_dettagli.add_widget(Label(text = "7-(ulteriore) Puoi dormire\nsolo 4h a notte.", size_hint = (1,0.2)))
                box_interno.add_widget(box_dettagli)
            box.add_widget(box_interno)
            confermab = Button(text="CONFERMA", on_release=partial(confermaabilita2, f"{nome_abilita}"), size_hint = (0.999,0.2))
            box.add_widget(confermab)

            popup.open()

    def tiradadoskill(*args):
        nonlocal tirodado
        box.remove_widget(tirodado)
        if Temp.d6status == True:
            tiro = randrange(1, 7)
            box.add_widget(tirodado)
            tirodado.text = str(tiro)
            tirodado.font_size = 50
            tirodado.pos_hint = {"center_x": 0.78, "center_y": 0.405}
        if Temp.d8status == True:
            tiro = randrange(1, 9)
            box.add_widget(tirodado)
            tirodado.text = str(tiro)
            tirodado.font_size = 40
            tirodado.pos_hint = {"center_x": 0.792, "center_y": 0.45}
        if Temp.d10status == True:
            tiro = randrange(1, 11)
            box.add_widget(tirodado)
            tirodado.text = str(tiro)
            tirodado.font_size = 35
            tirodado.pos_hint = {"center_x": 0.8, "center_y": 0.445}
        if Temp.d12status == True:
            tiro = randrange(1, 13)
            box.add_widget(tirodado)
            tirodado.text = str(tiro)
            tirodado.font_size = 40
            tirodado.pos_hint = {"center_x": 0.798, "center_y": 0.42}

    box.add_widget(Label(text="guadagno imm.\n-3 +2(raz) -4 +3(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.24}))
    guadagnoimmediatoinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                       pos_hint={"x": 0.63, "top": 0.23})
    box.add_widget(guadagnoimmediatoinput)
    box.add_widget(Label(text="guadagno lun. ter.\n-3 +2(raz) -2 +1(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.21}))
    guadagnolungotermineinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                          pos_hint={"x": 0.63, "top": 0.20})
    box.add_widget(guadagnolungotermineinput)
    box.add_widget(Label(text="principi\n-6 +2(raz) -6 +1(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.18}))
    principiinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                              pos_hint={"x": 0.63, "top": 0.17})
    box.add_widget(principiinput)
    box.add_widget(Label(text="ordini\n-4 +2(raz) -3 0(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.15}))
    ordiniinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                            pos_hint={"x": 0.63, "top": 0.14})
    box.add_widget(ordiniinput)
    box.add_widget(Label(text="sforzo necessario\n-3 0(raz) -2 +1(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.12}))
    sforzonecessarioinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                      pos_hint={"x": 0.63, "top": 0.11})
    box.add_widget(sforzonecessarioinput)
    box.add_widget(Label(text="disposizione\n-3 +1(raz) -5 +3(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.09}))
    disposizioneinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                  pos_hint={"x": 0.63, "top": 0.08})
    box.add_widget(disposizioneinput)
    box.add_widget(Label(text="aspetto\n-4 +2(raz) -4 +2(em)", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.55, "top": 0.06}))
    aspettoinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                             pos_hint={"x": 0.63, "top": 0.05})
    box.add_widget(aspettoinput)
    box.add_widget(Label(text="credibilita(info passate)\nDa -7 a +5", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.24}))
    credibilitainput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                 pos_hint={"x": 0.78, "top": 0.23})
    box.add_widget(credibilitainput)
    box.add_widget(Label(text="reputazione\nDa -6 a +4", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.21}))
    reputazioneinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                 pos_hint={"x": 0.78, "top": 0.20})
    box.add_widget(reputazioneinput)
    box.add_widget(Label(text="potere sociale\nDa -3 a +3", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.18}))
    poteresocialeinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                   pos_hint={"x": 0.78, "top": 0.17})
    box.add_widget(poteresocialeinput)
    box.add_widget(Label(text="differenza fisica\nDa -3 a +3", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.15}))
    differenzafisicainput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                      pos_hint={"x": 0.78, "top": 0.14})
    box.add_widget(differenzafisicainput)
    box.add_widget(Label(text="ferite\nDa -3 a +3", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.12}))
    feriteinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                            pos_hint={"x": 0.78, "top": 0.11})
    box.add_widget(feriteinput)
    box.add_widget(Label(text="travestimento\nDa -8 a +2", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.09}))
    travestimentoinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                   pos_hint={"x": 0.78, "top": 0.08})
    box.add_widget(travestimentoinput)
    box.add_widget(Label(text="razza\nDa -8 a +0", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.7, "top": 0.06}))
    razzainput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                           pos_hint={"x": 0.78, "top": 0.05})
    box.add_widget(razzainput)
    box.add_widget(Label(text="conoscenza\nDa -3 a +3", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.85, "top": 0.24}))
    conoscenzainput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                pos_hint={"x": 0.93, "top": 0.23})
    box.add_widget(conoscenzainput)
    box.add_widget(Label(text="tiro nemico\nDa -1 a -12", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.85, "top": 0.21}))
    tironemicoinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                pos_hint={"x": 0.93, "top": 0.20})
    box.add_widget(tironemicoinput)
    box.add_widget(Label(text="skill nemica\nDa 0 a -7", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.85, "top": 0.18}))
    skillnemicainput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                                 pos_hint={"x": 0.93, "top": 0.17})
    box.add_widget(skillnemicainput)
    box.add_widget(Label(text="altro\nDa -6 a +6", font_size=11, size_hint=(0.05, 0.05),
                         pos_hint={"x": 0.85, "top": 0.15}))
    altroinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.03),
                           pos_hint={"x": 0.93, "top": 0.14})
    box.add_widget(altroinput)
    totaleinput = TextInput(text="0", padding=(1, 1, 1, 1), size_hint=(0.03, 0.04),
                            pos_hint={"x": 0.93, "top": 0.10})
    box.add_widget(totaleinput)

    def calcola(*args):
        Temp.bottoneskill = ""
        tiradadoskill()
        totaleinput.text = str(
            int(altroinput.text) + int(skillnemicainput.text) + int(tironemicoinput.text) + int(
                conoscenzainput.text)
            + int(razzainput.text) + int(travestimentoinput.text) + int(feriteinput.text) + int(
                differenzafisicainput.text)
            + int(poteresocialeinput.text) + int(reputazioneinput.text) + int(credibilitainput.text) + int(
                aspettoinput.text) + int(disposizioneinput.text)
            + int(sforzonecessarioinput.text) + int(ordiniinput.text) + int(principiinput.text) + int(
                guadagnolungotermineinput.text) + int(guadagnoimmediatoinput.text))

    box.add_widget(
        Button(size_hint=(0.05, 0.04), text="somma\ntira", pos_hint={"x": 0.87, "top": 0.10}, on_release=calcola))
    popup.open()


