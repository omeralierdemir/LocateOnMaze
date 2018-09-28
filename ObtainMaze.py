import math


def findBeamWhite(startPoint,direction,img):  #  sisayhta  beyaz arama

    y,x = img.shape
    i,j = startPoint    # ------> i==y j==x
    yon = []
    state = True


    while state:

        kopru = img[i][j]

        if( kopru == 255):  # eşik değeri vermek gerekebilir.

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




def findBeamBlack(startPoint,direction,img):  # beyazda siyah arama

    y,x = img.shape
    i,j = startPoint    # ------> i==y j==x
    yon = []
    state = True



    while state:

        kopru = img[i][j]



        if( kopru == 0):   # eşik değeri vermek gerekebilir

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






def mazeDetection(limit,img):


    maxY,maxX =  img.shape
    maxY,maxX = maxY - 1, maxX - 1  # hocam buradaki amacımız img.shape de kaç adet piksel olduğunu döner y ve x eksenleri için bunların 1 eksiğinden başlattın çünkü tam sayı geldiğinde büyük ihtimalle index aşımı hatası verecekti.
    aralıkY = math.floor(maxY/limit)
    aralıkX = math.floor(maxX/limit)
    points = []
    kosePoints = []
    color = 0  # siyah -----> 1 , beyaz -----> 0



    for i in range(4):
        direction = i

        if(direction == 0):

            y,x = aralıkY, 0

            if(img[y][x] == 255):

                color = 0

            else:
                color = 1

        elif (direction == 1):

            y, x = maxY - 1 , aralıkX


            if (img[y][x] == 255):

                color = 0

            else:
                color = 1


        elif (direction == 2):

            y, x = maxY - aralıkY, maxX - 1  # maxX -1, maxY -1 işlemini zaten yukarıda yapmaktasın. Bir sıkıntı çıkaracağını sanmıyorum ama yinede dikkatli olmalısın



            if (img[y][x] == 255):

                color = 0

            else:
                color = 1


        elif (direction == 3):

            y, x = 0, maxX - aralıkX


            if (img[y][x] == 255):

                color = 0

            else:
                color = 1

        for j in range(limit):

            point = [y,x]

            points.append(whiteOrBlack(point,color,direction,img))


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




def whiteOrBlack(point,color,direction,img):

    state = True
    whitePointList = []
    hudut = 0



    while (state):

        if (color == 0):  # beyaz alan

            oldPointWhite = point

            point = findBeamBlack(point, direction, img)

            if (point == [0, 0]):
                state = False

            color = 1
            whitePointList.append(oldPointWhite)

        elif (color == 1):

            oldPointBlack = point

            point = findBeamWhite(point, direction, img)

            result = wallThickness(oldPointBlack, point, direction)

            if (result >= 3 and result <= 15):

                state = False

                hudut = whitePointList[-1]

            elif (point == [0, 0]):

                state = False


            color = 0

    return hudut



def wallThickness(oldPoint,newPoint,direction):


    farkY =abs(oldPoint[0] - newPoint[0])
    farkX = abs(oldPoint[1] - newPoint[1])

    if(direction in [0,2]):

        result = farkX

    else:

        result = farkY


    return result



def xPoint(y,y1,y2,x1,x2):  # 2 noktası bilinen doğrunun denkleminden


    a = y2 - y1
    b = y - y2

    x = (x2 - x1) * (b/a) + x2

    return x


def yPoint(x,y1,y2,x1,x2):  # 2 noktası bilinen doğrunun denkleminden



    a = x2 - x1
    b = x - x2




    y =  (y2 - y1) * (b/a) + y2
    return y