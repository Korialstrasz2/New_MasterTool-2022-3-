import ast
import json
import os
from math import floor

from random import randrange
import Moduli.SharedData as Shared
from Moduli.Grafica import Popups_Notifiche

nomefinestra = ""
programstart = False
bloccosalva = []

randomizza = 0
riequip = False
tiporandom1 = ""


pathrisorse = Shared.path_dati

materiali_legg_pes = {}
materiali_leggeri = []
materiali_pesanti = []
da_esterno = False

if pathrisorse == "":
    pathrisorse = r"C:\Users\alexo\PycharmProjects\MasterSlim\Dati"
    Shared.path_dati = r"C:\Users\alexo\PycharmProjects\MasterSlim\Dati"
    da_esterno = True


with open(f"{pathrisorse}\oggetti-categorie-armi.txt", "r") as oggcatarmi:
    Shared.categorie_armi = ast.literal_eval(oggcatarmi.read())
Shared.gruppoarmi = []
for indice in Shared.categorie_armi.keys():
    Shared.gruppoarmi.append(indice)
with open(f"{pathrisorse}\gruppo-non-armi.txt", "r") as grpnnarmi:
    Shared.nonarmi = ast.literal_eval(grpnnarmi.read())
    for nonarma in Shared.nonarmi:
        Shared.gruppoarmi.remove(nonarma)

with open(f"{pathrisorse}\gruppo-armi-comuni.txt", "r") as grparmicom:
    Shared.gruppoarmicomuni = ast.literal_eval(grparmicom.read())
with open(f"{pathrisorse}\materiali-caratteristiche.txt", "r") as matcar:
    Shared.materiali_legg_pes = ast.literal_eval(matcar.read())
with open(f"{Shared.path_dati}/negozi-con-zona.json", "r") as negozi_ris:
    Shared.negozi = json.load(negozi_ris)


for tipoarma in materiali_legg_pes:
    for tipoleggpes in materiali_legg_pes[tipoarma]:
        if tipoleggpes == "leggero":
            for i in range(len(materiali_legg_pes[tipoarma][tipoleggpes])):
                materiali_leggeri.append(materiali_legg_pes[tipoarma][tipoleggpes][str(i + 1)])
        elif tipoleggpes == "pesante":
            for i in range(len(materiali_legg_pes[tipoarma][tipoleggpes])):
                materiali_pesanti.append(materiali_legg_pes[tipoarma][tipoleggpes][str(i + 1)])
materiali_leggeri = list(set(materiali_leggeri))
materiali_pesanti = list(set(materiali_pesanti))

equipaggiabili = ["anello_1", "anello_2", "anello_3", "anello_4", "anello_5", "anello_6", "anello_7", "anello_8",
                  "orecchino_1", "orecchino_2", "orecchino_3", "orecchino_4", "orecchino_5", "orecchino_6",
                  "spilla", "fascia", "mantello", "amuleto", "cintura"]

def importa_oggetti():
    fileoggetti = Shared.path_dati + r"\oggetti.json"
    with open(fileoggetti, 'r') as json_file:
        Shared.file_oggetti = json.load(json_file)
        for item in Shared.file_oggetti:
            if type(Shared.file_oggetti[item][0]) == int:
                Shared.db_oggetti[Shared.file_oggetti[item][0]] = {}
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["ID"] = Shared.file_oggetti[item][0]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["NOME"] = Shared.file_oggetti[item][1]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["TIPO1"] = Shared.file_oggetti[item][2]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["TIPO2"] = Shared.file_oggetti[item][3]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["TIPO3"] = Shared.file_oggetti[item][4]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["DESCRIZIONE"] = Shared.file_oggetti[item][5]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["VALORE"] = Shared.file_oggetti[item][6]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["SLOT"] = Shared.file_oggetti[item][7]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO1"] = Shared.file_oggetti[item][8]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO2"] = Shared.file_oggetti[item][9]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO3"] = Shared.file_oggetti[item][10]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO4"] = Shared.file_oggetti[item][11]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO5"] = Shared.file_oggetti[item][12]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO6"] = Shared.file_oggetti[item][13]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["EFFETTO7"] = Shared.file_oggetti[item][14]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["LV_LOOT"] = Shared.file_oggetti[item][15]
                Shared.db_oggetti[Shared.file_oggetti[item][0]]["RARITA"] = Shared.file_oggetti[item][16]


def aggiungi_oggetto_in_posizione(id_precedente,dati):
    post_dict = {}
    flagskip = False
    found = False
    for _ in Shared.file_oggetti:
        if flagskip == False:
            if str(Shared.file_oggetti[_][0]) != str(id_precedente):
                post_dict[_] = Shared.file_oggetti[_]
            else:
                found = True
                post_dict[_] = Shared.file_oggetti[_]
                post_dict[str(int(_)+1)] = dati
                flagskip = True
        else:
            flagskip = False
    if not found:
        post_dict[str(int(id_precedente) + 2)] = dati
    fileoggetti = Shared.path_dati + r"\oggetti.json"
    with open(fileoggetti, "w") as json_file:
        json.dump(post_dict, json_file, indent=4)

    Shared.file_oggetti = post_dict
    importa_oggetti()

def trova_oggetto(ids=0, nome="", boxtipo1="", boxtipo2="", ):
    Shared.db_oggetti[9999999] = {'ID': 9999999, 'NOME': 'NA', 'TIPO1': 'NA','TIPO2': 'NA', 'TIPO3': 'NA',
                                  'DESCRIZIONE': 'NA','VALORE': '0', 'SLOT': 'NA', 'EFFETTO1': 'NA', 'EFFETTO2': 'NA',
                                  'EFFETTO3': 'NA','EFFETTO4': 'NA', 'EFFETTO5': 'NA', 'EFFETTO6': 'NA',
                                  'EFFETTO7': 'NA','LV_LOOT': '0', 'RARITA': '0'}
    try:
        int(ids)
    except:
        ids = ""
    risultati = []
    try:
        if ids == "":
            ids = 0
        if int(ids) > 0:
            for item in Shared.db_oggetti:
                if str(item) == str(ids):
                    return Shared.db_oggetti[item]

        else:
            for item in Shared.db_oggetti:
                if nome.lower() in str(Shared.db_oggetti[item]["NOME"]).lower():
                    if boxtipo1 == "" or boxtipo1.lower() in str(Shared.db_oggetti[item]["TIPO1"]).lower():
                        if boxtipo2 == "" or boxtipo2.lower() in str(Shared.db_oggetti[item]["TIPO2"]).lower():
                            risultati.append(Shared.db_oggetti[item])


        if len(risultati) == 0:
            for item in Shared.db_oggetti:
                if str(item) == "9999999":
                    risultati.append(Shared.db_oggetti[item])
                    return risultati
        if len(risultati) > 20:
            risultati = risultati[:20]
            risultati.append(Shared.db_oggetti[9999999])


        if len(risultati) == 0:
            for item in Shared.db_oggetti:
                if str(item) == "9999999":
                    risultati.append(Shared.db_oggetti[item])
                    return risultati

        return risultati if len(risultati) > 0 else []
    except:
        Popups_Notifiche.nodigit(stringa="Errore caricamento Oggetti - ID ")

def cambia_legg_pes(input_ogg):
    tipo = "armature"
    if input_ogg["TIPO1"] in Shared.categorie_armi.keys():
        tipo = "armi"
    materiale1 = input_ogg["TIPO2"]
    for leggpes1 in materiali_legg_pes[tipo]:
        for livello in materiali_legg_pes[tipo][leggpes1]:
            if materiale1 == materiali_legg_pes[tipo][leggpes1][livello]:
                for leggpes2 in materiali_legg_pes[tipo]:
                    if leggpes2 != leggpes1:
                        return trova_oggetto(boxtipo1=input_ogg["TIPO1"],
                                             boxtipo2=materiali_legg_pes[tipo][leggpes2][livello])


def estrai_oggetto(tipo="casuale", livello=0, fortuna=10, norarita=False):
    if livello == "casuale":
        livello = randrange(1, 10)
    oggetti_tipo_rar = {}
    oggetti_tipo_rar[1] = {}
    oggetti_tipo_rar[2] = {}
    oggetti_tipo_rar[3] = {}
    oggetti_tipo_rar[4] = {}
    rarita = randrange(1, 100)
    if rarita < 71:
        risultato_rarita = 1
    elif rarita < 86:
        risultato_rarita = 2
    elif rarita < 96:
        risultato_rarita = 3
    else:
        risultato_rarita = 4
    if norarita:
        risultato_rarita = randrange(1,5)
    if tipo != "casuale":
        if tipo != "arma":
            for ogg in Shared.db_oggetti:
                if Shared.db_oggetti[ogg]["TIPO1"] == tipo:
                    if int(Shared.db_oggetti[ogg]["RARITA"]) == 1:
                        oggetti_tipo_rar[1][ogg] = Shared.db_oggetti[ogg]
                    elif int(Shared.db_oggetti[ogg]["RARITA"]) == 2:
                        oggetti_tipo_rar[2][ogg] = Shared.db_oggetti[ogg]
                    elif int(Shared.db_oggetti[ogg]["RARITA"]) == 3:
                        oggetti_tipo_rar[3][ogg] = Shared.db_oggetti[ogg]
                    elif int(Shared.db_oggetti[ogg]["RARITA"]) == 4:
                        oggetti_tipo_rar[4][ogg] = Shared.db_oggetti[ogg]
        else:
            for ogg in Shared.db_oggetti:
                if Shared.db_oggetti[ogg]["TIPO1"] in Shared.gruppoarmi:
                    if int(Shared.db_oggetti[ogg]["RARITA"]) == 1:
                        oggetti_tipo_rar[1][ogg] = Shared.db_oggetti[ogg]
                    elif int(Shared.db_oggetti[ogg]["RARITA"]) == 2:
                        oggetti_tipo_rar[2][ogg] = Shared.db_oggetti[ogg]
                    elif int(Shared.db_oggetti[ogg]["RARITA"]) == 3:
                        oggetti_tipo_rar[3][ogg] = Shared.db_oggetti[ogg]
                    elif int(Shared.db_oggetti[ogg]["RARITA"]) == 4:
                        oggetti_tipo_rar[4][ogg] = Shared.db_oggetti[ogg]

    else:
        for ogg in Shared.db_oggetti:
            if Shared.db_oggetti[ogg]["RARITA"] != "Vuoto":
                if int(Shared.db_oggetti[ogg]["RARITA"]) == 1:
                    oggetti_tipo_rar[1][ogg] = Shared.db_oggetti[ogg]
                elif int(Shared.db_oggetti[ogg]["RARITA"]) == 2:
                    oggetti_tipo_rar[2][ogg] = Shared.db_oggetti[ogg]
                elif int(Shared.db_oggetti[ogg]["RARITA"]) == 3:
                    oggetti_tipo_rar[3][ogg] = Shared.db_oggetti[ogg]
                elif int(Shared.db_oggetti[ogg]["RARITA"]) == 4:
                    oggetti_tipo_rar[4][ogg] = Shared.db_oggetti[ogg]

    if len(oggetti_tipo_rar[risultato_rarita]) == 0:
        risultato_rarita = randrange(1, 5)
    if len(oggetti_tipo_rar[risultato_rarita]) == 0:
        risultato_rarita = 1
    if len(oggetti_tipo_rar[risultato_rarita]) == 0:
        risultato_rarita = 2
    if len(oggetti_tipo_rar[risultato_rarita]) == 0:
        risultato_rarita = 3
    if len(oggetti_tipo_rar[risultato_rarita]) == 0:
        risultato_rarita = 4

    mod_fortuna = floor((int(fortuna) - 10) / 2)
    livello = int(livello) + randrange(0, 1) * mod_fortuna

    if livello < 1:
        livello = 1
    if livello > 10:
        livello = 10

    def riempi_ogg_lv(oggetti_tipo_rar, risultato_rarita, livello):
        gruppo_temp = []
        for item in oggetti_tipo_rar[risultato_rarita]:
            if str(livello) in str(oggetti_tipo_rar[risultato_rarita][item]["LV_LOOT"]).split("-"):
                gruppo_temp.append(item)
        return gruppo_temp

    ogg_lv = riempi_ogg_lv(oggetti_tipo_rar=oggetti_tipo_rar, risultato_rarita=risultato_rarita, livello=livello)
    if len(ogg_lv) > 0:
        indice = ogg_lv[randrange(0, len(ogg_lv))]
        return indice

    else:
        livello -= 1
        ogg_lv = riempi_ogg_lv(oggetti_tipo_rar=oggetti_tipo_rar, risultato_rarita=risultato_rarita, livello=livello)
        if len(ogg_lv) > 0:
            indice = ogg_lv[randrange(0, len(ogg_lv))]
            return indice
        else:
            livello += 2
            ogg_lv = riempi_ogg_lv(oggetti_tipo_rar=oggetti_tipo_rar, risultato_rarita=risultato_rarita,
                                   livello=livello)
            if len(ogg_lv) > 0:
                indice = ogg_lv[randrange(0, len(ogg_lv))]
                return indice
            else:
                livello = 1
                ogg_lv = riempi_ogg_lv(oggetti_tipo_rar=oggetti_tipo_rar, risultato_rarita=risultato_rarita,
                                       livello=livello)
                if len(ogg_lv) > 0:
                    indice = ogg_lv[randrange(0, len(ogg_lv))]
                    return indice
                else:
                    try:
                        gruppo_tot = []
                        for rarita in oggetti_tipo_rar:
                            if len(oggetti_tipo_rar[rarita]) > 0:
                                for oggetto in oggetti_tipo_rar[rarita]:
                                    gruppo_tot.append(oggetto)
                        indice = gruppo_tot[0]
                        return indice
                    except:
                        pass
    return 9999999


valori = {}
valori_armi = {}
valori_armature = {}
valori_chainmail = {}
valori_scudi = {}
valori_vesti = {}
valori_extra = []
valori_anelli = []
valori_orecchini = []
valori_spille = []
valori_fasce = []
valori_mantelli = []
valori_amuleti = []
valori_cinture = []
valori_pozioni = []
gruppoCategorie = []

gruppoequip = ["anello", "orecchino", "spilla", "fascia", "mantello", "amuleto", "cintura", "pozione"]
gruppoequip6 = ["anello", "orecch", "spilla", "fascia", "mantel", "amulet", "cintur", "pozion"]

tipi_negozio = ["generale", "contenitori", "fabbro", "taverna", "alchimista", "oggetti magici", "arcieria",
                "abbigliamento", "armaiolo", "fabbricante di armi", "carovana khajiit"]


def importa_db_oggetti():
    if "flagexportdboggetti.json" in os.listdir(Shared.path_cartella_shared):
        pathfile = os.path.join(Shared.path_cartella_shared, "flagexportdboggetti.json")
        with open(pathfile, 'r') as json_file:
            data = json.load(json_file)
        Shared.file_oggetti = data
    fileoggetti = Shared.path_dati + r"\oggetti.json"
    with open(fileoggetti, "w") as json_file:
        json.dump(data, json_file, indent=4)
    importa_oggetti()

def trova_ultimo_popolato():
    indice = 0
    for item in Shared.file_oggetti:
        if str(Shared.file_oggetti[item][0]).isdigit():
            ids = Shared.file_oggetti[item][0]
            if int(ids) > indice and int(ids) != 9999999:
                indice = ids
    return indice

def estrai_negozio(tipo_negozio, livello):
    try:
        tipo_negozio = tipo_negozio.lower()
        oggetti_estratti = []
        lv = int(livello)
        khajiit = False
        livello = int(livello)
        tot_oggetti = int(15 + (livello * 5.5))
        if tipo_negozio == "generale":
            tot_oggetti += int(tot_oggetti * 1.2)
            for x in range(int(livello * 1.5)):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="oggettivari", livello=lv, fortuna=10))
        elif tipo_negozio == "fabbro":
            tot_oggetti += int(tot_oggetti * 1)
            for x in range(livello*2):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="lingotto", livello=lv, fortuna=10))
        elif tipo_negozio == "oggetti magici":
            tot_oggetti += int(tot_oggetti * 0.7)
            for x in range(livello*1):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="gemmaanima", livello=lv, fortuna=10))
            for x in range(livello *2):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="pergamena", livello=lv, fortuna=10))
        elif tipo_negozio == "fabbricante di armi":
            tot_oggetti += int(tot_oggetti * 1.2)
            for x in range(livello*2):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="lingotto", livello=lv, fortuna=10))
        elif tipo_negozio == "arcieria":
            for x in range(livello*2):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="freccia", livello=lv, fortuna=10))
        elif tipo_negozio == "taverna":
            for x in range(livello*2):
                oggetti_estratti.append(estrai_oggetto(tipo="oggettivari", livello=1, fortuna=10))
            stanze_bagno_cibo = []
            for x in range(livello):
                stanze_bagno_cibo.append(estrai_oggetto(tipo="bagno", livello=lv, fortuna=10))
            for x in range((livello)+3):
                stanze_bagno_cibo.append(estrai_oggetto(tipo="stanza", livello=lv, fortuna=10))
                stanze_bagno_cibo.append(estrai_oggetto(tipo="cibo", livello=lv, fortuna=10))
            stanze_bagno_cibo = list(set(stanze_bagno_cibo))
            for x in stanze_bagno_cibo:
                oggetti_estratti.append(x)
        elif tipo_negozio == "alchimista":
            for x in range(int(livello*0.75)):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="pozione", livello=lv, fortuna=10,norarita=True))
                oggetti_estratti.append(estrai_oggetto(tipo="pozione", livello=lv-3, fortuna=10))
                oggetti_estratti.append(estrai_oggetto(tipo="pozione", livello=lv-4, fortuna=10))
        elif tipo_negozio == "carovana khajiit":
            khajiit = True
            tot_oggetti += int(tot_oggetti * 1.5)
            for x in range(livello * 3):
                lv = randrange(lv - 3, lv + 1)
                oggetti_estratti.append(estrai_oggetto(tipo="oggettivari", livello=lv, fortuna=10))

        numero_ogg_effettivi = randrange(int(tot_oggetti / 100 * 70), int(tot_oggetti / 100 * 130))
        pool = []
        for tipo in oggetti_per_negozio:
            if oggetti_per_negozio[tipo][tipo_negozio] == 4:
                for num in range(int(2.5 ** 0)):
                    pool.append({tipo: -2})
            elif oggetti_per_negozio[tipo][tipo_negozio] == 3:
                for num in range(int(2.5 ** 1)):
                    pool.append({tipo: -2})
            elif oggetti_per_negozio[tipo][tipo_negozio] == 2:
                for num in range(int(2.5 ** 2)):
                    pool.append({tipo: -1})
            elif oggetti_per_negozio[tipo][tipo_negozio] == 1:
                for num in range(int(2.5 ** 3)):
                    pool.append({tipo: 0})
            elif oggetti_per_negozio[tipo][tipo_negozio] == 0:
                for num in range(int(2.5 ** 4)):
                    pool.append({tipo: 0})

        tipo_temp = "usabile"
        for numero in range(numero_ogg_effettivi):
            index = randrange(len(pool))
            diz = pool[index]
            tipo = list(diz.keys())[0]
            lv = livello + diz[tipo]
            lv = randrange(lv - 3, lv + 1)
            if khajiit:
                sorte = randrange(1,4)
                if sorte == 1:
                    tipo = tipo_temp
            oggetto = estrai_oggetto(tipo=tipo, livello=lv, fortuna=10, norarita=khajiit)
            if oggetto == 9999999:
                print("tipo = " + str(tipo) + " lv = " + str(lv))
            oggetti_estratti.append(oggetto)
            tipo_temp = tipo
        oggetti_estratti.sort()
        return oggetti_estratti
    except:
        return [9999999]


oggetti_per_negozio = {
    "martello": {"generale": 3, "contenitori": 5, "fabbro": 1, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 4,
                 "abbigliamento": 5, "armaiolo": 3, "fabbricante di armi": 0, "carovana khajiit": 1},
    "tirapugni": {"generale": 3, "contenitori": 5, "fabbro": 3, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
                  "arcieria": 4,
                  "abbigliamento": 5, "armaiolo": 4, "fabbricante di armi": 0, "carovana khajiit": 1},
    "nunchaku": {"generale": 3, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "coltello": {"generale": 1, "contenitori": 4, "fabbro": 2, "taverna": 3, "alchimista": 4, "oggetti magici": 5,
                 "arcieria": 3,
                 "abbigliamento": 5, "armaiolo": 4, "fabbricante di armi": 0, "carovana khajiit": 1},
    "daga": {"generale": 3, "contenitori": 5, "fabbro": 1, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
             "arcieria": 4,
             "abbigliamento": 5, "armaiolo": 4, "fabbricante di armi": 0, "carovana khajiit": 1},
    "armblade": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "stiletto": {"generale": 3, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "shiv": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
             "arcieria": 5,
             "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "kriss": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 4,
              "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "mazza": {"generale": 3, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 5,
              "abbigliamento": 5, "armaiolo": 4, "fabbricante di armi": 0, "carovana khajiit": 1},
    "mazzafrusta": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                    "arcieria": 5,
                    "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "kusarigama": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                   "arcieria": 5,
                   "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 2, "carovana khajiit": 1},
    "spadalunga": {"generale": 3, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                   "arcieria": 5,
                   "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "sciabola": {"generale": 3, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "katana": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
               "arcieria": 5,
               "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "fioretto": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "estoc": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 5,
              "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "bastone": {"generale": 1, "contenitori": 5, "fabbro": 4, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
                "arcieria": 5,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "martellodaguerra": {"generale": 4, "contenitori": 3, "fabbro": 5, "taverna": 5, "alchimista": 5,
                         "oggetti magici": 5, "arcieria": 5,
                         "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "bastoneconpesi": {"generale": 3, "contenitori": 4, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                       "arcieria": 5,
                       "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "asciaaduemani": {"generale": 4, "contenitori": 3, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                      "arcieria": 5,
                      "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "spadone": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                "arcieria": 5,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "zweihander": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                   "arcieria": 5,
                   "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "lancia": {"generale": 3, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
               "arcieria": 5,
               "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "picca": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 5,
              "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "beccodicorvo": {"generale": 4, "contenitori": 3, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                     "arcieria": 5,
                     "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "tonfa": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 5,
              "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "tridente": {"generale": 3, "contenitori": 5, "fabbro": 2, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "coltellodalancio": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5,
                         "oggetti magici": 5, "arcieria": 4,
                         "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "accettadalancio": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5,
                        "oggetti magici": 5, "arcieria": 4,
                        "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "shuriken": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 4,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "balestra": {"generale": 3, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 1,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "balestraaripetizione": {"generale": 4, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5,
                             "oggetti magici": 5, "arcieria": 1,
                             "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "arcocorto": {"generale": 2, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                  "arcieria": 1,
                  "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "arcolungo": {"generale": 2, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                  "arcieria": 1,
                  "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "arcocomposito": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                      "arcieria": 1,
                      "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "chukonu": {"generale": 4, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                "arcieria": 1,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 1, "carovana khajiit": 1},
    "accetta": {"generale": 2, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                "arcieria": 5,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "ascia": {"generale": 1, "contenitori": 5, "fabbro": 1, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 5,
              "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "armatura": {"generale": 3, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 4,
                 "abbigliamento": 5, "armaiolo": 0, "fabbricante di armi": 4, "carovana khajiit": 1},
    "armaturaanimale": {"generale": 5, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5,
                        "oggetti magici": 5, "arcieria": 5,
                        "abbigliamento": 5, "armaiolo": 4, "fabbricante di armi": 5, "carovana khajiit": 1},
    "scudo": {"generale": 4, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
              "arcieria": 4,
              "abbigliamento": 5, "armaiolo": 0, "fabbricante di armi": 4, "carovana khajiit": 1},
    "chainmail": {"generale": 4, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                  "arcieria": 4,
                  "abbigliamento": 5, "armaiolo": 1, "fabbricante di armi": 4, "carovana khajiit": 1},
    "veste": {"generale": 4, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 4, "oggetti magici": 1,
              "arcieria": 5,
              "abbigliamento": 2, "armaiolo": 2, "fabbricante di armi": 5, "carovana khajiit": 1},
    "anello": {"generale": 3, "contenitori": 5, "fabbro": 3, "taverna": 5, "alchimista": 4, "oggetti magici": 0,
               "arcieria": 5,
               "abbigliamento": 2, "armaiolo": 4, "fabbricante di armi": 5, "carovana khajiit": 1},
    "orecchino": {"generale": 3, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 4, "oggetti magici": 0,
                  "arcieria": 5,
                  "abbigliamento": 2, "armaiolo": 4, "fabbricante di armi": 5, "carovana khajiit": 1},
    "spilla": {"generale": 3, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 4, "oggetti magici": 1,
               "arcieria": 5,
               "abbigliamento": 2, "armaiolo": 4, "fabbricante di armi": 5, "carovana khajiit": 1},
    "fascia": {"generale": 3, "contenitori": 4, "fabbro": 5, "taverna": 5, "alchimista": 4, "oggetti magici": 1,
               "arcieria": 5,
               "abbigliamento": 2, "armaiolo": 4, "fabbricante di armi": 5, "carovana khajiit": 1},
    "mantello": {"generale": 3, "contenitori": 4, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                 "arcieria": 5,
                 "abbigliamento": 2, "armaiolo": 3, "fabbricante di armi": 5, "carovana khajiit": 1},
    "amuleto": {"generale": 3, "contenitori": 5, "fabbro": 2, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                "arcieria": 5,
                "abbigliamento": 5, "armaiolo": 4, "fabbricante di armi": 5, "carovana khajiit": 1},
    "cintura": {"generale": 2, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                "arcieria": 5,
                "abbigliamento": 2, "armaiolo": 3, "fabbricante di armi": 5, "carovana khajiit": 1},
    "pozione": {"generale": 2, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 0, "oggetti magici": 2,
                "arcieria": 3,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "faretra": {"generale": 3, "contenitori": 0, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                "arcieria": 1,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "reagente": {"generale": 2, "contenitori": 5, "fabbro": 5, "taverna": 4, "alchimista": 0, "oggetti magici": 3,
                 "arcieria": 5,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "borsa reagenti": {"generale": 3, "contenitori": 0, "fabbro": 5, "taverna": 5, "alchimista": 3, "oggetti magici": 4,
                       "arcieria": 5,
                       "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "freccia": {"generale": 1, "contenitori": 5, "fabbro": 1, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
                "arcieria": 0,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 0, "carovana khajiit": 1},
    "sacca": {"generale": 0, "contenitori": 0, "fabbro": 5, "taverna": 3, "alchimista": 5, "oggetti magici": 4,
              "arcieria": 4,
              "abbigliamento": 3, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "portapozioni": {"generale": 3, "contenitori": 1, "fabbro": 5, "taverna": 5, "alchimista": 3, "oggetti magici": 3,
                     "arcieria": 5,
                     "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "borsello": {"generale": 1, "contenitori": 0, "fabbro": 5, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 5,
                 "abbigliamento": 2, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "portapergamene": {"generale": 4, "contenitori": 1, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 3,
                       "arcieria": 5,
                       "abbigliamento": 3, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "lingotto": {"generale": 2, "contenitori": 5, "fabbro": 0, "taverna": 5, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 3,
                 "abbigliamento": 5, "armaiolo": 0, "fabbricante di armi": 0, "carovana khajiit": 1},
    "setalchemico": {"generale": 3, "contenitori": 5, "fabbro": 5, "taverna": 4, "alchimista": 2, "oggetti magici": 4,
                     "arcieria": 5,
                     "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "altareincantamento": {"generale": 4, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5,
                           "oggetti magici": 4, "arcieria": 5,
                           "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "bastonemagico": {"generale": 4, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                      "arcieria": 5,
                      "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "oggettivari": {"generale": 0, "contenitori": 5, "fabbro": 4, "taverna": 0, "alchimista": 5, "oggetti magici": 5,
                    "arcieria": 5,
                    "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "usabile": {"generale": 2, "contenitori": 5, "fabbro": 3, "taverna": 4, "alchimista": 5, "oggetti magici": 3,
                "arcieria": 5,
                "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "gemma": {"generale": 3, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
              "arcieria": 5,
              "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "vestiti": {"generale": 1, "contenitori": 5, "fabbro": 5, "taverna": 4, "alchimista": 5, "oggetti magici": 2,
                "arcieria": 5,
                "abbigliamento": 0, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "trappola": {"generale": 2, "contenitori": 5, "fabbro": 2, "taverna": 4, "alchimista": 5, "oggetti magici": 5,
                 "arcieria": 1,
                 "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 3, "carovana khajiit": 1},
    "pergamena": {"generale": 4, "contenitori": 4, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                  "arcieria": 5,
                  "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "libromagie": {"generale": 4, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                   "arcieria": 5,
                   "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "gemmaanima": {"generale": 4, "contenitori": 5, "fabbro": 5, "taverna": 5, "alchimista": 5, "oggetti magici": 1,
                   "arcieria": 5,
                   "abbigliamento": 5, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1},
    "pietrapreziosa": {"generale": 3, "contenitori": 5, "fabbro": 4, "taverna": 5, "alchimista": 5, "oggetti magici": 2,
                       "arcieria": 5,
                       "abbigliamento": 2, "armaiolo": 5, "fabbricante di armi": 5, "carovana khajiit": 1}

}

if da_esterno:
    importa_oggetti()
