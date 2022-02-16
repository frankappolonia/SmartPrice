import tkinter as tk
from tkinter import Widget, ttk
from tkinter.constants import LEFT, TOP, X, Y
import UI

'''This file contains the class for the main GUI. This is where the main TK frame is built
and all other sub-pages are imported to. The main frame essentially is like a shell
(or a stage if you have used JavaFX).
GUI pages are called into this frame, rather than instatiating a new frame for 
every page. For instance, if a user selects the admin page, the gui page specs 
will be loaded in the BaseFrame class.'''

LARGE_FONT= ("Futura", 15)

class BaseFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, width=500, height=500, bg="#f7f5f5")
        container.pack( fill=None, expand = False)
      
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(0, weight=10)

        self.frames = {}
        for F in (StartPage, PasswordPage, UI.AdminPageGui, UI.PricingPageGUI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=2, sticky="nsew")
       
        backBt = ttk.Button(container, width=5, text="Back", command = lambda: self.show_frame(StartPage))
        backBt.grid(row=0, column=1, sticky = "w")
        homeBt = ttk.Button(container, width=5, text="Home", command = lambda: self.show_frame(StartPage))
        homeBt.grid(row=0, column=2, sticky = "w")

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

          #seperators
        verticalSep = ttk.Separator(self, style='TSeparator', orient='vertical')
        verticalSep.pack(side=LEFT, fill=Y)

        horizontalSep = ttk.Separator(self, orient='horizontal')
        horizontalSep.pack(side=TOP, fill=X)

        self.img = tk.PhotoImage(file="Banner_clear_2_5.png")
        self.panel = tk.Label(self, image=self.img)
        self.panel.pack(side=TOP)

        welcomeLabel = tk.Label(self, text="Welcome to ABE SmartPrice!", font=LARGE_FONT, pady=50, bg='white')
        welcomeLabel.pack(side=TOP)

        adminPage = ttk.Button(self,  text = "Admin (Add, Update, Delete Customer)", command = lambda: controller.show_frame(PasswordPage))
        adminPage.pack(side=TOP)

        pricingPage = ttk.Button(self, width=32, text = "Get Parts Pricing", command = lambda: controller.show_frame(UI.PricingPageGUI))
        pricingPage.pack(side=TOP, pady=20)

class PasswordPage(tk.Frame):
    '''This class builds the password prompt page to access the admin page.
     Successful entry of credentials will bring the user to the admin page.'''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        tk.Widget.configure(self, background='white')

        pwPrompt = tk.Label(self, text="Please enter your user name and password to proceeed.", pady=10, bg='white')
        pwPrompt.grid(row=0, column=1, columnspan=3, sticky="nsew")

        self.enterUsername = ttk.Entry(self, width =20) 
        self.enterUsername.grid(row = 1, column=2, pady=5,sticky='nsew')
        label_enterUsername = tk.Label(self, text="Enter username:  ", bg='white')
        label_enterUsername.grid(row = 1, column=1, pady=2, sticky='nw')

        self.enterPassword = ttk.Entry(self, width =20) 
        self.enterPassword.grid(row = 2, column=2, pady=5,sticky='nsew')
        label_enterPassword = tk.Label(self, text="Enter password:  ", bg='white')
        label_enterPassword.grid(row = 2, column=1, pady=2, sticky='nw')

        self.submitPasswrd = ttk.Button(self, text="Submit", command= lambda: checkPassword(self.enterUsername.get(), self.enterPassword.get()))
        self.submitPasswrd.grid(row = 3, column=2, sticky='nsew')

        '''Bypass button is strictly for testing purposes, will remove upon final release'''
        self.bypass = ttk.Button(self, text="Password bypass (For Testing purposes)", command=lambda: controller.show_frame(UI.AdminPageGui))
        self.bypass.grid(row = 4, column=2, sticky='nsew')

        def checkPassword(username, password):
            correctUser = 'matt'
            correctPass = 'teddy123'
    
            if username == correctUser and password == correctPass:
                controller.show_frame(UI.AdminPageGui)
                
        

app = BaseFrame()

def change_theme():
    '''Calling this function sets the third party theme for the application.'''
    #style = ttk.Style(app)
    app.tk.call('source', 'C:\\Users\\appolofr\\Documents\\GitHub\\SmartPrice\\Third Party\\Theme_SunValley\\sun-valley.tcl')
    app.tk.call('set_theme', 'light')

    # NOTE: The theme's real name is azure-<mode>
    if app.tk.call("ttk::style", "theme", "use") == "sun-valley-light":
        # Set light theme
        app.tk.call("set_theme", "light")

change_theme()
app.resizable(width=False, height=False)
app.mainloop()



