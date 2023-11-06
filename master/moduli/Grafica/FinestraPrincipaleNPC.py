import Moduli.SharedData as Shared
from Moduli.Logica import Oggetti
from kivy.properties import partial


def barravitaNPC(*args):
    self = Shared.finestra
    vita = int(Shared.npc_selezionato["pf_tot"])
    if vita == 0:
        vita = 0.00000000001
    dmg1 = int(float(Shared.npc_selezionato["danno"]))
    rapporto1 = int(float(100 / vita * dmg1))
    if rapporto1 <= 19:
        self.barravitaNPCkv.value = 100
    elif 20 <= rapporto1 <= 39:
        self.barravitaNPCkv.value = 80
    elif 40 <= rapporto1 <= 59:
        self.barravitaNPCkv.value = 60
    elif 60 <= rapporto1 <= 79:
        self.barravitaNPCkv.value = 40
    elif 80 <= rapporto1 <= 99:
        self.barravitaNPCkv.value = 19
    elif rapporto1 >= 100:
        self.barravitaNPCkv.value = 0

def show_npc():
    barravitaNPC()

def selezionanpc(numero):
    seleziona_npc_attuale(numeronpc=numero)
    datinpcattuale()
    show_npc()

def datinpcattuale():
    self = Shared.finestra
    self.nomenpckv.text = str(Shared.npc_selezionato["nomepg"])
    testoextra1 = str(Shared.npc_selezionato["extra1"])
    if len(testoextra1) > 90:
        testoextra1 = testoextra1[:45] + "\n" + testoextra1[45:90] + "\n" + testoextra1[90:]
    elif len(testoextra1) > 45:
        testoextra1 = testoextra1[:45] + "\n" + testoextra1[45:]
    testoextra2 = str(Shared.npc_selezionato["extra2"])
    if len(testoextra2) > 90:
        testoextra2 = testoextra2[:45] + "\n" + testoextra2[45:90] + "\n" + testoextra2[90:]
    elif len(testoextra2) > 45:
        testoextra2 = testoextra2[:45] + "\n" + testoextra2[45:]
    testoextra3 = str(Shared.npc_selezionato["extra3"])
    if len(testoextra3) > 90:
        testoextra3 = testoextra3[:45] + "\n" + testoextra3[45:90] + "\n" + testoextra3[90:]
    elif len(testoextra3) > 45:
        testoextra3 = testoextra3[:45] + "\n" + testoextra3[45:]
    testoextra4 = str(Shared.npc_selezionato["extra4"])
    if len(testoextra4) > 90:
        testoextra4 = testoextra4[:45] + "\n" + testoextra4[45:90] + "\n" + testoextra4[90:]
    elif len(testoextra4) > 45:
        testoextra4 = testoextra4[:45] + "\n" + testoextra4[45:]
    testoextra5 = str(Shared.npc_selezionato["extra5"])
    if len(testoextra5) > 90:
        testoextra5 = testoextra5[:45] + "\n" + testoextra5[45:90] + "\n" + testoextra5[90:]
    elif len(testoextra5) > 45:
        testoextra5 = testoextra5[:45] + "\n" + testoextra5[45:]
    testoextra6 = str(Shared.npc_selezionato["extra6"])
    if len(testoextra6) > 90:
        testoextra6 = testoextra6[:45] + "\n" + testoextra6[45:90] + "\n" + testoextra6[90:]
    elif len(testoextra6) > 45:
        testoextra6 = testoextra6[:45] + "\n" + testoextra6[45:]
    self.exra1npckv.text = testoextra1
    self.exra2npckv.text = testoextra2
    self.exra3npckv.text = testoextra3
    self.exra4npckv.text = testoextra4
    self.exra5npckv.text = testoextra5
    self.exra6npckv.text = testoextra6
    self.panpckv.text = "TOT: " + \
                        str(int(Shared.npc_selezionato["pa_tot"]) - int(Shared.npc_selezionato["malus_pa"])) + " Atk:" + \
                        str(Shared.npc_selezionato["pa_arma"])
    self.armanpckv.text = str(
        (Oggetti.trova_oggetto(Shared.npc_selezionato["id_arma_1"]))["NOME"])

def seleziona_npc_attuale(numeronpc):
    Shared.npc_selezionato = Shared.npc_numeri_assegnati[numeronpc]
    Shared.numero_npc_attuale = numeronpc
