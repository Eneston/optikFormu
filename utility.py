import cv2 as cv

def preprocess(img):
    tmpdraw = img.copy()  #büyük dikdörtgeni çizmek için gercek resmin bir kopyası alındı.
    bigcount = img.copy()
    canny = cv.Canny(img,10,50) # resmin kenarları algılandı
    countours,hierarchy = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE) #Resmin kenarları çizildi.
    cv.drawContours(tmpdraw,countours,-1,(255,0,0),10) #Kenarların çizimi gerçekleşti.
    cv.imshow("a",tmpdraw) # burada deneme amaclı ekranda gösterdik
    cv.waitKey(0) 
    

    big = rectangles(countours) # burada en büyük dikdörtgeni almak için fonksıyon cagırdık.
    
    # Burada dış dikdörtgen algılıyor.
    peri = cv.arcLength(big,True) #cevre 
    aprox = cv.approxPolyDP(big,0.02*peri,True) 
    biggestCount = aprox
    #

    cv.drawContours(bigcount,biggestCount,-1,(255,0,0),10) # en buyuk dikdörtgen çizdik
    cv.imshow("a",bigcount) # burada deneme amaclı ekranda gösterdik.
    cv.waitKey(0) 

def rectangles(countours): # Dikdörtgen adı altında fonksiyon ismi tanımladım ve içine countours parametresini verdim. 
    rect = [] # rect adında boş bir dizi oluşturdum.
    for i in countours:
        area = cv.contourArea(i) # Döngüye alıp çizilen kenarların her bırı ıcın bır alan hesabı yaptı.

        if area > 500: 
            peri = cv.arcLength(i,True) # arclength cevre hesabı yaptırdık.
            aprox = cv.approxPolyDP(i,peri * 0.02,True) # approxplydp ile çizilen kenarın kac kenarlı oldugu bulmaya çalışıyor.
            
            if len(aprox) == 4: # kenar sayısı 4 olanlarını aldım.
                rect.append(i) # rect dizisine ekledik
    rect = sorted(rect,key=cv.contourArea,reverse=True) # dikdörtgenleri sıraladık
    return rect[0] # en buyuk dikdörtgen aldı.