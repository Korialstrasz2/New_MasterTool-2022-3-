from math import floor

import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain, Popups_Notifiche, Popups_Effetti
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori, GestioneSkill
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
pgselezionato = Shared.pg_selezionato

class Temp:
    numeroclockperimporta = 0
    pe_spesi_tot = 0

def calcola_livello(pe_totatli):
    pe_per_salire = 20
    livello = 1
    pe_tot = int(pe_totatli)
    while True:
        if pe_tot >= pe_per_salire:
            pe_tot -= pe_per_salire
            pe_per_salire += 1
            livello += 1
        else:
            return livello

def costo_skill(costo):
    try:
        costo = costo.split(" ")[0]
        modificatore = 3 + int(costo)
        if modificatore > 9:
            modificatore = 9
        costo_finale = floor(int(costo) + int(costo)/modificatore * (int(Shared.pg_selezionato["livello"])*0.7) /1.5)
        stringa_finale = str(costo_finale) + " pe"
        return stringa_finale
    except AttributeError:
        pass
def gestione_skill(*args):
    layout = FloatLayout()
    popup = Popup(title=f"Gestione Skill", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1400, 700),
                  auto_dismiss=True)

    def cercagruppo(ids):
        gruppotemp = ""
        for skill_da_checkare in Shared.skill_importate:
            skill = Shared.skill_importate[skill_da_checkare]
            if skill["ID"] in ["Nome", "PERK"]:
                gruppotemp = skill["NOME"]
            if str(skill["ID"]) == str(ids):
                return gruppotemp

    def cerca(*args):
        if len(boxid.text) > 0:
            gruppo = cercagruppo(boxid.text)
            oggetto = GestioneSkill.cerca_skill(ids=str(boxid.text))
            boxnome.text = f"""{gruppo}: {str(oggetto["NOME"])}"""
            boxtipo1.text = str(oggetto["DESCRIZIONE"])
            boxtipo2.text = str(oggetto["PE_USABILI"])
            boxnpe.text = str(oggetto["PE"])
            boxdettaglio1.text = str(oggetto["DETTAGLIO1"])
            boxdettaglio2.text = str(oggetto["DETTAGLIO2"])
            boxtipo3.text = str(oggetto["TIPO"])


    layout.add_widget(Label(size_hint=(0.05, 0.05), pos_hint={"x": 0, "y": 0.95}, text="ID"))
    boxid = TextInput(size_hint=(0.05, 0.05), pos_hint={"x": 0, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.25, 0.05), pos_hint={"x": 0.05, "y": 0.95}, text="NOME"))
    boxnome = TextInput(size_hint=(0.25, 0.05), pos_hint={"x": 0.05, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.65, 0.05), pos_hint={"x": 0.3, "y": 0.95}, text="DESCRIZIONE"))
    boxtipo1 = TextInput(size_hint=(0.65, 0.05), pos_hint={"x": 0.3, "y": 0.9})
    layout.add_widget(Label(size_hint=(0.04, 0.05), pos_hint={"x": 0.0, "y": 0.85}, text="COLORE"))
    boxtipo2 = TextInput(size_hint=(0.04, 0.05), pos_hint={"x": 0.0, "y": 0.8})
    layout.add_widget(Label(size_hint=(0.035, 0.05), pos_hint={"x": 0.04, "y": 0.85}, text="N. PE"))
    boxnpe = TextInput(size_hint=(0.035, 0.05), pos_hint={"x": 0.04, "y": 0.8})
    layout.add_widget(Label(size_hint=(0.125, 0.05), pos_hint={"x": 0.075, "y": 0.85}, text="TIPO"))
    boxtipo3 = TextInput(size_hint=(0.125, 0.05), pos_hint={"x": 0.075, "y": 0.8})
    layout.add_widget(Label(size_hint=(0.4, 0.05), pos_hint={"x": 0.2, "y": 0.85}, text="DETTAGLIO1"))
    boxdettaglio1 = TextInput(size_hint=(0.4, 0.05), pos_hint={"x": 0.2, "y": 0.8})
    layout.add_widget(Label(size_hint=(0.4, 0.05), pos_hint={"x": 0.6, "y": 0.85}, text="DETTAGLIO2"))
    boxdettaglio2 = TextInput(size_hint=(0.4, 0.05), pos_hint={"x": 0.6, "y": 0.8})
    layout.add_widget(boxid)
    layout.add_widget(boxnome)
    layout.add_widget(boxtipo1)
    layout.add_widget(boxtipo2)
    layout.add_widget(boxnpe)
    layout.add_widget(boxtipo3)
    layout.add_widget(boxdettaglio1)
    layout.add_widget(boxdettaglio2)
    layout.add_widget(Button(size_hint=(0.05, 0.05), pos_hint={"x": 0.95, "y": 0.9}, text="Cerca", on_release=cerca))


    scroller = ScrollView(size_hint=(1, 0.7), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    layout.add_widget(scroller)
    layout1 = GridLayout(cols=4, spacing=0, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    layout1.add_widget(Label(size_hint=(None, None), size=(50, 30), text="ID"))
    layout1.add_widget(Label(size_hint=(None, None), size=(600, 30), text="Descrizione"))
    layout1.add_widget(Label(size_hint=(None, None), size=(50, 30), text="ID"))
    layout1.add_widget(Label(size_hint=(None, None), size=(600, 30), text="Descrizione"))

    def selezionDaBottone(ids):
        boxid.text = str(ids)
        cerca()

    for singolo in Shared.skill_sbloccate_pg:
        if int(singolo) not in [9999994,9999995,9999996,9999997,9999998,9999999]:
            skill_da_aggungere = GestioneSkill.cerca_skill(ids=str(singolo))
            layout1.size_hint_y += 0.01
            exec(
                f"Temp.bottone_id_skill_{singolo} = Button(text=str(skill_da_aggungere['ID']),size_hint=(None,None), size=(50, 30))")
            exec(f"Temp.bottone_id_skill_{singolo}.on_release = partial(selezionDaBottone, singolo)")
            layout1.add_widget(eval(f"Temp.bottone_id_skill_{singolo}"))
            testo_pre = skill_da_aggungere["DESCRIZIONE"]
            if type(testo_pre) != str:
                testo_pre = "non disponibile"
            testo = testo_pre if len(testo_pre) <75 else f"{testo_pre[0:int(len(testo_pre)/2)]}\n{testo_pre[int(len(testo_pre)/2):int(len(testo_pre))]}"
            layout1.add_widget(Label(text=testo, size_hint=(None, None), size=(600, 30)))

    popup.open()


def skill_excel_open(*args):
    box = FloatLayout()
    popup = Popup(title=f'Skill e Perk', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(1500, 950),
                  auto_dismiss=True)
    notepic = AsyncImage(allow_stretch=True, size_hint=(1, 1), source='Art/NPCbgshort.png',
                    pos_hint={"center_x": 0.5, "center_y": 0.5})

    box.add_widget(notepic)

    scroller = ScrollView(size_hint=(1, 0.8), effect_cls="ScrollEffect", pos_hint={"x": 0, "y": 0})
    box.add_widget(scroller)
    layout1 = GridLayout(cols=2, spacing=0, size_hint_x=1, size_hint_y=1.2, height=200)
    scroller.add_widget(layout1)

    layoutmenu = GridLayout(cols=7, spacing=0, size_hint_x=1, size_hint_y=0.2, pos_hint={"x": 0, "y": 0.8})
    box.add_widget(layoutmenu)

    def openspendi(dizion, *args):
        ids = dizion["ID"]
        nome = dizion["NOME"]
        perk = dizion["PERK"]
        colore = dizion["PE_USABILI"]
        titolo = f"{ids} - {nome}"
        box = GridLayout(padding=(5), cols=2, rows=12)
        popup = Popup(title=titolo, title_size=(20),
                      title_align='center', content=box,
                      size_hint=(None, None), size=(350, 300),
                      auto_dismiss=True)
        if ids in [9999994,9999995,9999996,9999997,9999998]:
            box_pe = TextInput(text="0", input_type='number', font_size=15)
            box.add_widget(Label(text=f"Punti attuali"))
            box.add_widget(Label(text=""))
            box.add_widget(Label(text="rimanenti\ntotali:"))
            box.add_widget(box_pe)

        elif perk == True:
            try:
                testo = Shared.skill_sbloccate_pg[str(dizion["ID"])] if len(Shared.skill_sbloccate_pg[str(dizion["ID"])]) > 0 else "0"
            except:
                testo = "0"
            box_pe = TextInput(text=testo, font_size=15)
            box.add_widget(Label(text=f"Attuale"))
            box.add_widget(Label(text=""))
            box.add_widget(Label(text="Inserisci\nTesto:"))
            box.add_widget(box_pe)

        elif not nome.startswith("PE TOT"):
            box_rossi = TextInput(text="0", input_type='number', font_size=15)
            box_verdi = TextInput(text="0", input_type='number', font_size=15)
            box_blu = TextInput(text="0", input_type='number', font_size=15)
            box_generali = TextInput(text="0", input_type='number', font_size=15)
            costo = costo_skill(dizion["PE"])
            box.add_widget(Label(text=f"costo: {costo} punti {colore}"))
            box.add_widget(Label(text="Inserisci quanti PE spendi"))
            box.add_widget(Label(text="Rossi:"))
            box.add_widget(box_rossi)
            box.add_widget(Label(text="Verdi:"))
            box.add_widget(box_verdi)
            box.add_widget(Label(text="Blu:"))
            box.add_widget(box_blu)
            box.add_widget(Label(text="Generali:"))
            box.add_widget(box_generali)

        def salvaskillcomprata(listaidstext, *args):
            if listaidstext[-1] == False:
                if "RIMUOVI" not in listaidstext:
                    if ids not in [9999994,9999995,9999996,9999997,9999998]:
                        try:
                            spesi_tot = int(box_rossi.text) + int(box_verdi.text) +int(box_blu.text) +int(box_generali.text)
                            for disponibili in [9999994,9999995,9999996,9999997,9999998]:
                                try:
                                    a = int(Shared.skill_sbloccate_pg[str(disponibili)])
                                except:
                                    Shared.skill_sbloccate_pg[str(disponibili)] = 0
                            Shared.skill_sbloccate_pg[str(listaidstext[0])] = spesi_tot
                            Shared.skill_sbloccate_pg["9999994"] -= int(box_rossi.text)
                            Shared.skill_sbloccate_pg["9999995"] -= int(box_verdi.text)
                            Shared.skill_sbloccate_pg["9999996"] -= int(box_blu.text)
                            Shared.skill_sbloccate_pg["9999997"] -= int(box_generali.text)
                            Salvataggio.salva_skill_sbloccate()
                        except:
                            Popups_Notifiche.nosave()
                    else:
                        try:
                            Shared.skill_sbloccate_pg[str(listaidstext[0])] = int(box_pe.text)
                            Salvataggio.salva_skill_sbloccate()
                        except:
                            Popups_Notifiche.nosave()
                else:
                    if str(listaidstext[0]) in Shared.skill_sbloccate_pg:
                        Shared.skill_sbloccate_pg.pop(str(listaidstext[0]))
                        Salvataggio.salva_skill_sbloccate()
            else:
                if "RIMUOVI" not in listaidstext:
                    Shared.skill_sbloccate_pg[str(listaidstext[0])] = box_pe.text
                    Salvataggio.salva_skill_sbloccate()
                else:
                    # normalmente dovrebbe esserci solo il try
                    try:
                        Shared.skill_sbloccate_pg.pop(str(listaidstext[0]))
                    except:
                        Shared.skill_sbloccate_pg[str(listaidstext[0])] = ""
                    Salvataggio.salva_skill_sbloccate()

        rimuovib = Button(text="RIMUOVI", on_press =partial(salvaskillcomprata,[ids,"RIMUOVI", perk]), on_release=popup.dismiss)
        box.add_widget(rimuovib)
        confermab = Button(text="CONFERMA",on_press =partial(salvaskillcomprata,[ids, perk]),  on_release=popup.dismiss)
        box.add_widget(confermab)
        popup.open()

    def updatescroller(gruppo, *args):
        calcolapespesi()
        layout1.clear_widgets()
        y = 0.9
        l1sh = 0.8
        flagperk = False
        for skill in gruppo:
            testo = ""
            spesi = ""
            if str(skill["ID"]) in Shared.skill_sbloccate_pg:
                spesi = Shared.skill_sbloccate_pg[str(skill["ID"])]
            for colonna in skill:
                testocheck = str(skill[colonna])
                if testocheck == "None":
                    testocheck = ""
                if colonna == "PE":
                    try:
                        testocheck = costo_skill(testocheck)
                    except:
                        pass

                if colonna == "NOME":
                    testocheck = testocheck.upper()

                if testocheck != "":
                    testo += testocheck + " || "

                l1sh += 0.0055
            colorestandard = (1, 1, 1, 0.75)
            coloresbloccato = (0.5, 1, 0.5, 0.75)
            larghezzapulsante = 0.03
            skill["PERK"] = flagperk
            if type(skill["NOME"]) == str and skill["NOME"].startswith("PERK M"):
                flagperk = True
            if flagperk:
                larghezzapulsante = 0.08
            if type(skill["NOME"]) == str and skill["NOME"].startswith("PE TOT"):
                spesi = str(Temp.pe_spesi_tot)
                livello_raggiunto = str(calcola_livello(spesi))
                testo += f"|| corrispondente a LV {livello_raggiunto}"
                if livello_raggiunto != str(Shared.pg_selezionato["livello"]):
                    Popups_Notifiche.livello(livello_calcolato=livello_raggiunto, livello_attuale=str(Shared.pg_selezionato["livello"]))
            if len(str(spesi)) > 0:
                colore = coloresbloccato
            else:
                colore = colorestandard
            testo = testo.rstrip(" ")
            testo = testo.rstrip(" ||")
            testo = testo[:-8] if testo.endswith("False") else testo
            if len(testo) > 2 and not testo.startswith("9999999"):
                layout1.add_widget(
                    TextInput(text=testo, pos_hint={"center_x": 0.5, "center_y": y}, hint_text_color=(0, 0, 0, 1),
                              size_hint=(0.92, 0.7), padding=(2, 2, 2, 2), font_size=20, background_color=colore))
                layout1.add_widget(
                    Button(text=str(spesi), pos_hint={"center_x": 0.5, "center_y": y}, color=(0, 0, 0, 1),
                           on_release=partial(openspendi, skill), size_hint=(larghezzapulsante, 0.7),
                           font_size=23, background_color=(1, 1, 1, 0.75)))
            layout1.size_hint_y = l1sh

    def calcolapespesi(*args):
        Temp.pe_spesi_tot = 0
        for skill_da_checkare in Shared.skill_sbloccate_pg:
            if skill_da_checkare != "None" and int(skill_da_checkare) not in [9999994,9999995,9999996,9999997,9999998]:
                try:
                    a = int(Shared.skill_sbloccate_pg[skill_da_checkare])
                    Temp.pe_spesi_tot += a
                except:
                    pass


    calcolapespesi()

    gruppi = []
    gruppo = []
    for skill_da_checkare in Shared.skill_importate:
        skill = Shared.skill_importate[skill_da_checkare]
        if skill["ID"] in ["Nome", "PERK"] and len(gruppo) > 0:
            gruppi.append(gruppo)
            gruppo = []
        gruppo.append(skill)
    gruppi.append(gruppo)
    for cluster_skill in gruppi:
        nome = cluster_skill[0]["NOME"]
        descr = str(cluster_skill[0]["DESCRIZIONE"])
        if descr.startswith("Tutti"):
            colore = (1,1,1,1)
        elif descr.startswith("Verdi"):
            colore = (0, 1, 0, 1)
        elif descr.startswith("Rossi"):
            colore = (1, 0, 0, 1)
        elif descr.startswith("Blu"):
            colore = (0, 0, 1, 1)
        elif descr.startswith("Vari"):
            colore = (0.5, 0.5, 0.5, 1)
        elif descr.startswith("Religione"):
            colore = (0.59, 0.59, 0.8, 1)
        else:
            colore = (0,0,0,1)

        layoutmenu.add_widget(Button(text=nome, background_color = colore, size_hint=(0.1, 0.05),
                                     pos_hint={"x": 0.9, "y": 0.9}, color = (1,1,1,1),
                                     on_release=partial(updatescroller, cluster_skill)))
    layoutmenu.add_widget(Button(text="APRI EFFETTI", size_hint=(0.1, 0.05), pos_hint={"x": 0.9, "y": 0.9},
                                 on_release=Popups_Effetti.gestisci_effetti_open))
    if Shared.bloccaskill == False:
        popup.open()


def popup_skill_esistente(*args, dati_nuova_skill):
    layout = GridLayout(cols=1, spacing=0, size_hint_y=1, height=200)
    popup = Popup(title='ID skill già presente, sovrascrivere?', title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(700, 300),
                  auto_dismiss=False)

    def accettafuoo(*args):
        GestioneSkill.aggiungi_skill_in_posizione(posizione_precedente=str(dati_nuova_skill[0]),
                                                  posizione_nuova=str(dati_nuova_skill[0]),
                                                  dati=dati_nuova_skill)
        GestioneSkill.salva_db_skill()
        popup.dismiss()

    accetta = Button(text="V Accetta", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                     pos_hint={"x": 0, "y": 0}, on_release=accettafuoo)
    rifiuta = Button(text="X Rifiuta", color=(1, 1, 1, 1), font_size=19, italic=True, size_hint=(0.2, 0.1),
                     pos_hint={"x": 0.8, "y": 0}, on_release=popup.dismiss)

    layout.add_widget(accetta)
    layout.add_widget(rifiuta)
    popup.open()

def crea_nuova_skill(*args):
    layout = FloatLayout()
    popup = Popup(title=f"Nuova skill", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(1400, 320),
                  auto_dismiss=True)


    def cercagruppo(ids):
        gruppotemp = ""
        for skill_da_checkare in Shared.skill_importate:
            skill = Shared.skill_importate[skill_da_checkare]
            if skill["ID"] in ["Nome", "PERK"]:
                gruppotemp = skill["NOME"]
            if str(skill["ID"]) == str(ids):
                return gruppotemp

    def cerca(*args):
        if len(boxid.text) > 0:
            gruppo = cercagruppo(boxid.text)
            oggetto = GestioneSkill.cerca_skill(ids=str(boxid.text))
            boxnome.text = f"""{gruppo}: {str(oggetto["NOME"])}"""
            boxtipo1.text = str(oggetto["DESCRIZIONE"])
            boxtipo3.text = str(oggetto["PE_USABILI"])
            boxtipo2.text = str(oggetto["PE"])
            boxdett1.text = str(oggetto["DETTAGLIO1"])
            boxdett2.text = str(oggetto["DETTAGLIO2"])
            boxtipo.text = str(oggetto["TIPO"])
        else:
            boxid.text = "0"
            cerca()

    def crea(*args):
        stringa = []
        stringa.append(boxid.text)
        stringa.append(boxnome.text)
        stringa.append(boxtipo1.text)
        stringa.append(boxtipo2.text)
        stringa.append(boxtipo3.text)
        stringa.append(boxdett1.text)
        stringa.append(boxdett2.text)
        stringa.append(boxtipo.text)
        stringa.append(boxextra.text)
        if str(GestioneSkill.cerca_skill(boxid.text)["ID"]) == "9999999":
            try:
                if GestioneSkill.aggiungi_skill_in_posizione(posizione_precedente=str(int(stringa[0])-1),
                                                          posizione_nuova=str(stringa[0]),
                                                          dati=stringa) != "Invalido":
                    GestioneSkill.salva_db_skill()

                else:
                    Popups_Notifiche.nosave()
            except:
                Popups_Notifiche.nosave()
        else:
            popup_skill_esistente(dati_nuova_skill=stringa)

    layout.add_widget(Label(size_hint=(0.05, 0.05), pos_hint={"x": 0, "y": 0.95}, text="Numero ID"))
    boxid = TextInput(size_hint=(0.05, 0.15), pos_hint={"x": 0, "y": 0.7})
    layout.add_widget(Label(size_hint=(0.2, 0.05), pos_hint={"x": 0.05, "y": 0.95}, text="Nome"))
    boxnome = TextInput(size_hint=(0.2, 0.15), pos_hint={"x": 0.05, "y": 0.7})
    layout.add_widget(Label(size_hint=(0.4, 0.05), pos_hint={"x": 0.25, "y": 0.90}, text="Descriz. Effetto"))
    boxtipo1 = TextInput(size_hint=(0.4, 0.15), pos_hint={"x": 0.25, "y": 0.7})
    layout.add_widget(
        Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.65, "y": 0.95}, text="n. PE necessari\n(ad es '5 pe')"))
    layout.add_widget(Label(size_hint=(0.1, 0.05), pos_hint={"x": 0.75, "y": 0.95}, text="Tipo PE necessari"))
    boxtipo2 = TextInput(size_hint=(0.1, 0.15), pos_hint={"x": 0.65, "y": 0.7})
    boxtipo3 = TextInput(size_hint=(0.1, 0.15), pos_hint={"x": 0.75, "y": 0.7})

    layout.add_widget(
        Label(size_hint=(0.25, 0.05), pos_hint={"x": 0.0, "y": 0.5}, text="(non necessario) Dettaglio 1"))
    layout.add_widget(Label(size_hint=(0.25, 0.05), pos_hint={"x": 0.25, "y": 0.5}, text="(non necessario) Dettaglio 2"))
    boxdett1 = TextInput(size_hint=(0.25, 0.15), pos_hint={"x": 0.0, "y": 0.2})
    boxdett2 = TextInput(size_hint=(0.25, 0.15), pos_hint={"x": 0.25, "y": 0.2})
    layout.add_widget(
        Label(size_hint=(0.25, 0.05), pos_hint={"x": 0.5, "y": 0.5}, text="(non necessario) Tipo"))
    layout.add_widget(Label(size_hint=(0.25, 0.05), pos_hint={"x": 0.75, "y": 0.5}, text="(non necessario) Extra"))
    boxtipo = TextInput(size_hint=(0.25, 0.15), pos_hint={"x": 0.5, "y": 0.2})
    boxextra = TextInput(size_hint=(0.25, 0.15), pos_hint={"x": 0.75, "y": 0.2})

    layout.add_widget(boxid)
    layout.add_widget(boxnome)
    layout.add_widget(boxtipo1)
    layout.add_widget(boxtipo2)
    layout.add_widget(boxtipo3)
    layout.add_widget(boxdett1)
    layout.add_widget(boxdett2)
    layout.add_widget(boxtipo)
    layout.add_widget(boxextra)
    layout.add_widget(
        Button(size_hint=(0.15, 0.2), pos_hint={"x": 0.85, "y": 0.75}, text="Cerca", on_release=cerca))
    layout.add_widget(
        Button(size_hint=(0.15, 0.2), pos_hint={"x": 0.85, "y": 0.55}, text="Crea", on_release=crea))

    popup.open()
