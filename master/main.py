import os
import Moduli.SharedData as Shared

path = os.getcwd()
Shared.path_main = path
Shared.path_moduli = f"{path}\Moduli"
Shared.path_grafica = f"{path}\Moduli\Grafica"
Shared.path_dati = f"{path}\Dati"
Shared.path_audio = f"{path}\Audio"
Shared.path_PG_e_Unici = f"{path}\Dati\PG e Unici"
Shared.path_art = f"{path}\Art"
Shared.path_db_nomi = f"{path}\Dati\\Nomi"

import Moduli.Grafica.KivyInput as KivyInput
KivyInput.start_kivy()