import numpy as np
import cv2




def findBeam(startPoint,direction,imgEdge):  # [y,x] şeklinde olmalı


    i,j = startPoint    # ------> i==y j==x
    yon = []
    state = True

    if(direction == 0):

        while state:

            if(imgEdge[i][j] == 225):

                state = False

            else:

                if(direction == 0):  #  ------> 0 == 0

                    i, j = i, j + 1

                elif(direction == 1): # -----> 1 == 2

                    i,j = i + 1, j


                elif(direction == 2):  # ------> 2 == 4


                    i,j = i , j - 1


                elif(direction == 3):  # ------> 3 == 6


                    i,j = i - 1 , j
    return [i,j]






def tekrarSayisiBulma(korNoktalari):  # en çok tekrar eden kordinatı bulup, o koordinatı döndürür ----> [tekrarSayısı,[x,y]]



    dizi = []

    for i in korNoktalari:
        dizi.append([korNoktalari.count(i), i])


    dizi.sort()

    tekrarSa = dizi[0]

    return dizi[1][-1],tekrarSa




def ortalamaKoordinatNoktasi(korNoktalari): # belirli sayıda tekrar etmeyen koordinat noktalrının ortalamasını alarak ortalama bir koordinat noktası döndürür.


    toplamDeg = []
    top1, top2 = 0, 0

    for i in korNoktalari:
        top1 = top1 + i[0]
        top2 = top2 + i[1]



    ort1 = top1/len(korNoktalari)
    ort2 = top1/len(korNoktalari)

    return toplamDeg.append([ort1, ort2])


def koordinatTespit(startPoint,loopNum1,loopNum2,edgeImg):

    kopru = []
    y,x = edgeImg
    pikselFark1 = y / loopNum1
    pikselFark2 = x / loopNum2
    sonuc = []
    dizi1 = []
    dizi2 = []
    dizi3 = []
    dizi4 = []




    dizi1 = diziOlustur(startPoint,loopNum1,pikselFark1,0,edgeImg)
    dizi2 = diziOlustur(startPoint,loopNum2,pikselFark2,3,edgeImg)
    dizi3 = diziOlustur(startPoint,loopNum1,pikselFark1,2,edgeImg)
    dizi4 = diziOlustur(startPoint,loopNum2,pikselFark2,1,edgeImg)



    topDizi = [dizi1,dizi2,dizi3,dizi4]

    for i in topDizi:


        kopru,point = tekrarSayisiBulma(i)

        if(point>1):

            sonuc.append(kopru)
        else:

            sonuc.append(ortalamaKoordinatNoktasi(i))

    """  p1 = [dizi2[0],dizi1[1]]
       p2 = [dizi2[0],dizi3[1]]
       p3 = [dizi4[0],dizi3[1]]
       p4 = [dizi4[0],dizi1[1]]"""

    p1 = [sonuc[1][0],sonuc[0][1]]
    p2 = [sonuc[1][0], sonuc[2][1]]
    p3 = [sonuc[3][0], sonuc[2][1]]
    p4 = [sonuc[3][0], sonuc[0][1]]









def diziOlustur(startPoint,loopNum,pikselFark,direction,edgeImg):


    dizi = []
    y,z = startPoint

    for i in range(loopNum):





        dizi.append(findBeam([y,z],direction,edgeImg))

        if (direction == 3):

            y = y - pikselFark

        else:


            y = y + pikselFark







    return dizi







def edgeDetection(img):


    img = cv2.imread('ilk.png', 0)
    edges = cv2.Canny(img, 800, 1100)




    cv2.imshow("isim", edges)
    cv2.waitKey(0)


    return edges















