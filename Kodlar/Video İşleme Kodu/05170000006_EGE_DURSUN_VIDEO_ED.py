#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EGE DOĞAN DURSUN
05170000006
EGE ÜNİVERSİTESİ
MÜHENDİSLİK FAKÜLTESİ
BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
2020-2021 ÖĞRETİM YILI / GÜZ DÖNEMİ

GÖRÜNTÜ İŞLEME DERSİ
PROJE - 1
VIDEO EDGE DETECTION
"""

#Importing necessary libraries
import cv2
import numpy as np

#Opening the video file
cap = cv2.VideoCapture("Baby_goats.mp4")

#Notice the problem if a problem happens during opening the file
if(cap.isOpened() == False):
  print("There has been an error while opening the video file!")
else:
  print("Video file has been found without any problems...")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    
    #Convert the video frames to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Using filter to get contours of the objects inside the video
    edges = cv2.Canny(gray, 50, 60)

    #Show the current frame
    cv2.imshow('Frame', edges)

    #Press Q to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  
  else:
    break

#Finalize the process
cap.release()

cv2.destroyAllWindows()