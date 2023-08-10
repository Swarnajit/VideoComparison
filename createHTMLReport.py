from moviepy.editor import *
import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr
import IPython.display as ipd
from playVideo import *
import math
from converToAudio import *

video_path1 = 'C:\\Users\\swarn\\Downloads\\Reel_2.mp4'
video_path2 = 'C:\\Users\\swarn\\Downloads\\Reel_3.mp4'
spanOfClip = 10
  
# Load the video clip
video_clip1 = VideoFileClip(video_path1)
video_clip2 = VideoFileClip(video_path2)
  
# Define the start and end times of the subclip (in seconds)
start_time = 0  # start time of subclip in seconds
end_time = video_clip1.duration    # end time of subclip in seconds

rows=[]
clip_endtime =[]

while(start_time<=end_time):

  if(end_time-start_time>=spanOfClip):
      duration = start_time +spanOfClip
  else:
      duration = math.floor(end_time)

  # if(duration<=end_time):
  subclip1 = video_clip1.subclip(start_time, duration)
  subclip1.write_videofile(location1+str(start_time)+'.mp4')

  subclip1_audio = subclip1.audio
  subclip1_audio.write_audiofile(location1+str(start_time)+'.wav')

  PlotAudio(location1+str(start_time))

  subclip2 = video_clip2.subclip(start_time, duration)
  subclip2.write_videofile(location2+str(start_time)+'.mp4')

  subclip2_audio = subclip2.audio
  subclip2_audio.write_audiofile(location2+str(start_time)+'.wav')
  PlotAudio(location2+str(start_time))

  rows.extend(GetSubclip(start_time))

  clip_endtime.append(duration)

  start_time+=spanOfClip


html = """\
    <table border='1'>
    <tr><th>Message</th><th>Image Mismatch</th><th>Audio Mismatch</th></tr>"""
for row in rows:
    first = row.split('_', 1)[0]

    clipUpto = int(first)+spanOfClip

    html = html + "<tr>"
    html = html + "<td><p>Mismatch found from " + first + "th to "+ str(clipUpto) +"th second</p></td>"
    html = html + "<td><a href=" + 'C:\\Users\\swarn\\Videos\\Captures\\' + row + '.jpg' + ">"+row+"</td>"
    html = html + "<td><a href=" + 'C:\\Users\\swarn\\Videos\\Captures\\' + first + '_soundDifference.jpg' + ">"+row+"</td>"
    html = html + "</tr>"
html = html + "</table>"

# Creating the HTML file
f = open('temp.html','w')
f.write(html)
f.close()