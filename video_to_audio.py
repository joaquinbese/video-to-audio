from tkinter.filedialog import *
import os
from glob import glob
from pydub import AudioSegment


video = askdirectory()






# Path where the videos are located
extension_list = ('*.3gpp', '*.flv','webm','*.mp4')

os.chdir(video)
for extension in extension_list:
    mp3_filenames = map(lambda x: os.path.splitext(x)[0] + '.mp3', glob(extension))
    for video, mp3_filename in zip(glob(extension), mp3_filenames):
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')


print("Complete!")
