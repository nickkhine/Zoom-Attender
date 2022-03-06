import tkinter as tk
from tkinter import DISABLED, ttk
from tkinter import filedialog as fd
import threading


class View(tk.Tk):

    pad = 10
    

    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Zoom Attender")
        self._make_main_frame()

        #zoom path
        path_frame = ttk.Frame(self.main_frame)
        path_frame.pack()
        path_frame['padding'] = (143,10,5,10)
        self.pathBox = ttk.Entry(path_frame,width = 50)
        self.pathBox.grid(row=0,column=0)
        self.set_text(self.controller.get_zoomPath())
        
        #browse button
        browseButton =ttk.Button(path_frame,text = "Browse Local files", command = self.openFileExplorer)
        browseButton.grid(row=0,column=1)
        
        # Create Text Boxes
        entry_frame = ttk.Frame(self.main_frame)
        entry_frame.pack()

        meeting_id = ttk.Entry(entry_frame, width=30)
        meeting_id.grid(row=1, column=1, padx=20, pady=(10, 0))

        meeting_password = ttk.Entry(entry_frame, width=30)
        meeting_password.grid(row=2, column=1)

        start_hour = ttk.Entry(entry_frame, width=30,justify="right")
        start_hour.grid(row=3, column=1)

        start_minutes = ttk.Entry(entry_frame, width=30)
        start_minutes.grid(row=3, column=2)

        self.startRadio = tk.StringVar()
        self.startRadio.set("AM")
        AM = ttk.Radiobutton(entry_frame, text = "AM",variable = self.startRadio, value = "AM")
        AM.grid(row = 3, column= 3)
        PM = ttk.Radiobutton(entry_frame, text = "PM",variable = self.startRadio, value = "PM")
        PM.grid(row = 3, column= 4)

        end_hour = ttk.Entry(entry_frame, width=30,justify="right")
        end_hour.grid(row=4, column=1)

        end_minutes = ttk.Entry(entry_frame, width=30)
        end_minutes.grid(row=4, column=2)

        self.endRadio = tk.StringVar()
        self.endRadio.set("AM")
        AM = ttk.Radiobutton(entry_frame, text = "AM",variable = self.endRadio, value = "AM")
        AM.grid(row = 4, column= 3)
        PM = ttk.Radiobutton(entry_frame, text = "PM",variable = self.endRadio, value = "PM")
        PM.grid(row = 4, column= 4)



        # Create Text Box Labels
        meeting_id_label = ttk.Label(entry_frame, text="Meeting id")
        meeting_id_label.grid(row=1, column=0, pady=(10, 0))

        meeting_password_label = ttk.Label(entry_frame, text="Meeting password")
        meeting_password_label.grid(row=2, column=0)

        start_time_label = ttk.Label(entry_frame, text="Start Time")
        start_time_label.grid(row=3, column=0,padx = 0)

        end_time_label = ttk.Label(entry_frame, text="End Time")
        end_time_label.grid(row=4, column=0)



        # Create Submit Button
        #added threading to fix non-responsive gui since self.controller.click_start() is infinite loop
        submit_btn = ttk.Button(self.main_frame, text="Start",command = threading.Thread(target=(
            lambda : self.controller.click_start(meeting_id.get(),meeting_password.get(),start_hour.get(),start_minutes.get(),
            self.startRadio.get(),end_hour.get(),end_minutes.get(),self.endRadio.get(),self.pathBox.get()))).start)
        submit_btn.pack()

        self.message_label = ttk.Label(self.main_frame, text='', foreground='red')
        self.message_label.pack()

        
    def main(self):
        self.mainloop()
    
    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx = self.pad, pady = self.pad)

    def _make_entry(self):
        ent = ttk.Entry(self.main_frame, justify= "right" )
        ent.pack()

    def set_text(self,text):
        self.pathBox.delete(0,tk.END)
        self.pathBox.insert(0,text)

    def openFileExplorer(self):
        zoom_path = fd.askopenfilename(initialdir="",title = "select a file",filetypes=[("exe files", ".exe")])
        self.set_text(zoom_path)
    
    def show_timeError(self,message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
    
    def hide_message(self):
        self.message_label['text'] = ''

    def show_success(self,message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)
       
        
    
        