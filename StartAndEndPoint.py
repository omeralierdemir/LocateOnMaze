import cv2
import numpy as np

import  FindCorner as fc







def komsuluk(y,x,end,green,img):  # unutma i == y ekseni  j == x ekseni
    i, j = y,x
    state = True
    dugum = []


    dizi= [[0,0],[0,0]]  # burada hata olabilir...  burada en son 3 eleman eklemede sıkıntı çıkarıyor ondan böyle 2 tane 0-0 dizisi atadın  ----> Hacı burada boş küme ile başlattım. return evresinden önce o elemanı silmelisin
    deg = 0
    dogruYol = 0

    while state:

        yon = []

        if (img[i][j + 1] == 255 and [i,j+1] not in backPath[-1]): # burda bug var i,j dizinin ilk elamanını 0-0 yapıyorum ama etraflıca düşün
            yon.append(0)
            kopru = 0

        if (img[i + 1][j + 1] == 255 and [i+1,j+1] not in backPath[-1]):
            yon.append(1)
            kopru = 1

        if (img[i + 1][j] == 255 and [i+1,j] not in backPath[-1]):
            yon.append(2)
            kopru = 2


        if (img[i + 1][j - 1] == 255 and [i+1,j-1] not in backPath[-1]):
            yon.append(3)
            kopru = 3

        if (img[i][j - 1] == 255 and [i,j-1] not in backPath[-1]):
            yon.append(4)
            kopru = 4

        if (img[i - 1][j - 1] == 255 and [i-1,j-1] not in backPath[-1]):
            yon.append(5)
            kopru = 5

        if (img[i - 1][j] == 255 and [i-1,j] not in backPath[-1]):
            yon.append(6)  #duvgum değikeninin adını yon olarak değiştir.
            kopru = 6

        if (img[i - 1][j + 1] == 255 and [i-1,j+1] not in backPath[-1]):  # buralara dikkat et ve 255 değerine de

            yon.append(7)
            kopru = 7










        if (len(yon) > 1):# dugum içini başka bir değişkene ata sebebi bu şekilde dugum her zaman 0 büyük oluyor. !!!!DİKKAT ETMELİSİN!!!!!!!!!


            dizi.append([i, j])



            dugum = dugumNoktalari(i, j, yon)








            break  # ana döngüye ait break






        elif (len(yon) <= 0 and [i,j] not  in  end ):

            dizi.append([i, j])
            rangeDetection(i,j,green)
            break







        else:  # yon ==1 ise diye de koşul koyabilirsin
            #dizi == path
            dizi.append([i,j])

            interim = dugumNoktalari(i, j, yon)  #x,ydi değiştirdim i,j ile hata yapmış olabilirim...

            i,j = interim[0][0],interim[0][1] # sebebi dizi içinde dizi döndermesidir.

            backPath.append([dizi[-1],dizi[-2],dizi[-3]])# 3 tane eklemene gerek kalmayabilir

            backPath[-1] = backPath[-1] + backPath[0]  # burada geri dönüşü engellemek için ilk başta gönderdiğin düğüm bilgilerinide ekleyerek ilerliyoruz sisteme yük bindiriyor( fazla veri gerekirse silinecek) ileleyen süreçte elden geçir kodu

    #dizi.pop(0)
    #dizi.pop(0)   bunları diğer durumlar içinde yazabilirsin düğümler yoksa diye


    geriDonus = backPath[-1]
    return dizi,dugum , dogruYol, geriDonus








def dugumNoktalari(x1,y1,dugum):


    deger = []
    for i in dugum:
        x,y = x1,y1
        if (i == 0):

            x, y = x, y + 1

            deger.append([x, y])

        elif (i == 1):

            x, y = x + 1, y + 1
            deger.append([x , y])

        elif (i == 2):

            x, y = x + 1, y
            deger.append([x, y])

        elif (i == 3):

            x, y = x + 1, y - 1
            deger.append([x, y])

        elif (i == 4):

            x, y = x, y - 1
            deger.append([x, y])

        elif (i == 5):

            x, y = x - 1, y - 1
            deger.append([x, y])

        elif (i == 6):

            x, y = x - 1, y
            deger.append([x, y])

        elif (i == 7):

            x, y = x - 1, y + 1
            deger.append([x, y])

    return deger




def rangeDetection(y,x,green):

    p1,p2,p3,p4 = fc.koordinatTespit(20,40)         #buradaki amaç baslangıç noktasına en yakın olan cornerPointleri tespit ederek o noktaya göre thining son bitini kıyaslayarak thining yönünü belirleme
    liste = []
    cornerPoint = [p1,p2,p3,p4]
    cerceveNoktasi = green[0] / 2
    count = 0
    state = 0

    for i in cornerPoint:

        liste = [[i[0] - cerceveNoktasi[0],i[1] - cerceveNoktasi[1],count ]] + liste


        count += 1


    liste.sort()
    corner = liste[0][2]

    if(corner == 0):

        if(p1[0] - y > 0 and p1[1] - x < 0):

            state = 1
        else:
            state = 0

    elif(corner == 1):

        if (p2[0] - y > 0 and p2[1] - x > 0):

            state = 1
        else:
            state = 0


    elif (corner == 2):

        if (p3[0] - y < 0 and p3[1] - x > 0):

            state = 1
        else:
            state = 0

    elif (corner == 3):

        if (p4[0] - y < 0 and p4[1] - x < 0):

            state = 1
        else:
            state = 0



    return state





def findThinPath():
    img = cv2.imread('son.png', 1)

    thn = cv2.ximgproc.thinning(img, None, cv2.ximgproc.THINNING_ZHANGSUEN)

    green,red = detectPoint(img)

    for i in range(green[1][0],green[0][0]):

        for j in range(green[1][1],green[0][1]):

            if(thn[i][j] == 255):

                # burada bulduğun thn noktasını findkornerden gelen değer ile karşılaştır konumuna göre yön ataması yap ve ona göre 2 tane nokta koordinatı dön ( başlangıç ve backPoint olmak üzere)
                komsuluk(i,j,green,thn)



def detectPoint(img):
    green = []
    red = []
    xR, yR = [], []
    xG, yG = [], []

    for i in range(len(img)):
        for j in range(len(img[i])):
            b, g, r = img[i][j]
            if (r < 90 and g > 170 and b < 90):

                green.append([i, j])

            elif (r > 190 and g < 80 and b < 80):  # green ve red için spesifik eşik değerleri belirlenmeli

                red.append([i, j])

    for i in red:
        xR.append(i[0])
        yR.append(i[1])

    xR.sort()
    yR.sort()

    yH, xH = yR[-1], xR[-1]
    yL, xL = yR[0], xR[0]

    for i in green:
        xG.append(i[0])
        yG.append(i[1])

    xG.sort()
    yG.sort()

    yHG, xHG = yG[-1], xG[-1]
    yLG, xLG = yG[0], xG[0]

    cv2.rectangle(img, (yHG, xHG), (yLG, xLG), (255, 0, 0), 1)
    cv2.rectangle(img, (yH, xH), (yL, xL), (255, 0, 0), 1)


    return  [[yHG,xHG],[yLG,xLG]],[[yH,xH],[yL,xL]]



img = cv2.imread("son.png")
detectPoint(img)

cv2.imshow("omer",img)
cv2.waitKey(0)





