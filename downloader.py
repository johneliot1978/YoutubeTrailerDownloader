#pip install youtube-search-python
#pip install yt_dlp
import os
import json
import time
from youtubesearchpython import *
from yt_dlp import YoutubeDL


def download_trailer_info (trailerName):
  ytSearchString = trailerName +" movie trailer" 
  mySearch = VideosSearch(ytSearchString, limit = 1)
  jsonBlob = mySearch.result(mode = ResultMode.json)
  ytStringID = jsonBlob[76:87] 
  ytStringBase = "https://www.youtube.com/watch?v="
  ytStringFull = ytStringBase+ytStringID
  trailerFilename = trailerName+"-trailer.mp4" 
  savePath = "..\\Movies\\"+trailerName+"\\"+trailerFilename
  ydl_opts = {
    "outtmpl": savePath,
    "format" : "mp4"
  }

  with YoutubeDL(ydl_opts) as ydl:
    ydl.download(ytStringFull)
    print("sleeping for 1 second to avoid hammering...")
    time.sleep(5)
  return


basepath = "..\Movies\\"
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir(): 
            trailer = (basepath+entry.name+"\\"+entry.name+"-trailer.mp4") #forumulate what path and trailer filename should look like based on the directory its in
            print("\nChecking for: " +trailer)
            if os.path.exists(trailer):
              print("Trailer FOUND skipping...\n") 
            else:
              print("Trailer MISSING..!\n downloading")
              download_trailer_info (entry.name)
