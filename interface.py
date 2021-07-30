import tkinter as tk
from tkinter.constants import S
from tkinter.filedialog import askopenfilename, asksaveasfilename

from app import VideoCreation

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Variables
        self.testText = tk.StringVar()
        self.vidPath = ""
        self.audPath = ""
        self.finalVideoPath = ""

        # Initializing functions
        self.create_widgets()

    def create_widgets(self):
        # Video Button
        self.get_vid = tk.Button(self)
        self.get_vid["text"] = "Select the desired video"
        self.get_vid["command"] = self.getVid
        self.get_vid.pack()

        # Audio Button
        self.get_aud = tk.Button(self)
        self.get_aud["text"] = "Select the desired audio"
        self.get_aud["command"] = self.getAud
        self.get_aud.pack()

        # Create Video Button
        self.create_vid = tk.Button(self)
        self.create_vid["text"] = "Create the video"
        self.create_vid["command"] = self.createVid
        self.create_vid.pack()

        # Quit Button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        print(self.testText.get())

    def getVid(self):
        self.vidPath = askopenfilename()
        print(self.vidPath)

    def getAud(self):
        self.audPath = askopenfilename()
        print(self.audPath)

    def createVid(self):
        self.finalVideoPath = asksaveasfilename()
        vidClass = VideoCreation(self.vidPath, self.audPath, self.finalVideoPath)
        vidClass.generateVideo()
        print('Video was saved')

root = tk.Tk()
root.geometry("200x150")
app = Application(master=root)
app.mainloop()