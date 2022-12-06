# youtube_trailer_downloader
Walks through a directory called Movies and uses all contained directory names to search youtube for associated movie trailer (so works well if movie folder names are movie title and year of release, eg ./Movies/Bladerunner (1982) ) 
then downloads first result from returned search results and names it the same as the movie folder name placing it inside the related movie folder with a suffix -trailer.mp4 (eg ./Movies/Bladerunner (1982)/Bladerunner (1982)-trailer.mp4)

Requirements: 
you will need to pip install both the below libraries

youtube-search-python
https://github.com/alexmercerind/youtube-search-python

yt_dlp
https://github.com/yt-dlp/yt-dlp

Assumes you have a ./Movies/ folder containing each movie in its own folder named "movietitle (date)" and you are running the script from the path one level up from Movies folder ../Movies/ you can adjust in script if needed, see comments for where.
