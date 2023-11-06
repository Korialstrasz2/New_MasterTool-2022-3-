from math import floor

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori, Oggetti
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

def popup_check_differenze_pgnpc(dictinput):
    layout = GridLayout(cols=1,rows = 4, spacing=0, size_hint_y=1, height=200)
    popup = Popup(title='Dati ricevuti!', title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(800, 800),
                  auto_dismiss=False)

    def accettafuoo(*args):
        ImportazioneAttori.processa_pg_npc_importato(dictinput)
        FinestraPrincipaleMain.FunzioniFinestra.show_all()
        popup.dismiss()

    def trova_oggetto_e_aggiungi_nome(valore):
        try:
            valore = str(valore)
            if valore.startswith("id:"):
                valore = valore[3:]
            int(valore)
            valore = Oggetti.trova_oggetto(valore)["NOME"]
        except:
            pass
        return valore

    accetta = Button(text="V Accetta", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                     pos_hint={"x": 0, "y": 0}, on_release=accettafuoo)
    rifiuta = Button(text="X Rifiuta", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                     pos_hint={"x": 0.8, "y": 0}, on_release=popup.dismiss)

    nome_excel = dictinput["nome_valore_excel"]
    nome_in_uso = dictinput["nome_in_uso"]

    if nome_excel not in Shared.pgnpc_importati_base:
        Shared.pgnpc_importati_base[nome_excel] = dictinput
    if nome_in_uso not in Shared.pg_png_inizializzati:
        Shared.pg_png_inizializzati[nome_excel] = dictinput


    da_aprire = False

    testo = f"Cambiamenti a : {nome_in_uso}\n"
    layout.add_widget(
        Label(text=testo, color=(1, 1, 1, 1),
              size_hint=(0.1, 0.1), font_size=20, background_color=(1, 1, 1, 0.5)))


    cambiamenti = []
    cambiamentiflag = False
    pgold = Shared.pg_png_inizializzati[nome_excel]
    for valore in Shared.dati_base_pg:
        if valore not in dictinput:
            dictinput[valore] = Shared.campi_nuovi_valore_standard[valore]
        if valore != "mana_in_sifone" and not str(dictinput[valore]) == str(pgold[valore]):
            nuovo = str(dictinput[valore])
            vecchio = str(pgold[valore])
            nuovo_nome = ""
            vecchio_nome = ""

            if valore.startswith("id_") or valore.startswith("equip_") or valore.startswith("zaino_slot"):
                nuovo_nome = f"({trova_oggetto_e_aggiungi_nome(nuovo)})"
                vecchio_nome = f"({trova_oggetto_e_aggiungi_nome(vecchio)})"
            if Shared.mastermode or (nome_in_uso == Shared.pg_selezionato['nome_in_uso']):
                stringa = f"{str(valore)}: {vecchio} {vecchio_nome}->{nuovo} {nuovo_nome}"
            else:
                stringa = f"{str(valore)}: xxx  -> xxx"
            cambiamenti.append(stringa)
            cambiamentiflag = True



    scroller = ScrollView(size_hint=(1, 1), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    layout.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)


    l1_size_h_y = 1.2
    if cambiamentiflag == True:
        da_aprire = True
        for testo in cambiamenti:
            if len(testo)>160:
                testo = testo[:70] + "\n" + testo[70:140] + "\n" + testo[140:]
            elif len(testo)>80:
                testo = testo[:70] + "\n" + testo[70:]
            layout1.add_widget(
                Label(text=testo, color=(1, 1, 1, 1),
                      size_hint=(0.1, 0.5), font_size=20, background_color=(1, 1, 1, 0.5)))
            l1_size_h_y += 0.1
    layout1.size_hint_y = l1_size_h_y


    layout.add_widget(accetta)
    layout.add_widget(rifiuta)
    if da_aprire and not str(nome_in_uso).startswith("__natura__Null"):
        popup.open()

