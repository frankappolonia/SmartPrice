import tkinter as tk

class AdminPasswordPage(tk.Frame):
    '''This class builds the password prompt page to access the admin page.
     Successful entry of credentials will bring the user to the admin page.'''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        pwPrompt = tk.Label(self, text="Please enter your user name and password to proceeed.", pady=50)
        pwPrompt.grid(row=0, column=0, sticky="nsew")

        self.enterUsername = tk.Entry(self, width =20) 
        self.enterUsername.grid(row = 1, column=1, pady=5,sticky=tk.W)
        label_enterUsername = tk.Label(self, text="Enter username:  ")
        label_enterUsername.grid(row = 1, column=0, pady=2, sticky=tk.E)

        self.enterPassword = tk.Entry(self, width =20) 
        self.enterPassword.grid(row = 2, column=1, pady=5,sticky=tk.W)
        label_enterPassword = tk.Label(self, text="Enter password:  ")
        label_enterPassword.grid(row = 2, column=0, pady=2, sticky=tk.E)
