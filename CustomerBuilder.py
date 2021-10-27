import dbFunctions

'''Module that has different functions for the customer table:
1. User inputs for establishing new customer info, updating info, and deleting info.
2. Creating and inserting new customers into the customer table.
3. Creating and inserting updated customer info into the customer table.
4. Deleting customers from the customer table.'''


'''----------- 1. USER INPUTS --------------------'''

def InputNewCustomerInfo():
    '''Function that takes the new customers info as input.
    Returns account name, account number, and the list price modification'''

    while True:
        try:
            accountNum = int(input("Enter the account number: "))
            accountName = input("Enter the account or customer name: ")
            listPriceMod = float(input("Enter the list price modifier: "))
            break
        except ValueError:
            print("Invalid input. Account number and list price mod must be an int")

    return [accountNum, accountName, listPriceMod]

def InputUpdatedCustomerInfo():
    '''Function that takes updated customer info as input.
    Returns account number, updated account name, and updated list price modification'''

    while True:
        try:
            accountNum = int(input("Enter account number: "))
            accountName = input("Enter the new customer name: ")
            listPriceMod = input("Enter the new list price modifier: ")
            break
        except ValueError:
            print("Invalid Input. Account number and list price mod must be an int.")

    return [accountNum, accountName, listPriceMod]

def InputCustomerDeletionID():
    '''Function that calls an input to get a customer ID for deleteing the
    customer in question from the table.'''
    
    while True:
        try:
            accountNum = int(input("Enter the account number you wish to delete."))
            break
        except ValueError:
            print("Invalid input. Account number must be an integer.")

    return accountNum

def InputSelectCustomerMod():
    '''Function that calls an input to get a customer ID for retrieving the customer's
    list price mod.'''

    while True:
        try:
            accountNum = int(input("Enter the customer you want to see the mod: "))
            break
        except ValueError:
            print("Invalid input. Account number must be an integer.")

    return accountNum


'''------------- 2. CUSTOMER CREATION AND INSERTION----------------'''

def createCustomer(customerInfo):
    '''Takes a list of customer information as argument, and calls the 
    commit_customer function to insert the new row into the customer table.

    Uses the commit_customer function.'''

    database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"
    connection = dbFunctions.create_connection(database)

    with connection:
        # customerInfo is AWLAYS [accountNum, accountName, listPriceMod]
        customerParam = (customerInfo[0], customerInfo[1], customerInfo[0], customerInfo[2])
        #                 (ID,               name,         customerNumber,   listPriceMod)
        customerID = commit_createCustomer(connection, customerParam)

def commit_createCustomer(conn, customerParam):
    '''Commits new customer (row) into the customer table. Takes a DB connection
    and customer info as arguments.
    Returns the row ID'''

    sql = '''   INSERT INTO customer(id, name, customerNumber, listPriceMod)
                VALUES(?, ?, ?, ?)'''

    cursor = conn.cursor()
    cursor.execute(sql, customerParam)
    conn.commit()
    return cursor.lastrowid


'''------------------- 3. CUSTOMER UPDATING------------------------'''

def updateCustomer(updatedSpecsList):
    '''Takes a list of updated customer information as argument, and calls
    the commit_updateCustomer function to insert the updated informaton to the customer table.
     
     Uses commit_updateCustomer function.'''

    database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"
    connection = dbFunctions.create_connection(database)

    with connection:
        # updatedSpecsList is AWLAYS [acountNum, newAccountName, newListPriceMod]
        commit_updateCustomer(connection, (updatedSpecsList[1], updatedSpecsList[2], updatedSpecsList[0]))
                                   #(new account,         new list price,       the id of the row)

def commit_updateCustomer(conn, customer):
    '''Commits updated info to a particular customer already in the table..
        Takes DB connection and updated customer info as arguments.'''
    
    sql = '''   UPDATE customer
                SET name = ? ,
                    listPriceMod = ? 
                WHERE ID = ?'''

    cursor = conn.cursor()
    cursor.execute(sql, customer)
    conn.commit()


'''------------- 4. CUSTOMER DELETION------------------'''

def deleteCustomer(customerID):
    '''Takes a customer ID as input and passes it to the commit_deleteCustomer 
    function.
        
        Uses the commit_deleteCustomer function.'''

    database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"
    connection = dbFunctions.create_connection(database)

    with connection:
        commit_deleteCustomer(connection, customerID)

def commit_deleteCustomer(conn, customerID):
    '''Commits the deletion of a customer. Takes DB conneciton and customer ID as 
    arguments.'''

    sql = 'DELETE FROM customer WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (customerID,))
    conn.commit()





    

