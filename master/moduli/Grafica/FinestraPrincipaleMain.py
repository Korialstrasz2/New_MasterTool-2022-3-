import ast
import os
from datetime import datetime
from random import randrange

import Moduli.Logica.Oggetti  # NECESSARIO!
from Moduli.Grafica import FinestraPrincipalePG, FinestraPrincipaleCombat, FinestraPrincipaleNPC, \
    FinestraPrincipaleMappa_Immagini, Griglia, Popups_Effetti, Popups_NomePG, Popups_Notifiche, Popups_MasterMode, \
    Popups_Mappe, Popups_FinestraPrincipale, Popups_Zaino, Popups_FinestraPrincipaleImportaPG, Popups_Negozio, \
    Popups_Viaggio, Popups_SkillOpen, Popups_NPCGenerale, Popups_Bottoni_Custom
from Moduli.Logica import EquipAttore, Salvataggio, MeccanicaDanno, GestioneSkill, ImportazioneAttori
from kivy.uix.screenmanager import Screen
import Moduli.SharedData as Shared
from Moduli.Utils.CartellaShared import seleziona_cartella_shared


class FinestraPrincipale(Screen):
    # fai in modo che i dati dei nemici vengano presi da un file excel che viene inizializzato e salvato ogni volta,
    # in modo che tutti i programmi prendano dal file e possano combattere lo stesso nemico
    scalaimgmain = "1.0"
    nomeclass = ""

    def gestisci_effetti_open(self):
        Popups_Effetti.gestisci_effetti_open()

    def show_all(self):
        FunzioniFinestra.show_all()

    def on_enter(self, *args):
        Shared.finestra = self
        FinestraPrincipalePG.barrapa()
        # vecchia funzione loadingscreeen
        self.loadscreen.size_hint = 0, 0
        self.loadscreen.pos_hint = {"x": 2, "top": 2}
        self.loadscreen.source = f"{Shared.path_art}/bg.jpg"
        seleziona_cartella_shared()
        GestioneSkill.importa_skill_pg(Shared.pg_selezionato["nome_in_uso"])
        self.selezionacombattente(0)
        self.selezionacombattente(1)
        self.show_all()
        Shared.entrato_in_finestra_pricipale = True
        FinestraPrincipalePG.immagine_piccola()
        pathrisorse = f"{Shared.path_art}/bgeritrattipg"
        nome = Shared.pg_selezionato["nomepg"]

        for file in os.listdir(pathrisorse):
            if file.startswith(f"bg{nome}"):
                Shared.finestra.ids.immaginebg.source = f'Art/bgeritrattipg/bg{nome}.png'
                Shared.finestra.ids.immaginebgcut.source = f'Art/bgeritrattipg/bg{nome}cut.png'
                break

        ImportazioneAttori.check_file_pg_e_npc_per_update()

    def salva_tutto(self):
        self.show_all()

    def barrapab(self):
        FinestraPrincipalePG.barrapa()

    def pareset(self):
        FinestraPrincipalePG.pareset()

    def nomepgopen(self):
        self.show_all()
        Popups_NomePG.nomepgopen()

    def PG_NPC_open(self):
        Popups_FinestraPrincipaleImportaPG.PG_NPC_open()

    def printer1(self):
        Popups_Zaino.zainoopen()

    def salvanote(self):
        FinestraPrincipalePG.salvanote()

    def conferma(self):
        FunzioniFinestra.conferma()

    def selezionanpc(self, numero):
        exec(f"FinestraPrincipaleNPC.selezionanpc({numero})")

    def NPCopen(self, numeronpc):
        exec(f"Popups_NPCGenerale.NPCopen({numeronpc})")

    def selezionamagia(self, numero):
        exec(f"FinestraPrincipalePG.selezionamagia({numero})")

    def slidemanaspell1(self, *args):
        FinestraPrincipalePG.slidemanaspell1(*args)

    def slidemanaspell2(self, *args):
        FinestraPrincipalePG.slidemanaspell2(*args)

    def slidepoterespell1(self, *args):
        FinestraPrincipalePG.slidepoterespell1(*args)

    def slidepoterespell2(self, *args):
        FinestraPrincipalePG.slidepoterespell2(*args)

    def tirameteo(self, *args):
        FunzioniFinestra.tirameteo(*args)

    def tempoavanza(self, *args):
        FunzioniFinestra.tempoavanza(*args)

    def aggiunginotecondivise(self, *args):
        FunzioniFinestra.aggiunginotecondivise(*args)

    def selezionacombattente(self, numero):
        FinestraPrincipaleCombat.selezionacombattente(numero)
        if Shared.entrato_in_finestra_pricipale == True:
            FinestraPrincipaleCombat.invertiattaccante()
            FinestraPrincipaleCombat.invertiattaccante()

    def invertiattaccante(self):
        FinestraPrincipaleCombat.invertiattaccante()

    def colazione(self):
        FinestraPrincipalePG.colazione()

    def pranzo(self):
        FinestraPrincipalePG.pranzo()

    def cena(self):
        FinestraPrincipalePG.cena()

    def skill(self):
        Popups_SkillOpen.skillopen()

    def attaccanemico(self):
        MeccanicaDanno.attaccanemico()

    def tiradadiattacco(self):
        MeccanicaDanno.tiradadiattacco()

    def selezionacarattattacco(self, numero):
        MeccanicaDanno.selezionacarattattacco(numero)

    def dannofisico(self):
        MeccanicaDanno.dannofisico()

    def dannoelementale(self, tipo):
        MeccanicaDanno.dannoelementale(tipo)

    def dannopuro(self):
        MeccanicaDanno.dannopuro()

    def sifonereset(self):
        FinestraPrincipalePG.sifonereset()

    def pffull(self):
        FinestraPrincipalePG.pffull()

    def manafull(self):
        FinestraPrincipalePG.manafull()

    def enfull(self):
        FinestraPrincipalePG.enfull()

    def powfull(self):
        FinestraPrincipalePG.powfull()

    def stanchezzapiu(self):
        FinestraPrincipalePG.stanchezzapiu()

    def stanchezzameno(self):
        FinestraPrincipalePG.stanchezzameno()

    def modgenpiu(self):
        FinestraPrincipalePG.modgenpiu()

    def modgenmeno(self):
        FinestraPrincipalePG.modgenmeno()

    def malattie_status_open(self):
        Popups_FinestraPrincipale.malattie_status_open()

    def negozio_open(self):
        Popups_Negozio.negozio_open()

    def razze_info_open(self):
        Popups_FinestraPrincipale.razze_info_open()

    def spinner_info_clicked(self, selezione):
        if selezione == "Master\nResource":
            os.startfile(Shared.path_dati + "\Master resource.ods")
        elif selezione == "Città":
            Popups_FinestraPrincipale.citta_info_open()
        elif selezione == "DB Oggetti":
            os.startfile(Shared.path_dati + "\oggetti.xlsx")

        Shared.finestra.ids.spinner_info.text = ""

    def meteo_info_open(self):
        Popups_FinestraPrincipale.meteo_info_open()

    def viaggioopen(self):
        Popups_Viaggio.viaggioopen()

    def notecondivise(self):
        Popups_FinestraPrincipale.notecondivise()

    def aprimapperegione(self):
        Popups_Mappe.aprimapperegione()

    def aprimappelocale(self):
        Popups_Mappe.aprimappelocale()

    def aprimappecitta(self):
        Popups_Mappe.aprimappecitta()

    def apriimgnpc(self):
        Popups_Mappe.apriimgnpc()

    def aprimapperistrette(self):
        if Shared.mastermode:
            Popups_Mappe.aprimapperistrette()
        else:
            Popups_MasterMode.master_mode_check()

    def resetimgmain(self):
        FinestraPrincipaleMappa_Immagini.resetimgmain()

    def mostradettagliimgmain(self):
        FinestraPrincipaleMappa_Immagini.mostradettagliimgmain()

    def imgscalapiupiu(self):
        FinestraPrincipaleMappa_Immagini.imgscalapiupiu()

    def imgscalapiu(self):
        FinestraPrincipaleMappa_Immagini.imgscalapiu()

    def imgscalamenomeno(self):
        FinestraPrincipaleMappa_Immagini.imgscalamenomeno()

    def imgscalameno(self):
        FinestraPrincipaleMappa_Immagini.imgscalameno()

    def imgsu(self):
        FinestraPrincipaleMappa_Immagini.imgsu()

    def imggiu(self):
        FinestraPrincipaleMappa_Immagini.imggiu()

    def imgsinistra(self):
        FinestraPrincipaleMappa_Immagini.imgsinistra()

    def imgdestra(self):
        FinestraPrincipaleMappa_Immagini.imgdestra()

    def noimmaginemain(self):
        FinestraPrincipaleMappa_Immagini.noimmaginemain()

    def grigliasino(self):
        Griglia.grigliasino()

    def giragriglia(self):
        Griglia.giragriglia()

    def ombra(self):
        FinestraPrincipaleMappa_Immagini.ombra()

    def bottonehex(self):
        Griglia.bottonehex()

    def grigliaxs(self):
        Griglia.grigliaxs()

    def griglias(self):
        Griglia.griglias()

    def grigliam(self):
        Griglia.grigliam()

    def griglial(self):
        Griglia.griglial()

    def grigliaxl(self):
        Griglia.grigliaxl()

    def bottone_custom(self,numero):
        FunzioniFinestra.bottone_custom(self,numero)

class FunzioniFinestra():
    def bottone_custom(unused, numero):
        dati_locali = Shared.dati_bottoni[f"bottone_{numero}"]
        if len(dati_locali["nome_effetto"]) > 1:
            for effetto in range(1,32):
                if str(Shared.pg_selezionato[f'nome_effetto_{effetto}']) == "Vuoto"\
                        and str(Shared.pg_selezionato[f'codice_effetto_{effetto}']) == "Vuoto":
                    Shared.pg_selezionato[f'nome_effetto_{effetto}'] = dati_locali["nome_effetto"]
                    Shared.pg_selezionato[f'descrizione_effetto_{effetto}'] = dati_locali["descrizione_effetto"]
                    Shared.pg_selezionato[f'codice_effetto_{effetto}'] = dati_locali["codice_effetto"]
                    print(effetto)
                    break
        FunzioniFinestra.conferma()
        try:
            Shared.finestra.ids.boxdannokv.text = dati_locali["campo_PF"] if len(dati_locali["campo_PF"]) > 0 else Shared.finestra.ids.boxdannokv.text
            Shared.finestra.ids.boxmanaspesokv.text = dati_locali["campo_Mana"] if len(dati_locali["campo_Mana"]) > 0 else Shared.finestra.ids.boxmanaspesokv.text
            Shared.finestra.ids.boxenergiaspesakv.text = dati_locali["campo_Energia"] if len(dati_locali["campo_Energia"]) > 0 else Shared.finestra.ids.boxenergiaspesakv.text
            Shared.finestra.ids.boxpoterespesokv.text = dati_locali["campo_Potere"] if len(dati_locali["campo_Potere"]) > 0 else Shared.finestra.ids.boxpoterespesokv.text
            Shared.finestra.ids.pa_usa_6.text = dati_locali["campo_Punti_Azione"] if len(dati_locali["campo_Punti_Azione"]) > 0 else Shared.finestra.ids.pa_usa_6.text
            FinestraPrincipalePG.barrapa()
            Shared.finestra.ids.boxmodattacco.text = dati_locali["campo_Bonus_Atk"] if len(dati_locali["campo_Bonus_Atk"]) > 0 else Shared.finestra.ids.boxmodattacco.text
            Shared.finestra.ids.boxbonustier.text = dati_locali["campo_Bonus_Tier"] if len(dati_locali["campo_Bonus_Tier"]) > 0 else Shared.finestra.ids.boxbonustier.text
            Shared.finestra.ids.bonusdanno.text = dati_locali["campo_Bonus_DMG"] if len(dati_locali["campo_Bonus_DMG"]) > 0 else Shared.finestra.ids.bonusdanno.text
        except(KeyError):
            print("Nuooo")
        #popup per ultimo
        if len(dati_locali["link"]) > 0:
            from Moduli.Grafica import Popups_Test
            if dati_locali["link"] == "Bottoni":
                Popups_Bottoni_Custom.apri()
            elif dati_locali["link"] == "Sblocca\nSkill":
                from Moduli.Grafica import Popups_NomePG_Skill
                Popups_NomePG_Skill.skill_excel_open()
            elif dati_locali["link"] == "Zaino":
                Popups_Zaino.zainoopen()
            elif dati_locali["link"] == "Mappa\nGlobale":
                Popups_Test.openmappa()
            elif dati_locali["link"] == "Mappa\nGlobale Hex":
                Popups_Test.openmappa(hex=True)
            elif dati_locali["link"] == "Alchimia":
                from Moduli.Grafica import Popups_Alchimia
                Popups_Alchimia.alchimiaopen()
            elif dati_locali["link"] == "Calcolatrice":
                from Moduli.Grafica import Popups_Calcolatrice
                Popups_Calcolatrice.calcolatrice(None)
        if len(dati_locali["titolo_popup"])>1 or len(dati_locali["contenuto_popup"])>1:
            Popups_Notifiche.custom_popup(titolo=str(dati_locali["titolo_popup"]),contenuto=str(dati_locali["contenuto_popup"]))

    def checklistaskill(unused=False):
        self = Shared.finestra
        controlla_skill = self.skill_sbloccatekv.text
        if str(controlla_skill) in ["0",""]:
            controlla_skill = "9999999$$9999999"
        try:
            for indice in sorted(controlla_skill.split("$$")):
                if Shared.skill_importate[str(indice)]["TIPO"]:
                    pass
            return True
        except:
            Popups_Notifiche.nosave()
            return False

    def show_all(unused = False):
        self = Shared.finestra
        EquipAttore.unpack_skill(str(Shared.pg_selezionato['nome_in_uso']))
        EquipAttore.unpack_faretra(str(Shared.pg_selezionato['nome_in_uso']))
        EquipAttore.unpack_pasti(str(Shared.pg_selezionato['nome_in_uso']))
        EquipAttore.unpack_magie(str(Shared.pg_selezionato['nome_in_uso']))
        FinestraPrincipalePG.show_effetti()
        FinestraPrincipalePG.show_caratteristiche_atk_def()
        FinestraPrincipalePG.show_valori_primari()
        FinestraPrincipalePG.shownote()
        FinestraPrincipalePG.showbottoni()
        if Shared.entrato_in_finestra_pricipale == True:
            FinestraPrincipaleNPC.show_npc()
            FinestraPrincipaleCombat.invertiattaccante()
            FinestraPrincipaleCombat.invertiattaccante()
        if Shared.entrato_in_finestra_pricipale == False:
            FinestraPrincipalePG.colazione()
            FinestraPrincipalePG.colazione()
            FinestraPrincipalePG.pranzo()
            FinestraPrincipalePG.pranzo()
            FinestraPrincipalePG.cena()
            FinestraPrincipalePG.cena()
        FinestraPrincipalePG.nomi_magie()
        FinestraPrincipalePG.barrapa()
        FinestraPrincipalePG.meggaggi_pg()
        FinestraPrincipaleNPC.barravitaNPC()


    def conferma(self=False):
        if FunzioniFinestra.checklistaskill():
            ImportazioneAttori.check_file_pg_e_npc_per_update()
            FinestraPrincipalePG.salvanote()
            EquipAttore.salva_pasti()
            FinestraPrincipalePG.box_finestra()
            FunzioniFinestra.show_all()
            FinestraPrincipaleNPC.barravitaNPC()
            Salvataggio.salva_pgnpc(Shared.pg_selezionato["nome_in_uso"])
            FunzioniFinestra.show_all()

    def tempoavanza(unused = False):
        self = Shared.finestra
        if Temp.tempo == "Mattina":
            Temp.tempo = "Pomeriggio"
            self.ids.tempokv.source = "Art/pomeriggio.png"
        elif Temp.tempo == "Pomeriggio":
            Temp.tempo = "Sera"
            self.ids.tempokv.source = "Art/sera.png"
        elif Temp.tempo == "Sera":
            Temp.tempo = "Notte"
            self.ids.tempokv.source = "Art/notte.png"
        elif Temp.tempo == "Notte":
            Temp.tempo = "Mattina"
            self.ids.tempokv.source = "Art/mattina.png"



    def tirameteo(unused = False):
        self = Shared.finestra
        tiro_1 = randrange(1, 3)
        if tiro_1 == 2 or self.ids.tempoinfokv.text == "":
            tiro_2 = randrange(1, 21)
            if tiro_2 < 11:
                self.ids.tempoinfokv.text = "Soleggiato: No cambiamenti"
            elif tiro_2 < 15:
                self.ids.tempoinfokv.text = "Pioggia: \n-Costo movimento in combat +25%\n-Attacco -3"
            elif tiro_2 < 17:
                self.ids.tempoinfokv.text = """Grande Pioggia: \n-Costo movimento in combat +50%\n-Attacco -5
    -Ogni casella dopo la prima possibilita di mancare atk o cast a distanza +10%\n-danno da fuoco -25%
    -danno elettro +25%\n-costo movimento in viaggio +50%"""
            elif tiro_2 < 19:
                self.ids.tempoinfokv.text = """Nebbia:
    -Ogni casella dopo la prima possibilita di mancare atk o cast a distanza +20%
    -danno da gelo +25%"""
            elif tiro_2 == 19:
                self.ids.tempoinfokv.text = """Temporale:
    -Costo movimento in combat +50%\nAttacco -7
    -Ogni casella dopo la prima possibilita di mancare atk o cast a distanza +20%
    -costo movimento in viaggio +100%"""
            elif tiro_2 == 20:
                self.ids.tempoinfokv.text = """Tempesta:
    -Costo movimento in combat +100%\n-Attacco -10
    -Ogni casella dopo la prima possibilita di mancare atk o cast a distanza +33%
    -costo movimento in viaggio +200%"""


    def aggiunginotecondivise(unused = False):
        self = Shared.finestra
        testonuovo = self.ids.notecondivisekv.text

        percorsofile = Shared.path_cartella_shared + f"/notecondivise.txt"

        if not os.path.exists(percorsofile):
            with open(percorsofile, "x") as f:
                pass
        with open(percorsofile, "a") as f:
            f.write("\n" + testonuovo)
        self.ids.notecondivisekv.text = ""

class Temp:
    fermaserver = False
    entered = False
    tempo = "Mattina"
    offset_immagine = [0, 0]
    posizione_immagine = (717.706, 218.317)
    immagine_attiva = "Art/immagini/vuoto.png"
    prex = 0
    prey = 0
    actx = 0
    acty = 0
