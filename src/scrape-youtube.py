import urllib.request 
import re

# https://www.youtube.com/playlist?list=LLiVqIj4D1NNP22w_GidsiUg
search_keyword = 'lexologics'
playlist = 'LLiVqIj4D1NNP22w_GidsiUg'

url = 'https://www.youtube.com/results?search_query=' + search_keyword
url2 = 'https://www.youtube.com/playlist?list=' + playlist
url3 = 'https://www.youtube.com/lexologics/videos'  

html = urllib.request.urlopen(url, 
    cafile="./venv/lib/python3.9/site-packages/certifi/cacert.pem",
    capath="./venv/lib/python3.9/site-packages/certifi/"
).read().decode() 

html2 = urllib.request.urlopen(url2, 
    cafile="./venv/lib/python3.9/site-packages/certifi/cacert.pem",
    capath="./venv/lib/python3.9/site-packages/certifi/"
).read().decode() 

html3 = urllib.request.urlopen(url3, 
    cafile="./venv/lib/python3.9/site-packages/certifi/cacert.pem",
    capath="./venv/lib/python3.9/site-packages/certifi/"
).read().decode() 

video_ids = re.findall(r'watch\?v=(\S{11})', html)
iterate = int(len(video_ids))

video_search = re.findall(r'watch\?v=(\S{11})', html)
video_playlist = re.findall(r'playlist\?list=(\S{11})', html2)
video_watch = re.findall(r'lexologics\videos\?v=(\S{11})', html3)

for i in range(iterate):
    #print("https://www.youtube.com/watch?v=" + str(video[i]))
    #print("https://www.youtube.com/lexologics/playlist?list=" + str(video_playlist[i]))
    pass
#print(iterate)
print(int(len(video_search)))
print(int(len(video_playlist)))
print(int(len(video_watch)))
print(url2)