from moviepy.editor import *
from moviepy.video import *
from moviepy.video.fx.resize import resize
import os
from time import sleep
def mergerScript(preset):
   
    # output_video_size = 1280
    # intro = VideoFileClip(preset)
    # outro = VideoFileClip('Assets/KryptoLogoGlitch_1.mp4')

    # Load files
    videos = []
    # files = [f for f in os.listdir("/Media") if os.path.isfile(f)]
    files = os.listdir("./Media")
    for f in files:
        videos.append(f)
        print(f)

    # Merge and export videos
    if len(videos)==0:
        print("No videos found in Media folder.")
        sleep(3)
    for video in videos:
        print("processing ", video)
        clip1 = VideoFileClip("Media/"+video)
        intro = VideoFileClip(preset).fx(resize,width=clip1.w)
        outro = VideoFileClip('Assets/KryptoLogoGlitch_1.mp4').fx(resize,width=clip1.w)
        final_clip=concatenate_videoclips([intro,clip1,outro],method='compose')
        newname= video.split('.')[0] + 'Merged.mp4'
        final_clip.write_videofile("Exports/"+newname, fps=30)

# main
while True:
    print("Welcome to VideoMergerScript from Kryptonauten\nFirst put your videos in Media folder then continue\n")
    print("1. BuzzFive\n2. BitcoinMachine\n3. Stephan Zeigt\n")
    option = input("Select your preset: ")
    if option=="1":
        preset="Assets/5 MINUTEN BITCOIN.mp4"
        break
    elif option=="2":
        preset="Assets/Intro BitcoinMachine.mp4"
        break
    elif option=="3":
        preset="Assets/StephanZeigt.mp4"
        break
    else:
        print("invalid input try again.")

mergerScript(preset)