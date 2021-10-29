#from tkinter import *
import tkinter as tk
from tkinter.constants import ANCHOR, CENTER
import AdminPage, AdminPasswrdPage, PricingPage

'''This file contains the class for the main GUI. This is where the main TK frame is built
and all other sub-pages are imported to. The main frame essentially is like a shell.
GUI pages are called into this frame, rather than instatiating a new frame for 
every page. For instance, if a user selects the admin page, the gui page specs 
will be loaded in the BaseFrame class.'''

LARGE_FONT= ("Verdana", 12)
class BaseFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, width=500, height=500)
        container.pack( fill=None, expand = False)
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(0, weight=10)

        self.frames = {}
        for F in (StartPage, AdminPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

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

        welcomeLabel = tk.Label(self, text="Welcome to ABE SmartPrice!", font=LARGE_FONT, pady=50)
        welcomeLabel.grid(row=0, column=0, sticky="nsew")

        adminPage = tk.Button(self, text = "Admin (Add, Update, Delete Customer)", command = lambda: controller.show_frame(AdminPage))
        adminPage.grid(row=1, column=0, sticky = "nswe", pady=15)

        pricingPage = tk.Button(self, text = "Get Parts Pricing")
        pricingPage.grid(row=2, column=0, sticky="nsew", pady=15)


app = BaseFrame()
app.mainloop()



    
'''  def __init__(self):
        
        self.Window = Tk()
        self.Window.geometry("400x450")
        self.Window.title("ABE SmartParts")
        self.insertCustomer()

    #Entering to database
        self.enter_customerNumber = Entry(self.Window, width =20) 
        self.enter_customerNumber.grid(row = 0, column=1, pady=2, sticky=W)
        self.label_customerNumber = Label(Window, text="Customer Number ")
        self.label_customerNumber.grid(row = 0, column=0, pady=2, sticky=E)

        self.enter_customerName = Entry(self.Window, width =20)
        self.enter_customerName.grid(row = 1, column=1, pady=2, sticky=W)
        self.label_customerName = Label(self.Window, text="Customer Name ")
        self.label_customerName.grid(row = 1, column=0, pady=2, sticky=E)

        self.enter_ListPriceMod = Entry(self.Window, width =20)
        self.enter_ListPriceMod.grid(row = 2, column=1, pady=2, sticky=W)
        self.label_ListPriceMod = Label(self.Window, text="List Price Mod ")
        self.label_ListPriceMod.grid(row = 2, column=0, pady=2, sticky=E)

    def insertCustomer(self):
        customerValues = [self.enter_customerNumber.get(), self.enter_customerName.get(),self.enter_ListPriceMod.get()]
        CustomerBuilder.createCustomer(customerValues)

        #clears the values entered
        self.enter_customerName.delete(0, END)
        self.enter_customerNumber.delete(0, END)
        self.enter_ListPriceMod.delete(0, END)
    
        self.submitCustomer = Button(self.Window, text = "Add customer to DB", command = self.insertCustomer)
        self.submitCustomer.grid(row=3, column=0, columnspan=2, pady=2)
    '''
