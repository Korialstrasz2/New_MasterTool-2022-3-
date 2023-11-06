import Moduli.SharedData as Shared
from Moduli.Grafica import FinestraPrincipaleMain

listazoomimmagini = [0.12,0.3,0.5,0.7,1.0,1.05,1.11,1.18,1.24,1.31,1.39,1.47,1.55,1.64,1.74,1.84,1.94,
                     2.05,2.17,2.29,2.42,2.56,2.71,2.86,3.03,3.20,3.38,3.57,3.78,3.99,4.22,4.46,4.72,4.99,
                     5.27,5.57,5.89,6.22,6.58,6.96,7.35,7.77,8.21,8.68,9.18,9.70,10.26,10.84,11.46,12.11,
                     12.80,13.53,14.30,15.12,17]
zoomattuale = 4

def taglia_decimali(numero):
    stringa = str(float(numero))
    divisi = stringa.split(".")
    interi = divisi[0]
    decimali = divisi[1]
    totale = f"{interi}.{decimali[:2]}"
    return totale

def resetimgmain():
    global zoomattuale
    self1 = Shared.finestra
    self1.ids.boximgmain.scale = 1.0
    zoomattuale = 4
    Shared.offset_immagine = [0, 0]
    self1.ids.boximgmain.pos = Shared.posizione_immagine
    self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(Shared.offset_immagine)}"


def mostradettagliimgmain():
    global listazoomimmagini
    self1 = Shared.finestra
    Shared.offset_immagine[0] = int(
        str(int(Shared.posizione_immagine[0] - self1.ids.boximgmain.pos[0]))[:4])
    Shared.offset_immagine[1] = int(
        str(int(Shared.posizione_immagine[1] - self1.ids.boximgmain.pos[1]))[:4])
    self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(Shared.offset_immagine)}"

def imgsu():
    self1 = Shared.finestra
    ximg,yimg = self1.ids.boximgmain.pos
    yimg -= 50
    self1.ids.boximgmain.pos = (ximg, yimg)
    Shared.offset_immagine[1] = int(str(int(Shared.posizione_immagine[1] - self1.ids.boximgmain.pos[1]))[:4])
    self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(Shared.offset_immagine)}"
def imggiu():
    self1 = Shared.finestra
    ximg,yimg = self1.ids.boximgmain.pos
    yimg += 50
    self1.ids.boximgmain.pos = (ximg, yimg)
    Shared.offset_immagine[1] = int(str(int(Shared.posizione_immagine[1] - self1.ids.boximgmain.pos[1]))[:4])
    self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(Shared.offset_immagine)}"
def imgsinistra():
    self1 = Shared.finestra
    ximg,yimg = self1.ids.boximgmain.pos
    ximg += 50
    Shared.offset_immagine[0] = int(str(int(Shared.posizione_immagine[0] - self1.ids.boximgmain.pos[0]))[:4])
    self1.ids.boximgmain.pos = (ximg, yimg)
    self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(Shared.offset_immagine)}"
def imgdestra():
    self1 = Shared.finestra
    ximg,yimg = self1.ids.boximgmain.pos
    ximg -= 50
    Shared.offset_immagine[0] = int(str(int(Shared.posizione_immagine[0] - self1.ids.boximgmain.pos[0]))[:4])
    self1.ids.boximgmain.pos = (ximg, yimg)
    self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(Shared.offset_immagine)}"

def imgscalapiupiu():
    global zoomattuale
    global listazoomimmagini
    self1 = Shared.finestra
    try:
        self1.ids.boximgmain.scale = float(taglia_decimali(float(listazoomimmagini[zoomattuale + 7])))
        zoomattuale += 7
        self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(FinestraPrincipaleMain.Temp.offset_immagine)}"
    except:
        pass

def imgscalapiu():
    global zoomattuale
    global listazoomimmagini
    self1 = Shared.finestra
    try:
        self1.ids.boximgmain.scale = float(taglia_decimali(float(listazoomimmagini[zoomattuale + 1])))
        zoomattuale += 1
        self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(FinestraPrincipaleMain.Temp.offset_immagine)}"
    except:
        pass

def imgscalamenomeno():
    global zoomattuale
    global listazoomimmagini
    self1 = Shared.finestra
    try:
        self1.ids.boximgmain.scale = float(taglia_decimali(float(listazoomimmagini[zoomattuale - 7])))
        zoomattuale -= 7
        self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(FinestraPrincipaleMain.Temp.offset_immagine)}"
    except:
        pass

def imgscalameno():
    global zoomattuale
    global listazoomimmagini
    self1 = Shared.finestra
    try:
        self1.ids.boximgmain.scale = float(taglia_decimali(float(listazoomimmagini[zoomattuale - 1])))
        zoomattuale -= 1
        self1.ids.bottonedettagliimgmain.text = f"scala: {taglia_decimali(self1.ids.boximgmain.scale)}\n{str(FinestraPrincipaleMain.Temp.offset_immagine)}"
    except:
        pass


def noimmaginemain():
    self1 = Shared.finestra
    if self1.ids.immaginemain.source != 'Art/immagini/vuoto.png':
        FinestraPrincipaleMain.Temp.immagine_attiva = self1.ids.immaginemain.source
        self1.ids.immaginemain.source = 'Art/immagini/vuoto.png'
    else:
        self1.ids.immaginemain.source = FinestraPrincipaleMain.Temp.immagine_attiva

def ombra():
    self1 = Shared.finestra
    if self1.ids.immegineombra.source != 'Art/immagini/vuoto.png':
        self1.ids.immegineombra.source = 'Art/immagini/vuoto.png'
    else:
        self1.ids.immegineombra.source = 'Art/immagini/ombra.png'
