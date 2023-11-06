from datetime import datetime
from math import floor
import Moduli.SharedData as Shared
import Moduli.Logica.Oggetti as Oggetti
from Moduli.Grafica import Popups_Notifiche
from Moduli.Logica import GestioneSkill

class FormuleTemp:
    formule = []


def print_skill(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    index_descrizioni = 1
    gruppotesti = list(sorted(attore_attivo["skill_attive"].keys()))
    while index_descrizioni < 60:
        for indicesk, skill in enumerate(gruppotesti):
            totalep = f"{GestioneSkill.cerca_skill(ids=str(skill))['NOME'].upper()}: {GestioneSkill.cerca_skill(ids=str(skill))['DESCRIZIONE']}"
            totale = f"{GestioneSkill.cerca_skill(ids=str(skill))['NOME'].upper()}: {GestioneSkill.cerca_skill(ids=str(skill))['DESCRIZIONE']} ({(str(skill))})"
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
def fixa_bonus_con_effetti(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    lista = {
            "Armi \nLunghe": ["Shared.pg_selezionato['atk_skill_lunghe'] += ", "atk_skill_lunghe"],
            "Armi \nMedie\n(lunghezza)": ["Shared.pg_selezionato['atk_skill_medie1'] += ", "atk_skill_medie1"],
            "Armi \nCorte": ["Shared.pg_selezionato['atk_skill_corte'] += ", "atk_skill_corte"],
            "Armi \nPotenti": ["Shared.pg_selezionato['atk_skill_potenti'] += ", "atk_skill_potenti"],
            "Armi \nMedie\n(potenza)": ["Shared.pg_selezionato['atk_skill_medie2'] += ", "atk_skill_medie2"],
            "Armi \nPrecise": ["Shared.pg_selezionato['atk_skill_precise'] += ", "atk_skill_precise"],
            "Armi \nTaglio": ["Shared.pg_selezionato['atk_skill_taglio'] += ", "atk_skill_taglio"],
            "Armi \nContundenti": ["Shared.pg_selezionato['atk_skill_contundente'] += ", "atk_skill_contundente"],
            "Armi \nPerforanti": ["Shared.pg_selezionato['atk_skill_perforante'] += ", "atk_skill_perforante"],
            "Attacco \nMani Nude": ["Shared.pg_selezionato['atk_skill_maninude'] += ", "atk_skill_maninude"],
            "Tier \nMani Nude": ["Shared.pg_selezionato['tier_skill_maninude'] += ", "tier_skill_maninude"],
            "Set Leggeri": ["Shared.pg_selezionato['def_skill_leggera'] += ", "def_skill_leggera"],
            "Set Pesanti": ["Shared.pg_selezionato['def_skill_pesante'] += ", "def_skill_pesante"],
            "Senza Armatura": ["Shared.pg_selezionato['def_skill_noarmatura'] += ", "def_skill_noarmatura"],
            "Scudi": ["Shared.pg_selezionato['def_skill_scudo'] += ", "def_skill_scudo"],
            "RD Fisica": ["Shared.pg_selezionato['rd_fis_base'] += ", "rd_fis_base"],
            "Res Contundente": ["Shared.pg_selezionato['res_contundente_base'] += ", "res_contundente_base"],
            "Res Taglio": ["Shared.pg_selezionato['res_taglio_base'] += ", "res_taglio_base"],
            "Res Perforante": ["Shared.pg_selezionato['res_perforante_base'] += ", "res_perforante_base"],
            "Res Fuoco": ["Shared.pg_selezionato['res_fuoco_base'] += ", "res_fuoco_base"],
            "Res Gelo": ["Shared.pg_selezionato['res_gelo_base'] += ", "res_gelo_base"],
            "Res Elettro": ["Shared.pg_selezionato['res_elettro_base'] += ", "res_elettro_base"],
            "RD Fuoco": ["Shared.pg_selezionato['rd_fuoco_base'] += ", "rd_fuoco_base"],
            "RD Gelo": ["Shared.pg_selezionato['rd_gelo_base'] += ", "rd_gelo_base"],
            "RD Elettro": ["Shared.pg_selezionato['rd_elettro_base'] += ", "rd_elettro_base"]

    }
    for item in lista:
        if item in attore_attivo and str(attore_attivo[lista[item][1]]) != "0":
            for numero_effetto in range(1,32):
                if lista[item][1] in attore_attivo[f"codice_effetto_{numero_effetto}"]:
                    break
                if attore_attivo[f"nome_effetto_{numero_effetto}"] == ("Vuoto"
                   "") and attore_attivo[f"descrizione_effetto_{numero_effetto}"] == ("Vuoto"
                   "") and attore_attivo[f"codice_effetto_{numero_effetto}"] == ("Vuoto"):
                    attore_attivo[f"nome_effetto_{numero_effetto}"] = item
                    attore_attivo[f"descrizione_effetto_{numero_effetto}"] = "Creato Automaticamente"
                    valore = str(attore_attivo[lista[item][1]])
                    codice = lista[item][0] + valore
                    attore_attivo[f"codice_effetto_{numero_effetto}"] = codice
                    break
        attore_attivo[lista[item][1]] = 0
        if lista[item][1] in Shared.dati_base_pg:
            Shared.dati_base_pg.remove(lista[item][1])
def equip_npc(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]

    """
    fix fatta per gestire i bonus usando gli effetti invece di salvare tutto direttamente nel PG.
    In successive iterazioni da gestire direttamete tramite effetti al pari di atk, def e così via.
    """
    fixa_bonus_con_effetti(nome_NPC_Attori)
    azzera_attore_attivo(nome_NPC_Attori)
    for extra_value in Shared.campi_nuovi_valore_standard:
        if extra_value not in attore_attivo:
            attore_attivo[extra_value] = Shared.campi_nuovi_valore_standard[extra_value]
    equip_oggetti(nome_NPC_Attori)
    equip_arma1(nome_NPC_Attori)
    equip_armatura(nome_NPC_Attori)
    equip_scudo(nome_NPC_Attori)
    equip_chainmail(nome_NPC_Attori)
    equip_veste(nome_NPC_Attori)
    calcola_carico(nome_NPC_Attori)
    calcola_effetti(nome_NPC_Attori)
    calcola_razze_caratteristiche(nome_NPC_Attori)
    formule_speciali(nome_NPC_Attori)
    formule_normali(nome_NPC_Attori)
    calcola_peso(nome_NPC_Attori)
    unpack_skill(nome_NPC_Attori)
    unpack_faretra(nome_NPC_Attori)
    unpack_alchimia(nome_NPC_Attori)
    unpack_pasti(nome_NPC_Attori)
    unpack_magie(nome_NPC_Attori)
    calcolo_pa(nome_NPC_Attori)
    calcola_formule_extra(nome_NPC_Attori)
    return attore_attivo

def calcolo_pa(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    if int(attore_attivo["forza_tot"]) > 10:
        mod = int(attore_attivo["forza_tot"]) - 10
        for bonus in range(mod):
            if attore_attivo["carico"] >= 1:
                attore_attivo["carico"] -= 1

    if int(attore_attivo["pa_tot"]) - int(attore_attivo["malus_pa"]) < 4:
        attore_attivo["malus_pa"] -= 4 - (int(attore_attivo["pa_tot"]) - int(attore_attivo["malus_pa"]))

    attore_attivo["carico"] = floor(int(attore_attivo["carico"]) / attore_attivo["mod_carico"]) if (
            floor(int(attore_attivo["carico"]) / attore_attivo["mod_carico"]) > 0) else 0


def azzera_attore_attivo(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["forza_bonus_extra"] = 0
    attore_attivo["resistenza_bonus_extra"] = 0
    attore_attivo["velocita_bonus_extra"] = 0
    attore_attivo["agilita_bonus_extra"] = 0
    attore_attivo["intelligenza_bonus_extra"] = 0
    attore_attivo["concentrazione_bonus_extra"] = 0
    attore_attivo["personalita_bonus_extra"] = 0
    attore_attivo["saggezza_bonus_extra"] = 0
    attore_attivo["fortuna_bonus_extra"] = 0
    attore_attivo["pf_item"] = 0
    attore_attivo["pf_extra"] = 0
    attore_attivo["pf_temp"] = 0
    attore_attivo["mana_item"] = 0
    attore_attivo["mana_extra"] = 0
    attore_attivo["mana_temp"] = 0
    attore_attivo["energia_item"] = 0
    attore_attivo["energia_extra"] = 0
    attore_attivo["energia_temp"] = 0
    attore_attivo["malus_pa_armatura"] = 0
    attore_attivo["pa_item"] = 0
    attore_attivo["pa_extra"] = 0
    attore_attivo["pa_temp"] = 0
    attore_attivo["attacco_arma"] = 0
    attore_attivo["attacco_item"] = 0
    attore_attivo["attacco_extra"] = 0
    attore_attivo["attacco_temp"] = 0
    attore_attivo["difesa_armatura"] = 0
    attore_attivo["difesa_item"] = 0
    attore_attivo["difesa_extra"] = 0
    attore_attivo["difesa_temp"] = 0
    attore_attivo["potere_item"] = 0
    attore_attivo["potere_extra"] = 0
    attore_attivo["barr_fis_item"] = 0
    attore_attivo["barr_fis_extra"] = 0
    attore_attivo["barr_mag_item"] = 0
    attore_attivo["barr_mag_extra"] = 0
    attore_attivo["sifone_di_mana_extra"] = 0
    attore_attivo["tier_arma"] = 0
    attore_attivo["tier_temp"] = 0
    attore_attivo["tier_item"] = 0
    attore_attivo["tier_extra"] = 0
    attore_attivo["rd_fis_extra"] = 0
    attore_attivo["res_contundente_extra"] = 0
    attore_attivo["res_taglio_extra"] = 0
    attore_attivo["res_perforante_extra"] = 0
    attore_attivo["res_fuoco_extra"] = 0
    attore_attivo["res_gelo_extra"] = 0
    attore_attivo["res_elettro_extra"] = 0
    attore_attivo["rd_fuoco_extra"] = 0
    attore_attivo["rd_gelo_extra"] = 0
    attore_attivo["rd_elettro_extra"] = 0
    attore_attivo["modificatore_generale_extra"] = 0
    attore_attivo["stanchezza_extra"] = 0
    attore_attivo["papermanaordine_extra"] = 0
    attore_attivo["enpermanaordine_extra"] = 0
    attore_attivo["papermanacaos_extra"] = 0
    attore_attivo["enpermanacaos_extra"] = 0
    attore_attivo["sconto_mana_per_potere_extra"] = 0
    attore_attivo["sconto_pa_per_potere_extra"] = 0
    attore_attivo["mod_carico"] = 3


def equip_oggetti(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    equipaggiabili = ["equip_anello_1", "equip_anello_2", "equip_anello_3", "equip_anello_4", "equip_anello_5",
                      "equip_anello_6", "equip_anello_7", "equip_anello_8",
                      "equip_orecchino_1", "equip_orecchino_2", "equip_orecchino_3", "equip_orecchino_4",
                      "equip_orecchino_5", "equip_orecchino_6",
                      "equip_spilla", "equip_fascia", "equip_mantello", "equip_amuleto", "equip_cintura"]

    for item in equipaggiabili:
        nomeequip = "eq_" + item
        attore_attivo[nomeequip] = Oggetti.trova_oggetto(ids=attore_attivo[item])
        if attore_attivo[nomeequip]["TIPO1"] == item.split('_')[1]:
            for effetto in range(1, 8):
                nomeeffetto = "EFFETTO" + str(effetto)
                if attore_attivo[nomeequip][nomeeffetto] is not None and attore_attivo[nomeequip][nomeeffetto][:
                11] == "Personaggio":

                    if (len(attore_attivo[nomeequip][nomeeffetto].split('Personaggio.'))) == 2:
                        dacambiarepre = attore_attivo[nomeequip][nomeeffetto].split('Personaggio.')[1]
                        dacambiare = dacambiarepre.split("+=")[0].strip()
                        valore = dacambiarepre.split("+=")[1].strip()
                        attore_attivo[dacambiare] = int(attore_attivo[dacambiare]) + int(valore)

                    elif (len(attore_attivo[nomeequip][nomeeffetto].split('Personaggio.'))) == 3:
                        extrabase = attore_attivo[nomeequip][nomeeffetto].split('Personaggio.')[2]
                        extra = eval(f"Shared.pg_selezionato['{extrabase}']")
                        dacambiarepre = attore_attivo[nomeequip][nomeeffetto].split('Personaggio.')[1]
                        dacambiare = dacambiarepre.split("+=")[0].strip()
                        valore = extra
                        attore_attivo[dacambiare] = int(attore_attivo[dacambiare]) + int(valore)
                elif attore_attivo[nomeequip][nomeeffetto] is not None and attore_attivo[nomeequip][
                                                                                   nomeeffetto][:
                                                                               18] == "Resistenze Fisiche":
                    dacambiare = attore_attivo[nomeequip][nomeeffetto].split("+")[1].strip()
                    attore_attivo["res_contundente_extra"] = int(attore_attivo["res_contundente_extra"]) + int(
                        dacambiare)
                    attore_attivo["res_perforante_extra"] = int(attore_attivo["res_perforante_extra"]) + int(
                        dacambiare)
                    attore_attivo["res_taglio_extra"] = int(attore_attivo["res_taglio_extra"]) + int(
                        dacambiare)
        else:
            Popups_Notifiche.noeq(stringa=attore_attivo[nomeequip]["NOME"])

def equip_arma1(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["eq_arma_1"] = Oggetti.trova_oggetto(ids=attore_attivo["id_arma_1"])
    if attore_attivo["eq_arma_1"]["TIPO1"] in Shared.categorie_armi:
        attore_attivo["bonus_arma"] = Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][2]
        if len(str(Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][3])) > 2:
            stringa = str(Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][3])
            exec(stringa)
        attore_attivo["attacco_arma"] = attore_attivo["eq_arma_1"]["EFFETTO1"]
        attore_attivo["tier_arma"] = attore_attivo["eq_arma_1"]["EFFETTO2"]
        attore_attivo["pa_arma"] = attore_attivo["eq_arma_1"]["EFFETTO3"]
        for effetto in range(4, 8):
            nomeeffetto = "EFFETTO" + str(effetto)
            if attore_attivo["eq_arma_1"][nomeeffetto] is not None and attore_attivo["eq_arma_1"][nomeeffetto][:
            11] == "Personaggio":
                dacambiarepre = attore_attivo["eq_arma_1"][nomeeffetto].split('Personaggio.')[1]
                dacambiare = dacambiarepre.split("+=")[0].strip()
                attore_attivo[dacambiare] = int(attore_attivo[dacambiare]) + int(dacambiarepre.split("+=")[1].strip())
            elif attore_attivo["eq_arma_1"][nomeeffetto] is not None and attore_attivo["eq_arma_1"][nomeeffetto][:
            18] == "Resistenze Fisiche":
                dacambiare = attore_attivo["eq_arma_1"][nomeeffetto].split("+")[1].strip()
                attore_attivo["res_contundente_extra"] = int(attore_attivo["res_contundente_extra"]) + int(dacambiare)
                attore_attivo["res_perforante_extra"] = int(attore_attivo["res_perforante_extra"]) + int(
                    dacambiare)
                attore_attivo["res_taglio_extra"] = int(attore_attivo["res_taglio_extra"]) + int(
                    dacambiare)
    else:
        Popups_Notifiche.noarma(stringa=attore_attivo["eq_arma_1"]["NOME"])

def equip_armatura(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["eq_armatura"] = Oggetti.trova_oggetto(ids=attore_attivo["id_armatura"])
    if attore_attivo["eq_armatura"]["TIPO1"] == "armatura" or attore_attivo["eq_armatura"][
        "TIPO1"] == "armaturaanimale":
        attore_attivo["difesa_armatura"] = attore_attivo["eq_armatura"]["EFFETTO1"]
        attore_attivo["malus_pa_armatura"] = attore_attivo["eq_armatura"]["EFFETTO2"]
        for effetto in range(3, 8):
            nomeeffetto = "EFFETTO" + str(effetto)
            if attore_attivo["eq_armatura"][nomeeffetto] is not None and attore_attivo["eq_armatura"][nomeeffetto][:
            11] == "Personaggio":
                dacambiarepre = attore_attivo["eq_armatura"][nomeeffetto].split('Personaggio.')[1]
                dacambiare = dacambiarepre.split("+=")[0].strip()
                attore_attivo[dacambiare] = int(attore_attivo[dacambiare]) + int(dacambiarepre.split("+=")[1].strip())
            elif attore_attivo["eq_armatura"][nomeeffetto] is not None and attore_attivo["eq_armatura"][nomeeffetto][:
            18] == "Resistenze Fisiche":
                dacambiare = attore_attivo["eq_armatura"][nomeeffetto].split("+")[1].strip()
                attore_attivo["res_contundente_extra"] = int(attore_attivo["res_contundente_extra"]) + int(dacambiare)
                attore_attivo["res_perforante_extra"] = int(attore_attivo["res_perforante_extra"]) + int(
                    dacambiare)
                attore_attivo["res_taglio_extra"] = int(attore_attivo["res_taglio_extra"]) + int(
                    dacambiare)

    else:
        Popups_Notifiche.noarmatura(stringa=attore_attivo["eq_armatura"]["NOME"])

def equip_scudo(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["eq_scudo"] = Oggetti.trova_oggetto(ids=attore_attivo["id_scudo"])
    if attore_attivo["eq_scudo"]["TIPO1"] == "scudo":
        attore_attivo["difesa_scudo"] = attore_attivo["eq_scudo"]["EFFETTO1"]
        attore_attivo["malus_pa_scudo"] = attore_attivo["eq_scudo"]["EFFETTO2"]
        for effetto in range(3, 8):
            nomeeffetto = "EFFETTO" + str(effetto)
            if attore_attivo["eq_scudo"][nomeeffetto] is not None and attore_attivo["eq_scudo"][nomeeffetto][:
            11] == "Personaggio":
                dacambiarepre = attore_attivo["eq_scudo"][nomeeffetto].split('Personaggio.')[1]
                dacambiare = dacambiarepre.split("+=")[0].strip()
                attore_attivo[dacambiare] = int(attore_attivo[dacambiare]) + int(dacambiarepre.split("+=")[1].strip())
            elif attore_attivo["eq_scudo"][nomeeffetto] is not None and attore_attivo["eq_scudo"][nomeeffetto][:
            18] == "Resistenze Fisiche":
                dacambiare = attore_attivo["eq_scudo"][nomeeffetto].split("+")[1].strip()
                attore_attivo["res_contundente_extra"] = int(attore_attivo["res_contundente_extra"]) + int(dacambiare)
                attore_attivo["res_perforante_extra"] = int(attore_attivo["res_perforante_extra"]) + int(
                    dacambiare)
                attore_attivo["res_taglio_extra"] = int(attore_attivo["res_taglio_extra"]) + int(
                    dacambiare)
    else:
        Popups_Notifiche.noscudo(stringa=attore_attivo["eq_scudo"]["NOME"])

def equip_chainmail(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["eq_chainmail"] = Oggetti.trova_oggetto(ids=attore_attivo["id_chainmail"])
    if attore_attivo["eq_chainmail"]["TIPO1"] == "chainmail":
        attore_attivo["difesa_chainmail"] = attore_attivo["eq_chainmail"]["EFFETTO1"]
        attore_attivo["malus_pa_chainmail"] = attore_attivo["eq_chainmail"]["EFFETTO2"]
        for effetto in range(3, 8):
            nomeeffetto = "EFFETTO" + str(effetto)
            if attore_attivo["eq_chainmail"][nomeeffetto] is not None and attore_attivo["eq_chainmail"][nomeeffetto][:
            11] == "Personaggio":
                dacambiarepre = attore_attivo["eq_chainmail"][nomeeffetto].split('Personaggio.')[1]
                dacambiare = dacambiarepre.split("+=")[0].strip()
                attore_attivo[dacambiare] = int(attore_attivo[dacambiare]) + int(dacambiarepre.split("+=")[1].strip())
            elif attore_attivo["eq_chainmail"][nomeeffetto] is not None and attore_attivo["eq_chainmail"][nomeeffetto][:
            18] == "Resistenze Fisiche":
                dacambiare = attore_attivo["eq_chainmail"][nomeeffetto].split("+")[1].strip()
                attore_attivo["res_contundente_extra"] = int(attore_attivo["res_contundente_extra"]) + int(dacambiare)
                attore_attivo["res_perforante_extra"] = int(attore_attivo["res_perforante_extra"]) + int(
                    dacambiare)
                attore_attivo["res_taglio_extra"] = int(attore_attivo["res_taglio_extra"]) + int(
                    dacambiare)
    else:
        Popups_Notifiche.nochainmail(stringa=attore_attivo["eq_chainmail"]["NOME"])

def equip_veste(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["eq_veste"] = Oggetti.trova_oggetto(ids=attore_attivo["id_veste"])
    if attore_attivo["eq_veste"]["TIPO1"] == "veste":
        attore_attivo["difesa_veste"] = attore_attivo["eq_veste"]["EFFETTO1"]
        attore_attivo["malus_pa_veste"] = attore_attivo["eq_veste"]["EFFETTO2"]
        for effetto in range(3, 8):
            nomeeffetto = "EFFETTO" + str(effetto)
            if attore_attivo["eq_veste"][nomeeffetto] is not None and attore_attivo["eq_veste"][nomeeffetto][:
            11] == "Personaggio":
                dacambiarepre = attore_attivo["eq_veste"][nomeeffetto].split('Personaggio.')[1]
                dacambiare = dacambiarepre.split("+=")[0].strip()
                attore_attivo[dacambiare] = float(attore_attivo[dacambiare]) + float(
                    dacambiarepre.split("+=")[1].strip().replace(",", "."))
            elif attore_attivo["eq_veste"][nomeeffetto] is not None and attore_attivo["eq_veste"][nomeeffetto][:
            18] == "Resistenze Fisiche":
                dacambiare = attore_attivo["eq_veste"][nomeeffetto].split("+")[1].strip()
                attore_attivo["res_contundente_extra"] = int(attore_attivo["res_contundente_extra"]) + int(dacambiare)
                attore_attivo["res_perforante_extra"] = int(attore_attivo["res_perforante_extra"]) + int(
                    dacambiare)
                attore_attivo["res_taglio_extra"] = int(attore_attivo["res_taglio_extra"]) + int(
                    dacambiare)
    else:
        Popups_Notifiche.noveste(stringa=attore_attivo["eq_veste"]["NOME"])

def calcola_carico(nome_NPC_Attori):
    """Peso in base al valore slot degli oggetti. 1 = leggero(anello) 4 = medio(spada lunga, set leggero) 6(armi lunghe)
    8(set pesante) il resto ha tutto 4 il moltiplicatore per il carico e 3"""
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["carico"] = 0
    ignora = ["Vuoto", "", " ", "None", None, "Slot1", "0", 0]
    for item in range(1, 41):
        nomeslot = str("zaino_slot_") + str(item)
        if attore_attivo[nomeslot] not in ignora:
            if item > int(attore_attivo["slot_zaino_magici"]):
                if str(attore_attivo[nomeslot]).startswith("id:"):
                    oggetto =Oggetti.trova_oggetto(str(attore_attivo[nomeslot]).split("id:")[1])
                    attore_attivo["carico"] += int(oggetto["SLOT"])
                else:
                    attore_attivo["carico"] += 3

def formule_normali(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    formule = {}
    attore_attivo["sifone_di_mana"] = int(attore_attivo["sifone_di_mana_extra"]) + int(
        attore_attivo["sifone_di_mana_base"])
    attore_attivo["rd_fis"] = int(attore_attivo["rd_fis_extra"]) + int(attore_attivo["rd_fis_base"])
    attore_attivo["res_contundente"] = int(attore_attivo["res_contundente_extra"]) + int(
        attore_attivo["res_contundente_base"])
    attore_attivo["res_taglio"] = int(attore_attivo["res_taglio_extra"]) + int(attore_attivo["res_taglio_base"])
    attore_attivo["res_perforante"] = int(attore_attivo["res_perforante_extra"]) + int(
        attore_attivo["res_perforante_base"])
    attore_attivo["res_fuoco"] = int(attore_attivo["res_fuoco_extra"]) + int(attore_attivo["res_fuoco_base"])
    attore_attivo["res_gelo"] = int(attore_attivo["res_gelo_extra"]) + int(attore_attivo["res_gelo_base"])
    attore_attivo["res_elettro"] = int(attore_attivo["res_elettro_extra"]) + int(attore_attivo["res_elettro_base"])
    attore_attivo["rd_fuoco"] = int(attore_attivo["rd_fuoco_extra"]) + int(attore_attivo["rd_fuoco_base"])
    attore_attivo["rd_gelo"] = int(attore_attivo["rd_gelo_extra"]) + int(attore_attivo["rd_gelo_base"])
    attore_attivo["rd_elettro"] = int(attore_attivo["rd_elettro_extra"]) + int(attore_attivo["rd_elettro_base"])
    attore_attivo["modificatore_generale"] = int(attore_attivo["modificatore_generale_extra"]) + int(
        attore_attivo["modificatore_generale_base"])
    attore_attivo["stanchezza"] = int(attore_attivo["stanchezza_extra"]) + int(attore_attivo["stanchezza_base"])
    attore_attivo["enpermanaordine"] = float(attore_attivo["enpermanaordine_extra"]) + float(
        attore_attivo["enpermanaordine_base"])
    attore_attivo["papermanaordine"] = float(attore_attivo["papermanaordine_extra"]) + float(
        attore_attivo["papermanaordine_base"])
    attore_attivo["enpermanacaos"] = float(attore_attivo["enpermanacaos_extra"]) + float(
        attore_attivo["enpermanacaos_base"])
    attore_attivo["papermanacaos"] = float(attore_attivo["papermanacaos_extra"]) + float(
        attore_attivo["papermanacaos_base"])
    attore_attivo["sconto_pa_per_potere"] = float(attore_attivo["sconto_pa_per_potere_extra"])

    attore_attivo["sconto_mana_per_potere"] = float(attore_attivo["sconto_mana_per_potere_extra"])

    attore_attivo["tier_tot"] = int(attore_attivo["tier_arma"]) + int(attore_attivo["tier_temp"]) + int(
        attore_attivo["tier_base"]) + \
                                int(attore_attivo["tier_item"]) + int(attore_attivo["tier_extra"])

    for formula in attore_attivo.keys():
        if formula.startswith("formula"):
            caratt_totale = formula.replace("formula_", "")
            formule[caratt_totale] = attore_attivo[formula]

    for item in formule:
        formula = formule[item].replace("–", "-")
        formula = formula.replace("pg_selezionato", "attore_attivo")
        formula = formula.replace("£", "'")
        formula = formula.replace("“", '"')
        formula = formula.replace("”", '"')
        formula = formula.replace(",", '.')
        formula = formula.replace("attacco_arma_attuale", "attacco_arma")
        try:
            attore_attivo[item] = int(eval(formula))
        except:
            print(f"formula scoppiata: {item}")
            attore_attivo[item] = eval(formula)


    if attore_attivo["eq_arma_1"]["TIPO3"] == "taglio":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_taglio"])
    elif attore_attivo["eq_arma_1"]["TIPO3"] == "contundente":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_contundente"])
    elif attore_attivo["eq_arma_1"]["TIPO3"] == "perforante":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_perforante"])
    if Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][0] == "corta":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_corte"])
    elif Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][0] == "media":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_medie1"])
    elif Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][0] == "lunga":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_lunghe"])
    elif Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][0] == "maninude":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_maninude"])
        attore_attivo["tier_tot"] += int(attore_attivo["tier_skill_maninude"])
    if Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][1] == "potente":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_potenti"])
    elif Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][1] == "media":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_medie2"])
    elif Shared.categorie_armi[attore_attivo["eq_arma_1"]["TIPO1"]][1] == "precisa":
        attore_attivo["attacco_tot"] += int(attore_attivo["atk_skill_precise"])
    if attore_attivo["eq_armatura"]["TIPO2"] in Shared.armature_leggere:
        attore_attivo["difesa_tot"] += int(attore_attivo["def_skill_leggera"])
    elif attore_attivo["eq_armatura"]["TIPO2"] in Shared.armature_pesanti:
        attore_attivo["difesa_tot"] += int(attore_attivo["def_skill_pesante"])
    elif attore_attivo["eq_armatura"]["TIPO2"] == "assente":
        attore_attivo["difesa_tot"] += int(attore_attivo["def_skill_noarmatura"])
    if attore_attivo["eq_scudo"]["TIPO2"] != "assente":
        attore_attivo["difesa_tot"] += int(attore_attivo["def_skill_scudo"])
    attore_attivo["difesa_tot"] += int(attore_attivo["difesa_veste"]) + int(attore_attivo["difesa_scudo"]) + +int(attore_attivo["difesa_chainmail"])


def unpack_faretra(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    frecce = []
    gruppofaretra = ['faretra_1',
                     'faretra_2', 'faretra_3', 'faretra_4', 'faretra_5', 'faretra_6', 'faretra_7', 'faretra_8',
                     'faretra_9', 'faretra_10', 'faretra_11', 'faretra_12', 'faretra_13', 'faretra_14', 'faretra_15',
                     'faretra_16', 'faretra_17', 'faretra_18', 'faretra_19', 'faretra_20', 'faretra_21', 'faretra_22',
                     'faretra_23', 'faretra_24', 'faretra_25', 'faretra_26', 'faretra_27', 'faretra_28',
                     'faretra_29', 'faretra_30']
    for frecciaspacchetta in attore_attivo["faretra"].split("$$"):
        frecce.append(frecciaspacchetta)
    for freccia in gruppofaretra:
        attore_attivo[freccia] = "NO"
    for numero, freccia in enumerate(frecce):
        numerofreccia = "faretra_" + str(numero + 1)
        attore_attivo[numerofreccia] = str(freccia)

def unpack_skill(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["skill_attive"] = {}
    attore_attivo["magie_attive"] = {}
    lista_scuole = ['ALTERAZIONE', 'RECUPERO', 'ILLUSIONE', 'NEGROMANZIA', 'EVOCAZIONE', 'MALEDIZIONI', 'DISTRUZIONE',
                    'MISTICISMO']

    for indice in sorted(attore_attivo["skill_sbloccate"].split("$$")):
        if indice in Shared.skill_importate.keys():
            try:
                if Shared.skill_importate[str(indice)]["TIPO"] not in lista_scuole:
                    attore_attivo["skill_attive"][str(indice)] = Shared.skill_importate[str(indice)]
                else:
                    attore_attivo["magie_attive"][str(indice)] = Shared.skill_importate[str(indice)]
            except:
                if int(attore_attivo["skill_sbloccate"]) == 0:
                    attore_attivo["skill_attive"]["9999999"] = Shared.skill_importate["9999999"]
        print_skill(nome_NPC_Attori)

def calcola_effetti(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    Shared.attore_attivo = attore_attivo
    def sostituisci_ed_esegui(stringa):
        attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
        if stringa[:12] == "Personaggio.":
            parte1 = stringa.replace("Personaggio.", "attore_attivo['")
            parte1 = parte1.split("+=")[0].strip()
            parte1 += "']"
            parte2 = stringa.split("+=")[1].strip()
            try:
                exec(f"{parte1} += {parte2}")
            except:
                exec(f"{parte1[:-2]}_extra'] += {parte2}")
                exec(f"{parte1[:-2]}_extra'] += {parte2}")
        else:
            try:
                exec(stringa)
            except:
                try:
                    exec(
                        f"""{(stringa).split("+=")[0].strip()} = int({float(eval(stringa.split("+=")[0].strip()))} + {float(eval(stringa.split("+=")[1].strip()))})""")
                except:
                    FormuleTemp.formule.append(stringa)

    for numeroeffetto in range(1, 32):
        codiceeff = eval(f"attore_attivo['codice_effetto_{numeroeffetto}']")
        codiceeff = codiceeff.replace("PersonaggioPy.Selezionato", "attore_attivo")
        codiceeff = codiceeff.replace("Shared.pg_selezionato", "Shared.attore_attivo")
        if "+=" in codiceeff:
            if "$$" not in codiceeff:
                sostituisci_ed_esegui(codiceeff)
            else:
                for effetto in codiceeff.split("$$"):
                    sostituisci_ed_esegui(effetto)

def calcola_formule_extra(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    Shared.attore_attivo = attore_attivo
    for formula in FormuleTemp.formule:
        if "_bonus_extra" in str(formula).split("+=")[0]:
            formula = formula.replace("_bonus_extra","_tot",1)
        elif "_extra" in str(formula).split("+=")[0]:
            formula = formula.replace("_extra","_tot",1)
        else:
            print(formula)
            raise Exception

        exec(formula)
    FormuleTemp.formule = []
def calcola_razze_caratteristiche(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    try:
        for effetto in Shared.dati_razze[attore_attivo["razza1"].lower().capitalize()].split("$$"):
            exec(effetto)
    except:
        if "__pg" in attore_attivo["nome_valore_excel"]:
            Popups_Notifiche.norazza(nome=attore_attivo["nomepg"], nomeinuso=attore_attivo["nome_in_uso"])
        else:
            pass

def calcola_peso(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    malus = 0
    gruppo = ["attore_attivo['malus_pa_armatura']", "attore_attivo['malus_pa_veste']",
              "attore_attivo['malus_pa_chainmail']", "attore_attivo['malus_pa_scudo']"]
    for item in gruppo:
        if eval(item) != "Vuoto":
            malus += int(eval(item))
    attore_attivo["malus_pa"] = malus

def unpack_alchimia(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    attore_attivo["alchimia_ingredienti_rossi_1"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[0]
    attore_attivo["alchimia_ingredienti_rossi_2"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[1]
    attore_attivo["alchimia_ingredienti_rossi_3"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[2]
    attore_attivo["alchimia_ingredienti_rossi_4"] = attore_attivo["alchimia_ingredienti_rossi_1_2_3_4"].split("$$")[3]
    attore_attivo["alchimia_ingredienti_verdi_1"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[0]
    attore_attivo["alchimia_ingredienti_verdi_2"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[1]
    attore_attivo["alchimia_ingredienti_verdi_3"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[2]
    attore_attivo["alchimia_ingredienti_verdi_4"] = attore_attivo["alchimia_ingredienti_verdi_1_2_3_4"].split("$$")[3]
    attore_attivo["alchimia_ingredienti_blu_1"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[0]
    attore_attivo["alchimia_ingredienti_blu_2"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[1]
    attore_attivo["alchimia_ingredienti_blu_3"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[2]
    attore_attivo["alchimia_ingredienti_blu_4"] = attore_attivo["alchimia_ingredienti_blu_1_2_3_4"].split("$$")[3]
    attore_attivo["alchimia_effetto_ingredienti_1"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        0]
    attore_attivo["alchimia_effetto_ingredienti_2"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        1]
    attore_attivo["alchimia_effetto_ingredienti_3"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        2]
    attore_attivo["alchimia_effetto_ingredienti_4"] = attore_attivo["alchimia_effetto_ingredienti_1_2_3_4"].split("$$")[
        3]

def unpack_magie(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
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
            attore_attivo[magianome] = f"{GestioneSkill.cerca_skill(ids=str(gruppomagie[indicemagia]))['NOME']}"
            attore_attivo[magiadescrizone] = f"{GestioneSkill.cerca_skill(ids=str(gruppomagie[indicemagia]))['DESCRIZIONE']}"
            attore_attivo[magiascuola] = f"{GestioneSkill.cerca_skill(ids=str(gruppomagie[indicemagia]))['TIPO']}"
            attore_attivo[magiaformula] = f"{GestioneSkill.cerca_skill(ids=str(gruppomagie[indicemagia]))['EXTRA1']}"
            attore_attivo[magiacostoinmana] = f"{GestioneSkill.cerca_skill(ids=str(gruppomagie[indicemagia]))['DETTAGLIO1']}"
            attore_attivo[magiaraggio] = f"{GestioneSkill.cerca_skill(ids=str(gruppomagie[indicemagia]))['DETTAGLIO2']}"
            indicemagia += 1
        else:
            attore_attivo[magianome] = "NO"
            attore_attivo[magiascuola] = "ALTERAZIONE"
            attore_attivo[magiadescrizone] = "NO"
            attore_attivo[magiacostoinmana] = "1 mana"
            attore_attivo[magiaraggio] = "NO"
            attore_attivo[magiaformula] = "M"

def formule_speciali(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    for formula in attore_attivo["formule_speciali"].split("$$"):
        formula = formula.replace("pg_selezionato", "attore_attivo")
        formula = formula.replace("–", "-")
        formula = formula.replace("£", "'")
        formula = formula.replace("“", '"')
        formula = formula.replace("”", '"')
        exec(formula)

def unpack_pasti(nome_NPC_Attori):
    attore_attivo = Shared.pg_png_inizializzati[nome_NPC_Attori]
    try:
        pasti = attore_attivo["pasti"].split("$$")
        attore_attivo["colazione"] = pasti[0]
        attore_attivo["pranzo"] = pasti[1]
        attore_attivo["cena"] = pasti[2]
    except:
        pasti = ['No', 'No', 'No']
        attore_attivo["colazione"] = pasti[0]
        attore_attivo["pranzo"] = pasti[1]
        attore_attivo["cena"] = pasti[2]

def salva_pasti():
    gruppopasti = ['colazione','pranzo', 'cena']
    stringa_totale = ""
    for pasto in gruppopasti:
        stringa_totale += f"{Shared.pg_selezionato[pasto]}$$"
    stringa_totale = stringa_totale[:-2]
    Shared.pg_selezionato["pasti"] = stringa_totale

def salva_faretra():
    gruppofaretra = ['faretra_1',
                     'faretra_2', 'faretra_3', 'faretra_4', 'faretra_5', 'faretra_6', 'faretra_7', 'faretra_8',
                     'faretra_9', 'faretra_10', 'faretra_11', 'faretra_12', 'faretra_13', 'faretra_14', 'faretra_15',
                     'faretra_16', 'faretra_17', 'faretra_18', 'faretra_19', 'faretra_20', 'faretra_21', 'faretra_22',
                     'faretra_23', 'faretra_24', 'faretra_25', 'faretra_26', 'faretra_27', 'faretra_28',
                     'faretra_29', 'faretra_30']
    stringa_totale = ""
    for freccia in gruppofaretra:
        stringa_totale += f"{Shared.pg_selezionato[freccia]}$$"
    stringa_totale = stringa_totale[:-2]
    Shared.pg_selezionato["faretra"] = stringa_totale