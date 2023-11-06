import json
import os
import shutil

import Moduli.SharedData as Shared


def importa_db_skill():
    file_path = Shared.path_dati + "\listaskill.json"
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    numero = 0
    for riga in data:
        skill = {}
        skill["ID"] = data[riga][0]
        skill["NOME"] = data[riga][1]
        skill["DESCRIZIONE"] = data[riga][2]
        skill["PE"] = data[riga][3]
        skill["PE_USABILI"] = data[riga][4]
        skill["DETTAGLIO1"] = data[riga][5]
        skill["DETTAGLIO2"] = data[riga][6]
        skill["TIPO"] = data[riga][7]
        skill["EXTRA1"] = data[riga][8]
        if type(skill["ID"]) == int:
            Shared.skill_importate[str(skill["ID"])] = skill
        else:
            Shared.skill_importate["a" + str(numero)] = skill
            numero += 1

def aggiungi_skill_in_posizione(posizione_precedente,posizione_nuova,dati):
    post_dict = {}
    skill = {}
    skill["ID"] = int(dati[0])
    skill["NOME"] = dati[1]
    skill["DESCRIZIONE"] = dati[2]
    skill["PE"] = dati[3]
    skill["PE_USABILI"] = dati[4]
    skill["DETTAGLIO1"] = dati[5]
    skill["DETTAGLIO2"] = dati[6]
    skill["TIPO"] = dati[7]
    skill["EXTRA1"] = dati[8]
    valido = False
    for _ in Shared.skill_importate:
        if _ != str(posizione_precedente):
            post_dict[_] = Shared.skill_importate[_]
        else:
            post_dict[_] = Shared.skill_importate[_]
            post_dict[str(posizione_nuova)] = skill
            valido = True
    Shared.skill_importate = post_dict
    if not valido:
        return "Invalido"

def importa_skill_pg(nomepg):
    data_local = {}
    data_shared = {}
    file_path = Shared.path_PG_e_Unici + f"\{nomepg}skill.json"
    try:
        with open(file_path, 'r') as json_file:
            data_local = json.load(json_file)
    except:
        pass
    try:
        file_path = Shared.path_cartella_shared + f"\{nomepg}\skill\{nomepg}skill.json"
        with open(file_path, 'r') as json_file:
            data_shared = json.load(json_file)
    except:
        pass
    if len(data_local) > len(data_shared):
        data = data_local
    else:
        data = data_shared
    Shared.skill_sbloccate_pg = data

def esporta_db_skill():
    if "flagexportdbskill.json" in os.listdir(Shared.path_cartella_shared):
        pathfile = os.path.join(Shared.path_cartella_shared, "flagexportdbskill.json")
        with open(pathfile, 'r') as json_file:
            data = json.load(json_file)
        Shared.skill_importate = data
    salva_db_skill()


def salva_db_skill():
    numero = 0
    dict = {}
    for skill in Shared.skill_importate:
        numero += 1
        lista = []
        for item in Shared.skill_importate[skill]:
            lista.append(Shared.skill_importate[skill][item])
        dict[str(numero)] = lista

    numefile = Shared.path_dati + "\listaskill.json"
    with open(numefile, 'w') as json_file:
        json.dump(dict, json_file, indent=4)

def cerca_skill(ids="0"):
    try:
        if str(ids) in Shared.skill_importate.keys():
            return Shared.skill_importate[str(ids)]
        else:
            return Shared.skill_importate["9999999"]
    except:
        for item in Shared.skill_importate:
            if str(item) == "9999999":
                return Shared.skill_importate[item]
