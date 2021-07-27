# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:47:27 2021

@author: chomi

"""

import os 
import time 

t1 = 0
cam = 'close'

def save(idx): # save all photos to path and deletes them on phone
    count = 1    
    path = 'C:/Users/chomi/Desktop/testing/'
    os.system('adb pull sdcard/DCIM/Camera ' + path) # copy all images to path 
    for file in os.listdir(path + 'Camera/'): # delete the images on phone
        if(file.startswith('202')):
            os.system('adb shell rm -f /sdcard/DCIM/Camera/'+file)
            name = 'A'+str(idx).zfill(4)+'-'+str(count).zfill(4)+'.jpg'
            os.renames(path+'Camera/' + file, path +'Camera/'+ name)
            count+=1
    shutdown()
    unlock()
    gall()
    shutdown()
def camera(): # open the camera app
    global t1, cam
    os.system('adb shell input keyevent KEYCODE_HOME')
    os.system('adb shell input touchscreen swipe 950 2200 950 1555 90') #open camera
    time.sleep(2)
    t1 = time.time()
    cam = 'open'

def take(): # take picture
    global t1, cam
    if(time.time() - t1 > 120 or cam == 'close'): # camera timeouts after 120 seconds
        camera() #reopen camera if screen timed out 
    os.system('adb shell input tap 540 920') # focus on center frame
    time.sleep(0.4) # wait for focus
    os.system('adb shell input tap 540 2000') # take photo
    t1 = time.time()

def shutdown(): # turn off phone
    global t1, cam    
    os.system('adb shell input keyevent KEYCODE_HOME')
    os.system('adb shell input keyevent KEYCODE_POWER')
    t1 = 0
    cam = 'close'

def restart(): # restart adb connection between phone and PC
    os.system('adb kill-server')
    os.system('adb devices')

def unlock(): # unlocks phone
    os.system('adb shell input keyevent KEYCODE_HOME')
    os.system('adb shell input touchscreen swipe 540 1800 540 1000 90')
    os.system('adb shell input text 2580') #2580 is the passcode
    os.system('adb shell input keyevent KEYCODE_ENTER')

def gall(): # deletes residual data in phone gallery
    os.system('adb shell input keyevent KEYCODE_HOME')
    os.system('adb shell input tap 250 1500')
    os.system('adb shell input touchscreen swipe 150 300 150 300 1000')
    os.system('adb shell input tap 540 2000')
    os.system('adb shell input tap 840 1900')

def reboot(): #restarts phone. 
    os.system('adb reboot')
    
def switch_cam(): # toggles between front and rear camera
    shutdown()
    camera()
    time.sleep(0.5)
    os.system('adb shell input touchscreen swipe 540 1300 540 1000 100')
    time.sleep(0.5)
    shutdown()

def zoomin(): # requires setting volume keys as zooming
    global t1
    global cam
    if(cam == 'open'):
        os.system('adb shell input keyevent KEYCODE_VOLUME_UP')
        t1 = time.time()

def zoomout():
    global t1
    global cam
    if(cam == 'open'):
        os.system('adb shell input keyevent KEYCODE_VOLUME_DOWN')
        t1 = time.time()
    
def stream(): # starts SCRCPY
    path = 'C:/Users/chomi/Desktop/scrcpy/scrcpy-noconsole.exe' #path to scrcpy
    os.startfile(path)
    
def stream_off(): # stops SCRCPY
    os.system('TASKKILL /F /T /IM scrcpy-noconsole.exe')

def focus(): # focus in center frame 
    global t1
    if(cam == 'open'):
        os.system('adb shell input tap 540 920')
        t1 = time.time()
        
