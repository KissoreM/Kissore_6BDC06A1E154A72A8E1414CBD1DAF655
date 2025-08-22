import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("image.jpeg")
h,w=img.shape[:2]
cv2.circle(img,(2000,2000),1000,(0,0,255),10)

rm = cv2.getRotationMatrix2D((w//2,h//2),45,1)
rotated=cv2.warpAffine(img,rm,(w,h))

resize=cv2.resize(img,None,fx=2,fy=2)

M = np.float32([[1,0,-1000],[0,1,0]])
translate = cv2.warpAffine(img,M,(w,h))
median = cv2.medianBlur(img,5)

plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()