import cv2
import numpy as np

import math

import FindCorner as fc


def komsuluk(y,x,geriYol,green,img):  # unutma i == y ekseni  j == x ekseni
    i, j = y,x
    state = True
    dugum = []
    backPath = geriYol[:]


    dizi= []  # burada hata olabilir...  burada en son 3 eleman eklemede sıkıntı çıkarıyor ondan böyle 2 tane 0-0 dizisi atadın  ----> Hacı burada boş küme ile başlattım. return evresinden önce o elemanı silmelisin
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

            for k in range(len(dugum)):
                dugum[k] = dugum[k] + [dizi]




            break  # ana döngüye ait break



        elif (len(yon) <= 0 and [i,j]):

            dizi.append([i, j])
            dugum = [[-1, -1, dizi]]

            break




        else:  # yon ==1 ise diye de koşul koyabilirsin
            #dizi == path
            dizi.append([i,j])

            interim = dugumNoktalari(i, j, yon)  #x,ydi değiştirdim i,j ile hata yapmış olabilirim...

            i,j = interim[0][0],interim[0][1] # sebebi dizi içinde dizi döndermesidir.
            backPath[-1].append([i,j])


    geriDonus = dizi[-1]
    return dugum, geriDonus




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


    yPozitif,xPozitif,yNeg,xNeg = 0,0,0,0
    p1,p2,p3,p4 = fc.koordinatTespit(20,40)         #buradaki amaç baslangıç noktasına en yakın olan cornerPointleri tespit ederek o noktaya göre thining son bitini kıyaslayarak thining yönünü belirleme
    liste = []
    cornerPoint = [p1,p2,p3,p4]
    cerceveNoktasi = [math.ceil(green[0][0] / 2) , math.ceil(green[0][1] / 2)] # green çerçevesinin en orta noktası baz alınarak işlem yapılmaya çalışılmıştır

    count = 0
    state = 0


    for i in cornerPoint:
        liste = [[i[0] - y, i[1] - x]]

        if(liste[0] > 0):

            yPozitif = yPozitif + 1

        elif (liste[0] < 0):

            yNeg =  yNeg + 1

        if (liste[1] > 0):

            xPozitif = xPozitif + 1

        elif (liste[1] < 0):

            xNeg = xNeg + 1


    if((yPozitif == 2 and  yNeg == 2 ) and (xPozitif == 2 and xNeg == 2)):

        state = True
    else:

        state = False



    return state





def findThinPath():


    safDugum = []
    araDugum = []
    state2 = False
    img = cv2.imread('son.png', 0)
    img3 = cv2.imread('son.png', 1)

    thn = cv2.ximgproc.thinning(img, None, cv2.ximgproc.THINNING_ZHANGSUEN)

    green,red = detectPoint(img3)

    for i in range(green[1][0],green[0][0]):

        for j in range(green[1][1],green[0][1]):




            if(thn[i][j] == 255):

                dugumler = [[i,j]]
                backPath = [[i,j]]
                araBackPath = [[i, j]]
                for k in range(2):

                    for l in dugumler:



                        ara,back = komsuluk(l[0],l[1],[araBackPath],green,thn)
                        araDugum.extend(ara)


                    for a in araDugum:

                        backPath.append([a[0],a[1]])
                        safDugum.append([a[0],a[1]])


                    backPath.append(back)

                    araBackPath = backPath[:]


                    dugumler = safDugum[:]
                    safDugum = []


                    araDugum = []



                for a in dugumler:

                    state = rangeDetection(a[0],a[1],green)



                    if(state):

                        startPoint = a[-1][1]
                        backPoint = a[-1][0]
                        state2 = True
                        break




            if(state2):

                break

        if(state2):

            break



    return backPoint,startPoint


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
        xR.append(i[1])
        yR.append(i[0])

    xR.sort()
    yR.sort()

    yH, xH = yR[-1], xR[-1]
    yL, xL = yR[0], xR[0]

    for i in green:
        xG.append(i[1])
        yG.append(i[0])

    xG.sort()
    yG.sort()

    yHG, xHG = yG[-1], xG[-1]
    yLG, xLG = yG[0], xG[0]

    cv2.rectangle(img, (yHG, xHG), (yLG, xLG), (255, 0, 0), 1)
    cv2.rectangle(img, (yH, xH), (yL, xL), (255, 0, 0), 1)


    return  [[yHG,xHG],[yLG,xLG]],[[yH,xH],[yL,xL]]



img1 = cv2.imread("son.png")
findThinPath()
#detectPoint(img1)
cv2.imshow("omer",img1)
cv2.waitKey(0)





