#install these as below
#pip install youtube-search-python
#pip install yt_dlp

#can adjust row 23 and 35 if you want to change path or have called your directory to process someting else
#can adjust row 31 if you want a delay between calls to youtube

import os
import json
import time
from youtubesearchpython import *
from yt_dlp import YoutubeDL


def download_trailer_info (trailerName):
  ytSearchString = trailerName +" movie trailer"
  mySearch = VideosSearch(ytSearchString, limit = 1)
  jsonBlob = mySearch.result(mode = ResultMode.json)
  ytStringID = jsonBlob[76:87] #fix this joke at some point
  ytStringBase = "https://www.youtube.com/watch?v="
  ytStringFull = ytStringBase+ytStringID
  trailerFilename = trailerName+"-trailer.mp4"
  savePath = "..\\Movies\\"+trailerName+"\\"+trailerFilename #Adjust as needed - assumption is that you are running script one level above a Movies folder, from which script will decend into and process all folders
  ydl_opts = {
    "outtmpl": savePath
  }
  
  with YoutubeDL(ydl_opts) as ydl:
    ydl.download(ytStringFull)
    print("sleeping for 2 minutes to avoid hammering...")
    time.sleep(1) #adjust this to something larger if you want to not hammer 
  return


basepath = "..\Movies\\" #Adjust as needed - assumption is that you are running script one level above a Movies folder, from which script will decend into and process all folders
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            trailer = (basepath+entry.name+"\\"+entry.name+"-trailer.mp4")
            print("\nChecking for: " +trailer)
            if os.path.exists(trailer):
              print("Trailer FOUND skipping...\n")
            else:
              print("Trailer MISSING..!\n downloading")
              download_trailer_info (entry.name)





