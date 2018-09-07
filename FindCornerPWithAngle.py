import cv2
import  numpy
import math





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



                if ( i ==  0):


                    i, j = 0, 0

                    break

                i,j = i - 1, j


            elif(direction == 2):  # ------> 2 == 4

                if ( j == 0):

                    i, j = 0, 0

                    break


                i,j = i , j - 1


            elif(direction == 3):  # ------> 3 == 6

                if (y - 1 == i):

                    i, j = 0, 0

                    break



                i,j = i + 1 , j



    return [i,j]


def komsuluk(koordinat,geriYol,limit,img):  # unutma i == y ekseni  j == x ekseni
    i, j = koordinat

    dugum = []
    backPath = geriYol[:]


    dizi= []  # burada hata olabilir...  burada en son 3 eleman eklemede sıkıntı çıkarıyor ondan böyle 2 tane 0-0 dizisi atadın  ----> Hacı burada boş küme ile başlattım. return evresinden önce o elemanı silmelisin
    deg = 0
    dogruYol = 0

    for k in range(limit):
        yon = []

        if (img[i][j + 1] == 255 and [i,j+1] not in backPath): # burda bug var i,j dizinin ilk elamanını 0-0 yapıyorum ama etraflıca düşün
            yon.append(0)
            kopru = 0

        if (img[i + 1][j + 1] == 255 and [i+1,j+1] not in backPath):
            yon.append(1)
            kopru = 1

        if (img[i + 1][j] == 255 and [i+1,j] not in backPath):
            yon.append(2)
            kopru = 2


        if (img[i + 1][j - 1] == 255 and [i+1,j-1] not in backPath):
            yon.append(3)
            kopru = 3

        if (img[i][j - 1] == 255 and [i,j-1] not in backPath):
            yon.append(4)
            kopru = 4

        if (img[i - 1][j - 1] == 255 and [i-1,j-1] not in backPath):
            yon.append(5)
            kopru = 5

        if (img[i - 1][j] == 255 and [i-1,j] not in backPath):
            yon.append(6)  #duvgum değikeninin adını yon olarak değiştir.
            kopru = 6

        if (img[i - 1][j + 1] == 255 and [i-1,j+1] not in backPath):  # buralara dikkat et ve 255 değerine de

            yon.append(7)
            kopru = 7






        if (len(yon) > 1):# dugum içini başka bir değişkene ata sebebi bu şekilde dugum her zaman 0 büyük oluyor. !!!!DİKKAT ETMELİSİN!!!!!!!!!

            dizi.append([i, j])
            dugum = dugumNoktalari(i, j, yon)
            filtreDugum = dugumFiltre(i, j, dugum)  # filtreDugum2 == backPath için dügüm

            if (len(filtreDugum) > 1):


                  # yapılacakları düşün dugum noktası çıkarsa

                filtreDugum2 = dugumFiltre2(i,j,filtreDugum)
                dugum = filtreDugum2[:]
                break

            else:
                backPath.append([i, j])

                i,j = filtreDugum[0]
                backPath.append([i, j])








        elif (len(yon) <= 0 and [i,j]):

            dizi.append([i, j])
            dugum = [[-1, -1, dizi]]

            break




        else:
            #dizi == path
            dizi.append([i,j])

            interim = dugumNoktalari(i, j, yon)  #x,ydi değiştirdim i,j ile hata yapmış olabilirim...

            i,j = interim[0][0],interim[0][1] # sebebi dizi içinde dizi döndermesidir.
            backPath.append([i,j])


    geriDonus = dizi[0]
    return dugum,dizi,geriDonus



def noDuplicateValue(list):



    s = []
    for i in list:
        if i not in s:
            s.append(i)

    return s

def dugumFiltre2(y,x,dugum):

    dizi = komsulukSaptama([y,x],dugum)

    gurultu = []
    for i in dizi:

        for j in dizi:


            y = abs(i[0] - j[0])
            x = abs(i[1] - j[1])

            if([y,x] == [1,0] and i[2] in [1,3,5,7]):

                gurultu.append([i[0],i[1]])

            elif([y,x] == [0,1] and i[2] in [1,3,5,7]):

                gurultu.append([i[0],i[1]])


    gurultu = noDuplicateValue(gurultu)
    for i in range(len(dizi)):

        dizi[i].pop(2)

    for i in gurultu:

        dizi.remove(i)



    return dizi


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

def dugumFiltre(i1,j1,dugum):


    dizi = []

    resDizi = []
    res2Dizi = []

    kopru = 0
    kopru2 = 0



    for i in dugum:
        for j in dugum:





            resDizi.append(abs(i[0] - j[0]))
            res2Dizi.append(abs(i[1] - j[1]))


    resDizi.sort()
    res2Dizi.sort()

    res = resDizi[-1]
    res2 = res2Dizi[-1]

    if(len(dugum) == 3 and res == 0): # dugum sayısı 3 e eşit olduğunda ve geliş guzergahının sagında veya solunda dugumlerin oldugu durum (y   ekseni için) # dikkat et bu durum gerçekleştiğinde dugum sayısı 3 de olsa aralarındaki fark 0 olmuyor. fark sıfır olsa dugum sayısı == 2 olmuş oluyor

        kopru = 0


    elif(len(dugum) ==  3 and res2 == 0):  # dugum sayısı 3 e eşit olduğunda ve geliş guzergahının altında veya ustunde dugumlerin oldugu durum (x ekseni için)

        kopru = 0


    elif(res > 1 or res2 > 1 or (res == 1 and res2 == 1)):


        dizi = dugum[:]
        kopru = 1





    if(kopru == 0):

        for n in dugum:

            if ([i1, j1 + 1] == n):  # ----> 0

                dizi.append(n)


            elif([i1 + 1,j1] == n):  # ----> 2

                dizi.append(n)


            elif ([i1, j1 - 1] == n): # ----> 4

                dizi.append(n)

            elif ([i1 -1, j1] == n):  # ----> 6

                dizi.append(n)


    return dizi


def komsulukSaptama(koordinat,dugum):

    i,j = koordinat
    yon = []

    for k in range(len(dugum)):

        araDeger = [dugum[k][0],dugum[k][1]]


        if ([i,j + 1] == araDeger):  # burda bug var i,j dizinin ilk elamanını 0-0 yapıyorum ama etraflıca düşün
            yon.append(0)

            dugum[k].append(0)
            kopru = 0

        elif ([i + 1,j + 1] == araDeger):
            yon.append(1)
            dugum[k].append(1)
            kopru = 1

        elif ([i + 1,j] == araDeger):
            yon.append(2)
            dugum[k].append(2)
            kopru = 2

        elif ([i + 1,j - 1] == araDeger):
            yon.append(3)
            dugum[k].append(3)
            kopru = 3

        elif ([i,j - 1] == araDeger):
            yon.append(4)
            dugum[k].append(4)
            kopru = 4

        elif ([i - 1,j - 1] == araDeger):
            yon.append(5)
            dugum[k].append(5)
            kopru = 5

        elif ([i - 1,j] == araDeger):
            yon.append(6)

            dugum[k].append(6)# duvgum değikeninin adını yon olarak değiştir.
            kopru = 6

        elif ([i - 1,j + 1] == araDeger):  # buralara dikkat et ve 255 değerine de

            yon.append(7)
            dugum[k].append(7)
            kopru = 7

    return dugum




def edgeDetection(img):


    edges = cv2.Canny(img, 200, 600)




    return edges



def calculationAngle(startP,endP):

    y,x = startP[0] - endP[0], startP[1] - endP[1]



    hipotenus = math.sqrt(x**2 + y**2)

    sinX = x / hipotenus

    teta =  math.asin(sinX)
    teta = teta * 180/math.pi

    return teta


def findRightAngle(kose,backPath,edge):


    flag = 0
    corners = []
    ara = kose[:]
    oldAngle = 0
    state = True
    geriDonus = backPath[:]
    dizi = []
    while (state):

        dugum, path, geriDonus = komsuluk(ara, geriDonus, 15, edge)
        geriDonus = [path[-3], path[-2], path[-1]]
        angle = int(calculationAngle(path[0],path[-1]))




        for i in range(21):



            dizi.append(oldAngle -10 + i)


        if(flag == 0):
            oldAngle = angle

            flag = 1

        else:

            if (angle in dizi):

                oldAngle = angle

            else:

                state = False
                corners.append([path[0], path[-1]])
                # path bilgisini tut

        dizi = []




        ara = path[-1]
    return path[math.floor(len(path)/2)]
def isaret(list):

    bit = []

    for i in list:

        if(i<0):

            bit.append(0)
        else:
            bit.append(1)

    return bit


def rightDetection(limit,edgeImg):


    maxY,maxX =  edgeImg.shape
    maxY,maxX = maxY - 1, maxX - 1  # hocam buradaki amacımız img.shape de kaç adet piksel olduğunu döner y ve x eksenleri için bunların 1 eksiğinden başlattın çünkü tam sayı geldiğinde büyük ihtimalle index aşımı hatası verecekti.
    aralıkY = math.floor(maxY/limit)
    aralıkX = math.floor(maxX/limit)
    points = []
    kosePoints = []
    y,x = aralıkY,aralıkX
    turev = []
    turevler = []
    kopru = []
    index = 0
    flag = 0
    mutlakTurev = []
    mutlakTurevler = []


    for i in range(4):
        direction = i

        if(direction == 0):

            y,x = aralıkY, 0

        elif (direction == 1):

            y, x = maxY - 1 , aralıkX


        elif (direction == 2):

            y, x = maxY - aralıkY, maxX - 1

        elif (direction == 3):

            y, x = 0, maxX - aralıkX

        for j in range(limit):

            point = findBeam([y,x],direction,edgeImg)
            points.append(point)



            if (direction == 0):

                y = y + aralıkY


            elif(direction == 1):

                x = x + aralıkX

            elif(direction == 2):

                y = y - aralıkY

            else:

                x = x - aralıkX



        kosePoints.append(points)
        points = []


    for i in range(len(kosePoints)):
        for j in range(len(kosePoints[0])-1):

            if(len(turev)== 0):

                y1 = kosePoints[i][j][0] - kosePoints[i][j + 1][0]
                x1 = kosePoints[i][j][1] - kosePoints[i][j + 1][1]

                y1M = abs(kosePoints[i][j][0]) - abs(kosePoints[i][j + 1][0])
                x1M = abs(kosePoints[i][j][1]) - abs(kosePoints[i][j + 1][1])

                turev.append([y1,x1])
                mutlakTurev.append([y1M,x1M])
            else:

                if(kosePoints[i][j] == [0,0] or kosePoints[i][j + 1] == [0,0] ):

                    continue

                else:

                    y1 = kosePoints[i][j][0] - kosePoints[i][j+1][0]
                    x1 = kosePoints[i][j][1] - kosePoints[i][j + 1][1]

                    y1M = abs(kosePoints[i][j][0]) - abs(kosePoints[i][j + 1][0])
                    x1M = abs(kosePoints[i][j][1]) - abs(kosePoints[i][j + 1][1])

                    turev.append([y1,x1])
                    mutlakTurev.append([y1M, x1M])
        turevler.append(turev)
        turev = []
        mutlakTurevler.append(mutlakTurev)
        mutlakTurev = []
    for i in range(len(turevler)):
        for j in range(len(turevler[i])-1):

            isaretBit1 = isaret(turevler[i][j])
            isaretBit2 = isaret(turevler[i][j+1])

            if(isaretBit1 != isaretBit2):


                if((mutlakTurevler[i][j+1][0]<=120 or mutlakTurevler[i][j+1][1]<=120) or (mutlakTurevler[i][j+1][0]>=-120 or mutlakTurevler[i][j+1][1]>=-120)):

                    index = j  # j + 1 yapılabilir
                    flag = 1
                    break





        if (flag == 0):
            index = isaretBit2
        kopru.append(index)
        index = 0


    for i in range(len(kopru)):


        kopru[i] = kosePoints[i][math.floor(kopru[i] / 2) + 1]

    return kopru

def dugumDetection(edgeImg):



    geriDugum = []
    result = []
    result2 = []
    kopru = rightDetection(10,edgeImg)
    for i in kopru:

        dugum,path, backPath = komsuluk(i,[[0,0]],1,edgeImg)

        geriDugum.extend(dugum)
        geriDugum.append(backPath)

        result.append(dugum)
        result2.append(geriDugum)
        geriDugum = []


    return result,result2

def cornerDetection(edgeImg):

    result = []
    cornerPoint = []
    dugums,backPaths = dugumDetection(edgeImg)

    for i in range(len(dugums)):

        for j in range(len(dugums[i])):

            ara = findRightAngle(dugums[i][j],backPaths[i],edgeImg)

            cornerPoint.append(ara)
            print()

    # labirentSaptama()
    #dugumSaptama()------> her köşe için 2 tane dügüm noktası toplamda 8 tane dügüm noktası döndürecek back pathle beraber
    #findRightAngle() ------> komsuluk u çağıracak içerisinde farklı açı değeri çıkana kadar.
    # bu fonksiyon içinde de çıkan köşeler derlenip-toparlanacak ve köşeler tespit edilecek



    #notlar hacı komşuluğu dügüm noktalarından başlat bulduğun ilk noktadan değil. Bulduğun ilk noktayıda arguman olarak backPath olarak ver. Böylece geri dönüşleri
    #rahat engellemiş olursun.

    print()
img = cv2.imread("rt1.png",0)
edges = edgeDetection(img)
#a = komsuluk([94,38],[[0,0]],1,edges)

#dugumDetection(edges)
cornerDetection(edges)

#d = findRightAngle([53,149],[[53,149],[53,148]],edges)

print()
#komsuluk([73,47],[[[74,47]]],15,edges)
#komsuluk([66,51],[[[67,50],[67,51]]],15,edges)


#rightDetection(10,edges)