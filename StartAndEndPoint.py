import cv2
import numpy as np






def findThinPath():
    img = cv2.imread('son.png', 1)

    thn = cv2.ximgproc.thinning(img, None, cv2.ximgproc.THINNING_ZHANGSUEN)

    green,red = detectPoint(img)

    for i in range(green[1][0],green[0][0]):

        for j in range(green[1][1],green[0][1]):

            if(thn[i][j] == 255):

                # burada bulduğun thn noktasını findkornerden gelen değer ile karşılaştır konumuna göre yön ataması yap ve ona göre 2 tane nokta koordinatı dön ( başlangıç ve backPoint olmak üzere)




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



detectPoint()

cv2.imshow("omer",img)
cv2.waitKey(0)



