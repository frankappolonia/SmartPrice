#from tkinter import *
import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, NSEW
import AdminPage, AdminPasswrdPage, PricingPage
#from PIL import Image, ImageTk



'''This file contains the class for the main GUI. This is where the main TK frame is built
and all other sub-pages are imported to. The main frame essentially is like a shell.
GUI pages are called into this frame, rather than instatiating a new frame for 
every page. For instance, if a user selects the admin page, the gui page specs 
will be loaded in the BaseFrame class.'''

LARGE_FONT= ("Verdana", 12)
class BaseFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, width=500, height=500, bg="white")
        container.pack( fill=None, expand = False)
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(0, weight=10)

        self.frames = {}
        for F in (StartPage, AdminPage.AdminPageGui, PricingPage.PricingPageGUI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=2, sticky="nsew")
       
        backButton = tk.Button(container, text="Back", command = lambda: self.show_frame(StartPage))
        backButton.grid(row=0, column=1, sticky = "w")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        '''self.frames is the dictonary of pages above. A key is passed to the 'controller'
        argument to determine which page of the GUI is displayed .'''

        frame = self.frames[cont] 
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.frames = {}
        tk.Widget.configure(self, background='white')

        self.img = tk.PhotoImage(file="Banner (Small).png")
        self.panel = tk.Label(self, image=self.img)
        self.panel.grid(row=1, column=0, columnspan=3, sticky="nsew")

        #self.buttonImg = tk.PhotoImage(file="roundedButton_15x10.png")

        path = "C:\\Users\\appolofr\\Documents\GitHub\SmartPrice\\roundedButton.png"
        #ima = Image.open(path)
        #imaRes = ima.resize(20,30)


        #buttonIm = ImageTk.PhotoImage(imaRes)

        welcomeLabel = tk.Label(self, text="Welcome to ABE SmartPrice!", font=LARGE_FONT, pady=50, bg='white')
        welcomeLabel.grid(row=2, column=0, columnspan=4, sticky="nsew")

        adminPage = tk.Button(self,  text = "Admin (Add, Update, Delete Customer)", command = lambda: controller.show_frame(AdminPage.AdminPageGui))
        adminPage.grid(row=3, column=0, columnspan=4, sticky = "nswe", pady=15)

        pricingPage = tk.Button(self, text = "Get Parts Pricing", command = lambda: controller.show_frame(PricingPage.PricingPageGUI))
        pricingPage.grid(row=4, column=0, columnspan=4, sticky="nsew", pady=15)


app = BaseFrame()
app.mainloop()



