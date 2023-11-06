import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, Popups_NomePG_Interno, Popups_NomePG_Skill, Popups_MasterMode, \
    Popups_Notifiche, Popups_NomePG_Oggetti_Tutti, Popups_Genera_Nomi, Popups_Idee_Quest, Popups_Bottoni_Custom
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori
from Moduli.Utils import CartellaShared
from kivy.lang import Builder
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def reminder_bonus_razza():
    popup = Popup(title=f"Sei a livello {Shared.pg_selezionato['livello']}, ricorda di aggiornare i bonus",
                  title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()

def nomepgopen():
    Builder.load_string("""
<Label>:
    color: 1,1,1,1
<TextInput>:
    background_color: 1,1,1,0.7""")
    layout = FloatLayout()
    pgselezionato = Shared.pg_selezionato
    razza2 = '' if pgselezionato['razza2'] == 'None' else pgselezionato['razza2']
    razza3 = '' if pgselezionato['razza3'] == 'None' else pgselezionato['razza3']
    titolo = f"{pgselezionato['nomepg']} - Livello: {pgselezionato['livello']} - Fortuna: {pgselezionato['fortuna_tot']} - Razza: {pgselezionato['razza1']} {razza2} {razza3}"
    popup = Popup(title=titolo, title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1500, 800),
                  auto_dismiss=True)


    def importadaexcel(*args):
        Shared.counter_click_importa_skill += 1
        if Shared.counter_click_importa_skill == 5:
            nuova_stringa_skill = ""
            Shared.counter_click_importa_skill = 0
            for skill_da_checkare in Shared.skill_sbloccate_pg:
                if str(skill_da_checkare) not in ["9999994","9999995","9999996","9999997","9999998"]:
                    nuova_stringa_skill += str(skill_da_checkare) + "$$"
            nuova_stringa_skill = nuova_stringa_skill.strip("$$")
            Shared.finestra.skill_sbloccatekv.text = nuova_stringa_skill
            FinestraPrincipaleMain.FunzioniFinestra.conferma()

    def aggiungi_valore(tipo, *args):
        if tipo != "livello":
            exec(f"Shared.pg_selezionato['{tipo}_base'] = str(int(Shared.pg_selezionato['{tipo}_base'])+1)")
        else:
            Shared.pg_selezionato["livello"] = str(int(Shared.pg_selezionato['livello']) + 1)
            if int(Shared.pg_selezionato["livello"]) % 5 == 0:
                reminder_bonus_razza()

        FinestraPrincipaleMain.FunzioniFinestra.conferma()
        FinestraPrincipaleMain.FunzioniFinestra.show_all()

    def abbassa_valore(tipo, *args):
        if tipo != "livello":
            exec(f"Shared.pg_selezionato['{tipo}_base'] = str(int(Shared.pg_selezionato['{tipo}_base'])-1)")
        else:
            Shared.pg_selezionato["livello"] = str(int(Shared.pg_selezionato['livello']) - 1)
        FinestraPrincipaleMain.FunzioniFinestra.conferma()
        FinestraPrincipaleMain.FunzioniFinestra.show_all()

    bottoneformule = Button(text="Formule",
                            color=(1, 1, 1, 1),
                            font_size=30,
                            italic=True,
                            size_hint=(0.2, 0.1),
                            pos_hint={"x": 0, "y": 0.9},
                            on_release=Popups_NomePG_Interno.formuleopen)
    layout.add_widget(bottoneformule)
    bottonecritici = Button(text="Razza",
                            color=(1, 1, 1, 1),
                            font_size=30,
                            italic=True,
                            size_hint=(0.2, 0.1),
                            pos_hint={"x": 0, "y": 0.8},
                            on_release=Popups_NomePG_Interno.razzeopen)
    layout.add_widget(bottonecritici)
    bottonecritici = Button(text="Critici",
                            color=(1, 1, 1, 1),
                            font_size=30,
                            italic=True,
                            size_hint=(0.2, 0.1),
                            pos_hint={"x": 0, "y": 0.7},
                            on_release=Popups_NomePG_Interno.criticiopen)
    layout.add_widget(bottonecritici)

    bottone_agg_lv = Button(text="+ Livello", color=(1, 1, 1, 1), font_size=30, italic=True, size_hint=(0.1, 0.1),
                               pos_hint={"x": 0.1, "y": 0.1}, on_release=partial(aggiungi_valore, "livello"))
    layout.add_widget(bottone_agg_lv)
    bottone_abb_lv = Button(text="- Livello", color=(1, 1, 1, 1), font_size=30, italic=True, size_hint=(0.1, 0.1),
                               pos_hint={"x": 0, "y": 0.1}, on_release=partial(abbassa_valore, "livello"))
    layout.add_widget(bottone_abb_lv)
    from Moduli.Grafica import Popups_Test
    bottone_mappa_test = Button(text="Mappa\nGlobale",
                                   color=(1, 1, 1, 1),
                                   font_size=30,
                                   italic=True,
                                   size_hint=(0.1, 0.1),
                                   pos_hint={"x": 0.4, "y": 0.9},
                                   on_release=Popups_Test.openmappa)
    layout.add_widget(bottone_mappa_test)
    bottone_mappa_test = Button(text="Viaggio\nGlobale",
                                   color=(1, 1, 1, 1),
                                   font_size=30,
                                   italic=True,
                                   size_hint=(0.1, 0.1),
                                   pos_hint={"x": 0.5, "y": 0.9},
                                   on_release=partial(Popups_Test.openmappa, hex=True))
    layout.add_widget(bottone_mappa_test)
    bottone_tutti_oggetti = Button(text="Tutti Gli Oggetti",
                                   color=(1, 1, 1, 1),
                                   font_size=30,
                                   italic=True,
                                   size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.4, "y": 0.8},
                                   on_release=Popups_NomePG_Oggetti_Tutti.oggetti_tutti_open)
    layout.add_widget(bottone_tutti_oggetti)
    bottone_crea_oggetti = Button(text="Crea Oggetti",
                                   color=(1, 1, 1, 1),
                                   font_size=30,
                                   italic=True,
                                   size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.4, "y": 0.7},
                                   on_release=Popups_NomePG_Oggetti_Tutti.crea_nuovo_oggetto)
    layout.add_widget(bottone_crea_oggetti)
    bottoneesporta_ogetti = Button(text="Esporta \nDB Oggetti",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.9},
                                         on_release=Salvataggio.flag_esporta_db_oggetti)
    layout.add_widget(bottoneesporta_ogetti)
    bottoneimporta_ogetti= Button(text="Importa \nDB Oggetti",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.8},
                                         on_release=Salvataggio.flag_importa_db_oggetti)
    layout.add_widget(bottoneimporta_ogetti)
    bottonegestisci_skill = Button(text="Skill",
                                   color=(1, 1, 1, 1),
                                   font_size=30,
                                   italic=True,
                                   size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.6, "y": 0.9},
                                   on_release=Popups_NomePG_Skill.gestione_skill)
    layout.add_widget(bottonegestisci_skill)
    bottonesblocca_skill = Button(text="Sblocca Skill",
                                  color=(1, 1, 1, 1),
                                  font_size=30,
                                  italic=True,
                                  size_hint=(0.2, 0.1),
                                  pos_hint={"x": 0.6, "y": 0.8},
                                  on_release=Popups_NomePG_Skill.skill_excel_open)
    layout.add_widget(bottonesblocca_skill)
    bottonecopia_skill = Button(text="         Copia Skill in \n sbloccate (clicca 5 volte)",
                                  color=(1, 1, 1, 1),
                                  font_size=25,
                                  italic=True,
                                  size_hint=(0.2, 0.1),
                                  pos_hint={"x": 0.6, "y": 0.7},
                                  on_release=importadaexcel)
    layout.add_widget(bottonecopia_skill)
    bottonecarica_pg = Button(text="Carica PG da file",
                                  color=(1, 1, 1, 1),
                                  font_size=30,
                                  italic=True,
                                  size_hint=(0.2, 0.1),
                                  pos_hint={"x": 0.6, "y": 0.6},
                                  on_release=Salvataggio.aggiungi_pg_da_json)
    layout.add_widget(bottonecarica_pg)
    bottonecartella_shared = Button(text="Seleziona catella condivisa",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.2},
                                         on_release=CartellaShared.seleziona_cartella_shared)
    layout.add_widget(bottonecartella_shared)
    bottoneesporta_npc = Button(text="Esporta NPC",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.7},
                                         on_release=Salvataggio.flag_esporta_npc)
    layout.add_widget(bottoneesporta_npc)
    bottoneimporta_npc = Button(text="Importa NPC",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.6},
                                         on_release=Salvataggio.importa_tutti_npc)
    layout.add_widget(bottoneimporta_npc)
    bottonecrea_skill = Button(text="Crea nuova skill",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.6, "y": 0.1},
                                         on_release=Popups_NomePG_Skill.crea_nuova_skill)
    layout.add_widget(bottonecrea_skill)
    bottoneesporta_skill = Button(text="Esporta \nDB Skill",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.5},
                                         on_release=Salvataggio.flag_esporta_db_skill)
    layout.add_widget(bottoneesporta_skill)
    bottoneimporta_skill= Button(text="Importa \nDB Skill",
                                         color=(1, 1, 1, 1),
                                         font_size=25,
                                         italic=True,
                                         size_hint=(0.2, 0.1),
                                         pos_hint={"x": 0.2, "y": 0.4},
                                         on_release=Salvataggio.flag_importa_db_skill)
    bottone_gestisci_bottoni = Button(text="Gestisci Bottoni",
                                   color=(1, 1, 1, 1),
                                   font_size=30,
                                   italic=True,
                                   size_hint=(0.2, 0.1),
                                   pos_hint={"x": 0.4, "y": 0.1},
                                   on_release=Popups_Bottoni_Custom.apri)
    layout.add_widget(bottone_gestisci_bottoni)
    layout.add_widget(bottoneimporta_skill)
    bottonecrea_excel = Button(text=f"Crea Excel",
                               color=(1, 1, 1, 1),
                               font_size=21,
                               italic=True,
                               size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.0, "y": 0.0},
                               on_release=Salvataggio.crea_excel_sunto_pg)
    layout.add_widget(bottonecrea_excel)
    bottoneconsigli_quest = Button(text=f"Idee Quest",
                               color=(1, 1, 1, 1),
                               font_size=21,
                               italic=True,
                               size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.2, "y": 0.0},
                               on_release=Popups_Idee_Quest.idee_quest_open)
    if Shared.mastermode:
        layout.add_widget(bottoneconsigli_quest)
    bottonegenera_nomi = Button(text=f"Genera Nomi",
                               color=(1, 1, 1, 1),
                               font_size=21,
                               italic=True,
                               size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.4, "y": 0.0},
                               on_release=Popups_Genera_Nomi.apri)
    layout.add_widget(bottonegenera_nomi)
    bottonemastermode = Button(text=f"Master Mode: {Shared.mastermode}",
                               color=(1, 1, 1, 1),
                               font_size=21,
                               italic=True,
                               size_hint=(0.2, 0.1),
                               pos_hint={"x": 0.6, "y": 0.0},
                               on_release=mastermode_switch)
    layout.add_widget(bottonemastermode)


    def importa_npc(nome, *args):
        if Shared.counter_click_pg_importato == 0 and nome in Shared.pg_png_inizializzati:
            Popups_Notifiche.pg_gia_importato(nome)
            Shared.counter_click_pg_importato = 1
        else:
            nomenpc = ImportazioneAttori.crea_attore_attivo(nome)
            EquipAttore.equip_npc(nomenpc)
            Shared.counter_click_pg_importato = 0

    scroller = ScrollView(size_hint=(0.2, 0.8), effect_cls="ScrollEffect", pos_hint={"x": 0.8, "y": 0.2})
    layout.add_widget(scroller)
    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=1.2, height=200)
    y_layout_1 = 0.2
    for NPC_box in Shared.pgnpc_importati_base:
        if NPC_box.startswith("__pg"):
            testo = NPC_box[6:]
            layout1.add_widget(
                Button(text=testo, color=(1, 1, 1, 1), font_size=20, background_color=(1, 1, 1, 1),
                       on_release=partial(importa_npc, NPC_box)))
            y_layout_1 += 0.1
    layout1.size_hint_y = y_layout_1
    scroller.add_widget(layout1)
    popup.open()

def mastermode_switch(*args):
    if Shared.clicked_mastermode < 4:
        Shared.clicked_mastermode+=1
    else:
        Shared.clicked_mastermode = 0
        if Shared.mastermode:
            Shared.mastermode = False
        else:
            Popups_MasterMode.master_mode_check()