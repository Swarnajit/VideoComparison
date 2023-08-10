from moviepy.editor import *
import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr
import IPython.display as ipd
from playVideo import *

video_path1 = 'C:\\Users\\swarn\\Downloads\\Reel_2.mp4'
video_path2 = 'C:\\Users\\swarn\\Downloads\\Reel_3.mp4'
location1 = 'C:\\Users\\swarn\\Videos\\Captures\\Video1\\'
location2 = 'C:\\Users\\swarn\\Videos\\Captures\\Video2\\'
resultStorage = 'C:\\Users\\swarn\\Videos\\Captures\\'

def PlotAudio(filename_withwout_extension):

    #audio2='Second'
    y, sr = lr.load(filename_withwout_extension+'.wav')
    ipd.Audio(y, rate=sr)
    plt.figure(figsize=(15, 5))
    lr.display.waveshow(y, sr=sr, alpha=0.8)
    #plt.show()
    plt.savefig(filename_withwout_extension+'_sound.jpg')

def AudioDifference(audioAt):

    # Load audio data and sample rate using librosa
    audio1, sr1 = lr.load(location1+str(audioAt)+'.wav')
    audio2, sr2 = lr.load(location2+str(audioAt)+'.wav')

    # Ensure both audio signals have the same length (you might want to handle this differently depending on your use case)
    min_length = min(len(audio1), len(audio2))
    audio1 = audio1[:min_length]
    audio2 = audio2[:min_length]

    # Calculate the difference between the audio signals
    difference = np.abs(audio1 - audio2)

    # Calculate the root mean square error (RMSE)
    rmse = np.sqrt(np.mean(difference**2))

    print(f"Root Mean Square Error (RMSE): {rmse}")

    # Loading images
    img1 = cv2.resize(cv2.imread(location1+str(audioAt)+'_sound.jpg'),(1000,500))
    img2 = cv2.resize(cv2.imread(location2+str(audioAt)+'_sound.jpg'),(1000,500))

    x = np.zeros((500,10,3),np.uint8)
    result = np.hstack((img1,x,img2))

    name = resultStorage + str(audioAt)+'_soundDifference.jpg'
    # writing the extracted images
    cv2.imwrite(name, result)

def GetSubclip(start_time):

    AudioDifference(start_time)

    imagesToPlot = CompareImages(start_time)

    return imagesToPlot

# dir_list = os.listdir(location)
 
# print("Files and directories in '", location, "' :")
 
# dir_list.sort()

# prints all files
# print(dir_list)


# # Create the subclip
# subclip1 = video_clip.subclip(0, 20)
# subclip2 = video_clip.subclip(20, 40)



# # Load the video clip
# video_path = 'C:\\Users\\swarn\\Downloads\\Hotel California.avi'
# video_clip = VideoFileClip(video_path)

# # Define the start and end times of the subclip (in seconds)
# start_time = 10  # start time of subclip in seconds
# end_time = 20    # end time of subclip in seconds

# # Create the subclip
# subclip1 = video_clip.subclip(0, 20)
# subclip2 = video_clip.subclip(20, 40)

# output_audio_path1 = 'C:\\Users\\swarn\\Downloads\\Sample1.wav'
# subclip_audio = subclip1.audio
# subclip_audio.write_audiofile(output_audio_path1)

# output_audio_path2 = 'C:\\Users\\swarn\\Downloads\\Sample2.wav'
# subclip_audio = subclip2.audio
# subclip_audio.write_audiofile(output_audio_path2)

# PlotAudio(output_audio_path1)
# PlotAudio(output_audio_path2)

# Load audio files
# audio_path_1 = 'C:\\Users\\swarn\\Downloads\\Hotel California.wav'
# audio_path_2 = 'C:\\Users\\swarn\\Downloads\\Sample1.wav'

# y1, sr1 = librosa.load(audio_path_1)
# y2, sr2 = librosa.load(audio_path_2)

# # Ensure both audio signals have the same length
# min_len = min(len(y1), len(y2))
# y1 = y1[:min_len]
# y2 = y2[:min_len]

# # Calculate RMSE-based percentage difference
# rmse = np.sqrt(np.mean((y1 - y2)**2))
# percentage_diff = (rmse / np.max(y1)) * 100.0

# print(f"RMSE-based percentage difference: {percentage_diff:.2f}%")