import tkinter as tk
from tkinter import ttk
import dbFunctions
from UniversalModifiers import UniversalModifiers


LARGE_FONT= ("Verdana", 12)

class PricingPageGUI(tk.Frame):

    ''' Class that builds the pricing page. Here, the user can select various price
    modifying options to calculate the price of a part. The user can also display customer
    information and pricing levels.
    1. Basic setup
    2. Entry price mods
    3. Check button price mods
    4. Display customer info
    5. CLass methods '''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        '''1. Basic setup'''
        #this provides formatting for a 3 column grid
        tk.Widget.configure(self, background='white')

        blanklabel = tk.Label(self, text="", padx=50, bg='white')
        blanklabel.grid(row =0, column =2)

        #Status text widgit
        self.priceTxt = tk.Text(self, height = 10, width=37)
        self.priceTxt.grid(row = 13, column = 0, columnspan=3, sticky="nsw")
        self.priceTxt.insert(tk.END, "Price Breakdown:")

        addCustomerTitle = tk.Label(self, text="Get Pricing", font=LARGE_FONT, bg='white')
        addCustomerTitle.grid(row=0, column=1, pady=10)

        #methods
        self.clearEntry
        self.updatePriceBreakdownText
        self.updatePriceLevelsText
        self.getPriceLevels

        #seperators
        verticalSep = ttk.Separator(self, orient='vertical')
        verticalSep.grid(row=0, column=3, rowspan=15, sticky='nsw')
        horizontalSep = ttk.Separator(self, orient='horizontal')
        horizontalSep.grid(row=0, column=0, columnspan=7, sticky='new')

        '''2. Entered Pricing modifiers'''
        self.enter_customerNumber = ttk.Entry(self, width =20) 
        self.enter_customerNumber.grid(row = 1, column=1, pady=5,sticky=tk.W)
        label_customerNumber = tk.Label(self, text="Customer Number ", bg='white')
        label_customerNumber.grid(row = 1, column=0, pady=2, sticky='w')

        self.enter_timeSpent = ttk.Entry(self, width =20)
        self.enter_timeSpent.grid(row = 2, column=1, pady=5, sticky=tk.W)
        label_timeSpent = tk.Label(self, text="Time Spent (Days) ", bg='white')
        label_timeSpent.grid(row = 2, column=0, pady=2, sticky='w')

        self.enter_shippingCost= ttk.Entry(self, width =20)
        self.enter_shippingCost.grid(row = 3, column=1, pady=5, sticky=tk.W)
        label_shippingCost = tk.Label(self, text="Shipping costs ", bg='white')
        label_shippingCost.grid(row = 3, column=0, pady=2, sticky='w')

        self.enter_listPrice = ttk.Entry(self, width =20) 
        self.enter_listPrice.grid(row = 4, column=1, pady=5,sticky=tk.W)
        label_listPrice = tk.Label(self, text="List Price ", bg='white')
        label_listPrice.grid(row = 4, column=0, pady=2, sticky='w')

        self.enter_compPrice = ttk.Entry(self, width =20)
        self.enter_compPrice.grid(row = 5, column=1, pady=5, sticky=tk.W)
        label_compPrice = tk.Label(self, text="Competitor Price ", bg='white')
        label_compPrice.grid(row = 5, column=0, pady=2, sticky='w')

        ''' 3. Check buttons pricing modifiers'''
        self.check_expiditedDelivery = ttk.Checkbutton(self, width =17, text="Expidited Delivery")
        self.check_expiditedDelivery.grid(row = 8, column=1, pady=5, sticky=tk.W)

        self.check_hotItem = ttk.Checkbutton(self, width = 15, text="Hot Item")
        self.check_hotItem.grid(row = 8, column=0, pady=5, sticky= tk.W )

        self.check_truckDown = ttk.Checkbutton(self, width = 15, text="Truck Down")
        self.check_truckDown.grid(row = 8, column=2, pady=5, sticky= tk.W )

        submitUpdateCustomer = ttk.Button(self, text = "Calculate Pricing", command = lambda:[self.updateStatusText("customer {0} updated.".format(self.update_customerNumber.get())), self.clearEntry()])
        submitUpdateCustomer.grid(row=9, column=0, columnspan=3, pady=2)

        ''' 4. Display customer info '''
        displayCustomerTitle = tk.Label(self, text="Display Customer Levels", font=LARGE_FONT, bg='white')
        displayCustomerTitle.grid(row=0, column=3, columnspan=4, pady=10, padx=10)

        self.enter_customerNumber2 = ttk.Entry(self, width=20)
        self.enter_customerNumber2.grid(row=1, column =4, pady=5, padx=10, sticky="ne")
        label_customerNumber2 = tk.Label(self, text="Customer Number", bg="white")
        label_customerNumber2.grid(row=1, column=3, pady=2, sticky= "nw")

        displayInfo = ttk.Button(self, text = "Display Levels", command = lambda:[self.getPriceLevels(), self.clearEntry()])
        displayInfo.grid(row=2, column=3, columnspan=3, pady=2)

        self.customerT = tk.Text(self, height = 4, width=3)
        self.customerT.grid(row = 3, column = 3, columnspan=3, sticky="nsew")


    ''' 5. Class methods'''
    
    def updatePriceBreakdownText(self, status):
            '''This function updates the price breakdown text box. The status text tells the user
            if their enter/update/or delete customer action was successful or not, and the pricing
            breakdown of the information they entered.'''
        
            self.priceTxt.delete(1.0, tk.END) #clears textbox before adding new message
            self.priceTxt.insert(tk.END, " Status: " + status)

    def updatePriceLevelsText(self, status):
            '''This function updates the price levels text box. The status text tells the user
            if their enter/update/or delete customer action was successful or not, and the pricing
            breakdown of the information they entered.'''
        
            self.customerT.delete(1.0, tk.END) #clears textbox before adding new message
            self.customerT.insert(tk.END, status + "\n")
    
    def getPriceLevels(self):
        ''' This function gets the pricing levels and customer information from the DB table. 
        It then displays it in the customerT text widget.'''

        customerNum = self.enter_customerNumber2.get()
        info = dbFunctions.select_AllCustomerInfo(customerNum)
        list(info)

        self.updatePriceLevelsText("Customer: {0} \n Name: {1} \n List price mod: {2} ".format(customerNum, info[0], info[2]))

    def clearEntry(self):
        '''Function that clears the user entered data from the form
            whenever calculate price button is clicked.'''
        self.enter_customerNumber.delete(0, tk.END)
        self.enter_timeSpent.delete(0, tk.END)
        self.enter_shippingCost.delete(0, tk.END)
        self.enter_listPrice.delete(0, tk.END)
        self.enter_compPrice.delete(0, tk.END)
    
    def calculatePricing(self):
        '''Function that calculates pricing based upon user inputs'''
        customerNumber = int(self.enter_customerNumber.get())
        shippingCost = int(self.enter_shippingCost.get())
        listPrice = int(self.enter_listPrice.get())
        listPriceMod = listPrice * int(dbFunctions.select_listPriceMod(customerNumber))
        compPrice = int(self.enter_compPrice.get())

        hotItemMod,expiditedMod = 1
        truckDown = 0

        # check boxes
        if self.check_hotItem.getboolean():
            hotItemMod = None
        if self.check_truckDown.getboolean():
            truckDown = UniversalModifiers.truckDownFee()
        if  self.check_expiditedDeliery.getboolean():
            expiditedMod = UniversalModifiers.expiditedDeliveryMod(shippingCost)
    

        days = int(self.enter_timeSpent.get())
        if days >= 1:
            timeSpentMod = UniversalModifiers.timeSinkFee(days)

            totalCost =  (listPriceMod * timeSpentMod) + shippingCost
        else:
            totalCost =  listPriceMod + shippingCost


        
        
        return totalCost

