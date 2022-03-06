from model import Model
from view import View
import time
from datetime import datetime

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def main(self):
        self.view.main()
    
    def get_zoomPath(self):
        return self.model.get_zoomPath()

    def click_browse(self,zoomPath):
        print(zoomPath)

    def validate_time(self,hour,min): 
        if(len(hour) > 2 or len(min) > 2 or hour.isdigit() == False or min.isdigit() == False ):
            raise ValueError("Invalid time entered")

    
    def convert24(self,str1):
      
        # Checking if last two elements of time
        # is AM and first two elements are 12
        if str1[-2:] == "AM" and str1[:2] == "12":
            return "00" + str1[2:-2]
            
        # remove the AM    
        elif str1[-2:] == "AM":
            return str1[:-2]
        
        # Checking if last two elements of time
        # is PM and first two elements are 12   
        elif str1[-2:] == "PM" and str1[:2] == "12":
            return str1[:-2]
            
        else:
            
            # add 12 to hours and remove PM
            return str(int(str1[:2]) + 12) + str1[2:5]

    
    def click_start(self,id,passcode,startHour,startMin,startampm,endHour,endMin,endampm,zoomPath):
        self.model.set_zoomPath(zoomPath)

        startHour = startHour.zfill(2)
        startMin = startMin.zfill(2)
        endHour = endHour.zfill(2)
        endMin = endMin.zfill(2)

        ##validate times entered
        try:
            self.validate_time(startHour,startMin)
            self.validate_time(endHour,endMin)
        except ValueError as err:
            self.view.show_timeError(err)
            return

        startTime = startHour + ":" + startMin + " " + startampm
        startTime = self.convert24(startTime)
        print(startTime)
        endTime = endHour + ":" + endMin + " " + endampm
        endTime = self.convert24(endTime)
        print(endTime)

        #self.view.show_success("Started")
        #keep checking if it is time to join a zoom session
        while True:
            curTime = datetime.now().strftime("%H:%M")
            print(curTime)
            if(curTime == startTime):
                self.model.join_session(id,passcode,zoomPath)
                break
            time.sleep(30)

        #keep checking if it is time to end a zoom session
        while(True):
            curTime = datetime.now().strftime("%H:%M")
            print(curTime)
            if(curTime == endTime):
                self.model.end_session()
                break
            time.sleep(30)
        

if __name__ == '__main__':
    zoomBot = Controller()
    zoomBot.main() 