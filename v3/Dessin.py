# ! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Dessin.py
    classe qui permet le dessin du chemin sur les images
"""
__author__ = "Maxime Tellene"
__copyright__ = "Univ Lyon1, 2020"
__license__ = "Public Domain"
__version__ = "3.0"

from PIL import Image, ImageDraw
from datetime import datetime
from init import couleurs_salles


class Dessin:
    color_line = (0, 0, 0)

    def __init__(self, image_url):
        temp = image_url.split('.')
        temp2 = temp[0] + "_drawn_" + str(datetime.now()) + "." + temp[1]
        temp = temp2.split('/')
        self.nom_image = temp[0] + "/temp/" + temp[1]
        self.image = Image.open(image_url)
        self.dessin = ImageDraw.Draw(self.image, mode="RGBA")

    def __str__(self):
        return str(self.nom_image)

    def display_draw(self):
        self.image.show()

    def save_draw(self):
        self.image.save("" + self.nom_image, "PNG")

    def draw_entree(self):
        self.dessin.line([(238, 133), (352, 133)], fill=self.color_line)

    def relier_entree_1(self):
        self.dessin.line([(352, 133), (406, 220)], fill=self.color_line)

    def traverser_1(self):
        self.dessin.rectangle([(419, 232), (578, 208)], fill=couleurs_salles[1])
        self.dessin.rectangle([(578, 208), (540, 130)], fill=couleurs_salles[1])
        self.dessin.line([(406, 220), (565, 220), (565, 120), (537, 120)], fill=self.color_line)

    def relier_1_2(self, image_1):
        self.dessin.line([(537, 120), (537, 64)], fill=self.color_line)
        image_1.dessin.line([(209, 302), (209, 250), (260, 250)], fill=self.color_line)

    def traverser_2(self):
        self.dessin.rectangle([(290, 238), (330, 310)], fill=couleurs_salles[2])
        self.dessin.rectangle([(330, 310), (392, 274)], fill=couleurs_salles[2])
        self.dessin.line([(260, 250), (310, 250), (310, 295), (392, 295)], fill=self.color_line)

    def relier_et_traverser_3(self):
        self.dessin.rectangle([(484, 274), (590, 309)], fill=couleurs_salles[3])
        self.dessin.rectangle([(590, 309), (560, 73)], fill=couleurs_salles[3])
        self.dessin.rectangle([(560, 73), (488, 113)], fill=couleurs_salles[3])

        self.dessin.line([(392, 295), (575, 295), (575, 82), (387, 82)], fill=self.color_line)

    def raccourci_ss(self):
        self.dessin.line([(392, 295), (410, 295), (460, 243), (460, 140), (400, 82)], fill=self.color_line)

    def traverser_4(self):
        self.dessin.rectangle([(325, 75), (283, 154)], fill=couleurs_salles[4])
        self.dessin.rectangle([(283, 154), (85, 135)], fill=couleurs_salles[4])

        self.dessin.line([(380, 82), (310, 82), (310, 140), (108, 140), (108, 151)], fill=self.color_line)

    def relier_4(self):
        self.dessin.line([(400, 82), (310, 82)], fill=self.color_line)

    def sortir_ss(self):
        self.dessin.line([(108, 151), (108, 250), (127, 250), (127, 300)], fill=self.color_line)

    def pas_passer_ss(self):
        self.dessin.line([(537, 120), (402, 120)], fill=self.color_line)

    def relier_ss_etage0(self):
        self.dessin.line([(455, 64), (455, 120), (402, 120)], fill=self.color_line)

    def raccourci_etage_0_1(self):
        self.dessin.line([(402, 120), (402, 12), (183, 12), (183, 70)], fill=self.color_line)

    def relier_1_5(self):
        self.dessin.line([(402, 120), (355, 120)], fill=self.color_line)

    def relier_entree_5(self):
        self.dessin.line([(352, 133), (355, 120)], fill=self.color_line)

    def traverser_5(self):
        self.dessin.rectangle([(376, 103), (331, 54)], fill=couleurs_salles[5])
        self.dessin.rectangle([(331, 54), (300, 91)], fill=couleurs_salles[5])
        self.dessin.line([(355, 120), (355, 70), (300, 70)], fill=self.color_line)

    def relier_5_6(self):
        self.dessin.line([(300, 70), (285, 70)], fill=self.color_line)

    def traverser_6(self):
        self.dessin.rectangle([(285, 53), (195, 90)], fill=couleurs_salles[6])
        self.dessin.line([(285, 70), (183, 70)], fill=self.color_line)

    def relier_etage_0_7(self, image1):
        self.dessin.line([(183, 70), (72, 70)], fill=self.color_line)
        image1.dessin.line([(76, 36), (150, 36)], fill=self.color_line)

    def traverser_7(self):
        self.dessin.rectangle([(145, 19), (212, 56)], fill=couleurs_salles[7])
        self.dessin.line([(140, 36), (200, 36)], fill=self.color_line)

    def raccourci_etage_1_1(self):
        self.dessin.rectangle([(145, 19), (212, 56)], fill=couleurs_salles[7])
        self.dessin.line([(145, 36), (186, 36), (150, 85), (150, 236)], fill=self.color_line)

    def relier_7_8(self):
        self.dessin.line([(200, 36), (225, 36)], fill=self.color_line)

    def traverser_8(self):
        self.dessin.rectangle([(240, 56), (335, 20)], fill=couleurs_salles[8])
        self.dessin.line([(225, 36), (360, 36)], fill=self.color_line)

    def relier_8_9(self):
        self.dessin.line([(360, 36), (360, 82)], fill=self.color_line)

    def traverser_9(self):
        self.dessin.rectangle([(404, 74), (583, 91)], fill=couleurs_salles[9])
        self.dessin.rectangle([(583, 91), (546, 198)], fill=couleurs_salles[9])
        self.dessin.line([(360, 82), (563, 82), (563, 185), (535, 185)], fill=self.color_line)

    def raccourci_etage_1_2(self):
        self.dessin.line([(360, 36), (360, 90), (535, 185)], fill=self.color_line)

    def raccourci_etage_1_3(self):
        self.dessin.line([(535, 185), (535, 342), (280, 342), (280, 237)], fill=self.color_line)

    def relier_raccourci_etage1_2_10(self):
        self.dessin.line([(535, 185), (465, 185)], fill=self.color_line)

    def relier_9_10(self):
        self.dessin.line([(465, 185), (535, 185)], fill=self.color_line)

    def traverser_10(self):
        self.dessin.rectangle([(480, 175), (391, 195)], fill=couleurs_salles[10])
        self.dessin.polygon([(391, 195), (365, 170), (387, 170), (403, 175)], fill=couleurs_salles[10])
        self.dessin.rectangle([(365, 170), (387, 132)], fill=couleurs_salles[10])
        self.dessin.line([(465, 185), (390, 185), (378, 171), (378, 125)], fill=self.color_line)

    def relier_10_11(self):
        self.dessin.line([(378, 125), (351, 125), (351, 200)], fill=self.color_line)

    def relier_8_11(self):
        self.dessin.line([(360, 36), (348, 111), (351, 200)], fill=self.color_line)

    def traverser_11(self):
        self.dessin.rectangle([(300, 257), (385, 216)], fill=couleurs_salles[11])
        self.dessin.line([(351, 200), (351, 237), (280, 237)], fill=self.color_line)

    def relier_11_12(self):
        self.dessin.line([(280, 237), (270, 237)], fill=self.color_line)

    def traverser_12(self):
        self.dessin.rectangle([(260, 219), (177, 255)], fill=couleurs_salles[12])
        self.dessin.line([(270, 237), (150, 237)], fill=self.color_line)

    def sortie_etage_1(self):
        self.dessin.line([(150, 237), (62, 237)], fill=self.color_line)

    def sortie_depuis_etage_1(self):
        self.dessin.rectangle([(140, 250), (237, 289)], fill=couleurs_salles[13])
        self.dessin.line([(55, 271), (185, 271)], fill=self.color_line)

    def raccourci_etage_0_2(self):
        self.dessin.rectangle([(140, 250), (237, 289)], fill=couleurs_salles[13])
        self.dessin.line([(183, 70), (144, 119), (144, 218), (185, 271)], fill=self.color_line)

    def sortie(self):
        self.dessin.rectangle([(250, 250), (318, 289)], fill=couleurs_salles[14])
        self.dessin.rectangle([(333, 289), (381, 239)], fill=couleurs_salles[15])
        self.dessin.line([(185, 271), (352, 271), (352, 222), (328, 202), (238, 202)], fill=self.color_line)
