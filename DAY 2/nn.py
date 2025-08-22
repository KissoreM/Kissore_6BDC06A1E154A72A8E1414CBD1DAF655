import cv2
import matplotlib.pyplot as plt


img = cv2.imread("image.jpg")

gaussian = cv2.GaussianBlur(img,(3,3),0)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,100)

threshold, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
