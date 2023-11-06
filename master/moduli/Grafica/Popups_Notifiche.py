import Moduli.SharedData as Shared
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

nomi_in_uso_norazza = []

def nodigit(*args, stringa):
    popup = Popup(title=f"{stringa} non è un valore valido", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def norazza(nome, nomeinuso, *args):
    if nomeinuso not in nomi_in_uso_norazza:
        nomi_in_uso_norazza.append(nomeinuso)
        popup = Popup(title=f"Valori razza di {nome} non caricati. controlla il nome", title_size=(30),
                      title_align='center',
                      size_hint=(None, None), size=(700, 200),
                      auto_dismiss=True)
        popup.open()
    else:
        return


def noarma(*args, stringa):
    popup = Popup(title=f"{stringa} non è un'arma", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def boxcheck(*args):
    popup = Popup(title=f"Controlla i box", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def nosave(*args):
    popup = Popup(title=f"Impossibile salvare. Controlla i box skill", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def noarmatura(*args, stringa):
    popup = Popup(title=f"{stringa} non è un set di armatura", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def noscudo(*args, stringa):
    popup = Popup(title=f"{stringa} non è uno scudo", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def noeq(*args, stringa):
    popup = Popup(title=f"{stringa} non è un oggetto equipaggiabile", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def nochainmail(*args, stringa):
    popup = Popup(title=f"{stringa} non è una chainmail", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def noveste(*args, stringa):
    popup = Popup(title=f"{stringa} non è una veste", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def noslotselezionato():
    popup = Popup(title=f"Nessuno slot selezionato", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()


def noidselezionato(*args):
    popup = Popup(title="Nessun Indirizzo Valido", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()

def pg_gia_importato(nome_pg):
    popup = Popup(title=f"{nome_pg[6:]} già importato. Selezionalo\n di nuovo per importarlo nuovamente.", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()

def livello(livello_calcolato, livello_attuale):
    popup = Popup(title=f"Livello calcolato: {livello_calcolato}\nlivello attuale: {livello_attuale}", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()

def guida_crea_pg_da_npc(*args):
    testo = """Assicurati di aver IMPORTATO un npc. Rinomina
     il suo id da __skeever__ (o chi per lui) a __pg__. 
     A quel punto cambiagli il nome in quello che vuoi, tipo Garzuul
    """
    popup = Popup(title=f"{testo}", title_size=(30),
                  title_align='center',
                  size_hint=(None, None), size=(700, 200),
                  auto_dismiss=True)
    popup.open()

def custom_popup(*args,titolo,contenuto):
    box = BoxLayout()
    testo = titolo
    popup = Popup(title=f"{testo}", title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(700, 350),
                  auto_dismiss=True)
    box.add_widget(TextInput(text = contenuto))
    popup.open()