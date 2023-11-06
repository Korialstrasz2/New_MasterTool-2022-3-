from math import floor
import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, FinestraPrincipalePG
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori, GestioneSkill
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class NPC():
    pass

prefissi_per_pgnpc = ["__pg__", "__uman", "__nonm", "__natu", "__daed"]

def PG_NPC_open():
    layout = FloatLayout()
    popup = Popup(title='Pg e NPC - Seleziona', title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1500, 800),
                  auto_dismiss=True)

    def seleziona_npc(numeronpc, *args):
        try:
            FinestraPrincipaleMain.FunzioniFinestra.conferma()
        except:
            pass
        ImportazioneAttori.seleziona_attuale(eval(f"NPC.bottone_npc_{str(numeronpc)}.text"))
        if (Shared.pg_selezionato["nome_in_uso"][-4:-2] != "_n") and\
                 (Shared.pg_selezionato["nome_in_uso"].startswith("__pg__")):
            Shared.bloccaskill = False
            GestioneSkill.importa_skill_pg(Shared.pg_selezionato["nome_in_uso"])
        else:
            Shared.bloccaskill = True
        EquipAttore.equip_npc(Shared.pg_selezionato["nome_in_uso"])
        FinestraPrincipalePG.shownote()
        FinestraPrincipaleMain.FunzioniFinestra.conferma()

    NPC.bottone_npc_1 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0, "y": 0.9}, on_release=partial(seleziona_npc, 1))
    NPC.bottone_npc_2 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.2, "y": 0.9}, on_release=partial(seleziona_npc, 2))
    NPC.bottone_npc_3 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.4, "y": 0.9}, on_release=partial(seleziona_npc, 3))
    NPC.bottone_npc_4 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.6, "y": 0.9}, on_release=partial(seleziona_npc, 4))
    NPC.bottone_npc_5 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.8, "y": 0.9}, on_release=partial(seleziona_npc, 5))
    NPC.bottone_npc_6 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0, "y": 0.8}, on_release=partial(seleziona_npc, 6))
    NPC.bottone_npc_7 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.2, "y": 0.8}, on_release=partial(seleziona_npc, 7))
    NPC.bottone_npc_8 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.4, "y": 0.8}, on_release=partial(seleziona_npc, 8))
    NPC.bottone_npc_9 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.6, "y": 0.8}, on_release=partial(seleziona_npc, 9))
    NPC.bottone_npc_10 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.8, "y": 0.8}, on_release=partial(seleziona_npc, 10))
    NPC.bottone_npc_11 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0, "y": 0.7}, on_release=partial(seleziona_npc, 11))
    NPC.bottone_npc_12 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.2, "y": 0.7}, on_release=partial(seleziona_npc, 12))
    NPC.bottone_npc_13 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.4, "y": 0.7}, on_release=partial(seleziona_npc, 13))
    NPC.bottone_npc_14 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.6, "y": 0.7}, on_release=partial(seleziona_npc, 14))
    NPC.bottone_npc_15 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.8, "y": 0.7}, on_release=partial(seleziona_npc, 15))
    NPC.bottone_npc_16 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0, "y": 0.6}, on_release=partial(seleziona_npc, 16))
    NPC.bottone_npc_17 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.2, "y": 0.6}, on_release=partial(seleziona_npc, 17))
    NPC.bottone_npc_18 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.4, "y": 0.6}, on_release=partial(seleziona_npc, 18))
    NPC.bottone_npc_19 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.6, "y": 0.6}, on_release=partial(seleziona_npc, 19))
    NPC.bottone_npc_20 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.8, "y": 0.6}, on_release=partial(seleziona_npc, 20))
    NPC.bottone_npc_21 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0, "y": 0.5}, on_release=partial(seleziona_npc, 21))
    NPC.bottone_npc_22 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.2, "y": 0.5}, on_release=partial(seleziona_npc, 22))
    NPC.bottone_npc_23 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.4, "y": 0.5}, on_release=partial(seleziona_npc, 23))
    NPC.bottone_npc_24 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.6, "y": 0.5}, on_release=partial(seleziona_npc, 24))
    NPC.bottone_npc_25 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.8, "y": 0.5}, on_release=partial(seleziona_npc, 25))
    NPC.bottone_npc_26 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0, "y": 0.4}, on_release=partial(seleziona_npc, 26))
    NPC.bottone_npc_27 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.2, "y": 0.4}, on_release=partial(seleziona_npc, 27))
    NPC.bottone_npc_28 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.4, "y": 0.4}, on_release=partial(seleziona_npc, 28))
    NPC.bottone_npc_29 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.6, "y": 0.4}, on_release=partial(seleziona_npc, 29))
    NPC.bottone_npc_30 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.8, "y": 0.4}, on_release=partial(seleziona_npc, 30))
    NPC.bottone_npc_31 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0, "y": 0.3}, on_release=partial(seleziona_npc, 31))
    NPC.bottone_npc_32 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.2, "y": 0.3}, on_release=partial(seleziona_npc, 32))
    NPC.bottone_npc_33 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.4, "y": 0.3}, on_release=partial(seleziona_npc, 33))
    NPC.bottone_npc_34 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.6, "y": 0.3}, on_release=partial(seleziona_npc, 34))
    NPC.bottone_npc_35 = Button(text="", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                                pos_hint={"x": 0.8, "y": 0.3}, on_release=partial(seleziona_npc, 35))

    indice_per_bottoni = 1

    for NPC_box in Shared.pg_png_inizializzati:
        if not NPC_box.startswith("__natura__Null"):
            if Shared.mastermode:
                exec(f"NPC.bottone_npc_{indice_per_bottoni}.text = NPC_box")
                exec(f"layout.add_widget(NPC.bottone_npc_{indice_per_bottoni})")
                indice_per_bottoni += 1
            else:
                if NPC_box.startswith("__pg") and NPC_box in Shared.pg_png_creati_dal_pc:
                    exec(f"NPC.bottone_npc_{indice_per_bottoni}.text = NPC_box")
                    exec(f"layout.add_widget(NPC.bottone_npc_{indice_per_bottoni})")
                    indice_per_bottoni += 1

    popup.open()
