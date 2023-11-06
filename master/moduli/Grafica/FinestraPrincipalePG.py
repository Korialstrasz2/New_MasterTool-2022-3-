import os
from datetime import datetime, timedelta
from math import floor

from Moduli.Grafica import Popups_Effetti, FinestraPrincipaleMain, Popups_Notifiche, Popups_Magie, Popups_Sifone
from kivy.uix.button import Button
import Moduli.SharedData as Shared
from Moduli.Logica import EquipAttore
from kivy.properties import partial

kvcaratteristiche = ["forza_totkv", "resistenza_totkv", "velocita_totkv", "agilita_totkv", "intelligenza_totkv",
                     "concentrazione_totkv", "personalita_totkv", "saggezza_totkv", "modificatore_generalekv",
                     "stanchezzakv", "difesa_totkv", "attacco_totkv"]
class Temp:
    pa_spesi_somma = 0
    statusbottonemagia = 0
    orabottonesifone = datetime.now()

def barrapa():
    self = Shared.finestra
    Temp.pa_spesi_somma = 0
    malus = Shared.pg_selezionato["malus_pa"]
    carico = Shared.pg_selezionato["carico"]
    malusshow = malus + carico
    for item in range(1, 7):
        try:
            int(eval(f"self.pa_usa_{item}.text"))
        except:
            Popups_Notifiche.boxcheck()
            return
        exec(
            f"self.pa_usa_{item}.text = str(0) if self.pa_usa_{item}.text == '' else self.pa_usa_{item}.text")
        exec(f"Temp.pa_spesi_somma += int(self.pa_usa_{item}.text)")
    Temp.pa_spesi_somma += int(self.pa_usa_spell.text)
    self.pa_spesi.text = str(Temp.pa_spesi_somma)
    self.barrapa.max = int(Shared.pg_selezionato['pa_tot']) - malus
    self.barrapa.value = int((int(Shared.pg_selezionato['pa_tot']) - Temp.pa_spesi_somma) - malus)
    self.barrapatext.text = f"            {int(Shared.pg_selezionato['pa_tot']) - int(self.pa_spesi.text) - malus} / " \
                            f"{int(Shared.pg_selezionato['pa_tot']) - malus}         (-{malusshow})"


def meggaggi_pg():
    self = Shared.finestra
    totale = ""
    temp = ""
    flag_status = False
    for effetto in Shared.pg_selezionato:
        if effetto.startswith("nome_effetto_"):
            temp = Shared.pg_selezionato[effetto]
        elif effetto.startswith("descrizione_effetto_"):

            if temp.startswith("S-") or temp.startswith("M-"):
                flag_status = True
            if flag_status:
                self.ids.messaggipg.background_color = (0.5,1,0.5,0.4)

            else:
                self.ids.messaggipg.background_color = (1,1,1,0.3)
            if Shared.pg_selezionato[effetto].endswith("(t)"):
                totale += str(temp) + " - "
    self.ids.messaggipg.text = totale

def pareset():
    self = Shared.finestra
    for item in range(1, 7):
        exec(f"self.pa_usa_{item}.text = str(0)")
    self.pa_usa_spell.text = str(0)
    barrapa()

effetti_aperti = []
gruppodiario = ['diario1', 'diario2', 'diario3', 'diario4', 'diario5', 'diario6', 'diario7', 'diario8', 'diario9',
                'diario10', 'diario11', 'diario12', 'diario13', 'diario14', 'diario15', 'diario16', 'diario17',
                'diario18', 'missione_1', 'missione_2', 'missione_3', 'missione_4',
                'missione_5',
                'missione_6', 'missione_7', 'missione_8', 'missione_reward_1', 'missione_reward_2', 'missione_reward_3',
                'missione_reward_4', 'missione_reward_5', 'missione_reward_6', 'missione_reward_7', 'missione_reward_8',
                'note_finestraprincipale_1', 'note_finestraprincipale_2', 'note_finestraprincipale_3',
                'note_finestraprincipale_4',
                'note_extra','appunti1', 'appunti2', 'appunti3', 'appunti4', 'appunti5', 'appunti6',
                'appunti7', 'appunti8', 'appunti9', 'appunti10', 'appunti11', 'appunti12', 'appunti13', 'appunti14',
                'appunti15', 'appunti16', 'appunti17', 'appunti18', 'appunti19', 'appunti20', 'appunti21', 'appunti22',
                'appunti23', 'appunti24', 'appunti25', 'appunti26', 'appunti27', 'appunti28', 'appunti29', 'appunti30',
                'descrizione_skill_1', 'descrizione_skill_2', 'descrizione_skill_3', 'descrizione_skill_4',
                'descrizione_skill_5', 'descrizione_skill_6', 'descrizione_skill_7', 'descrizione_skill_8',
                'descrizione_skill_9', 'descrizione_skill_10', 'descrizione_skill_11', 'descrizione_skill_12',
                'descrizione_skill_13', 'descrizione_skill_14', 'descrizione_skill_15', 'descrizione_skill_16',
                'descrizione_skill_17', 'descrizione_skill_18', 'descrizione_skill_19', 'descrizione_skill_20',
                'descrizione_skill_21', 'descrizione_skill_22', 'descrizione_skill_23', 'descrizione_skill_24',
                'descrizione_skill_25', 'descrizione_skill_26', 'descrizione_skill_27', 'descrizione_skill_28',
                'descrizione_skill_29', 'descrizione_skill_30', 'descrizione_skill_31', 'descrizione_skill_32',
                'descrizione_skill_33', 'descrizione_skill_34', 'descrizione_skill_35', 'descrizione_skill_36',
                'descrizione_skill_37', 'descrizione_skill_38', 'descrizione_skill_39', 'descrizione_skill_40',
                'descrizione_skill_41', 'descrizione_skill_42', 'descrizione_skill_43', 'descrizione_skill_44',
                'descrizione_skill_45', 'descrizione_skill_46', 'descrizione_skill_47', 'descrizione_skill_48',
                'descrizione_skill_49', 'descrizione_skill_50', 'descrizione_skill_51', 'descrizione_skill_52',
                'descrizione_skill_53', 'descrizione_skill_54', 'descrizione_skill_55', 'descrizione_skill_56',
                'descrizione_skill_57', 'descrizione_skill_58', 'descrizione_skill_59', 'faretra_1',
                'faretra_2', 'faretra_3', 'faretra_4', 'faretra_5', 'faretra_6', 'faretra_7', 'faretra_8',
                'faretra_9', 'faretra_10', 'faretra_11', 'faretra_12', 'faretra_13', 'faretra_14', 'faretra_15',
                'faretra_16', 'faretra_17', 'faretra_18', 'faretra_19', 'faretra_20', 'faretra_21', 'faretra_22',
                'faretra_23', 'faretra_24', 'faretra_25', 'faretra_26', 'faretra_27', 'faretra_28',
                'faretra_29', 'faretra_30','extra1','extra2','extra3','extra4','extra5','extra6','extra7',
                'extra8','extra9','extra10','skill_sbloccate']

def show_effetti():
    x = 0.037
    y = 0.582
    xtemp = 0.249
    ytemp = 0.582
    self = Shared.finestra

    for doppio in effetti_aperti:
        if effetti_aperti.count(doppio) > 1:
            effetti_aperti.remove(doppio)

    for cancella in effetti_aperti:
        exec(f"""self.remove_widget(self.effetto{cancella}kv)""")

    for item in range(1, 32):
        nomeeffetto = "nome_effetto_" + str(item)
        descrizioneeffetto = "descrizione_effetto_" + str(item)
        valore = str(Shared.pg_selezionato[nomeeffetto])
        descrizione = str(Shared.pg_selezionato[descrizioneeffetto])

        if not descrizione.endswith("(t)"):
            exec(f"""self.effetto{item}kv = Button(disabled=False, size_hint=(0.042, 0.013), text=valore,
             on_release=partial(Popups_Effetti.gestisci_effetti_open,numero_open={item}),
                                   background_color = (1,0,0,0.3),pos_hint={{"x": {x}, "top": {y}}})""")
            if Shared.pg_selezionato[nomeeffetto] != "Vuoto":
                exec(f"""self.add_widget(self.effetto{item}kv)""")
                effetti_aperti.append(item)
                x += 0.042
                if x >= 0.23:
                    x = 0.037
                    y -= 0.013
        else:
            exec(f"""self.effetto{item}kv = Button(disabled=False, size_hint=(0.058, 0.013), text=valore,
             on_release=partial(Popups_Effetti.gestisci_effetti_open,numero_open={item}),
                                   background_color = (1,1,0.3,0.3),pos_hint={{"x": {xtemp}, "top": {ytemp}}})""")
            if Shared.pg_selezionato[nomeeffetto] != "Vuoto":
                exec(f"""self.add_widget(self.effetto{item}kv)""")
                effetti_aperti.append(item)
                ytemp -= 0.013


def show_caratteristiche_atk_def():
    self = Shared.finestra
    for item in kvcaratteristiche[:-4]:
        caratt = item[:-2]
        valore = Shared.pg_selezionato[caratt]
        totale = f"       {round(float(valore))} ({floor((round(float(valore)) - 10) / 2)})"
        exec(f"""self.ids.{item}.text = totale""")
    for item in kvcaratteristiche[-4:]:
        caratt = item[:-2]
        valore = Shared.pg_selezionato[caratt]
        totale = f"         {round(float(valore))}"
        exec(f"""self.ids.{item}.text = totale""")
    self.labelarma.text = str(Shared.pg_selezionato["eq_arma_1"]["NOME"]) + \
                          "\n" + str(Shared.pg_selezionato["eq_arma_1"]["TIPO3"]) + \
                          " pa per atk: " + str(Shared.pg_selezionato["eq_arma_1"]["EFFETTO3"])+ \
                          "\nbonus arma:  " + str(Shared.pg_selezionato["bonus_arma"])

def immagine_piccola(*args):
    nome = Shared.pg_selezionato["nome_valore_excel"][6:]

    cartella = os.listdir(Shared.path_art + f"/bgeritrattipg")
    if f"miniritratto{nome}.png" in cartella:
        Shared.finestra.ids.immaginepiccolapg.source = Shared.path_art + f"/bgeritrattipg/miniritratto{nome}.png"
    else:
        Shared.finestra.ids.immaginepiccolapg.source = Shared.path_art + f"/empty.png"

def show_valori_primari():
    self = Shared.finestra
    self.ids.textbarravitakv.text = f"{int(Shared.pg_selezionato['pf_tot']) - int(Shared.pg_selezionato['danno'])}" \
                                    f" / {int(Shared.pg_selezionato['pf_tot'])}  ({int(Shared.pg_selezionato['danno'])})"
    if (int(Shared.pg_selezionato['pf_tot']) - int(Shared.pg_selezionato['danno'])) != 0:
        self.ids.barravitakv.value = 100 * \
                                     ((int(Shared.pg_selezionato['pf_tot']) -
                                       int(Shared.pg_selezionato['danno']))
                                      / int(Shared.pg_selezionato['pf_tot']))
    else:
        self.ids.barravitakv.value = 0
    valore_rosso = float(int(Shared.pg_selezionato['danno']) / int(Shared.pg_selezionato['pf_tot']))
    valore_rosso = valore_rosso / 1.7
    if valore_rosso < 0.2 and valore_rosso != 0:
        valore_rosso = 0.2

    self.ids.filtrocoloreimgpg.background_color = (1,0,0,valore_rosso)

    self.ids.textbarramanakv.text = f"{int(Shared.pg_selezionato['mana_tot']) - int(Shared.pg_selezionato['mana_speso'])}" \
                                    f" / {int(Shared.pg_selezionato['mana_tot'])}  ({int(Shared.pg_selezionato['mana_speso'])})"

    if (int(Shared.pg_selezionato['mana_tot']) - int(Shared.pg_selezionato['mana_speso'])) != 0:
        self.ids.barramanakv.value = 100 * \
                                     ((int(Shared.pg_selezionato['mana_tot']) - int(Shared.pg_selezionato['mana_speso']))
                                      / int(Shared.pg_selezionato['mana_tot']))
    else:
        self.ids.barramanakv.value = 0

    self.ids.textbarraenergiakv.text = f"{int(Shared.pg_selezionato['energia_tot']) - int(Shared.pg_selezionato['energia_spesa'])}" \
                                       f" / {int(Shared.pg_selezionato['energia_tot'])}  ({int(Shared.pg_selezionato['energia_spesa'])})"
    if (int(Shared.pg_selezionato['energia_tot']) - int(Shared.pg_selezionato['energia_spesa'])) != 0:
        self.ids.barraenkv.value = 100 * \
                                   ((int(Shared.pg_selezionato['energia_tot']) - int(Shared.pg_selezionato['energia_spesa'])) /
                                    int(Shared.pg_selezionato['energia_tot']))
    else:
        self.ids.barraenkv.value = 0

    self.ids.textbarrapoterekv.text = f"{int(Shared.pg_selezionato['potere_tot']) - int(Shared.pg_selezionato['potere_speso'])} " \
                                      f"/ {int(Shared.pg_selezionato['potere_tot'])}  ({int(Shared.pg_selezionato['potere_speso'])})"
    if (int(Shared.pg_selezionato['potere_tot']) - int(Shared.pg_selezionato['potere_speso'])) != 0:
        self.ids.barrapowkv.value = 100 * \
                                    ((int(Shared.pg_selezionato['potere_tot']) - int(
                                        Shared.pg_selezionato['potere_speso'])) /
                                     int(Shared.pg_selezionato['potere_tot']))

    else:
        self.ids.barrapowkv.value = 0
    if int(int(Shared.pg_selezionato['sifone_di_mana'])) > 0:
        self.ids.bottonesifonekv.text = f"Sifone: {int(float(Shared.pg_selezionato['mana_in_sifone']))}"


def shownote():
    self = Shared.finestra
    for item in gruppodiario:
        exec(f"self.{item}kv.text = str(Shared.pg_selezionato[item])")

def showbottoni():
    self = Shared.finestra
    for bottone in range(1,7):
        exec(f"self.ids.button_statusrapidokv{bottone}.text = Shared.dati_bottoni['bottone_{bottone}']['nome']")

def checklistaskill():
    self = Shared.finestra
    controlla_skill = self.skill_sbloccatekv.text
    if str(controlla_skill) == "0":
        controlla_skill = "9999999$$9999999"
    try:
        for indice in sorted(controlla_skill.split("$$")):
            if Shared.skill_importate[int(indice)]["TIPO"]:
                pass
        return True
    except:
        Popups_Notifiche.nosave()
        return False

def salvanote():
    self = Shared.finestra
    for item in gruppodiario:
        exec(f"Shared.pg_selezionato[item] = self.{item}kv.text")
    EquipAttore.salva_faretra()
    shownote()


def cena():
    self = Shared.finestra
    if Shared.pg_selezionato['cena'] == "No":
        self.ids.cenakv.source = "Art/cenasi.png"
        Shared.pg_selezionato['cena'] = "Fatta"
    elif Shared.pg_selezionato['cena'] == "Fatta":
        self.ids.cenakv.source = "Art/cenano.png"
        Shared.pg_selezionato['cena'] = "No"


def colazione():
    self = Shared.finestra
    if Shared.pg_selezionato['colazione'] == "No":
        self.ids.colazionekv.source = "Art/colazionesi.png"
        Shared.pg_selezionato['colazione'] = "Fatta"
    elif Shared.pg_selezionato['colazione'] == "Fatta":
        self.ids.colazionekv.source = "Art/colazioneno.png"
        Shared.pg_selezionato['colazione'] = "No"


def pranzo():
    self = Shared.finestra
    if Shared.pg_selezionato['pranzo'] == "No":
        self.ids.pranzokv.source = "Art/pranzosi.png"
        Shared.pg_selezionato['pranzo'] = "Fatto"
    elif Shared.pg_selezionato['pranzo'] == "Fatto":
        self.ids.pranzokv.source = "Art/pranzono.png"
        Shared.pg_selezionato['pranzo'] = "No"

def nomi_magie(): #dopo aver importato magie
    self = Shared.finestra
    for item in range(1, 37):
        exec(f"self.magia{item}testokv.text = str(Shared.pg_selezionato['magia_{item}_nome'])")

def box_finestra():
    def validanumero(item):
        if item != "":
            try:
                eval(item)
            except:
                Popups_Notifiche.nodigit(stringa=item)
                item = "1-1"
            return eval(item)
        else:
            return 0
    self = Shared.finestra
    Shared.pg_selezionato["danno"] = int(Shared.pg_selezionato["danno"]) + int(validanumero(item=self.boxdannokv.text))
    Shared.pg_selezionato["mana_speso"] = int(Shared.pg_selezionato["mana_speso"]) + int(validanumero(item=self.boxmanaspesokv.text))
    if self.boxmanaspesokv.text[0] != "-":
        Shared.pg_selezionato["mana_in_sifone"] = int(float(Shared.pg_selezionato["mana_in_sifone"])) + int(self.boxmanaspesokv.text) / \
                                      100 * int(float(Shared.pg_selezionato["sifone_di_mana"]))
    Shared.pg_selezionato["energia_spesa"] = int(Shared.pg_selezionato["energia_spesa"]) + int(
        validanumero(item=self.boxenergiaspesakv.text))
    Shared.pg_selezionato["potere_speso"] = int(Shared.pg_selezionato["potere_speso"]) + int(validanumero(item=self.boxpoterespesokv.text))
    self.boxpoterespesokv.text = "0"
    self.boxenergiaspesakv.text = "0"
    self.boxmanaspesokv.text = "0"
    self.boxdannokv.text = "0"
    self.boxpoterefree1.text = "0"
    self.boxpoterefree2.text = "0"

def selezionamagia(numero):
    famiglia_ordine = ["Alterazione", "Recupero", "Illusione", "Negromanzia"]
    famiglia_caos = ["Evocazione", "Distruzione", "Maledizioni", "Misticismo"]

    if Temp.statusbottonemagia != numero:
        Shared.pg_selezionato["Magiaattuale"] = {}
        nomemagia = "magia_"+ str(numero) + "_nome"
        scuolamagia = "magia_"+ str(numero) + "_scuola"
        formulamagia = "magia_"+ str(numero) + "_formula"
        descrizionemagia = "magia_"+ str(numero) + "_descrizione"
        costoinmanamagia = "magia_"+ str(numero) + "_costo_in_mana"
        raggiomagia = "magia_"+ str(numero) + "_raggio"
        Shared.pg_selezionato["Magiaattuale"]["nome"] = str(Shared.pg_selezionato[nomemagia])
        Shared.pg_selezionato["Magiaattuale"]["descrizione"] = str(Shared.pg_selezionato[descrizionemagia])
        Shared.pg_selezionato["Magiaattuale"]["scuola"] = str(Shared.pg_selezionato[scuolamagia])
        Shared.pg_selezionato["Magiaattuale"]["formula"] = str(Shared.pg_selezionato[formulamagia])
        Shared.pg_selezionato["Magiaattuale"]["costoinmana"] = str(Shared.pg_selezionato[costoinmanamagia])
        Shared.pg_selezionato["Magiaattuale"]["raggio"] = str(Shared.pg_selezionato[raggiomagia])



        if Shared.pg_selezionato["Magiaattuale"]["scuola"].lower().capitalize() in famiglia_ordine:
            Shared.pg_selezionato["Magiaattuale"]["famiglia"] = "Ordine"
        elif Shared.pg_selezionato["Magiaattuale"]["scuola"].lower().capitalize() in famiglia_caos:
            Shared.pg_selezionato["Magiaattuale"]["famiglia"] = "Caos"


        self = Shared.finestra

        self.magiaselezionata1kv.text = str(str(Shared.pg_selezionato["Magiaattuale"]["nome"]) +
                                            '\n' + str(Shared.pg_selezionato["Magiaattuale"]["scuola"]) +
                                            ' -  ' + str(Shared.pg_selezionato["Magiaattuale"]["raggio"])+
                                            '\n' + str(Shared.pg_selezionato["Magiaattuale"]["costoinmana"]))
        self.magiaselezionata2kv.text = str(str(Shared.pg_selezionato["Magiaattuale"]["nome"]) +
                                            '\n' + str(Shared.pg_selezionato["Magiaattuale"]["scuola"]) +
                                            ' -  ' + str(Shared.pg_selezionato["Magiaattuale"]["raggio"])+
                                            '\n' + str(Shared.pg_selezionato["Magiaattuale"]["costoinmana"]))

        self.slidemanaspell1kv.max = int(int(Shared.pg_selezionato["mana_tot"]) - int(Shared.pg_selezionato["mana_speso"]) +
                                         ((int(Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"]) +
                                           int(self.boxpoterefree1.text)) * float(Shared.pg_selezionato["sconto_mana_per_potere"])))
        self.slidepoterespell1kv.max = int(
            Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"])
        self.slidemanaspell2kv.max = int(int(Shared.pg_selezionato["mana_tot"]) - int(Shared.pg_selezionato["mana_speso"]) + (
                (int(Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"])) * float(
            Shared.pg_selezionato["sconto_mana_per_potere"])))
        self.slidepoterespell2kv.max = int(
            Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"])
        Temp.statusbottonemagia = numero

    elif Temp.statusbottonemagia == numero:
        Popups_Magie.magiaopen(numero)
        Temp.statusbottonemagia = 0

def slidepoterespell1(*args):

    self = Shared.finestra
    self.slidepoterespell1kv.max = int(Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"]) + int(
        self.boxpoterefree1.text)
    if self.boxmanaslide1.text == "":
        self.boxmanaslide1.text = str("0")
    if self.boxmanaspesokv.text == "":
        self.boxmanaspesokv.text = str("0")
    if self.boxpoterespesokv.text == "":
        self.boxpoterespesokv.text = str("0")
    if self.boxpoterefree1.text == "":
        self.boxpoterefree1.text = str("0")
    self.boxpotereslide1.text = str(int(args[1]))
    self.boxpoterespesokv.text = str(
        int(args[1]) - (int(self.boxpoterefree1.text)))


def slidepoterespell2(*args):
    self = Shared.finestra
    self.slidepoterespell2kv.max = int(Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"]) + int(
        self.boxpoterefree2.text)
    if self.boxmanaslide2.text == "":
        self.boxmanaslide2.text = str("0")
    if self.boxmanaspesokv.text == "":
        self.boxmanaspesokv.text = str("0")
    if self.boxpoterespesokv.text == "":
        self.boxpoterespesokv.text = str("0")
    if self.boxpoterefree2.text == "":
        self.boxpoterefree2.text = str("0")
    self.boxpotereslide2.text = str(int(args[1]))
    self.boxpoterespesokv.text = str(
        int(args[1]) - (int(self.boxpoterefree2.text)))


def slidemanaspell1(*args):
    if "Magiaattuale" in Shared.pg_selezionato.keys() and Shared.pg_selezionato["Magiaattuale"]["formula"] not in [None,"None",""]:
        self = Shared.finestra
        if self.boxmanaslide1.text == "":
            self.boxmanaslide1.text = str("0")
        if self.boxmanaspesokv.text == "":
            self.boxmanaspesokv.text = str("0")
        if self.boxpoterespesokv.text == "":
            self.boxpoterespesokv.text = str("0")
        if self.boxenergiaspesakv.text == "":
            self.boxenergiaspesakv.text = str("0")
        self.boxmanaslide1.text = str(int(args[1]))
        formula = Shared.pg_selezionato["Magiaattuale"]["formula"]
        formula = formula.lower().replace("m", str(self.boxmanaslide1.text))
        self.slidemanaspell1kv.max = int(int(Shared.pg_selezionato["mana_tot"]) - int(Shared.pg_selezionato["mana_speso"]) +
                                         ((int(Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"]) +
                                           int(self.boxpoterefree1.text)) * float(Shared.pg_selezionato["sconto_mana_per_potere"])))
        formula = str(formula).replace(",",".")
        self.effettospellkv1.text = str(floor(eval(formula)))
        self.boxmanaspesokv.text = str(
            int(self.boxmanaslide1.text) - int(
                int(self.boxpotereslide1.text) * (float(Shared.pg_selezionato["sconto_mana_per_potere"]))))

        if Shared.pg_selezionato["Magiaattuale"]["famiglia"] == "Ordine":
            self.pa_usa_spell.text = str(int(float(self.boxmanaslide1.text) / float(Shared.pg_selezionato["papermanaordine"]) -
                                             (float(self.boxpotereslide1.text) * float(
                                                 Shared.pg_selezionato["sconto_pa_per_potere"]))))
            self.boxenergiaspesakv.text = str(
                int(float(self.boxmanaslide1.text) / float(Shared.pg_selezionato["enpermanaordine"]) + 0.7))

        elif Shared.pg_selezionato["Magiaattuale"]["famiglia"] == "Caos":
            self.pa_usa_spell.text = str(int(float(self.boxmanaslide1.text) / float(Shared.pg_selezionato["papermanacaos"]) -
                                             (float(self.boxpotereslide1.text) * float(
                                                 Shared.pg_selezionato["sconto_pa_per_potere"]))))
            self.boxenergiaspesakv.text = str(
                int(float(self.boxmanaslide1.text) / float(Shared.pg_selezionato["enpermanacaos"]) + 0.7))


def slidemanaspell2(*args):
    if "Magiaattuale" in Shared.pg_selezionato.keys() and Shared.pg_selezionato["Magiaattuale"]["formula"] not in [None,"None",""]:
        self = Shared.finestra
        if self.boxmanaslide2.text == "":
            self.boxmanaslide2.text = str("0")
        if self.boxmanaspesokv.text == "":
            self.boxmanaspesokv.text = str("0")
        if self.boxpoterespesokv.text == "":
            self.boxpoterespesokv.text = str("0")
        if self.boxenergiaspesakv.text == "":
            self.boxenergiaspesakv.text = str("0")
        self.boxmanaslide2.text = str(int(args[1]))
        formula = Shared.pg_selezionato["Magiaattuale"]["formula"]
        formula = formula.lower().replace("m", str(self.boxmanaslide2.text))
        self.slidemanaspell2kv.max = int(int(Shared.pg_selezionato["mana_tot"]) - int(Shared.pg_selezionato["mana_speso"]) +
                                         ((int(Shared.pg_selezionato["potere_tot"]) - int(Shared.pg_selezionato["potere_speso"]) +
                                           int(self.boxpoterefree2.text)) * float(Shared.pg_selezionato["sconto_mana_per_potere"])))
        formula = str(formula).replace(",",".")
        self.effettospellkv2.text = str(floor(eval(formula)))
        self.boxmanaspesokv.text = str(
            int(self.boxmanaslide2.text) - int(
                int(self.boxpotereslide2.text) * (float(Shared.pg_selezionato["sconto_mana_per_potere"]))))

        if Shared.pg_selezionato["Magiaattuale"]["famiglia"] == "Ordine":
            self.pa_usa_spell.text = str(int(float(self.boxmanaslide2.text) / float(Shared.pg_selezionato["papermanaordine"]) -
                                             (float(self.boxpotereslide2.text) * float(
                                                 Shared.pg_selezionato["sconto_pa_per_potere"]))))
            self.boxenergiaspesakv.text = str(
                int(float(self.boxmanaslide2.text) / float(Shared.pg_selezionato["enpermanaordine"]) + 0.7))

        elif Shared.pg_selezionato["Magiaattuale"]["famiglia"] == "Caos":
            self.pa_usa_spell.text = str(int(float(self.boxmanaslide2.text) / float(Shared.pg_selezionato["papermanacaos"]) -
                                             (float(self.boxpotereslide2.text) * float(
                                                 Shared.pg_selezionato["sconto_pa_per_potere"]))))
            self.boxenergiaspesakv.text = str(
                int(float(self.boxmanaslide2.text) / float(Shared.pg_selezionato["enpermanacaos"]) + 0.7))

def sifonereset():
    if Temp.orabottonesifone + timedelta(seconds=2) < datetime.now():
        Temp.orabottonesifone = datetime.now()
        self = Shared.finestra
        self.boxmanaspesokv.text = f"-{Shared.pg_selezionato['mana_in_sifone']}"
        Shared.pg_selezionato['mana_in_sifone'] = 0
        FinestraPrincipaleMain.FunzioniFinestra.conferma()
    else:
        Popups_Sifone.sifoneopen()

def pffull():
    Shared.master_hint_counter += 1
    if Shared.master_hint_counter >= 3:
        Shared.mastermode = True
    Shared.pg_selezionato["danno"] = 0
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def manafull():
    Shared.pg_selezionato["mana_speso"] = 0
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def enfull():
    Shared.pg_selezionato["energia_spesa"] = 0
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def powfull():
    Shared.pg_selezionato["potere_speso"] = 0
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def stanchezzapiu():
    Shared.pg_selezionato['stanchezza_base'] = str(int(Shared.pg_selezionato['stanchezza_base']) + 1)
    EquipAttore.equip_npc(Shared.pg_selezionato['nome_in_uso'])
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def stanchezzameno():
    Shared.pg_selezionato['stanchezza_base'] = str(int(Shared.pg_selezionato['stanchezza_base']) - 1)
    EquipAttore.equip_npc(Shared.pg_selezionato['nome_in_uso'])
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def modgenpiu():
    Shared.pg_selezionato['modificatore_generale_base'] = str(int(Shared.pg_selezionato['modificatore_generale_base']) + 1)
    EquipAttore.equip_npc(Shared.pg_selezionato['nome_in_uso'])
    FinestraPrincipaleMain.FunzioniFinestra.conferma()

def modgenmeno():
    Shared.pg_selezionato['modificatore_generale_base'] = str(int(Shared.pg_selezionato['modificatore_generale_base']) - 1)
    EquipAttore.equip_npc(Shared.pg_selezionato['nome_in_uso'])
    FinestraPrincipaleMain.FunzioniFinestra.conferma()