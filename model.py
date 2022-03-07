import time
import subprocess
import pyautogui

class Model():
    def __init__(self):
        self.something = 0

    def join_session(self,meeting_id,passcode,zoomPath):
        #launch zoom
        cmd = "start "+ zoomPath 
        subprocess.Popen(cmd, shell = True)
        time.sleep(5)

        #click on the first join button
        pyautogui.click('first_join.png')
        time.sleep(3)

        #enter the meeting id
        pyautogui.write(meeting_id)

        #click on the second join button
        pyautogui.click('second_join.png')
        time.sleep(3)

        #enter the passcode
        pyautogui.write(passcode)

        #click on the final join button
        pyautogui.click('last_join.png')
        time.sleep(3)

        #try to join audio if not already joined
        try:
            pyautogui.click('join_audio.png')
            time.sleep(3)
        except:
            print("audio joined")

        #try to mute microphone if not already muted
        try:
            #mute microphone
            pyautogui.click('microphone.png')
            time.sleep(3)
        except:
            print("mic muted")


    def end_session(self):
        pyautogui.click('first_leave.png')
        time.sleep(2)

        #Cant find last leave button so manually move mouse from relative pos
        pyautogui.dragRel(0, -60, duration=.05) #move up
        pyautogui.dragRel(-50, 0, duration=.05) #move left


    def get_zoomPath(self):
        try:
            with open("pathfile.txt", "r") as f:
                zoom_path = f.read()
                return zoom_path
        except FileNotFoundError:
                f = open("pathfile.txt", "w")
                f.close
                return ""

   
    def set_zoomPath(self,zoomPath):
        with open("pathfile.txt", "w") as f:
            f.write(zoomPath)
            
