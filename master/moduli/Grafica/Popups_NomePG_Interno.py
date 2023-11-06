import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain
from Moduli.Logica import EquipAttore, Salvataggio, ImportazioneAttori
from kivy.properties import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


def formuleopen(*args):

    layout1 = GridLayout(cols=1, spacing=0, size_hint_y=None, height=1040)
    scroller = ScrollView(size_hint=(1, None), size=(400, 400), effect_cls="ScrollEffect")
    popup = Popup(title="FORMULE", title_size=(30),
                  title_align='center', content=scroller,
                  size_hint=(None, None), size=(400, 500),
                  auto_dismiss=True)

    def sostituisci(*args, item_formula):
        layout2 = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        popup = Popup(title=item_formula, title_size=(30),
                      title_align='center', content=layout2,
                      size_hint=(0.5, 0.3), size=(400, 400),
                      auto_dismiss=True)

        def sovrascrivi(*args):
            nonlocal inputboxformule
            if item_formula != "Shared.pg_selezionato['formule_speciali']":
                exec(f"{item_formula} = inputboxformule.text")
                EquipAttore.equip_npc(Shared.pg_selezionato["nome_in_uso"])
            else:
                Shared.pg_selezionato['formule_speciali'] = inputboxformule.text
                EquipAttore.equip_npc(Shared.pg_selezionato["nome_in_uso"])

            Salvataggio.salva_pgnpc(Shared.pg_selezionato["nome_in_uso"])
            FinestraPrincipaleMain.FunzioniFinestra.show_all()

        if item_formula == "Shared.pg_selezionato['formule_speciali']":
            popup.size = (400, 600)
            layout2.add_widget(TextInput(font_size=20,
                                         text="Esempio : $$if Shared.pg_selezionato['eq_scudo']['TIPO3'] == 'leggero' :    Shared.pg_selezionato['attacco_item'] += 0",
                                         size_hint_y=None, height=100))
        inputboxformule = TextInput(font_size=20, text=eval(item_formula), size_hint_y=None, height=100)
        boxsovrascrivi = Button(text=str("Sovrascrivi"), size_hint_y=None, height=40, on_release=sovrascrivi)

        layout2.add_widget(inputboxformule)
        layout2.add_widget(boxsovrascrivi)
        popup.open()

    buttoncallbackspeciali = partial(sostituisci, item_formula="Shared.pg_selezionato['formule_speciali']")
    buttoncallbackforza = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_forza_tot']")
    buttoncallbackresistenza = partial(sostituisci,
                                       item_formula="Shared.pg_selezionato['formula_resistenza_tot']")
    buttoncallbackvelocita = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_velocita_tot']")
    buttoncallbackagilita = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_agilita_tot']")
    buttoncallbackintelligenza = partial(sostituisci,
                                         item_formula="Shared.pg_selezionato['formula_intelligenza_tot']")
    buttoncallbackconcentrazione = partial(sostituisci,
                                           item_formula="Shared.pg_selezionato['formula_concentrazione_tot']")
    buttoncallbackpersonalita = partial(sostituisci,
                                        item_formula="Shared.pg_selezionato['formula_personalita_tot']")
    buttoncallbacksaggezza = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_saggezza_tot']")
    buttoncallbackfortuna = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_fortuna_tot']")
    layout1.add_widget(Button(text=str("Speciali"), size_hint_y=None, height=40, on_release=buttoncallbackspeciali))
    layout1.add_widget(Button(text=str("Forza"), size_hint_y=None, height=40, on_release=buttoncallbackforza))
    layout1.add_widget(
        Button(text=str("Resistenza"), size_hint_y=None, height=40, on_release=buttoncallbackresistenza))
    layout1.add_widget(Button(text=str("Agilita"), size_hint_y=None, height=40, on_release=buttoncallbackagilita))
    layout1.add_widget(Button(text=str("Velocita"), size_hint_y=None, height=40, on_release=buttoncallbackvelocita))
    layout1.add_widget(
        Button(text=str("Intelligenza"), size_hint_y=None, height=40, on_release=buttoncallbackintelligenza))
    layout1.add_widget(
        Button(text=str("Concentrazione"), size_hint_y=None, height=40, on_release=buttoncallbackconcentrazione))
    layout1.add_widget(
        Button(text=str("Personalita"), size_hint_y=None, height=40, on_release=buttoncallbackpersonalita))
    layout1.add_widget(Button(text=str("Saggezza"), size_hint_y=None, height=40, on_release=buttoncallbacksaggezza))
    layout1.add_widget(Button(text=str("Fortuna"), size_hint_y=None, height=40, on_release=buttoncallbackfortuna))

    buttoncallbackpf_base = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_pf_base']")
    layout1.add_widget(Button(text=str("PF base"), size_hint_y=None, height=40, on_release=buttoncallbackpf_base))
    buttoncallbackpf_tot = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_pf_tot']")
    layout1.add_widget(Button(text=str("PF totale"), size_hint_y=None, height=40, on_release=buttoncallbackpf_tot))
    buttoncallbackmana_base = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_mana_base']")
    layout1.add_widget(
        Button(text=str("Mana base"), size_hint_y=None, height=40, on_release=buttoncallbackmana_base))
    buttoncallbackmana_tot = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_mana_tot']")
    layout1.add_widget(
        Button(text=str("Mana totale"), size_hint_y=None, height=40, on_release=buttoncallbackmana_tot))
    buttoncallbackenergia_base = partial(sostituisci,
                                         item_formula="Shared.pg_selezionato['formula_energia_base']")
    layout1.add_widget(
        Button(text=str("Energia base"), size_hint_y=None, height=40, on_release=buttoncallbackenergia_base))
    buttoncallbackenergia_tot = partial(sostituisci,
                                        item_formula="Shared.pg_selezionato['formula_energia_tot']")
    layout1.add_widget(
        Button(text=str("Energia totale"), size_hint_y=None, height=40, on_release=buttoncallbackenergia_tot))
    buttoncallbackpotere_base = partial(sostituisci,
                                        item_formula="Shared.pg_selezionato['formula_potere_base']")
    layout1.add_widget(
        Button(text=str("Potere base"), size_hint_y=None, height=40, on_release=buttoncallbackpotere_base))
    buttoncallbackpotere_tot = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_potere_tot']")
    layout1.add_widget(
        Button(text=str("Potere totale"), size_hint_y=None, height=40, on_release=buttoncallbackpotere_tot))
    buttoncallbackattacco_base = partial(sostituisci,
                                         item_formula="Shared.pg_selezionato['formula_attacco_base']")
    layout1.add_widget(
        Button(text=str("Attacco base"), size_hint_y=None, height=40, on_release=buttoncallbackattacco_base))
    buttoncallbackattacco_tot = partial(sostituisci,
                                        item_formula="Shared.pg_selezionato['formula_attacco_tot']")
    layout1.add_widget(
        Button(text=str("Attacco totale"), size_hint_y=None, height=40, on_release=buttoncallbackattacco_tot))
    buttoncallbackdifesa_base = partial(sostituisci,
                                        item_formula="Shared.pg_selezionato['formula_difesa_base']")
    layout1.add_widget(
        Button(text=str("Difesa base"), size_hint_y=None, height=40, on_release=buttoncallbackdifesa_base))
    buttoncallbackdifesa_tot = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_difesa_tot']")
    layout1.add_widget(
        Button(text=str("Difesa totale"), size_hint_y=None, height=40, on_release=buttoncallbackdifesa_tot))
    buttoncallbackpa_base = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_pa_base']")
    layout1.add_widget(Button(text=str("PA base"), size_hint_y=None, height=40, on_release=buttoncallbackpa_base))
    buttoncallbackpa_tot = partial(sostituisci, item_formula="Shared.pg_selezionato['formula_pa_tot']")
    layout1.add_widget(Button(text=str("PA totali"), size_hint_y=None, height=40, on_release=buttoncallbackpa_tot))
    buttoncallbackbarr_fis_tot = partial(sostituisci,
                                         item_formula="Shared.pg_selezionato['formula_barr_fis_tot']")
    layout1.add_widget(
        Button(text=str("Barriera Fisica"), size_hint_y=None, height=40, on_release=buttoncallbackbarr_fis_tot))
    buttoncallbackbarr_mag_tot = partial(sostituisci,
                                         item_formula="Shared.pg_selezionato['formula_barr_mag_tot']")
    layout1.add_widget(
        Button(text=str("Barriera Magica"), size_hint_y=None, height=40, on_release=buttoncallbackbarr_mag_tot))
    buttoncallbackcompri_a_meno_tot = partial(sostituisci,
                                              item_formula="Shared.pg_selezionato['formula_compri_a_meno_tot']")
    layout1.add_widget(
        Button(text=str("Compri a meno"), size_hint_y=None, height=40, on_release=buttoncallbackcompri_a_meno_tot))
    buttoncallbackvendi_a_piu_tot = partial(sostituisci,
                                            item_formula="Shared.pg_selezionato['formula_vendi_a_piu_tot']")
    layout1.add_widget(
        Button(text=str("Vendi a piu"), size_hint_y=None, height=40, on_release=buttoncallbackvendi_a_piu_tot))
    scroller.add_widget(layout1)
    popup.open()


def razzeopen(*args):
    layout1 = GridLayout(cols=2, spacing=0)
    popup = Popup(title="RAZZE", title_size=(30),
                  title_align='center', content=layout1,
                  size_hint=(None, None), size=(400, 350),
                  auto_dismiss=True)

    def bottoneconferma(*args):
        Shared.pg_selezionato['razza1'] = boxrazza1.text
        Shared.pg_selezionato['razza2'] = boxrazza2.text
        Shared.pg_selezionato['razza3'] = boxrazza3.text
        Salvataggio.salva_pgnpc(Shared.pg_selezionato["nome_in_uso"])

    layout1.add_widget(Label(text=str("Razza 1:"), size_hint_y=None, height=40))
    boxrazza1 = TextInput(text=str(Shared.pg_selezionato['razza1']), size_hint_y=None, height=40)
    layout1.add_widget(boxrazza1)
    layout1.add_widget(Label(text=str("Sottorazza"), size_hint_y=None, height=40))
    boxrazza2 = TextInput(text=str(Shared.pg_selezionato['razza2']), size_hint_y=None, height=40)
    layout1.add_widget(boxrazza2)
    layout1.add_widget(Label(text=str("Extra"), size_hint_y=None, height=40))
    boxrazza3 = TextInput(text=str(Shared.pg_selezionato['razza3']), size_hint_y=None, height=40)
    layout1.add_widget(boxrazza3)
    layout1.add_widget(Button(text=str("CONFERMA"), size_hint_y=None, height=40, on_release=bottoneconferma))
    popup.open()


def criticiopen(*args):
    layout1 = GridLayout(cols=2, spacing=0)
    popup = Popup(title="CRITICI", title_size=(30),
                  title_align='center', content=layout1,
                  size_hint=(None, None), size=(400, 350),
                  auto_dismiss=True)

    def bottoneconferma(*args):
        Shared.pg_selezionato['crit_min'] = boxcrtitmin.text
        Shared.pg_selezionato['crit_nor'] = boxcrtitnor.text
        Shared.pg_selezionato['crit_mag'] = boxcrtitmag.text
        Salvataggio.salva_pgnpc(Shared.pg_selezionato["nome_in_uso"])

    layout1.add_widget(Label(text=str("Inserisci come nell'esempio:"), size_hint_y=None, height=40))
    layout1.add_widget(TextInput(text=str("20,19"), size_hint_y=None, height=40))
    layout1.add_widget(Label(text=str("Critico Maggiore:"), size_hint_y=None, height=40))
    boxcrtitmag = TextInput(text=str(Shared.pg_selezionato['crit_mag']), size_hint_y=None, height=40)
    layout1.add_widget(boxcrtitmag)
    layout1.add_widget(Label(text=str("Critico:"), size_hint_y=None, height=40))
    boxcrtitnor = TextInput(text=str(Shared.pg_selezionato['crit_nor']), size_hint_y=None, height=40)
    layout1.add_widget(boxcrtitnor)
    layout1.add_widget(Label(text=str("Critico Minore:"), size_hint_y=None, height=40))
    boxcrtitmin = TextInput(text=str(Shared.pg_selezionato['crit_min']), size_hint_y=None, height=40)
    layout1.add_widget(boxcrtitmin)
    layout1.add_widget(Button(text=str("CONFERMA"), size_hint_y=None, height=40, on_release=bottoneconferma))
    popup.open()

def resistenzeopen(*args):
    layout = FloatLayout()
    popup = Popup(title="RESISTENZE", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(350, 500),
                  auto_dismiss=True)

    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.35, "y": 0.9}, text="Base"))
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.9}, text="TOT"))
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.8}, text="RD Fisica"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.8}, text=str(Shared.pg_selezionato['rd_fis'])))
    valorerdfis = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.8},
                            text=str(Shared.pg_selezionato['rd_fis_base']))
    layout.add_widget(valorerdfis)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.73}, text="Res. Contundente"))
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.73},
                            text=str(Shared.pg_selezionato['res_contundente'])))
    valoreresc = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.73},
                           text=str(Shared.pg_selezionato['res_contundente_base']))
    layout.add_widget(valoreresc)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.66}, text="Res. Perforante"))
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.66},
                            text=str(Shared.pg_selezionato['res_perforante'])))
    valoreresp = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.66},
                           text=str(Shared.pg_selezionato['res_perforante_base']))
    layout.add_widget(valoreresp)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.59}, text="Res. Taglio"))
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.59},
                            text=str(Shared.pg_selezionato['res_taglio'])))
    valorerest = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.59},
                           text=str(Shared.pg_selezionato['res_taglio_base']))
    layout.add_widget(valorerest)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.52}, text="RD Fuoco"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.52}, text=str(Shared.pg_selezionato['rd_fuoco'])))
    valorerdfu = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.52},
                           text=str(Shared.pg_selezionato['rd_fuoco_base']))
    layout.add_widget(valorerdfu)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.45}, text="RD Gelo"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.45}, text=str(Shared.pg_selezionato['rd_gelo'])))
    valorerdge = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.45},
                           text=str(Shared.pg_selezionato['rd_gelo_base']))
    layout.add_widget(valorerdge)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.38}, text="RD Elettro"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.4},
              text=str(Shared.pg_selezionato['rd_elettro'])))
    valorerdel = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.38},
                           text=str(Shared.pg_selezionato['rd_elettro_base']))
    layout.add_widget(valorerdel)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.31}, text="Res. Fuoco"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.31},
              text=str(Shared.pg_selezionato['res_fuoco'])))
    valoreresfu = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.31},
                            text=str(Shared.pg_selezionato['res_fuoco_base']))
    layout.add_widget(valoreresfu)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.24}, text="Res. Gelo"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.24}, text=str(Shared.pg_selezionato['res_gelo'])))
    valoreresge = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.24},
                            text=str(Shared.pg_selezionato['res_gelo_base']))
    layout.add_widget(valoreresge)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.17}, text="Res. Elettro"))
    layout.add_widget(
        Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.75, "y": 0.17},
              text=str(Shared.pg_selezionato['res_elettro'])))
    valoreresel = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.17},
                            text=str(Shared.pg_selezionato['res_elettro_base']))
    layout.add_widget(valoreresel)

    def salva(*args):
        Shared.pg_selezionato['rd_fis_base'] = int(valorerdfis.text)
        Shared.pg_selezionato['res_contundente_base'] = int(valoreresc.text)
        Shared.pg_selezionato['res_perforante_base'] = int(valoreresp.text)
        Shared.pg_selezionato['res_taglio_base'] = int(valorerest.text)
        Shared.pg_selezionato['rd_fuoco_base'] = int(valorerdfu.text)
        Shared.pg_selezionato['rd_gelo_base'] = int(valorerdge.text)
        Shared.pg_selezionato['rd_elettro_base'] = int(valorerdel.text)
        Shared.pg_selezionato['res_fuoco_base'] = int(valoreresfu.text)
        Shared.pg_selezionato['res_gelo_base'] = int(valoreresge.text)
        Shared.pg_selezionato['res_elettro_base'] = int(valoreresel.text)
        EquipAttore.equip_npc(Shared.pg_selezionato['nome_in_uso'])
        FinestraPrincipaleMain.FunzioniFinestra.conferma()


    layout.add_widget(
        Button(size_hint=(0.4, 0.1), pos_hint={"x": 0.3, "y": 0.0}, text="Salva", on_release=salva))

    popup.open()


def tipiattaccoopen(*args):
    layout = FloatLayout()
    popup = Popup(title="ATTACCO armi", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(350, 500),
                  auto_dismiss=True)

    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.9}, text="Taglio"))
    valoreatta = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.9},
                           text=str(Shared.pg_selezionato['atk_skill_taglio']))
    layout.add_widget(valoreatta)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.83}, text="Contundenti"))
    valoreatcon = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.83},
                            text=str(Shared.pg_selezionato['atk_skill_contundente']))
    layout.add_widget(valoreatcon)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.76}, text="Perforanti"))
    valoreatpe = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.76},
                           text=str(Shared.pg_selezionato['atk_skill_perforante']))
    layout.add_widget(valoreatpe)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.69}, text="Mani Nude"))
    valoreatmn = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.69},
                           text=str(Shared.pg_selezionato['atk_skill_maninude']))
    layout.add_widget(valoreatmn)
    layout.add_widget(Label(size_hint=(0.2, 0.07), pos_hint={"x": 0.6, "y": 0.69}, text="Tier"))
    valoretimn = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.8, "y": 0.69},
                           text=str(Shared.pg_selezionato['tier_skill_maninude']))
    layout.add_widget(valoretimn)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.62}, text="Corte"))
    valoreatco = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.62},
                           text=str(Shared.pg_selezionato['atk_skill_corte']))
    layout.add_widget(valoreatco)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.55}, text="Medie(lungh.)"))
    valoreatml = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.55},
                           text=str(Shared.pg_selezionato['atk_skill_medie1']))
    layout.add_widget(valoreatml)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.48}, text="Lunghe"))
    valoreatlu = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.48},
                           text=str(Shared.pg_selezionato['atk_skill_lunghe']))
    layout.add_widget(valoreatlu)

    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.41}, text="Precise"))
    valoreatpr = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.41},
                           text=str(Shared.pg_selezionato['atk_skill_precise']))
    layout.add_widget(valoreatpr)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.34}, text="Medie(tipo)"))
    valoreatmt = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.34},
                           text=str(Shared.pg_selezionato['atk_skill_medie2']))
    layout.add_widget(valoreatmt)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.27}, text="Potenti"))
    valoreatpo = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.27},
                           text=str(Shared.pg_selezionato['atk_skill_potenti']))
    layout.add_widget(valoreatpo)

    def salva(*args):
        Shared.pg_selezionato['atk_skill_taglio'] = int(valoreatta.text)
        Shared.pg_selezionato['atk_skill_contundente'] = int(valoreatcon.text)
        Shared.pg_selezionato['atk_skill_perforante'] = int(valoreatpe.text)
        Shared.pg_selezionato['atk_skill_maninude'] = int(valoreatmn.text)
        Shared.pg_selezionato['tier_skill_maninude'] = int(valoretimn.text)
        Shared.pg_selezionato['atk_skill_corte'] = int(valoreatco.text)
        Shared.pg_selezionato['atk_skill_medie1'] = int(valoreatml.text)
        Shared.pg_selezionato['atk_skill_lunghe'] = int(valoreatlu.text)
        Shared.pg_selezionato['atk_skill_precise'] = int(valoreatpr.text)
        Shared.pg_selezionato['atk_skill_medie2'] = int(valoreatmt.text)
        Shared.pg_selezionato['atk_skill_potenti'] = int(valoreatpo.text)
        FinestraPrincipaleMain.FunzioniFinestra.conferma()


    layout.add_widget(
        Button(size_hint=(0.4, 0.15), pos_hint={"x": 0.3, "y": 0.07}, text="Salva", on_release=salva))

    popup.open()


def tipidofesaopen(*args):
    layout = FloatLayout()
    popup = Popup(title="DIFESA armature", title_size=(30),
                  title_align='center', content=layout,
                  size_hint=(None, None), size=(350, 500),
                  auto_dismiss=True)

    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.9}, text="Leggera"))
    valoredile = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.9},
                           text=str(Shared.pg_selezionato['def_skill_leggera']))
    layout.add_widget(valoredile)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.83}, text="Pesante"))
    valoredipe = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.83},
                           text=str(Shared.pg_selezionato['def_skill_pesante']))
    layout.add_widget(valoredipe)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.76}, text="Senza"))
    valoredise = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.76},
                           text=str(Shared.pg_selezionato['def_skill_noarmatura']))
    layout.add_widget(valoredise)
    layout.add_widget(Label(size_hint=(0.35, 0.07), pos_hint={"x": 0.05, "y": 0.69}, text="Scudo"))
    valoredisc = TextInput(size_hint=(0.2, 0.07), pos_hint={"x": 0.4, "y": 0.69},
                           text=str(Shared.pg_selezionato['def_skill_scudo']))
    layout.add_widget(valoredisc)

    def salva(*args):
        Shared.pg_selezionato['def_skill_leggera'] = int(valoredile.text)
        Shared.pg_selezionato['def_skill_pesante'] = int(valoredipe.text)
        Shared.pg_selezionato['def_skill_noarmatura'] = int(valoredise.text)
        Shared.pg_selezionato['def_skill_scudo'] = int(valoredisc.text)

        FinestraPrincipaleMain.FunzioniFinestra.conferma()

    layout.add_widget(
        Button(size_hint=(0.4, 0.15), pos_hint={"x": 0.3, "y": 0.07}, text="Salva", on_release=salva))

    popup.open()

