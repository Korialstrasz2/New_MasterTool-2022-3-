import ast
import copy
import json
import os
import shutil

import Moduli.Logica.EquipAttore as EquipAttore
import Moduli.SharedData as Shared
from Moduli.Grafica import Popups_ScreenPGImportato, FinestraPrincipaleMain, Popups_Bottoni_Custom
from Moduli.Logica import Salvataggio


def importa_bottoni():
    nome_pg = Shared.pg_selezionato["nome_in_uso"]
    if nome_pg.startswith("__pg__"):
        pathcompleto_shared = Shared.path_cartella_shared + f"/{nome_pg}/bottoni/{nome_pg}bottoni.json"
        pathcompleto_dati = Shared.path_PG_e_Unici + f"/bottoni/{nome_pg}bottoni.json"
        recente = Popups_Bottoni_Custom.find_most_recent_file(pathcompleto_shared, pathcompleto_dati)
        if recente != "inesistenti":
            with open(recente, "r") as json_file:
                Shared.dati_bottoni = ast.literal_eval(json_file.read())
        else:
            Shared.dati_bottoni = Salvataggio.crea_bottoni_base()


def seleziona_attuale(nome_NPC_Attori):
    Shared.pg_selezionato = Shared.pg_png_inizializzati[nome_NPC_Attori]
    if Shared.entrato_in_finestra_pricipale:
        from Moduli.Grafica import FinestraPrincipalePG
        FinestraPrincipalePG.immagine_piccola()
    importa_bottoni()

def findAndImport(PGname):
    nomeperdb = "__pg__" + PGname
    crea_attore_attivo(nomeperdb)
    seleziona_attuale(nomeperdb)
    EquipAttore.equip_npc(nomeperdb)
    seleziona_attuale(nomeperdb)
    return nomeperdb

def assegna_npc(nome_attore, numeronpc):
    Shared.pg_png_inizializzati[nome_attore]["numero_npc"] = numeronpc
    Shared.npc_numeri_assegnati[int(numeronpc)] = Shared.pg_png_inizializzati[nome_attore]

def seleziona_npc_attuale(numeronpc):
    Shared.npc_selezionato = Shared.npc_numeri_assegnati[int(numeronpc)]
    Shared.numero_npc_attuale = numeronpc

def importa_tutti_NPC():
    for numeronpc in range(1, 11):
        nomenpc = crea_attore_attivo("__natura__Null")
        EquipAttore.equip_npc(nomenpc)
        assegna_npc(nomenpc, numeronpc)
    seleziona_npc_attuale(1)

def processa_pg_npc_importato(dati):
    Shared.pg_png_inizializzati[dati["nome_in_uso"]] = dati
    Shared.pg_selezionato = Shared.pg_png_inizializzati[Shared.pg_selezionato["nome_in_uso"]]
    EquipAttore.equip_npc(dati["nome_in_uso"])
    if int(dati["numero_npc"]) > 0:
        assegna_npc(dati["nome_in_uso"],dati["numero_npc"])


def crea_attore_attivo(nome_excel):
    def trova_nome(nome):
        if nome not in Shared.pg_png_inizializzati:
            return nome
        else:
            if nome[-4] == "_" and nome[-3] == "n":
                numero = int(nome[-2] + nome[-1]) / 100
                numero = "%0.2f" % (round(numero + 0.01, 2))
                nuovonome = nome[:-2] + str(numero)[2:4]
                return trova_nome(nuovonome)
            else:
                nome += "_n01"
                return trova_nome(nome)
    nome = trova_nome(nome_excel)
    Shared.pg_png_inizializzati[nome] = copy.deepcopy(Shared.pgnpc_importati_base[nome_excel])
    Shared.pg_png_inizializzati[nome]['nome_in_uso'] = nome
    if nome not in Shared.pg_png_creati_dal_pc:
        Shared.pg_png_creati_dal_pc.append(nome)
    return nome

def crea_attore_attivo_da_dati(da_importare,nuovo_nome):
    dati = copy.deepcopy(da_importare)
    nome_excel = "__umani__"+nuovo_nome + "lv" + str(da_importare["livello"])
    dati["nome_valore_excel"] = nome_excel
    dati["nomepg"] = nuovo_nome
    inizializza_pg_esterno(dati)
    nome_nuovo = crea_attore_attivo(nome_excel)
    EquipAttore.equip_npc(nome_nuovo)
    return nome_nuovo
def inizializza_pg_esterno(data):
    if data["nome_valore_excel"] not in Shared.pgnpc_importati_base:
        Shared.pgnpc_importati_base[data["nome_valore_excel"]] = copy.deepcopy(data)
    if data["nome_valore_excel"] not in Shared.pg_png_creati_dal_pc:
        Shared.pg_png_creati_dal_pc.append(data["nome_valore_excel"])

def json_piu_recente_no_skill(cartella):
    try:
        files = os.listdir(cartella)
        files_with_time = []
        for file in files:
            if file.endswith("json") and not file.endswith("skill.json"):
                file_path = os.path.join(cartella, file)
                file_time = os.path.getmtime(file_path)
                files_with_time.append((file_time, file))
        files_with_time.sort()
        files2 = [file for _, file in files_with_time]
        return files2[-1]
    except:
        return "no file"

def check_file_pg_e_npc_per_update():
#     prendi i nomi in uso dei pg e npc, controlla nelle cartelle che il file del pg sia il piu recente
#     se cosi non fosse, importalo
    for pgattivo in Shared.pg_png_inizializzati:
        file_path = os.path.join(Shared.path_cartella_shared, pgattivo)
        if pgattivo not in Shared.file_letti_per_pg:
            Shared.file_letti_per_pg[pgattivo] = []
        nomefiilerecente = json_piu_recente_no_skill(file_path)
        if nomefiilerecente not in Shared.file_letti_per_pg[pgattivo] and nomefiilerecente != "no file":
            Shared.file_letti_per_pg[pgattivo].append(nomefiilerecente)
            if len(Shared.file_letti_per_pg[pgattivo]) > 15:
                Shared.file_letti_per_pg[pgattivo] = Shared.file_letti_per_pg[pgattivo][10:]
            if nomefiilerecente != "no file":
                pathpg = os.path.join(file_path,nomefiilerecente)
                with open(pathpg, 'r') as json_file:
                    data = json.load(json_file)
                Popups_ScreenPGImportato.popup_check_differenze_pgnpc(data)