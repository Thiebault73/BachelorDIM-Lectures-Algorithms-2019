# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:02:50 2019

@author: bebertt
"""

import cv2
import numpy as np

img_gray=cv2.imread("img/s3.png",0)
img_bgr=cv2.imread("img/s3.png",1)
img=cv2.imread("img/s3.png")

# permet de connaître la taille d'une image
'''
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)

'''
cv2.imshow("BGR image", img)
cv2.waitKey() 

# renvoir le nombre de ligne, colone et couleur
print("Gray levels image shape =" +str(img_gray.shape))
print("BGR image shape =" + str(img_bgr.shape))
  
'''
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        for cha in range(img.shape[2]):
            img[row,col,cha]=255-img[row,col,cha]
'''
## autre opération possible 
img=255-img

cv2.imshow("BGR image", img)
cv2.waitKey()