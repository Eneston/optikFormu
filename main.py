import cv2 as cv
import utility as ut
import os

p = os.getcwd() #(os işleitm sistemi için bir api)bulundugum dızını gosterıyor
path = os.listdir( p + '/fotograflar/') #bulundugum dızınde kı fotograflara attım ve listeledim
cvppath = "cevapanahtari.png" # bulundugum dızındekı cevap anahtarı
cevapanahtari = cv.imread(cvppath) #İmread -->cevap anahtarı okuyor.
cevapanahtari = ut.preprocess(cevapanahtari)  # utiltydeki preprocess fonksiyonu incele.

# Tum fotograflar belirtilen diziden teker teker okur ve sonuçu excelle yazdırıyor.
for i in range(0,len(path)):
    imgs = cv.imread('./fotograflar/' + path[i]) # fotograflar dızınıdekı tum sırayla fotoları okudu.
    ut.preprocess(imgs) #fotografı biçimlendirdi.




