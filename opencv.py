import cv2
img = cv2.imread("yigit.JPG")
cv2.imshow("resim", img)
# Farklı Renk Filreleri
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gri filtre", gray)
# resmi kaydetmek için
# cv2.imwrite("yeni.jpg",gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

# Resmi Kırpma 0 dan 400. pixele kadar 150px ten 400 px e kadar x ve y koord.
img_crop = img[0:400, 150:400]
cv2.imshow("kesilmiş", img_crop)

# Resmi Büyültme r,c : rowback color
r, c = img_crop.shape[:2]
new_img = cv2.resize(img, (2*r, 2*c))
cv2.imshow("buyuk", new_img)
