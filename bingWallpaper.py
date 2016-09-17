import requests	
import json
import shutil
import time
import os

url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1466006721475"
response = requests.get(url)
if response.status_code == 200 :
	rJson = response.json()
	imageUrl = 'http://www.bing.com' + rJson['images'][0]['url']
	image = requests.get(imageUrl, stream=True)
	imageName = "~/Pictures/Bing/image-" + time.strftime("%d-%m-%Y") + "." + rJson['images'][0]['url'].split('.')[1]
	print imageName
	wHandle = open(imageName, 'w')
	image.raw.decode_content = True
	shutil.copyfileobj(image.raw, wHandle)
	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://" + imageName)
else : 
	#create notification of connection failure
	pass
	
