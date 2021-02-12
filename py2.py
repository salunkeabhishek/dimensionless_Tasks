import cv2
import matplotlib.pyplot as plt 
import argparse
import xml.etree.ElementTree as ET
import time
import csv 
import datetime
import numpy as np
from PIL import Image
#read xml
tree = ET.parse('123.xml')
root = tree.getroot()



#read from terminal 
#ap = argparse.ArgumentParser()
#ap.add_argument("-i","--image", require=True, help ="path to the image")
#args = vars(ap.parse_args())
#image = cv2.imread(args["image"]) 



#read image
img = cv2.imread("img.jpg",0)


for child in root.findall('object'):
  title = child.find('name').text
  for subchild in child.findall('bndbox'):
    x = subchild.find('xmin').text
    x = int(x)
    y = subchild.find('ymin').text
    y = int(y)
    h = subchild.find('xmax').text
    h = int(h)
    w = subchild.find('ymax').text
    w = int(w)
    ts = time.time()
    ct = datetime.datetime.now()
    #x,y,w,h = cv2.boundingRect(cnt)
    stp = (x,y)
    endpt = (x+w,y+h)
    co =(36,255,12)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    #img = cv2.rectangle(img,[int(x) for x in stp],[int(x) for x in endpt],[int(x) for x in co],1)
    img = cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),3)
    img = cv2.putText(img,title,(x,y-10),font,0.9,(255,0,0),3)

plt.figure()
plt.imshow(img) 
plt.show() 