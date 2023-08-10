import cv2
import numpy as np
import time
import datetime
from tqdm import tqdm
import os
from imagecomparison import imageComparison
from moviepy.editor import *

location1 = 'C:\\Users\\swarn\\Videos\\Captures\\Video1\\'
location2 = 'C:\\Users\\swarn\\Videos\\Captures\\Video2\\'


# Takes screenshot
def TakeScreenshot(cam, startingTime,location):
    listOfFrames = []
    currentFrame = startingTime
    fps = cam.get(cv2.CAP_PROP_FPS)    
    print('fps:', fps)  # float `fps`

    frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)  
    print('frames count:', frame_count)  # float `frame_count`

    # calculate duration of the video
    seconds = round(frame_count / fps)
    video_time = datetime.timedelta(seconds=seconds)
    print(f"duration in seconds: {seconds}")
    print(f"video time: {video_time}")

    for currentFrame in tqdm(range(int(frame_count)),
        desc="Loading…",
        ascii=False, ncols=75):
        #time.sleep(1)
        # reading from frame
        ret,frame = cam.read()
        
        if ret:
            # if video is still left continue creating images

            if currentFrame % 10 == 0:
                listOfFrames.append(currentFrame)
                name = location+ str(currentFrame) + '.jpg'
                #print('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            # currentFrame += 1
        else:
            break

    return listOfFrames


# Completion progess bar
def ProgressBar(lastFrame, currentFrame):
    for lastFrame in tqdm (range (currentFrame),
            desc="Loading…",
            ascii=False, ncols=75):
        time.sleep(0.001)

    #print("Complete.")

#def DeleteFile(listOfFrames, framesNotDelete, location):
def DeleteFile(listOfFrames, location):
    for frameIndex in listOfFrames:
        #if frameIndex not in framesNotDelete:
        filePath = 'C:\\Users\\swarn\\Videos\\Captures\\'+location+'\\' + str(frameIndex) + '.jpg'
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            print("The file does not exist")
    
    
def CompareImages(startingTime):
    try:
        video1Link = location1+str(startingTime)+'.mp4'
        video2Link = location2+str(startingTime)+'.mp4'

        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture(video1Link)
        vCap = cv2.VideoCapture(video2Link)
        listOfVideo1= TakeScreenshot(cap, startingTime, location1)
        listOfVideo2 = TakeScreenshot(vCap, startingTime,location2)

        getDifferentImagesIndex = []

        # check if video can be opened
        if(cap.isOpened()==False):
            print("Error opening the video file")
        else:
            # get vcap property 
            width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
            print('width, height:', width, height)
            
            fps = cap.get(cv2.CAP_PROP_FPS)    
            print('fps:', fps)  # float `fps`
            
            frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  
            print('frames count:', frame_count)  # float `frame_count`

        # # read until video is completed
        # while(cap.isOpened()):
        #     # capture frame by frame
        #     ret, frame = cap.read()
        #     if ret == True:
        #         # Display resulting frame
        #         cv2.imshow("Frame",frame)
        #         cv2.resizeWindow("Frame",(int((width/5)),int((height/10))))
            
        #         # press 'q' to exit
        #         if cv2.waitKey(25) & 0xFF == ord('q'):
        #                 break  
        #     else:
        #         break

        cap.release()

        for frameIndex in listOfVideo1:
            returnedIndex = imageComparison.compareImagesAtFrame(startingTime,frameIndex)
            if(returnedIndex!=0):
                getDifferentImagesIndex.append(str(startingTime)+'_'+str(frameIndex))

        cv2.destroyAllWindows()

    finally:
        DeleteFile(listOfVideo1,'Video1')
        DeleteFile(listOfVideo2,'Video2')

        return getDifferentImagesIndex