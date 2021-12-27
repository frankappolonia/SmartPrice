from db import CustomerBuilder 
from db import dbFunctions


''' Script that tests different Customer table commands from the CustomerBuilder module.'''

scriptFlag = True
while scriptFlag:
    x = int(input("enter 1 for getCustomer, 2 for updateCustomer, 3 for delete customer, 4, to select mod, 0 to quit: "))
    
    if x == 1:
        #create customer
        CustomerBuilder.createCustomer(CustomerBuilder.InputNewCustomerInfo())
    elif x == 2:
        #update customer
        CustomerBuilder.updateCustomer(CustomerBuilder.InputUpdatedCustomerInfo())
    elif x == 3:
        #delete customer
        CustomerBuilder.deleteCustomer(CustomerBuilder.InputCustomerDeletionID()) 
    elif x == 4:
        y = dbFunctions.select_listPriceMod(CustomerBuilder.InputSelectCustomerMod())
        print(y)
    elif x == 5:
        z = dbFunctions.select_AllCustomerInfo(CustomerBuilder.InputSelectCustomerMod())
        print(z)
        
    elif x == 0:
        print("test end")
        scriptFlag = False
