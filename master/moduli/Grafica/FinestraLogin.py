from Moduli.Grafica import KivyInput, Popups_NuovoPG
from Moduli.Logica import GestioneSkill, Inizializza, ImportazioneAttori
from kivy.uix.screenmanager import Screen
import Moduli.SharedData as Shared
from Moduli.Utils import CartellaShared

class FinestraLogin(Screen):
    clicks = 0
    tempself = ""
    Inizializza.importa_dati_iniziali_pg_npc_e_oggetti()
    def namebutton(self, nomepg, master):
        self.tempself = self
        if nomepg != "":
            Shared.finestra_login = self
            if nomepg != "Nuovo PG":
                if nomepg.endswith("-"):
                    if master:
                        Shared.mastermode = True
                    nomepg = nomepg[:-1]
                elif master:
                    Shared.master_hint = True
                KivyInput.sm.current = "FinestraPrincipale"
                Shared.pg_login = nomepg
                Shared.nome_per_db_skill = nomepg
                GestioneSkill.importa_db_skill()
                Inizializza.crea_dati_base_pg()
                ImportazioneAttori.findAndImport(nomepg)
                ImportazioneAttori.importa_tutti_NPC()
            elif nomepg == "Nuovo PG":
                Popups_NuovoPG.nuovo_pg_open()
        else:
            self.clicks += 1
            if self.clicks > 2:
                self.namebutton(nomepg = "Master-", master = True)