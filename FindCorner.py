import numpy as np
import cv2




def findBeam(startPoint,direction,imgEdge):  # [y,x] şeklinde olmalı

    y,x = imgEdge.shape
    i,j = startPoint    # ------> i==y j==x
    yon = []
    state = True



    while state:

        kopru = imgEdge[i][j]





        if( kopru == 255):

            state = False
        else:

            if(direction == 0):  #  ------> 0 == 0

                if ( x - 1 ==  j):
                    i, j = 0, 0

                    break

                i, j = i, j + 1

            elif(direction == 1): # -----> 1 == 2



                if ( y - 1 ==  i):


                    i, j = 0, 0

                    break

                i,j = i + 1, j


            elif(direction == 2):  # ------> 2 == 4

                if ( j == 0):

                    i, j = 0, 0

                    break


                i,j = i , j - 1


            elif(direction == 3):  # ------> 3 == 6

                if (i == 0):

                    i, j = 0, 0

                    break



                i,j = i - 1 , j






    return [i,j]








def koordinatTespit(loopNum1,loopNum2):


    img = cv2.imread("ilk.png",0)
    edgeImg = edgeDetection(img)
    kopru = []
    y,x = edgeImg.shape
    pikselFark1 = round(y / loopNum1)
    pikselFark2 = round(x / loopNum2)
    sonuc = []
    dizi1 = []
    dizi2 = []
    dizi3 = []
    dizi4 = []




    dizi1 = diziOlustur([0,0],loopNum1,pikselFark1,0,edgeImg)
    dizi2 = diziOlustur([y-1,0],loopNum2,pikselFark2,3,edgeImg)
    dizi3 = diziOlustur([0,x-1],loopNum1,pikselFark1,2,edgeImg)
    dizi4 = diziOlustur([0,0],loopNum2,pikselFark2,1,edgeImg)



    topDizi = [dizi1,dizi2,dizi3,dizi4]

    for i in topDizi:


        kopru,point = tekrarSayisiBulma(i)

        if(point > 1):

            sonuc.append(kopru)
        else:

            sonuc.append(ortalamaKoordinatNoktasi(i))

    """  p1 = [dizi2[0],dizi1[1]]
       p2 = [dizi2[0],dizi3[1]]
       p3 = [dizi4[0],dizi3[1]]
       p4 = [dizi4[0],dizi1[1]]"""

    p1 = [sonuc[1][0], sonuc[0][1]]
    p2 = [sonuc[1][0], sonuc[2][1]]
    p3 = [sonuc[3][0], sonuc[2][1]]
    p4 = [sonuc[3][0], sonuc[0][1]]

    print(p1,p2,p3,p4)









def diziOlustur(startPoint,loopNum,pikselFark,direction,edgeImg):


    dizi = []
    y,x = startPoint

    for i in range(loopNum):





        dizi.append(findBeam([y,x],direction,edgeImg))

        if (direction == 3 or direction == 1):

            x = x + pikselFark

        else:


            y = y + pikselFark







    return dizi







def edgeDetection(img):


    img = cv2.imread('ilk.png', 0)
    edges = cv2.Canny(img, 800, 1100)




    return edges







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






def filtre(dizi):


    for i in dizi:


        if(i == [0,0]):

            dizi.remove([0,0])


koordinatTespit(20,40)





