from pytube import YouTube
from moviepy.editor import *
import os

print("Welcome to Chase's YouTube Converter, made by Dominic, his favorite owner")

# The list of all YouTube URL's to convert 
url_collection = ['https://www.youtube.com/watch?v=rdMReUOMKyI']

for url in url_collection:
    youtube = YouTube(url)

    print('Processing...')
    video = youtube.streams.first()

    # Store video title into variable
    title = video.title
   
    print("Downloading '{}' into storage device".format(title))
    video.download(r'C:\temp\audio_files')

    # Filter out special characters from video title
    title = title.replace('/', '')
    title = title.replace(',', '')
    title = title.replace('\\', '')
    title = title.replace('\'', '')
    title = title.replace('.', '')
    title = title.replace(':', '')
    title = title.replace('$', '')

    video_file = r'C:\temp\audio_files\{}.3gpp'.format(title)
    mp3_file = r'C:\temp\audio_files\{}.mp3'.format(title)

    videoclip = VideoFileClip(video_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    
    audioclip.close()
    videoclip.close()

    os.remove(r'C:\temp\audio_files\{}.3gpp'.format(title))
    
    print('done converting YouTube URL to file')
    del youtube
    del video  
