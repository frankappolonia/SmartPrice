import tkinter as tk


LARGE_FONT= ("Verdana", 12)

class PricingPageGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        '''1. Basic setup'''
        #this provides formatting for a 3 column grid
        blanklabel = tk.Label(self, text="", padx=50)
        blanklabel.grid(row =0, column =2)

        #Status text widgit
        self.T = tk.Text(self, height = 10, width=3)
        self.T.grid(row = 13, column = 0, columnspan=3, sticky="nsew")
        self.T.insert(tk.END, "Price Breakdown:")


        def updateStatusText(status):
            '''This function updates the status text bar. The status text tells the user
            if their enter/update/or delete customer action was successful or not. This function
            is called with every button command in this class.'''

            self.T.delete(1.0, tk.END) #clears textbox before adding new message
            self.T.insert(tk.END, " Status: " + status)

        def clearEntry():
            '''Function that clears the user entered data from the form
            whenever calculate price button is clicked.'''
            self.enter_customerNumber.delete(0, tk.END)
            self.enter_timeSpent.delete(0, tk.END)
            self.enter_shippingCost.delete(0, tk.END)
            self.enter_listPrice.delete(0, tk.END)
            self.enter_compPrice.delete(0, tk.END)

        addCustomerTitle = tk.Label(self, text="Get Pricing", font=LARGE_FONT)
        addCustomerTitle.grid(row=0, column=1, pady=10)

        '''2. Entered Pricing modifiers'''
        self.enter_customerNumber = tk.Entry(self, width =20) 
        self.enter_customerNumber.grid(row = 1, column=1, pady=5,sticky=tk.W)
        label_customerNumber = tk.Label(self, text="Customer Number ")
        label_customerNumber.grid(row = 1, column=0, pady=2, sticky=tk.E)

        self.enter_timeSpent = tk.Entry(self, width =20)
        self.enter_timeSpent.grid(row = 2, column=1, pady=5, sticky=tk.W)
        label_timeSpent = tk.Label(self, text="Time Spent (Days) ")
        label_timeSpent.grid(row = 2, column=0, pady=2, sticky=tk.E)

        self.enter_shippingCost= tk.Entry(self, width =20)
        self.enter_shippingCost.grid(row = 3, column=1, pady=5, sticky=tk.W)
        label_shippingCost = tk.Label(self, text="Shipping costs ")
        label_shippingCost.grid(row = 3, column=0, pady=2, sticky=tk.E)

        self.enter_listPrice = tk.Entry(self, width =20) 
        self.enter_listPrice.grid(row = 6, column=1, pady=5,sticky=tk.W)
        label_listPrice = tk.Label(self, text="List Price ")
        label_listPrice.grid(row = 6, column=0, pady=2, sticky=tk.E)

        self.enter_compPrice = tk.Entry(self, width =20)
        self.enter_compPrice.grid(row = 7, column=1, pady=5, sticky=tk.W)
        label_compPrice = tk.Label(self, text="Competitor Price ")
        label_compPrice.grid(row = 7, column=0, pady=2, sticky=tk.E)

        ''' 3. Check buttons pricing modifiers'''
        self.update_ListPriceMod = tk.Checkbutton(self, width =15, text="Expidited Delivery",)
        self.update_ListPriceMod.grid(row = 8, column=1, pady=5, sticky=tk.W)

        self.check_hotItem = tk.Checkbutton(self, width = 15, text="Hot Item")
        self.check_hotItem.grid(row = 8, column=0, pady=5, sticky= tk.W )

        self.check_truckDown = tk.Checkbutton(self, width = 15, text="Truck Down")
        self.check_truckDown.grid(row = 8, column=2, pady=5, sticky= tk.W )



        submitUpdateCustomer = tk.Button(self, text = "Calculate Pricing", command = lambda:[ updateStatusText("customer {0} updated.".format(self.update_customerNumber.get())), clearEntry()])
        submitUpdateCustomer.grid(row=9, column=0, columnspan=3, pady=2)
