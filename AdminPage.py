import tkinter as tk
from tkinter import ttk
import CustomerBuilder
 
LARGE_FONT= ("Verdana", 12)
class AdminPageGui(tk.Frame):

    ''' Class that builds the admin page. Here, the user can add, update or delete
    customers from the customer DB table. Need admin privilidge (username and password)
    to access this page.
    1. Basic setup
    2. Add Customer
    3. Update Customer
    4. Delete Customer
    5. CLass methods '''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        '''1. Basic setup'''

        tk.Widget.configure(self, background='white')

        #seperators
        verticalSep = ttk.Separator(self, orient='vertical')
        verticalSep.grid(row=0, column=2, rowspan=15, padx=20, sticky='wens')
        horizontalSep = ttk.Separator(self, orient='horizontal')
        horizontalSep.grid(row=0, column=0, columnspan=9, sticky='new')

        #Status text widgit
        self.T = tk.Text(self, height = 6, width=25, fg='gray')
        self.T.grid(row = 6, column = 3, columnspan=2, sticky="ns")
        self.T.insert(tk.END, "Status:")

        #label_= tk.Label(self, text="", bg='white')
        #label_.grid(row = 0, column=2, rowspan=4, pady=2, sticky='ew')

        self.updateStatusText
        self.clearEntry
        
        '''2. Add customer'''
        self.insertCustomer

        addCustomerTitle = tk.Label(self, text="Add Customer", font=LARGE_FONT, bg='white')
        addCustomerTitle.grid(row=0, column=0, pady=10, sticky='w')

        self.enter_customerNumber = ttk.Entry(self, width =15) 
        self.enter_customerNumber.grid(row = 1, column=1, pady=5,sticky='e')
        label_customerNumber = tk.Label(self, text="Customer Number ", bg='white')
        label_customerNumber.grid(row = 1, column=0, pady=2, sticky='w')

        self.enter_customerName = ttk.Entry(self, width =15)
        self.enter_customerName.grid(row = 2, column=1, pady=5, sticky='e')
        label_customerName = tk.Label(self, text="Customer Name ", bg='white')
        label_customerName.grid(row = 2, column=0, pady=2, sticky='w')

        self.enter_ListPriceMod = ttk.Entry(self, width =15)
        self.enter_ListPriceMod.grid(row = 3, column=1, pady=5, sticky='e')
        label_ListPriceMod = tk.Label(self, text="List Price Mod ", bg='white')
        label_ListPriceMod.grid(row = 3, column=0, pady=2, sticky='w')

        submitCustomer = ttk.Button(self, text = "Add customer to DB", command = lambda: self.insertCustomer()) 
        submitCustomer.grid(row=4, column=0, columnspan=2, pady=2, sticky='we')

        '''3. Update Customer'''
        self.updateCustomer

        updateCustomerTitle = tk.Label(self, text="Update Customer", font=LARGE_FONT, bg='white')
        updateCustomerTitle.grid(row=0, column=4, columnspan=1, pady=10, sticky='w')

        self.update_customerNumber = ttk.Entry(self, width =15) 
        self.update_customerNumber.grid(row = 1, column=4, pady=5, sticky='e')
        label_updateCustomerNumber = tk.Label(self, text="Customer Number", bg='white')
        label_updateCustomerNumber.grid(row = 1, column=3, pady=2, sticky='w')

        self.update_customerName = ttk.Entry(self, width =15)
        self.update_customerName.grid(row = 2, column=4, pady=5, sticky='e')
        label_updateCustomerName = tk.Label(self, text="Customer Name", bg='white')
        label_updateCustomerName.grid(row = 2, column=3, pady=2, sticky='w')

        self.update_ListPriceMod = ttk.Entry(self, width =15)
        self.update_ListPriceMod.grid(row = 3, column=4, pady=5, sticky='e')
        label_updateListPriceMod = tk.Label(self, text="List Price Mod", bg='white')
        label_updateListPriceMod.grid(row = 3, column=3, pady=2, sticky='w')

        submitUpdateCustomer = ttk.Button(self, text = "Update customer", command = lambda: self.updateCustomer())
        submitUpdateCustomer.grid(row=4, column=3, columnspan=2, pady=2, sticky='we')

        '''4. Delete Customer'''
        self.delCustomer

        deleteCustomerTitle = tk.Label(self, text="Delete Customer", font=LARGE_FONT, bg='white')
        deleteCustomerTitle.grid(row=9, column=0, columnspan=2, pady=10, sticky='w')

        self.delete_customerNumber = ttk.Entry(self, width =20) 
        self.delete_customerNumber.grid(row = 10, column=1, pady=5,sticky='e')
        label_deleteCustomerNumber = tk.Label(self, text="Customer Number ", bg='white')
        label_deleteCustomerNumber.grid(row = 10, column=0, pady=2, sticky='w')

        submitDeleteCustomer = ttk.Button(self, text = "Delete customer", command = lambda: self.delCustomer())
        submitDeleteCustomer.grid(row=12, column=0, columnspan=2, pady=2, sticky='we')


    ''' 5. CLASS Methods '''
    def clearEntry(self):
        '''Function that clears the user entered data from the form
            whenever an entry button is clicked.'''
        self.enter_customerName.delete(0, tk.END)
        self.enter_customerNumber.delete(0, tk.END)
        self.enter_ListPriceMod.delete(0, tk.END)
        self.update_customerName.delete(0, tk.END)
        self.update_customerNumber.delete(0, tk.END)
        self.update_ListPriceMod.delete(0, tk.END)
        self.delete_customerNumber.delete(0, tk.END)

    def updateStatusText(self, status):
        '''This function updates the status text bar. The status text tells the user
            if their enter/update/or delete customer action was successful or not. This function
            is called with every button command in this class.'''

        self.T.delete(1.0, tk.END) #clears textbox before adding new message
        self.T.insert(tk.END, " Status: " + status)
         
    def insertCustomer(self):
        '''Takes the values entered in the GUI and passes them to the createCustomer function from
        the customerBuilder module. createCustomer inserts a new customer into the table. Additonally, contains
        exception handling for valid inputs to the customer DB table.
            Precondition: Takes customer number (int), customer name (str), and list price mod (float) as
             input -> goes to customerValues.
             
             Called with tk button'''
        
        # Checks if the accountnumber entry and listprice entry are integers
        accountNumFlag = self.enter_customerNumber.get().isdigit()
        listPriceFlag = self.enter_ListPriceMod.get().isdigit()

        if accountNumFlag and listPriceFlag: # execute insert customer 
            customerValues = [self.enter_customerNumber.get(), self.enter_customerName.get(), self.enter_ListPriceMod.get()]
            CustomerBuilder.createCustomer(customerValues)
            self.updateStatusText("customer {0} ({1}) added to DB.".format(self.enter_customerNumber.get(), self.enter_customerName.get()))
            self.clearEntry()

        else: #catch for invalid input
            self.updateStatusText("Invalid input. Account number and list price mod must be integers!")
            self.clearEntry()

    def updateCustomer(self):
        '''Takes the values entered in the GUI and passes them to the updateCustomer function from
        the CustomerBuilder module. updateCustomer updates the values of an existing customer in the table. Additonally,
        does exception handling for valid inputs to the customer DB table.
            Precondition: Takes customer number (int), customer name (str), and list price mod (float) as
             input -> goes to customerValues.
             
             Called with tk button'''

        accountNumFlag = self.update_customerNumber.get().isdigit()
        listPriceFlag = self.update_ListPriceMod.get().isdigit()

        if accountNumFlag and listPriceFlag:
            customerValues = [self.update_customerNumber.get(), self.update_customerName.get(), self.update_ListPriceMod.get()]
            CustomerBuilder.updateCustomer(customerValues)
            self.updateStatusText("customer {0} updated.".format(self.update_customerNumber.get()))
            self.clearEntry()
        else:
            self.updateStatusText("Invalid input. Account number and list price mod must be integers!")
            self.clearEntry()

    def delCustomer(self):
        '''Takes the customer number entered in the GUI and passes it to deleteCustomer funtion from the 
        customerBuilder module. deleteCustomer removes an entire row from the table.
            Precondition: Takes customer number (int) as input.
            
            Called with tk button'''

        accountNumFlag = self.delete_customerNumber.get().isdigit()

        if accountNumFlag:
            customerValues = self.delete_customerNumber.get()
            CustomerBuilder.deleteCustomer(customerValues)
            self.updateStatusText("customer {0} deleted".format(self.delete_customerNumber.get()))
            self.clearEntry()
        else:
            self.updateStatusText("Invalid input. Account number must be an integer!")
            self.clearEntry()
