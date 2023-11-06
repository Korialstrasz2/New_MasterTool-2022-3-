import copy
import os
import threading
import json
from datetime import datetime, timedelta
import openpyxl
# from math import floor
# import PersonaggioPy
# import Popups
# from Oggetti import pathrisorse
# import shutil
# import copy
# import NPC
# import Oggetti
# from Popups import Zaino
# import client
# import server
import ast
from time import sleep
import Moduli.SharedData as Shared
from Moduli.Logica import Oggetti


def crea_dati_base_pg():
    file_path = Shared.path_dati + "\lista-valori-pg.json"
    to_import = []
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    for item in data:
        to_import.append(item)
    Shared.dati_base_pg = aggiungi_campi_nuovi(to_import)

def aggiungi_campi_nuovi(dati_base):
    dati_base.extend(Shared.campi_nuovi_valore_standard)
    nuova_lista = []
    for _ in dati_base:
        if _ not in nuova_lista:
            nuova_lista.append(_)
    return nuova_lista
def importa_dati_iniziali_pg_npc_e_oggetti():
    def addnpc(listanpc):
        for npc in listanpc:
            Shared.pgnpc_importati_base[npc] = {}
            for caratteristica in listanpc[npc]:
                Shared.pgnpc_importati_base[npc][caratteristica] = listanpc[npc][caratteristica]
    def addpg(nome,pg):
        nome = nome[:-5] # rimuove.json
        Shared.pgnpc_importati_base[nome] = {}
        for caratteristica in pg:
            Shared.pgnpc_importati_base[nome][caratteristica] = pg[caratteristica]


    timer_start2 = datetime.now()
    with open(Shared.path_dati + r"\NemicieNPC - Umani.json", 'r') as json_file:
        data = json.load(json_file)
        addnpc(data)
    with open(Shared.path_dati + r"\NemicieNPC - Nonmorti.json", 'r') as json_file:
        data = json.load(json_file)
        addnpc(data)
    with open(Shared.path_dati + r"\NemicieNPC - Natura.json", 'r') as json_file:
        data = json.load(json_file)
        addnpc(data)
    with open(Shared.path_dati + r"\NemicieNPC - Daedra_Automi.json", 'r') as json_file:
        data = json.load(json_file)
        addnpc(data)

    for file in os.listdir(Shared.path_PG_e_Unici):
        if file.startswith("__pg") and file.endswith("json") and not file.endswith("skill.json"):
            pathcompleto = Shared.path_PG_e_Unici + "\\" + file
            with open(pathcompleto, 'r') as json_file:
                data = json.load(json_file)
                addpg(file,data)
    Oggetti.importa_oggetti()



    print("Importazione in " + str(datetime.now() - timer_start2))

"""
è
PS C:\ Users\alexo\PycharmProjects\FPNew> cd filesfp                                                                                                                                                                                                                                                                   
PS C:\ Users\alexo\PycharmProjects\FPNew\filesfp> pyinstaller "main.py"   

mappa combat con elevazioni e caselle speciali
mappa del mondo con piu cose e oscurata

immagine omino completa con equip
solo armature. falle bene
mappa globale che cliccando sulle citta da negozi e mappa locale

dump di dettagli quali tempo, momento della giornata

creatore casuale quest..? con chatgpt??

Fix installer!

fai tanti nemici

aggiungi negozi e aggiorna descrizioni città

"""


grupposkill = {}

nomi_in_uso_norazza = []

with open(f"{Shared.path_dati}\dati_razze.txt", "r") as datirazze:
    Shared.dati_razze = ast.literal_eval(datirazze.read())
with open(f"{Shared.path_dati}\dati_incontri_casuali.txt", "r") as datiincontricasuali:
    Shared.dati_incontri_casuali = ast.literal_eval(datiincontricasuali.read())
with open(f"{Shared.path_dati}\\tipi-missione.txt", "r") as datitipimissione:
    Shared.tipi_missione = datitipimissione.read().split("\n")


for file in os.listdir(Shared.path_db_nomi):
    if file.endswith(".txt"):
        nome = file[:-4]

        with open(f"{Shared.path_db_nomi}\{nome}.txt", "r") as dati:
            rawlist = dati.read().split(",")
            newlist = []
            for item in rawlist:
                temp1 = item.replace("\t","").replace("\n","").replace(" ","")
                newlist.append(temp1)
            Shared.razze_nomi_npc[nome] = newlist


def cerca_skill(ids=0):
    try:
        if int(ids) in grupposkill.keys():
            for item in grupposkill:
                if str(item) == str(ids):
                    return grupposkill[item]
        else:
            for item in grupposkill:
                if str(item) == "9999999":
                    return grupposkill[item]
    except:
        for item in grupposkill:
            if str(item) == "9999999":
                return grupposkill[item]


def print_skill(nome_NPC_Attori):
    attore_attivo = eval(f"NPC.Attori.{str(nome_NPC_Attori)}")
    index_descrizioni = 1
    gruppotesti = list(sorted(attore_attivo["skill_attive"].keys()))
    while index_descrizioni < 60:
        for indicesk, skill in enumerate(gruppotesti):
            totalep = f"{cerca_skill(ids=str(skill))['NOME'].upper()}: {cerca_skill(ids=str(skill))['DESCRIZIONE']}"
            totale = f"{cerca_skill(ids=str(skill))['NOME'].upper()}: {cerca_skill(ids=str(skill))['DESCRIZIONE']} ({(str(skill))})"
            if index_descrizioni < 58:
                if len(totalep) > 120:
                    nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
                    attore_attivo[nome_descrizione] = totale[:60]
                    index_descrizioni += 1
                    nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
                    attore_attivo[nome_descrizione] = f"    {totale[60:120]}"
                    index_descrizioni += 1
                    nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
                    attore_attivo[nome_descrizione] = f"    {totale[120:]}"
                    index_descrizioni += 1
                elif len(totalep) > 60:
                    nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
                    attore_attivo[nome_descrizione] = totale[:60]
                    index_descrizioni += 1
                    nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
                    attore_attivo[nome_descrizione] = f"    {totale[60:]}"
                    index_descrizioni += 1
                else:
                    nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
                    attore_attivo[nome_descrizione] = totale
                    index_descrizioni += 1
        while index_descrizioni < 60:
            nome_descrizione = "descrizione_skill_" + str(index_descrizioni)
            attore_attivo[nome_descrizione] = "Vuoto"
            index_descrizioni += 1


def unpack_magie(nome_NPC_Attori):
    attore_attivo = eval(f"NPC.Attori.{str(nome_NPC_Attori)}")
    gruppomagie = list(sorted(attore_attivo["magie_attive"].keys()))
    indicemagia = 0
    for magia in range(1, 37):
        magianome = "magia_" + str(magia) + "_nome"
        magiadescrizone = "magia_" + str(magia) + "_descrizione"
        magiascuola = "magia_" + str(magia) + "_scuola"
        magiaformula = "magia_" + str(magia) + "_formula"
        magiacostoinmana = "magia_" + str(magia) + "_costo_in_mana"
        magiaraggio = "magia_" + str(magia) + "_raggio"
        if indicemagia < len(gruppomagie):
            attore_attivo[magianome] = f"{cerca_skill(ids=str(gruppomagie[indicemagia]))['NOME']}"
            attore_attivo[magiadescrizone] = f"{cerca_skill(ids=str(gruppomagie[indicemagia]))['DESCRIZIONE']}"
            attore_attivo[magiascuola] = f"{cerca_skill(ids=str(gruppomagie[indicemagia]))['TIPO']}"
            attore_attivo[magiaformula] = f"{cerca_skill(ids=str(gruppomagie[indicemagia]))['EXTRA1']}"
            attore_attivo[magiacostoinmana] = f"{cerca_skill(ids=str(gruppomagie[indicemagia]))['DETTAGLIO1']}"
            attore_attivo[magiaraggio] = f"{cerca_skill(ids=str(gruppomagie[indicemagia]))['DETTAGLIO2']}"
            indicemagia += 1
        else:
            attore_attivo[magianome] = "NO"
            attore_attivo[magiascuola] = "ALTERAZIONE"
            attore_attivo[magiadescrizone] = "NO"
            attore_attivo[magiacostoinmana] = "1 mana"
            attore_attivo[magiaraggio] = "NO"
            attore_attivo[magiaformula] = "M"


def formule_speciali(nome_NPC_Attori):
    attore_attivo = eval(f"NPC.Attori.{str(nome_NPC_Attori)}")
    for formula in attore_attivo["formule_speciali"].split("$$"):
        formula = formula.replace("–", "-")
        formula = formula.replace("£", "'")
        formula = formula.replace("“", '"')
        formula = formula.replace("”", '"')
        exec(formula)


def unpack_pasti(nome_NPC_Attori):
    attore_attivo = eval(f"NPC.Attori.{str(nome_NPC_Attori)}")
    for pasto in attore_attivo["pasti"].split("$$"):
        attore_attivo["colazione"] = pasto
        attore_attivo["pranzo"] = pasto
        attore_attivo["cena"] = pasto


def calcola_effetti(nome_NPC_Attori):
    attore_attivo = eval(f"NPC.Attori.{str(nome_NPC_Attori)}")
    for numeroeffetto in range(1, 32):
        codiceeff = eval(f"attore_attivo['codice_effetto_{numeroeffetto}']")
        codiceeff = codiceeff.replace("PersonaggioPy.Selezionato", "attore_attivo")
        if "+=" in codiceeff:
            if "$$" not in codiceeff:
                if codiceeff[:12] == "Personaggio.":
                    parte1 = codiceeff.replace("Personaggio.", "attore_attivo['")
                    parte1 = parte1.split("+=")[0].strip()
                    parte1 += "']"
                    parte2 = codiceeff.split("+=")[1].strip()
                    try:
                        exec(f"{parte1} += {parte2}")
                    except:
                        exec(f"{parte1[:-2]}_extra'] += {parte2}")
                        exec(f"{parte1[:-2]}_extra'] += {parte2}")
                else:
                    exec(codiceeff)
            else:
                for effetto in codiceeff.split("$$"):
                    exec(effetto)


class Temp:
    fileskill = None
    nameColumn = 1
    enetered = False
    showbarraricercazaino = False
    entered = False
    numerodump = 0
    txtdariprendere = []
    clickimportadump = 0
    castellashared = ""
    negoziocliccato = ""
    datinegozioestratto = []
    esporta_nuova_skill = []


prefissi_per_pgnpc = ["__pg__", "__uman", "__nonm", "__natu", "__daed"]

def trova_pgnpc(ids="", nome="", livello=False):
    risultati = []
    if len(ids) > 0:
        for item in Shared.pgnpc_importati_base:
            if str(item) == ids:
                return Shared.pgnpc_importati_base[item]

    else:
        try:
            for item in Shared.pgnpc_importati_base:
                if type(Shared.pgnpc_importati_base[item]["nomepg"]) == str and nome.lower() in Shared.pgnpc_importati_base[item]["nomepg"].lower():
                    if livello:
                        if int(livello) == int(Shared.pgnpc_importati_base[item]["livello"]):
                            risultati.append(Shared.pgnpc_importati_base[item])
                    else:
                        risultati.append(Shared.pgnpc_importati_base[item])
        except:
            pass
    if len(risultati) == 0:
        for item in Shared.pgnpc_importati_base:
            if item == "__umani__Bandito_lv_1":
                risultati.append(Shared.pgnpc_importati_base[item])
                return risultati

    return risultati if (len(risultati) > 1 and len(risultati) < 75) else risultati[0]

