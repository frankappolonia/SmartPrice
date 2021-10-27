from CustomerBuilder import *
from dbFunctions import *


''' Script that tests different Customer table commands from the CustomerBuilder module.'''

scriptFlag = True
while scriptFlag:
    x = int(input("enter 1 for getCustomer, 2 for updateCustomer, 3 for delete customer, 4, to select mod, 0 to quit: "))
    
    if x == 1:
        #create customer
        createCustomer(InputNewCustomerInfo())
    elif x == 2:
        #update customer
        updateCustomer(InputUpdatedCustomerInfo())
    elif x == 3:
        #delete customer
        deleteCustomer(InputCustomerDeletionID()) 
    elif x == 4:
        y = select_listPriceMod(InputSelectCustomerMod())
        print(y)
    elif x == 5:
        z = select_AllCustomerInfo(InputSelectCustomerMod())
        print(z)
        
    elif x == 0:
        print("test end")
        scriptFlag = False
