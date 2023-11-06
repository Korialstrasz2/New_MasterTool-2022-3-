import ast
import json

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, Popups_Calcolatrice, Popups_NomePG_Oggetti_Tutti
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori, GestioneSkill, Oggetti
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class Temp:
    datinegozioestratto = {}
    negoziocliccato = ""

def ordina_lista_con_dizionari(lista_input,chiave):
    lista_chiavi = []
    for item in lista_input:
        lista_chiavi.append(item[chiave])
    lista_sorted = sorted(list(set(lista_chiavi)))
    lista_def = []
    for chiave_sorted in lista_sorted:
        for item in lista_input:
            if item[chiave] == chiave_sorted:
                lista_def.append(item)
    return lista_def


def negozio_open(*args):
    box = FloatLayout()
    popup = Popup(title=f'Negozio', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(1350, 800),
                  auto_dismiss=True)
    notepic = Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/alembic magical2.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)

    scroller = ScrollView(size_hint=(1, 0.85), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    def negozi_salva_negozio(*args):
        box_1 = GridLayout(cols=2)
        box_new = GridLayout(cols=2, spacing=0, size_hint=(1, 1))
        popup = Popup(title=f'Zone e Negozi', title_size=(30),
                      title_align='center', content=box_1,
                      size_hint=(None, None), size=(1100, 800),
                      auto_dismiss=True)



        def selezionanegozio(zona, *args):
            def genera_negozio(zona,nome,livello,*args):
                genera([zona,nome])
                campo_livello.text = str(livello)
            scroller_destra.remove_widget(box_new)
            box_new.clear_widgets()
            box_new.size_hint = (1, 1)
            for negozio in ordina_lista_con_dizionari(Shared.negozi[zona], "tipo"):
                tipo_negozio = negozio['tipo']
                nome_negozio = negozio['nome']
                livello_negozio = negozio['livello']
                proprietario_negozio = negozio['proprietario']
                testo_totale = tipo_negozio + f" ({str(livello_negozio)})" + "\n    " + nome_negozio + "\n    " + proprietario_negozio
                box_y = box_new.size_hint[1]
                box_y += 0.05
                box_new.size_hint = (1,box_y)
                box_new.add_widget(Button(text=testo_totale, color=(1, 1, 1, 1), font_size=20, on_release=partial(genera_negozio, zona,nome_negozio,livello_negozio)))
            scroller_destra.add_widget(box_new)


        def aggiunginegozio(*args):
            try:
                pass
            except:
                with open(f"{Shared.path_dati}/lista-negozi.txt", "w") as listaegozi:
                    nome = nomenuovonegozio.text + "_" + str(Temp.datinegozioestratto[1])
                    linee[nome] = Temp.datinegozioestratto[0]
                    listaegozi.write(str(linee))
                    Oggetti.negozi = linee



        scroller = ScrollView(size_hint=(0.5, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
        scroller_destra = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
        scroller_destra.add_widget(box_new)
        box_1.add_widget(scroller)
        box_1.add_widget(scroller_destra)
        layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
        scroller.add_widget(layout1)

        y = 0.9
        l1sh = 1.2
        nomenuovonegozio = TextInput(text="Nome Nuovo Negozio", pos_hint={"center_x": 0.5, "center_y": y},
                                     size_hint=(0.1, 0.05), font_size=20)
        layout1.add_widget(nomenuovonegozio)
        y -= 0.1
        l1sh += 0.05
        layout1.add_widget(
            Button(text="Salva Nuovo Negozio", pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                   size_hint=(0.1, 0.05), font_size=20, on_release=aggiunginegozio))
        y -= 0.1
        l1sh += 0.05
        for zona in sorted(list(Shared.negozi.keys())):
            layout1.add_widget(
                Button(text=zona, pos_hint={"center_x": 0.5, "center_y": y}, color=(1, 1, 1, 1),
                       size_hint=(0.1, 0.05), font_size=20, on_release=partial(selezionanegozio, zona)))
            y -= 0.1
            l1sh += 0.05

        layout1.size_hint_y = l1sh
        popup.open()

    def aggiungi_a_negozio(nome, *args):
        campo_negozio.text = nome

    def genera(lista = None, *args):
        try:
            if type(lista) == list:
                zona = Shared.negozi[lista[0]]
                for negozio in zona:
                    if negozio['nome'] == lista[1]:
                        risultato = negozio['oggetti']
                        livello_negozio = negozio['livello']
                        campo_negozio.text = negozio['nome'] +"\n"+ negozio['proprietario']
                        campo_negozio.font_size = 12
                        break

            else:
                campo_negozio.font_size = 15
                risultato = Oggetti.estrai_negozio(tipo_negozio=campo_negozio.text, livello=campo_livello.text)
                livello_negozio = int(campo_livello.text)
            Temp.datinegozioestratto = [risultato,livello_negozio]
            modificatore_prezzo = 0
            if livello_negozio == 1:
                modificatore_prezzo = 5
            elif livello_negozio == 2:
                modificatore_prezzo = 12
            elif livello_negozio == 3:
                modificatore_prezzo = 17
            elif livello_negozio == 4:
                modificatore_prezzo = 22
            elif livello_negozio == 5:
                modificatore_prezzo = 30
            elif livello_negozio == 6:
                modificatore_prezzo = 40
            elif livello_negozio == 7:
                modificatore_prezzo = 50
            elif livello_negozio == 8:
                modificatore_prezzo = 58
            elif livello_negozio == 9:
                modificatore_prezzo = 65
            elif livello_negozio == 10:
                modificatore_prezzo = 70
            elif livello_negozio > 10:
                modificatore_prezzo = 75
            if "generale" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio generale.png'
            elif "contenitori" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio contenitori.png'
            elif "fabbro" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio fabbro.png'
            elif "taverna" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio taverna.png'
            elif "alchimista" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio alchimista.png'
            elif "oggetti magici" in campo_negozio.text or "oggetti_magici" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio oggetti magici.png'
            elif "arcieria" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio arcieria.png'
            elif "abbigliamento" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio abbigliamento.png'
            elif "armaiolo" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio armaiolo.png'
            elif "fabbricante di armi" in campo_negozio.text or "fabbricante_di_armi" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio fabbricante di armi.png'
            elif "carovana khajiit" in campo_negozio.text or "carovana_khajiit" in campo_negozio.text:
                notepic.source = f'{Shared.path_art}/negozio carovana khajiit.png'

            oggetti_negozio = {}
            for oggetto in risultato:
                trovato = Oggetti.trova_oggetto(ids=oggetto)
                codice = trovato["ID"]
                nome = trovato["NOME"]
                tipo = trovato["TIPO1"]
                if int(trovato["VALORE"]) < 10:
                    modificatore_assoluto = 0
                elif int(trovato["VALORE"]) < 20:
                    modificatore_assoluto = int(livello_negozio / 2)
                elif int(trovato["VALORE"]) < 100:
                    modificatore_assoluto = livello_negozio
                elif int(trovato["VALORE"]) < 500:
                    modificatore_assoluto = livello_negozio * 2
                elif int(trovato["VALORE"]) < 1000:
                    modificatore_assoluto = livello_negozio * 3
                else:
                    modificatore_assoluto = livello_negozio * 5
                valore = str(int(int(int(trovato["VALORE"]) / 100 * (70 + modificatore_prezzo)) + modificatore_assoluto))
                if tipo not in list(oggetti_negozio.keys()):
                    oggetti_negozio[tipo] = [{"codice": codice, "nome": nome, "valore": valore}]
                else:
                    oggetti_negozio[tipo].append({"codice": codice, "nome": nome, "valore": valore})

            layout1.clear_widgets()
            layout1.size_hint_y = 1.3
            layout1.add_widget(Label())
            for tipologia in oggetti_negozio:
                layout1.add_widget(Label(text=str(tipologia).upper(), color=(0, 0, 0, 1),
                                         size_hint=(0.1, 0.05), font_size=25, background_color=(1, 1, 1, 0.5)))
                layout1.add_widget(
                    Image(allow_stretch=True, size_hint=(1, 1), source=f'{Shared.path_art}/iconenegozio/{tipologia}.png',
                          pos_hint={"center_x": 0.5, "center_y": 0.5}))
                text_tipologia = str(tipologia).replace(" ", "_")
                text_tipologia = str(text_tipologia).replace("(", "_")
                text_tipologia = str(text_tipologia).replace(")", "_")
                exec(f"layout{text_tipologia} = GridLayout(size_hint=(1, 0.3),cols=3, spacing=0, height=200)")
                layouttemp = eval(f"layout{text_tipologia}")
                layout1.size_hint_y += 0.07
                for oggetto in oggetti_negozio[tipologia]:
                    layout1.size_hint_y += 0.017
                    testo_oggetto =  f'{oggetto["codice"]} - {oggetto["nome"]} : {oggetto["valore"]}'
                    grandezza_font = 18
                    if len(testo_oggetto) > 55:
                        grandezza_font = 16
                    layouttemp.add_widget(
                        TextInput(text=testo_oggetto,
                                  hint_text_color=(0, 0, 0, 1),
                                  padding=(5, 7, 0, 0), size_hint=(0.1, 0.05), font_size=grandezza_font,
                                  background_color=(1, 1, 1, 0)))
                    layout1.size_hint_y += 0.02
                    layouttemp.size_hint_y += 0.15
                layout1.add_widget(layouttemp)
        except Exception as e:
            print(e)
            campo_negozio.text = "Nessun Risultato"

    def popola_text_da_negozi(*args):
        campo_negozio.text = Temp.negoziocliccato

    box.add_widget(Button(text="Generale", font_size=15, pos_hint={"x": 0, "y": 0.95},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "generale")))
    box.add_widget(Button(text="Contenitori", font_size=15, pos_hint={"x": 0.2, "y": 0.95},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "contenitori")))
    box.add_widget(Button(text="Fabbro", font_size=15, pos_hint={"x": 0.4, "y": 0.95},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "fabbro")))
    box.add_widget(Button(text="Taverna", font_size=15, pos_hint={"x": 0.6, "y": 0.95},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "taverna")))
    box.add_widget(Button(text="Alchimista", font_size=15, pos_hint={"x": 0.8, "y": 0.95},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "alchimista")))
    box.add_widget(Button(text="Oggetti Magici", font_size=15, pos_hint={"x": 0, "y": 0.90},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "oggetti magici")))
    box.add_widget(Button(text="Arcieria", font_size=15, pos_hint={"x": 0.2, "y": 0.90},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "arcieria")))
    box.add_widget(Button(text="Abbigliamento", font_size=15, pos_hint={"x": 0.4, "y": 0.90},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "abbigliamento")))
    box.add_widget(Button(text="Armaiolo", font_size=15, pos_hint={"x": 0.6, "y": 0.90},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "armaiolo")))
    box.add_widget(Button(text="Fabbricante di Armi", font_size=15, pos_hint={"x": 0.8, "y": 0.90},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "fabbricante di armi")))
    box.add_widget(Button(text="Carovana Khajiit", font_size=15, pos_hint={"x": 0, "y": 0.85},
                          size_hint=(0.2, 0.05), on_release=partial(aggiungi_a_negozio, "carovana khajiit")))
    campo_negozio = TextInput(text="Vuoto", font_size=15, pos_hint={"x": 0.2, "y": 0.85},
                              size_hint=(0.2, 0.05),padding=(2,2,2,2))
    box.add_widget(campo_negozio)
    campo_livello = TextInput(text="0", font_size=15, pos_hint={"x": 0.4, "y": 0.85},
                              size_hint=(0.025, 0.05))
    box.add_widget(campo_livello)
    box.add_widget(Button(text="Genera", font_size=15, pos_hint={"x": 0.425, "y": 0.85},
                          size_hint=(0.05, 0.05), on_release=genera))
    box.add_widget(Button(text="Calcol\natrice", font_size=15, pos_hint={"x": 0.475, "y": 0.85},
                          size_hint=(0.05, 0.05), on_release=Popups_Calcolatrice.calcolatrice))
    box.add_widget(TextInput(text="appunti spesa", font_size=12, pos_hint={"x": 0.525, "y": 0.85},
                          size_hint=(0.075, 0.05),padding=(2,2,2,2)))
    box.add_widget(Button(text="Negozi", font_size=15, pos_hint={"x": 0.6, "y": 0.85},
                          size_hint=(0.15, 0.05), on_release=negozi_salva_negozio))
    box.add_widget(Button(text="Imp.\nSelez.", font_size=15, pos_hint={"x": 0.75, "y": 0.85},
                          size_hint=(0.05, 0.05), on_release=popola_text_da_negozi ))
    box.add_widget(Button(text="Tutti gli oggetti", font_size=15, pos_hint={"x": 0.8, "y": 0.85},
                          size_hint=(0.2, 0.05), on_release=Popups_NomePG_Oggetti_Tutti.oggetti_tutti_open))
    popup.open()

