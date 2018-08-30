import cv2
import  numpy
import math


def komsuluk(koordinat,geriYol,limit,img):  # unutma i == y ekseni  j == x ekseni
    i, j = koordinat

    dugum = []
    backPath = geriYol[:]


    dizi= []  # burada hata olabilir...  burada en son 3 eleman eklemede sıkıntı çıkarıyor ondan böyle 2 tane 0-0 dizisi atadın  ----> Hacı burada boş küme ile başlattım. return evresinden önce o elemanı silmelisin
    deg = 0
    dogruYol = 0

    for k in range(limit):
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
            filtreDugum = dugumFiltre(i, j, dugum)  # filtreDugum2 == backPath için dügüm

            if (len(filtreDugum) > 1):

                  # yapılacakları düşün dugum noktası çıkarsa

                break

            else:
                backPath[-1].append([i, j])

                i,j = filtreDugum[0]
                backPath[-1].append([i, j])








        elif (len(yon) <= 0 and [i,j]):

            dizi.append([i, j])
            dugum = [[-1, -1, dizi]]

            break




        else:
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





def edgeDetection(img):


    edges = cv2.Canny(img, 50, 150)




    return edges



def calculationAngle(startP,endP):

    y,x = startP[0] - endP[0], startP[1] - endP[1]



    hipotenus = math.sqrt(x**2 + y**2)

    sinX = x / hipotenus

    teta = math.atan(sinX)


    return teta


def findRightAngle(dortKose):

    oldAngle = 0
    state = True
    for i in dortKose:

        for j in i:


            while(state):

                path,backPath =komsuluk()
                angle = calculationAngle(path[0],path[-1])

                if(angle-5 <= oldAngle or angle + 5 >= oldAngle):

                    oldAngle = angle

                else:

                    state = False
                    #path bilgisini tut


            state = True


def cornerDetection():


    # labirentSaptama()
    #dugumSaptama()------> her köşe için 2 tane dügüm noktası toplamda 8 tane dügüm noktası döndürecek back pathle beraber
    #findRightAngle() ------> komsuluk u çağıracak içerisinde farklı açı değeri çıkana kadar.
    # bu fonksiyon içinde de çıkan köşeler derlenip-toparlanacak ve köşeler tespit edilecek



    #notlar hacı komşuluğu dügüm noktalarından başlat bulduğun ilk noktadan değil. Bulduğun ilk noktayıda arguman olarak backPath olarak ver. Böylece geri dönüşleri
    #rahat engellemiş olursun.

    print()
img = cv2.imread("rt2.png",0)
edges = edgeDetection(img)
#komsuluk([94,38],[[[93,38]]],15,edges)
#komsuluk([73,47],[[[74,47]]],15,edges)
komsuluk([66,51],[[[67,50],[67,51]]],15,edges)