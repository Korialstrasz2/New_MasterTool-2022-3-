from math import floor
from random import randrange

from Moduli.Grafica import FinestraPrincipaleMain, FinestraPrincipaleNPC, Popups_Notifiche
from Moduli.Logica import Salvataggio
from kivy.clock import Clock
import Moduli.SharedData as Shared

d4 = lambda :randrange(1,5)
d6 = lambda :randrange(1,7)
d8 = lambda :randrange(1,9)
d10 = lambda :randrange(1,11)
d12 = lambda :randrange(1,13)
d20 = lambda :randrange(1,21)
d100 = lambda :randrange(1,101)

danni_armi = {
    "maninude": [3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,9,9,9,9],
    "corta": [4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,11,11,11,11],
    "media": [-30,-30,-30,-30,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,12,12,12,12,13,13,13,13],
    "lunga": [-30,-30,-30,-30,-30,-30,-30,-30,7,7,7,7,10,10,10,10,10,10,10,10,13,13,13,13,16,16,16,16]
}

tier_danni = {
    "-4": "1d4",
    "-3": "1d4",
    "-2": "1d4",
    "-1": "1d4",
    "0": "1d6",
    "1": "1d8",
    "2": "1d10",
    "3": "1d12",
    "4": "1d6+1d8",
    "5": "2d8",
    "6": "1d8+1d10",
    "7": "2d10",
    "8": "1d10+2d6",
    "9": "2d12",
    "10": "2d10+1d6",
    "11": "2d10+1d8",
    "12": "3d10",
    "13": "4d8",
    "14": "3d10+1d4",
    "15": "3d10+1d6",
    "16": "3d10+1d8",
    "17": "4d10",
    "18": "3d10+1d12",
    "19": "4d10+1d4",
    "20": "4d10+1d6",
    "21": "4d10+1d8",
    "22": "5d10",
    "23": "4d10+1d12",
    "24": "5d10+1d4",
    "25": "5d10+1d6",
    "26": "5d10+1d8",
    "27": "6d10",
    "28": "5d10+1d12",
    "29": "5d12+1d4",
    "30": "5d12+1d6",
    "31": "5d12+1d8",
    "32": "5d12+1d10",
    "33": "6d12",
    "34": "6d12+1d4",
    "35": "6d12+1d6",
    "36": "6d12+1d8",
    "37": "6d12+1d10",
    "38": "7d12+1d4",
    "39": "7d12+1d8",
    "40": "7d12+1d10"
}


livelli_resistenza = [-45,-35,-25,-15,0,15,23,30,35,40,45,50,55,60]

for item in Shared.categorie_armi:
    categoria = Shared.categorie_armi[item][0]


selezionati = []



def dannobonuscaratteristica():
    from Moduli.SharedData import Attaccante
    tot = 0
    if 0 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["forza_tot"]) - 10) / 2)
    if 1 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["resistenza_tot"]) - 10) / 2)
    if 2 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["velocita_tot"]) - 10) / 2)
    if 3 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["agilita_tot"]) - 10) / 2)
    if 4 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["intelligenza_tot"]) - 10) / 2)
    if 5 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["concentrazione_tot"]) - 10) / 2)
    if 6 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["personalita_tot"]) - 10) / 2)
    if 7 in Shared.bonusdannoselezionati:
        tot += floor((float(Attaccante["saggezza_tot"]) - 10) / 2)
    return tot

class Danniextra:
    danniextra = 0
    scrittadanno = ""

def attaccanemico():
    from Moduli.SharedData import Attaccante,Difensore
    self = Shared.finestra

    def crit_pic_off(*args):
        self.ids.critmagimgkv.size_hint = (0, 0)
        self.ids.critnorimgkv.size_hint = (0, 0)
        self.ids.critminimgkv.size_hint = (0, 0)

    try:
        int(self.boxdado.text)
        int(self.boxmodattacco.text)
        int(self.bonusdanno.text)
        int(self.boxbonustier.text)
    except:
        import Popups
        Popups_Notifiche.boxcheck()
        return



    crit_min = str(Attaccante['crit_min']).strip().split(',')
    crit_nor = str(Attaccante['crit_nor']).strip().split(',')
    crit_mag = str(Attaccante['crit_mag']).strip().split(',')
    self.labeltierdanno.text = "0"
    atkatktotale = str(int(Attaccante['attacco_tot']) + int(self.boxdado.text) + int(self.boxmodattacco.text)
                       - int(Difensore['difesa_tot']) + floor((int(Attaccante['fortuna_tot']) - 10) / 2))

    if int(atkatktotale) <= 0:
        atkatktotale = "Fail"
    elif int(atkatktotale) >= 20:
        atkatktotale = "20"
    tipoarma = Attaccante["eq_arma_1"]["TIPO1"]
    categoriaarma = Shared.categorie_armi[tipoarma][0]
    if atkatktotale != "Fail":
        tierdanno = danni_armi[categoriaarma][int(atkatktotale)+1]
    else:
        tierdanno = 0
    fortunacritico = int(Attaccante["fortuna_tot"])
    if fortunacritico < 12:
        fortunacritico = 12
    modfortuna = floor((fortunacritico - 10) / 2)
    if tierdanno > 0:
        if str(self.boxdado.text) in crit_min and tierdanno != 0:
            tierdanno += floor(modfortuna)
            self.ids.critminimgkv.size_hint = (0.35, 0.35)
            Clock.schedule_once(crit_pic_off, 5)
        elif str(self.boxdado.text) in crit_nor and tierdanno != 0:
            tierdanno += floor(modfortuna * 1.5)
            self.ids.critnorimgkv.size_hint = (0.5, 0.5)
            Clock.schedule_once(crit_pic_off, 5)
        elif str(self.boxdado.text) in crit_mag and tierdanno != 0:
            tierdanno += floor(modfortuna * 2)
            self.ids.critmagimgkv.size_hint = (0.7, 0.7)
            Clock.schedule_once(crit_pic_off, 5)
        if int(self.boxdado.text) == 1:
            self.labeltierdanno.text = "Fail Critico"
        elif int(self.boxdado.text) >= 1:
            tierdanno += int(Attaccante["tier_tot"])
            Danniextra.danniextra = int(self.bonusdanno.text) + dannobonuscaratteristica()
            self.labeltierdanno.text = tier_danni[str(tierdanno+int(self.boxbonustier.text))] + "\n+ " + f"{Danniextra.danniextra}"
    else:
        self.labeltierdanno.text = "No Danno"

    if int(self.boxdado.text) == 20 and atkatktotale == "Fail":
        self.labeltierdanno.text = tier_danni[str(Attaccante['livello'])]
    elif int(self.boxdado.text) == 19 and atkatktotale == "Fail":
        self.labeltierdanno.text = tier_danni[str(int(int(Attaccante['livello'])/2))]

def tiradadiattacco():
    self = Shared.finestra
    self.boxdado.text = str(d20())

    if "d" in self.labeltierdanno.text:
        dannotot = 0
        Danniextra.scrittadanno = ""
        daditext = self.labeltierdanno.text.split()[0]
        dadilista = list(daditext.split("+"))
        for item in dadilista:
            numerodadi = item[0]
            for tiro in range(int(numerodadi)):
                tirod0 = f"{item[1:]}()"
                tirod1 = eval(tirod0)
                dannotot += tirod1
                Danniextra.scrittadanno += f"{str(tirod1)}+"
        Danniextra.scrittadanno += f"{str(Danniextra.danniextra)}={int(Danniextra.danniextra)+int(dannotot)}"
        self.campodannokv.text = Danniextra.scrittadanno



def dannofisico():
    from Moduli.SharedData import Attaccante,Difensore
    self = Shared.finestra
    dannopreresistenza = 0
    if len(self.campodannokv.text) > 0:
        if "=" in self.campodannokv.text:
            dannopreresistenza = int(self.campodannokv.text.strip().split("=")[1])
        else:
            dannopreresistenza = int(self.campodannokv.text)
        if dannopreresistenza > 0:
            tipodanno = self.boxtipodanno.text.lower()
            resistenza = eval(f"Difensore['res_{tipodanno}']")
            if resistenza < -4:
                resistenza = -4
            elif resistenza > 7:
                resistenza = 7

            dannofinale = dannopreresistenza - (dannopreresistenza/100*livelli_resistenza[resistenza+4]) -\
                          Difensore['rd_fis']

            if dannofinale > 0:
                if self.labeldifensore.text == "PG":
                    self.boxdannokv.text = str(dannofinale)
                    FinestraPrincipaleMain.FunzioniFinestra.conferma()
                else:
                    nomepng = self.labeldifensore.text
                    Shared.npc_numeri_assegnati[int(nomepng)]["danno"] = int(Shared.npc_numeri_assegnati[int(nomepng)]["danno"]) + dannofinale
                    if str(Shared.numero_npc_attuale) == str(nomepng):
                        FinestraPrincipaleNPC.seleziona_npc_attuale(int(nomepng))
                        FinestraPrincipaleMain.FunzioniFinestra.conferma()
                        if self.labeldifensore.text != "PG":
                            Salvataggio.salva_pgnpc(Shared.npc_numeri_assegnati[Shared.numero_npc_attuale]["nome_in_uso"])

def dannoelementale(tipo):
    from Moduli.SharedData import Attaccante, Difensore
    self = Shared.finestra
    dannopreresistenza = 0
    if len(self.campodannokv.text) > 0:
        if "=" in self.campodannokv.text:
            dannopreresistenza = int(self.campodannokv.text.strip().split("=")[1])
        else:
            dannopreresistenza = int(self.campodannokv.text)

        if dannopreresistenza > 0:
            resistenza = eval(f"Difensore['res_{tipo}']")
            if resistenza < -4:
                resistenza = -4
            elif resistenza > 7:
                resistenza = 7
            rd = eval(f"Difensore['rd_{tipo}']")
            dannofinale = dannopreresistenza - (dannopreresistenza/100*livelli_resistenza[resistenza+4]) - rd


            if dannofinale > 0:
                if self.labeldifensore.text == "PG":
                    self.boxdannokv.text = str(dannofinale)
                    FinestraPrincipaleMain.FunzioniFinestra.conferma()
                else:
                    nomepng = self.labeldifensore.text
                    Shared.npc_numeri_assegnati[int(nomepng)]["danno"] = int(
                        Shared.npc_numeri_assegnati[int(nomepng)]["danno"]) + dannofinale
                    if str(Shared.numero_npc_attuale) == str(nomepng):
                        FinestraPrincipaleNPC.seleziona_npc_attuale(int(nomepng))
                        FinestraPrincipaleMain.FunzioniFinestra.conferma()
                        if self.labeldifensore.text != "PG":
                            Salvataggio.salva_pgnpc(
                                Shared.npc_numeri_assegnati[Shared.numero_npc_attuale]["nome_in_uso"])

def dannopuro():
    self = Shared.finestra
    dannopreresistenza = 0
    if len(self.campodannokv.text) > 0:
        if "=" in self.campodannokv.text:
            dannopreresistenza = int(self.campodannokv.text.strip().split("=")[1])
        else:
            dannopreresistenza = int(self.campodannokv.text)

        if dannopreresistenza > 0:
            dannofinale = dannopreresistenza

            if dannofinale > 0:
                if self.labeldifensore.text == "PG":
                    self.boxdannokv.text = str(dannofinale)
                    FinestraPrincipaleMain.FunzioniFinestra.conferma()
                else:
                    nomepng = self.labeldifensore.text
                    Shared.npc_numeri_assegnati[int(nomepng)]["danno"] = int(
                        Shared.npc_numeri_assegnati[int(nomepng)]["danno"]) + dannofinale
                    if str(Shared.numero_npc_attuale) == str(nomepng):
                        FinestraPrincipaleNPC.seleziona_npc_attuale(int(nomepng))
                        FinestraPrincipaleMain.FunzioniFinestra.conferma()
                        if self.labeldifensore.text != "PG":
                            Salvataggio.salva_pgnpc(
                                Shared.npc_numeri_assegnati[Shared.numero_npc_attuale]["nome_in_uso"])

def selezionacarattattacco(numero):
    self = Shared.finestra
    if numero == 0:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk0.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk0.background_color = (1,0,0,1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 1:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk1.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk1.background_color = (1,0,0,1)
            Shared.bonusdannoselezionati.append(numero)

    if numero == 2:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk2.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk2.background_color = (0,1,0,1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 3:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk3.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk3.background_color = (0,1,0,1)
            Shared.bonusdannoselezionati.append(numero)

    if numero == 4:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk4.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk4.background_color = (0.5,0.5,1,1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 5:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk5.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk5.background_color = (0.5,0.5,1,1)
            Shared.bonusdannoselezionati.append(numero)

    if numero == 6:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk6.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk6.background_color = (1,1,0,1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 7:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk7.background_color = (0,0,0,1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk7.background_color = (1,1,0,1)
            Shared.bonusdannoselezionati.append(numero)

