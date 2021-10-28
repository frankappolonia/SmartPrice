#from tkinter import *
import tkinter as tk
from tkinter.constants import ANCHOR, CENTER
import CustomerBuilder

add = "this is a github test"
#root = tk.Tk()
#frame = tk.Frame(root)

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

        

class AdminPage(tk.Frame):

    ''' Class that builds the admin page. Here, the user can add, update or delete
    customers from the customer DB table. Need admin privilidge (username and password)
    to access this page.
    0. Basic functions and setup utilized in 1-4
    1. Add Customer
    2. Update Customer
    3. Delete Customer '''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        '''0. Basic setup'''
        #this provides formatting for a 3 column grid
        blanklabel = tk.Label(self, text="", padx=50)
        blanklabel.grid(row =0, column =2)

        #Status text widgit
        self.T = tk.Text(self, height = 2, width=5)
        self.T.grid(row = 13, column = 0, columnspan=3, sticky="nsew")
        self.T.insert(tk.END, "Status:")

        def updateStatusText(status):
            '''This function updates the status text bar. The status text tells the user
            if their enter/update/or delete customer action was successful or not. This function
            is called with every button command in this class.'''

            self.T.delete(1.0, tk.END) #clears textbox before adding new message
            self.T.insert(tk.END, " Status: " + status)

        def clearEntry():
            '''Function that clears the user entered data from the form
            whenever an entry button is clicked.'''
            self.enter_customerName.delete(0, tk.END)
            self.enter_customerNumber.delete(0, tk.END)
            self.enter_ListPriceMod.delete(0, tk.END)
            self.update_customerName.delete(0, tk.END)
            self.update_customerNumber.delete(0, tk.END)
            self.update_ListPriceMod.delete(0, tk.END)
            self.delete_customerNumber.delete(0, tk.END)

        '''1. Add customer'''
        addCustomerTitle = tk.Label(self, text="Add Customer", font=LARGE_FONT)
        addCustomerTitle.grid(row=0, column=1, pady=10)

        self.enter_customerNumber = tk.Entry(self, width =20) 
        self.enter_customerNumber.grid(row = 1, column=1, pady=5,sticky=tk.W)
        label_customerNumber = tk.Label(self, text="Customer Number ")
        label_customerNumber.grid(row = 1, column=0, pady=2, sticky=tk.E)

        self.enter_customerName = tk.Entry(self, width =20)
        self.enter_customerName.grid(row = 2, column=1, pady=5, sticky=tk.W)
        label_customerName = tk.Label(self, text="Customer Name ")
        label_customerName.grid(row = 2, column=0, pady=2, sticky=tk.E)

        self.enter_ListPriceMod = tk.Entry(self, width =20)
        self.enter_ListPriceMod.grid(row = 3, column=1, pady=5, sticky=tk.W)
        label_ListPriceMod = tk.Label(self, text="List Price Mod ")
        label_ListPriceMod.grid(row = 3, column=0, pady=2, sticky=tk.E)
        

        def insertCustomer():
            customerValues = [self.enter_customerNumber.get(), self.enter_customerName.get(), self.enter_ListPriceMod.get()]
            CustomerBuilder.createCustomer(customerValues)

                #clears the values entered
        

        submitCustomer = tk.Button(self, text = "Add customer to DB", command = lambda:[insertCustomer(), updateStatusText("customer {0} ({1}) added to DB.".format(self.enter_customerNumber.get(), self.enter_customerName.get())), clearEntry()])
        submitCustomer.grid(row=4, column=0, columnspan=3, pady=2)


        '''2. Update Customer'''
        updateCustomerTitle = tk.Label(self, text="Update Customer", font=LARGE_FONT)
        updateCustomerTitle.grid(row=5, column=1, pady=10)

        self.update_customerNumber = tk.Entry(self, width =20) 
        self.update_customerNumber.grid(row = 6, column=1, pady=5,sticky=tk.W)
        label_updateCustomerNumber = tk.Label(self, text="Customer Number ")
        label_updateCustomerNumber.grid(row = 6, column=0, pady=2, sticky=tk.E)

        self.update_customerName = tk.Entry(self, width =20)
        self.update_customerName.grid(row = 7, column=1, pady=5, sticky=tk.W)
        label_updateCustomerName = tk.Label(self, text="Customer Name ")
        label_updateCustomerName.grid(row = 7, column=0, pady=2, sticky=tk.E)

        self.update_ListPriceMod = tk.Entry(self, width =20)
        self.update_ListPriceMod.grid(row = 8, column=1, pady=5, sticky=tk.W)
        label_updateListPriceMod = tk.Label(self, text="List Price Mod ")
        label_updateListPriceMod.grid(row = 8, column=0, pady=2, sticky=tk.E)

        def updateCustomer():
            '''Takes the values entered in the GUI and passes them to the update DB function.
            Precondition: Takes customer number (int), customer name (str), and list price mod (float) as
             input -> goes to customerValues.'''

            customerValues = [self.update_customerNumber.get(), self.update_customerName.get(), self.update_ListPriceMod.get()]
            CustomerBuilder.updateCustomer(customerValues)

                #clears the values entered in gui
            self.update_customerName.delete(0, tk.END)
            self.update_customerNumber.delete(0, tk.END)
            self.update_ListPriceMod.delete(0, tk.END)
        submitUpdateCustomer = tk.Button(self, text = "Update customer", command = lambda:[updateCustomer, updateStatusText("customer {0} updated.".format(self.update_customerNumber.get()))])
        submitUpdateCustomer.grid(row=9, column=0, columnspan=3, pady=2)
       

        '''3. Delete Customer'''
        deleteCustomerTitle = tk.Label(self, text="Delete Customer", font=LARGE_FONT)
        deleteCustomerTitle.grid(row=10, column=1, pady=10)

        self.delete_customerNumber = tk.Entry(self, width =20) 
        self.delete_customerNumber.grid(row = 11, column=1, pady=5,sticky=tk.W)
        label_deleteCustomerNumber = tk.Label(self, text="Customer Number ")
        label_deleteCustomerNumber.grid(row = 11, column=0, pady=2, sticky=tk.E)

        def delCustomer():
            '''Takes the customer number entered in the GUI and passes it to delete DB function.
            Precondition: Takes customer number (int) as input.'''

            customerValues = self.delete_customerNumber.get()
            CustomerBuilder.deleteCustomer(customerValues)

                #clears the values entered in gui
            self.delete_customerNumber.delete(0, tk.END)
        submitDeleteCustomer = tk.Button(self, text = "Delete customer", command = lambda: [delCustomer, updateStatusText("customer {0} deleted".format(self.delete_customerNumber.get()))])
        submitDeleteCustomer.grid(row=12, column=0, columnspan=3, pady=2)



class PricingPage(tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)





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
