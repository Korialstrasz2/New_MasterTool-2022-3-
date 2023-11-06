import os
import shutil
from random import randrange

from Moduli import SharedData
from docutils.nodes import colspec
# from kivy.core.audio import SoundLoader
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics.transformation import Matrix
import Moduli.SharedData as Shared
from Moduli.Grafica.FinestraPrincipaleMain import FinestraPrincipale
from Moduli.Grafica.FinestraLogin import FinestraLogin
from kivy.uix.slider import Slider

from Moduli.Logica import Oggetti
from kivy.clock import Clock
from kivy.compat import string_types
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import partial, StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import Moduli.SharedData as Shared
from kivy.uix.dropdown import DropDown


class CustomDropDown(DropDown):
    def hide_dropdown(self, *args):
        self.select('')



class Tooltip(Label):
    pass

def cercainfo(ids_input):
    return_string = ""

    risultato = Oggetti.trova_oggetto(ids=ids_input)

    if type(risultato) == dict:
        return_string += "ID : " + str(risultato["ID"])
        return_string += "\n NOME : " + str(risultato["NOME"])
        return_string += "\n TIPO1 : " + str(risultato["TIPO1"])
        return_string += "   |   TIPO2 : " + str(risultato["TIPO2"])
        return_string += "   |   TIPO3 : " + str(risultato["NOME"])
        descrizione = str(risultato["DESCRIZIONE"])
        if len(descrizione) > 80:
            descrizione = descrizione[:70] + "\n" + descrizione[70:]
        return_string += "\n DESCRIZIONE : " + descrizione
        return_string += "\n VALORE : " + str(risultato["VALORE"])
        return_string += "   |   PESO : " + str(risultato["SLOT"])
        if str(risultato["TIPO1"]) in Shared.categorie_armi:
            return_string += "\n ATTACCO : " + str(risultato["EFFETTO1"])
        elif str(risultato["TIPO1"]) in ["armatura", "armaturaanimale", "scudo", "chainmail", "veste"]:
            return_string += "\n DIFESA : " + str(risultato["EFFETTO1"])
        else:
            return_string += "\n EFFETTO1 : " + str(risultato["EFFETTO1"])

        if str(risultato["TIPO1"]) in Shared.categorie_armi:
            return_string += "   |   BONUS TIER : " + str(risultato["EFFETTO2"])
        elif str(risultato["TIPO1"]) in ["armatura", "armaturaanimale", "scudo", "chainmail", "veste"]:
            return_string += "   |   MALUS PA : " + str(risultato["EFFETTO2"])
        else:
            return_string += "   |   EFFETTO2 : " + str(risultato["EFFETTO2"])

        if str(risultato["TIPO1"]) in Shared.categorie_armi:
            return_string += "   |   PA PER ATTACCO : " + str(risultato["EFFETTO3"])
        else:
            return_string += "   |   EFFETTO3 : " + str(risultato["EFFETTO3"])
        return_string += "\n EFFETTO3 : " + str(risultato["EFFETTO3"])
        return_string += "   |   EFFETTO4 : " + str(risultato["EFFETTO4"])
        return_string += "   |   EFFETTO5 : " + str(risultato["EFFETTO5"])
        return_string += "\n EFFETTO6 : " + str(risultato["EFFETTO6"])
        return_string += "   |   EFFETTO7 : " + str(risultato["EFFETTO7"])
    return return_string


class ExpandableButton(Button):
    tooltip_txt = StringProperty('')
    tooltip_cls = ObjectProperty(Tooltip)


    def __init__(self, **kwargs):
        self._tooltip = None
        super(ExpandableButton, self).__init__(**kwargs)
        fbind = self.fbind
        fbind('tooltip_cls', self._build_tooltip)
        fbind('tooltip_txt', self._update_tooltip)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self._build_tooltip()

    def _build_tooltip(self, *largs):
        if self._tooltip:
            self._tooltip = None
        cls = self.tooltip_cls
        if isinstance(cls, string_types):
            cls = Factory.get(cls)
        self._tooltip = cls()
        self._update_tooltip()

    def _update_tooltip(self, *largs):
        txt = self.tooltip_txt
        if type(self.tooltip_txt) != str:
            txt = cercainfo(self.tooltip_txt.text)
        if txt:
            self._tooltip.text = txt
        else:
            self._tooltip.text = ''

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        self._tooltip.pos = pos
        Clock.unschedule(self.enlarge_button)  # cancel scheduled event since I moved the cursor
        self.shrink_button()  # close if it's opened
        if self.collide_point(*self.to_widget(*pos)):
            Clock.schedule_once(self.enlarge_button, 0)

    def shrink_button(self, *args):
        self.size_hint = (0.049, 0.039)
        self.img_collegata.size_hint = (0.049, 0.039)
        for _ in Shared.expanded_images:
            Window.remove_widget(_)
        Shared.expanded_images = []
    def enlarge_button(self, *args):
        self.size_hint = (0.07, 0.055)
        Shared.imgexpanded = Image(size_hint=(0.087, 0.07), pos_hint=self.img_collegata.pos_hint, allow_stretch = True, source = self.img_collegata.source)
        Window.add_widget(Shared.imgexpanded)
        Shared.expanded_images.append(Shared.imgexpanded)


class InfoTextInput(TextInput):
    tooltip_txt = StringProperty('')
    tooltip_cls = ObjectProperty(Tooltip)


    def __init__(self, **kwargs):
        self._tooltip = None
        super(InfoTextInput, self).__init__(**kwargs)
        fbind = self.fbind
        fbind('tooltip_cls', self._build_tooltip)
        fbind('tooltip_txt', self._update_tooltip)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self._build_tooltip()

    def _build_tooltip(self, *largs):
        if self._tooltip:
            self._tooltip = None
        cls = self.tooltip_cls
        if isinstance(cls, string_types):
            cls = Factory.get(cls)
        self._tooltip = cls()
        self._update_tooltip()

    def _update_tooltip(self, *largs):
        txt = self.tooltip_txt
        if type(self.tooltip_txt) != str:
            txt = cercainfo(self.tooltip_txt.text)
        if txt:
            self._tooltip.text = txt
        else:
            self._tooltip.text = ''

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        self._tooltip.pos = pos
        Clock.unschedule(self.display_tooltip)  # cancel scheduled event since I moved the cursor
        self.close_tooltip()  # close if it's opened
        if self.collide_point(*self.to_widget(*pos)):
            from Moduli.Grafica.Popups_Zaino import Zaino
            a = eval(eval(f"self.tooltip_txt"))
            txt = a.text
            txt = cercainfo(txt)
            self._tooltip.text = txt
            Clock.schedule_once(self.display_tooltip, 0.3)

    def close_tooltip(self, *args):
        Window.remove_widget(self._tooltip)

    def display_tooltip(self, *args):
        Window.add_widget(self._tooltip)

class WindowManager(ScreenManager):
    pass

sm = WindowManager()

def estrai_immagine_bg_login():
    lista = os.listdir(SharedData.path_art + "/bgLogin")
    indice = randrange(0, len(lista))
    try:
        shutil.copy(SharedData.path_art + "/bgLogin/" + lista[indice],
                    SharedData.path_art + "/bgLogin/ImgLogin.jpg")
    except:
        pass





class Zoom(ScatterLayout):
    move_lock = False
    scale_lock_left = False
    scale_lock_right = False
    scale_lock_top = False
    scale_lock_bottom = False

    def on_touch_up(self, touch):
        self1 = Shared.finestra
        if (int(str(int(Shared.posizione_immagine[0] - self1.ids.boximgmain.pos[0]))[:4]) in [-2, 0]
                and int(str(int(Shared.posizione_immagine[1] - self1.ids.boximgmain.pos[1]))[:4]) in [-11, -13, -8]):
            self1.ids.boximgmain.pos = (Shared.actx, Shared.acty)
        else:
            Shared.actx = self1.ids.boximgmain.pos[0]
            Shared.acty = self1.ids.boximgmain.pos[1]
        self.move_lock = False
        self.scale_lock_left = False
        self.scale_lock_right = False
        self.scale_lock_top = False
        self.scale_lock_bottom = False
        if touch.grab_current is self:
            touch.ungrab(self)
            x = self.pos[0] / 10
            x = round(x, 0)
            x = x * 10
            y = self.pos[1] / 10
            y = round(y, 0)
            y = y * 10
            self.pos = x, y
            return super(Zoom, self).on_touch_up(touch)

    def transform_with_touch(self, touch):
        changed = False
        x = self.bbox[0][0]
        y = self.bbox[0][1]
        width = self.bbox[1][0]
        height = self.bbox[1][1]
        mid_x = x + width / 2
        mid_y = y + height / 2
        inner_width = width * 0.5
        inner_height = height * 0.5
        left = mid_x - (inner_width / 2)
        right = mid_x + (inner_width / 2)
        top = mid_y + (inner_height / 2)
        bottom = mid_y - (inner_height / 2)

        # just do a simple one finger drag
        if len(self._touches) == self.translation_touches:
            # _last_touch_pos has last pos in correct parent space,
            # just like incoming touch
            dx = (touch.x - self._last_touch_pos[touch][0]) \
                 * self.do_translation_x
            dy = (touch.y - self._last_touch_pos[touch][1]) \
                 * self.do_translation_y
            dx = dx / self.translation_touches
            dy = dy / self.translation_touches
            if (
                    touch.x > left and touch.x < right and touch.y < top and touch.y > bottom or self.move_lock) and not self.scale_lock_left and not self.scale_lock_right and not self.scale_lock_top and not self.scale_lock_bottom:
                self.move_lock = True
                self.apply_transform(Matrix().translate(dx, dy, 0))
                changed = True

        change_x = touch.x - self.prev_x
        change_y = touch.y - self.prev_y
        anchor_sign = 1
        sign = 1
        if abs(change_x) >= 9 and not self.move_lock and not self.scale_lock_top and not self.scale_lock_bottom:
            if change_x < 0:
                sign = -1
            if (touch.x < left or self.scale_lock_left) and not self.scale_lock_right:
                self.scale_lock_left = True
                self.pos = (self.pos[0] + (sign * 10), self.pos[1])
                anchor_sign = -1
            elif (touch.x > right or self.scale_lock_right) and not self.scale_lock_left:
                self.scale_lock_right = True
            self.size[0] = self.size[0] + (sign * anchor_sign * 10)
            self.prev_x = touch.x
            changed = True
        if abs(change_y) >= 9 and not self.move_lock and not self.scale_lock_left and not self.scale_lock_right:
            if change_y < 0:
                sign = -1
            if (touch.y > top or self.scale_lock_top) and not self.scale_lock_bottom:
                self.scale_lock_top = True
            elif (touch.y < bottom or self.scale_lock_bottom) and not self.scale_lock_top:
                self.scale_lock_bottom = True
                self.pos = (self.pos[0], self.pos[1] + (sign * 10))
                anchor_sign = -1
            self.size[1] = self.size[1] + (sign * anchor_sign * 10)
            self.prev_y = touch.y
            changed = True
        return changed

    def on_touch_down(self, touch):
        self1 = Shared.finestra
        x, y = touch.x, touch.y
        self.prev_x = touch.x
        self.prev_y = touch.y

        if touch.is_mouse_scrolling:
            factor = None
            if touch.button == 'scrolldown':
                if self.scale < self.scale_max:
                    factor = 1.15
            elif touch.button == 'scrollup':
                if self.scale > self.scale_min:
                    factor = 1 / 1.15
            if factor is not None:
                self.apply_transform(Matrix().scale(factor, factor, factor),
                                     anchor=touch.pos)

        # if the touch isnt on the widget we do nothing
        if not self.do_collide_after_children:
            if not self.collide_point(x, y):
                return False

        # let the child widgets handle the event if they want
        touch.push()
        touch.apply_transform_2d(self.to_local)
        if super(Scatter, self).on_touch_down(touch):
            # ensure children don't have to do it themselves
            if 'multitouch_sim' in touch.profile:
                touch.multitouch_sim = True
            touch.pop()
            self._bring_to_front(touch)
            return True
        touch.pop()

        # if our child didn't do anything, and if we don't have any active
        # interaction control, then don't accept the touch.
        if not self.do_translation_x and \
                not self.do_translation_y and \
                not self.do_rotation and \
                not self.do_scale:
            return False

        if self.do_collide_after_children:
            if not self.collide_point(x, y):
                return False

        if 'multitouch_sim' in touch.profile:
            touch.multitouch_sim = True
        # grab the touch so we get all it later move events for sure
        self._bring_to_front(touch)
        touch.grab(self)
        self._touches.append(touch)
        self._last_touch_pos[touch] = touch.pos

        return True


def start_kivy():
    estrai_immagine_bg_login()
    kv = Builder.load_file(f"{Shared.path_dati}\interfaccia.kv")
    screens = [FinestraLogin(name="FinestraLogin"),
               FinestraPrincipale(name="FinestraPrincipale")]

    for screen in screens:
        sm.add_widget(screen)

    sm.current = "FinestraLogin"

    class FutureproofApp(App):
        def build(self):
            self.title = "GDR"
            return sm


    Window.size = (1919, 1038)
    Window.top = 0
    Window.left = 0


    FutureproofApp().run()