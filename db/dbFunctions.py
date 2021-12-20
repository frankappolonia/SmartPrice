import sqlite3
from sqlite3 import Error

'''Module that imports SQLite. Has numerous basic database functions:
1. Function to establish DB connection
2. Function to create table
3. Functions to select data from a table'''

database = "C:\\Users\\appolofr\\Documents\\Github\\SmartPrice\\test.db"

'''---------- 1. Connection to DB-----------------'''

def create_connection(path):
    '''Function that establishes a connection to the DB.
    Takes a path to the DB file as a parameter and returns a connection'''

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to DB Successful")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection


'''----------- 2. Create/Commit DB Table -----------'''

def create_table(conn, create_table_sql):
    #Template that can be used to create a new table. 
    # Paremeters are a DB connection, and table specifications.
    ''' create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement'''

    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(f"The error '{e}' occured")

def insertTable():
    '''Function to insert a newly created table to a DB.'''
    #database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"

    #this is where the customer table is created
    sql_create_customer_table = """CREATE TABLE IF NOT EXISTS (
                                    customer
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    customerNumber integer,
                                    listPriceMod integer NOT NULL   
                                    );"""
    #create connection to db file                              
    connection = create_connection(database)

    #create table 
    if connection is not None:
        create_table(connection, sql_create_customer_table)
        print("Table made")
    else:
        print("Error!")


''''----------- 3. Select Data from DB table --------------'''

def select_listPriceMod(id):

    '''Takes a customer id as argument. Returns the customer's listPriceMod from
    the customer table.'''

    #database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"
    conn = create_connection(database)

    cursor = conn.cursor()
    cursor.execute("SELECT listPriceMod FROM customer WHERE rowid=?", (id,))

    try:
        # Exception handling for invalid account number by user
        item = cursor.fetchone()[0] #fetchone returns a TUPLE, so I index the first element and cast it to a float.
        return item
    except TypeError:
        print("Not a valid account number!")
        
def select_AllCustomerInfo(id):
    '''Takes a customer id as argument. Returns all the customer information
    (name, account number, listPriceMod.)'''

    #database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"
    conn = create_connection(database)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer WHERE rowid=?", (id,))

    try: 
        #exception handiling for invalid account number from user
        item = cursor.fetchone()[1:]
        return item
    except TypeError:
        return "Not a valid account number!"

'''def run_select_data(id):

    database = "C:\\Users\\appolofr\\Documents\\vscode\\Air Brake\\test.db"
    conn = create_connection(database)
    with conn:
        return select_data(conn, id)'''