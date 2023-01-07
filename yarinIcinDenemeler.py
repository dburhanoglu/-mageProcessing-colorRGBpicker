import cv2

def RGBbul1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        colorsBGR1 = image[y, x]
        colorsRGB1 = tuple(reversed(colorsBGR1))
        print(" İşaretlediğiniz ürünün renk RGB degeri {} ".format(colorsRGB1))

image = cv2.imread("selpink.jpg")
imS = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)


cv2.namedWindow('RGBbul1')
cv2.moveWindow('RGBbul1', 40,30)
cv2.setMouseCallback('RGBbul1', RGBbul1)

while (1):
    cv2.imshow('RGBbul1', imS)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()



def RGBbul2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        colorsBGR2 = image[y, x]
        colorsRGB2 = tuple(reversed(colorsBGR2))
        print(" İşaretlediğiniz diğer ürünün renk RGB degeri {} ".format(colorsRGB2))



image2 = cv2.imread("kazak.jpg")
imS2 = cv2.resize(image2, ( 0 , 0 ), fx = 0.4 , fy = 0.4)

cv2.namedWindow('RGBbul2')
cv2.moveWindow('RGBbul2', 40,30)
cv2.setMouseCallback('RGBbul2', RGBbul2)


while (1):
    cv2.imshow('RGBbul2', imS2)
    if cv2.waitKey(10) & 0xFF == 27:
        break


cv2.destroyAllWindows()


