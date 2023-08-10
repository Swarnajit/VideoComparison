import numpy as np
import cv2
import imutils
from skimage.metrics import structural_similarity


location1 = 'C:\\Users\\swarn\\Videos\\Captures\\Video1\\'
location2 = 'C:\\Users\\swarn\\Videos\\Captures\\Video2\\'
resultStorage = 'C:\\Users\\swarn\\Videos\\Captures\\'

class imageComparison:

    def compareImagesAtFrame(startingTime,frameIndex):
        path1 = location1 + str(frameIndex) + '.jpg'
        path2 = location2 + str(frameIndex) + '.jpg'

        # Loading images
        img1 = cv2.resize(cv2.imread(path1),(500,500))
        img2 = cv2.resize(cv2.imread(path2),(500,500))
        # Grayscale
        gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

        # find the difference
        # # # # # res = cv2.absdiff(gray1,gray2)
        # # # # # res=res.astype(np.uint8)
        # # # # # percentage = (np.count_nonzero(res) * 100)/ res.size
        # # # # # print(percentage)
        # # # # # diff = cv2.absdiff(gray1,gray2)
        # # # # # cv2.imwrite('C:\\Users\\swarn\\Videos\\Captures\\absdiff.jpg',diff)
        # cv2.imshow("diff(img1,img2)",diff)
        (similar, diff) = structural_similarity(gray1, gray2, full = True)

        # convert diff from boolean to int
        diff  =(diff*255).astype("uint8")
        # cv2.imshow("Difference", diff)

        # Apply threshold
        thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        #cv2.imshow("Threshold",diff)

        # Dilation
        kernel = np.ones((5,5),np.uint8)
        dilate = cv2.dilate(thresh, kernel,iterations=1)
        # cv2.imshow("Dilation", dilate)

        # Find contours
        # contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL,
        #                 cv2.CHAIN_APPROX_SIMPLE)

        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)

        contours = imutils.grab_contours(contours)

        # Loop over each contour
        for contour in contours:
            if cv2.contourArea(contour)>100:
                # (x,y), radius = cv2.minEnclosingCircle(contour)
                # center = (int(x),int(y))
                # radius = int(radius)
                # cv2.circle(img1,center,radius,(0,255,0),2)
                # cv2.circle(img2,center,radius,(0,255,0),2)
                # calculate bounding box
                x, y, w, h = cv2.boundingRect(contour)
                # draw rectangle bounding box
                cv2.rectangle(img1,(x,y),(x+w,y+h), (0,0,255),2)
                cv2.rectangle(img2,(x,y),(x+w,y+h), (0,0,255),2)

                cv2.putText(img2, str(similar),(10,30), cv2.FONT_HERSHEY_SIMPLEX, .7, (255,0,0),2)

        # show final images with differences
        x = np.zeros((500,10,3),np.uint8)
        result = np.hstack((img1,x,img2))
        if(similar<0.9):
            #cv2.imshow("Differences",result)
            name = resultStorage + str(startingTime) + '_'+str(frameIndex)+'.jpg'
            # writing the extracted images
            cv2.imwrite(name, result)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            return frameIndex
        else:
            return 0
