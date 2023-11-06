import copy
from math import floor
import Moduli.SharedData as Shared
from Moduli.Grafica import Popups_Notifiche
from Moduli.Logica import MeccanicaDanno


class Temp:
    pa_spesi_somma = 0
    statusbottonemagia = 0
    combattenteslot = 1


def selezionacombattente(numero):
    self = Shared.finestra
    if numero == 0:
        if Temp.combattenteslot == 1:
            Shared.Attaccante = copy.deepcopy(Shared.pg_selezionato)
            self.labelattaccante.text = "PG"
            self.boxtipodanno.text = Shared.Attaccante["eq_arma_1"]["TIPO3"].capitalize()
            Temp.combattenteslot = 2

        elif Temp.combattenteslot == 2:
            Shared.Difensore = copy.deepcopy(Shared.pg_selezionato)
            self.labeldifensore.text = "PG"
            Temp.combattenteslot = 1

    elif numero >= 1:
        if Temp.combattenteslot == 1:
            Shared.Attaccante = copy.deepcopy(Shared.npc_numeri_assegnati[numero])
            self.labelattaccante.text = str(numero)
            self.boxtipodanno.text = Shared.Attaccante["eq_arma_1"]["TIPO3"].capitalize()
            Temp.combattenteslot = 2

        elif Temp.combattenteslot == 2:
            Shared.Difensore = copy.deepcopy(Shared.npc_numeri_assegnati[numero])
            self.labeldifensore.text = str(numero)
            Temp.combattenteslot = 1

    Shared.bonusdannoselezionati = []

    tipoarma = Shared.Attaccante["eq_arma_1"]["TIPO1"]
    categoriaarma = Shared.categorie_armi[tipoarma][0]
    if categoriaarma == "corta":
        selezionacarattattacco(2)
    if categoriaarma == "media":
        selezionacarattattacco(3)
    if categoriaarma == "lunga":
        selezionacarattattacco(0)
    if categoriaarma == "maninude":
        selezionacarattattacco(0)


def invertiattaccante():
    self = Shared.finestra
    numero_1 = self.labelattaccante.text
    numero_1b = self.labelattaccante.text
    numero_2 = self.labeldifensore.text
    if numero_2 == "PG":
        numero_2 = 0
    if numero_1 == "PG":
        numero_1 = 0
    selezionacombattente(int(numero_2))
    selezionacombattente(int(numero_1))
    if self.labelattaccante.text == numero_1b:
        selezionacombattente(int(numero_2))
        selezionacombattente(int(numero_2))
        selezionacombattente(int(numero_1))

selezionati = []

def selezionacarattattacco(numero):
    self = Shared.finestra

    if numero == 0:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk0.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk0.background_color = (1, 0, 0, 1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 1:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk1.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk1.background_color = (1, 0, 0, 1)
            Shared.bonusdannoselezionati.append(numero)

    if numero == 2:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk2.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk2.background_color = (0, 1, 0, 1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 3:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk3.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk3.background_color = (0, 1, 0, 1)
            Shared.bonusdannoselezionati.append(numero)

    if numero == 4:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk4.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk4.background_color = (0.5, 0.5, 1, 1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 5:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk5.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk5.background_color = (0.5, 0.5, 1, 1)
            Shared.bonusdannoselezionati.append(numero)

    if numero == 6:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk6.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk6.background_color = (1, 1, 0, 1)
            Shared.bonusdannoselezionati.append(numero)
    if numero == 7:
        if numero in Shared.bonusdannoselezionati:
            self.ids.boxatk7.background_color = (0, 0, 0, 1)
            Shared.bonusdannoselezionati.remove(numero)
        else:
            self.ids.boxatk7.background_color = (1, 1, 0, 1)
            Shared.bonusdannoselezionati.append(numero)
