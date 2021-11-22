import tkinter as tk
from tkinter import ttk
import AdminPage

class PasswordPage(tk.Frame):
    '''This class builds the password prompt page to access the admin page.
     Successful entry of credentials will bring the user to the admin page.'''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        
        pwPrompt = tk.Label(self, text="Please enter your user name and password to proceeed.", pady=50)
        pwPrompt.grid(row=0, column=0, sticky="nsew")

        self.enterUsername = ttk.Entry(self, width =20) 
        self.enterUsername.grid(row = 1, column=2, pady=5,sticky='nsew')
        label_enterUsername = tk.Label(self, text="Enter username:  ")
        label_enterUsername.grid(row = 1, column=1, pady=2, sticky='nw')

        self.enterPassword = ttk.Entry(self, width =20) 
        self.enterPassword.grid(row = 2, column=2, pady=5,sticky='nsew')
        label_enterPassword = tk.Label(self, text="Enter password:  ")
        label_enterPassword.grid(row = 2, column=1, pady=2, sticky='nw')

        self.submitPasswrd = ttk.Button(self, text="Submit", command= lambda: checkPassword(self.enterUsername.get(), self.enterPassword.get()))
        self.submitPasswrd.grid(row = 3, column=2, sticky='nsew')

    
        def checkPassword(username, password):
            correctUser = 'matt'
            correctPass = 'teddy123'
    
            if username == correctUser and password == correctPass:
                controller.show_frame(AdminPage.AdminPageGui)
                
        
