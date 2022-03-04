import os
import time
import easygui
from datetime import datetime
import subprocess
import pyautogui

#Launches and joins a zoom session
def join_session(meeting_id,passcode,zoomPath):
    #launch zoom
    cmd = "start "+ zoomPath 
    subprocess.Popen(cmd, shell = True)
    time.sleep(5)

    #click on the first join button
    first_join = pyautogui.locateCenterOnScreen('first_join.png')
    pyautogui.moveTo(first_join)
    pyautogui.click()
    time.sleep(3)

    #enter the meeting id
    pyautogui.write(meeting_id)

    #click on the second join button
    second_join = pyautogui.locateCenterOnScreen('second_join.png')
    pyautogui.moveTo(second_join)
    pyautogui.click()
    time.sleep(3)

    #enter the passcode
    pyautogui.write(passcode)

    #click on the final join button
    last_join = pyautogui.locateCenterOnScreen('last_join.png')
    pyautogui.moveTo(last_join)
    pyautogui.click()
    time.sleep(3)

    #join audio 
    join_audio = pyautogui.locateCenterOnScreen('join_audio.png')
    pyautogui.moveTo(join_audio)
    pyautogui.click()
    time.sleep(3)

    #mute microphone
    microphone = pyautogui.locateCenterOnScreen('microphone.png')
    pyautogui.moveTo(join_audio)
    pyautogui.click()
    time.sleep(3)


ans = input("Do you want to get a new zoom path?(Y/N)")
ans = ans.upper()
if(ans == 'Y'):
    os.remove("pathfile.txt")

zoomPath = ""
#Get the path for zoom application
try:
    with open("pathfile.txt", "r") as f:
        zoomPath = f.read()
except FileNotFoundError:
    zoomPath = easygui.fileopenbox()
    with open("pathfile.txt", "w") as f:
        f.write(zoomPath)

#parameters to join a zoom meeting
startTime = input("Enter start time(hh:mm): ")
meeting_id = input("Enter meeting id: ")
passcode = input("Enter meeting passcode: ")

#keep checking if it is time to join a zoom session
while True:
    curTime = datetime.now().strftime("%I:%M")
    print(curTime)
    if(curTime == startTime):
        join_session(meeting_id,passcode,zoomPath)
        break
    time.sleep(30)
