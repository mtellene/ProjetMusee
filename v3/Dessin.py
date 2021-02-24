from PIL import Image, ImageDraw
from datetime import datetime


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
        self.dessin.line([(215, 124), (315, 124)], fill=self.color_line)

    def traverser_1(self):
        self.dessin.line([(345, 197), (510, 197), (510, 105), (482, 105)], fill=self.color_line)

    def relier_entree_1(self):
        self.dessin.line([(315, 124), (345, 197)], fill=self.color_line)

    def traverser_2(self):
        self.dessin.line([(260, 226), (295, 226), (295, 260), (392, 260)], fill=self.color_line)

    def relier_1_2(self, image_1):
        self.dessin.line([(482, 105), (482, 57)], fill=self.color_line)
        image_1.dessin.line([(200, 270), (200, 226), (260, 226)], fill=self.color_line)

    def relier_et_traverser_3(self):
        self.dessin.line([(392, 260), (530, 260), (530, 82), (387, 82)], fill=self.color_line)

    def raccourci_ss(self):
        self.dessin.line([(392, 260), (424, 221), (424, 130), (387, 82)], fill=self.color_line)

    def traverser_4(self):
        self.dessin.line([(285, 82), (285, 130), (108, 130), (108, 151)], fill=self.color_line)

    def relier_4(self):
        self.dessin.line([(387, 82), (285, 82)], fill=self.color_line)

    def sortir_ss(self):
        self.dessin.line([(108, 151), (108, 224), (127, 224), (127, 272)], fill=self.color_line)

    def pas_passer_ss(self):
        self.dessin.line([(482, 105), (363, 105)], fill=self.color_line)

    def relier_ss_etage0(self):
        self.dessin.line([(363, 105), (410, 105), (410, 57)], fill=self.color_line)

    def raccourci_etage_0_1(self):
        self.dessin.line([(363, 105), (363, 10), (166, 10), (166, 66)], fill=self.color_line)

    def traverser_5(self):
        self.dessin.line([(324, 105), (324, 66), (275, 66)], fill=self.color_line)

    def relier_entree_5(self):
        self.dessin.line([(315, 124), (324, 105)], fill=self.color_line)

    def relier_1_5(self):
        self.dessin.line([(363, 105), (324, 105)], fill=self.color_line)

    def traverser_6(self):
        self.dessin.line([(262, 66), (166, 66)], fill=self.color_line)

    def relier_5_6(self):
        self.dessin.line([(275, 66), (166, 66)], fill=self.color_line)

    def traverser_7(self):
        self.dessin.line([(130, 55), (200, 55)], fill=self.color_line)

    def raccourci_etage_1_1(self):
        self.dessin.line([(130, 55), (165, 55), (132, 100), (132, 235)], fill=self.color_line)

    def relier_etage_0_7(self, image1):
        self.dessin.line([(166, 66), (66, 66)], fill=self.color_line)
        image1.dessin.line([(67, 55), (130, 55)], fill=self.color_line)

    def traverser_8(self):
        self.dessin.line([(225, 55), (315, 55)], fill=self.color_line)

    def relier_7_8(self):
        self.dessin.line([(200, 55), (225, 55)], fill=self.color_line)

    def traverser_9(self):
        self.dessin.line([(351, 95), (505, 95), (505, 185), (478, 185)], fill=self.color_line)

    def relier_8_9(self):
        self.dessin.line([(315, 55), (315, 95), (351, 95)], fill=self.color_line)

    def raccourci_etage_1_2(self):
        self.dessin.line([(315, 55), (315, 95), (335, 110), (465, 185)], fill=self.color_line)

    def raccourci_etage_1_3(self):
        self.dessin.line([(478, 185), (478, 327), (250, 327), (250, 235)], fill=self.color_line)

    def traverser_10(self):
        self.dessin.line([(456, 185), (350, 185), (337, 175), (337, 132)], fill=self.color_line)

    def relier_raccourci_etage1_2_10(self):
        self.dessin.line([(456, 185), (465, 185)], fill=self.color_line)

    def relier_9_10(self):
        self.dessin.line([(456, 185), (478, 185)], fill=self.color_line)

    def traverser_11(self):
        self.dessin.line([(320, 200), (320, 235), (250, 235)], fill=self.color_line)

    def relier_10_11(self):
        self.dessin.line([(337, 132), (315, 132), (315, 175), (320, 200)], fill=self.color_line)

    def relier_8_11(self):
        self.dessin.line([(315, 55), (315, 132), (315, 175), (320, 200)], fill=self.color_line)

    def traverser_12(self):
        self.dessin.line([(235, 235), (132, 235)], fill=self.color_line)

    def relier_11_12(self):
        self.dessin.line([(235, 235), (250, 235)], fill=self.color_line)

    def sortie_etage_1(self):
        self.dessin.line([(132, 235), (54, 235)], fill=self.color_line)

    def sortie_depuis_etage_1(self):
        self.dessin.line([(53, 245), (325, 245), (325, 200), (297, 183), (215, 183)], fill=self.color_line)

    def raccourci_etage0_2(self):
        self.dessin.line([(166, 66), (134, 107), (134, 200), (170, 245)], fill=self.color_line)

    def sortie_depuis_raccourci_etage0(self):
        self.dessin.line([(170, 245), (325, 245), (325, 200), (297, 183), (215, 183)], fill=self.color_line)

