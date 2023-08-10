import numpy as np


# input array
in_arr1 = np.array([ 1, 2, 3] )
print ("1st Input array : \n", in_arr1)

in_arr2 = np.array([ 4, 5, 6] )
print ("2nd Input array : \n", in_arr2)

# Stacking the two arrays horizontally
x= np.zeros((3),np.uint8)
out_arr = np.hstack((in_arr1, x, in_arr2))
print ("Output horizontally stacked array:\n ", out_arr)



# import cv2
# from PIL import Image, ImageChops

# # #load the images
# # img1 = cv2.imread('C:\\Users\\swarn\\OneDrive\\Pictures\\image1.jpg')
# # img2 = cv2.imread('C:\\Users\\swarn\\OneDrive\\Pictures\\image2.jpg')

# # assign images
# img1 = Image.open('C:\\Users\\swarn\\OneDrive\\Pictures\\image1.jpg')
# img2 = Image.open('C:\\Users\\swarn\\OneDrive\\Pictures\\image2.jpg')

# # # convert the images to greyscale
# # img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# # img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# diff = ImageChops.difference(img1,img2)

# # # define the function to compute MSE between two images
# # def mse(img1,img2):
# #     h,w=img1.shape
# #     diff = cv2.subtract(img1,img2)
# #     err = np.sum(diff**2)
# #     mse = err/(float(h*w))
# #     return mse, diff


# # error, diff = mse(img1,img2)
# # print("Image matching Error between the two images:",error)

# diff.show()
# # cv2.imshow("difference", diff)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

from tqdm import tqdm
import time
 
 
for i in tqdm (range (30),
               desc="Loading…",
               ascii=False, ncols=75):
    time.sleep(1)
     
print("Complete.")