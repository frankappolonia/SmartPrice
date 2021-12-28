# SmartPrice
Desktop application that provides smart pricing for the parts counter at Air Brake & Equipment.

  There are various subjective variables in the truck parts industry that makes pricing difficult (demand, truck-down situations, shipping, delivery, etc). Pricing for part x varies depending on these variables. Moreover, particular customers have different pricing levels (municipal, private, etc). Accordingly, it can be difficult for parts countermen to correctly price parts. This applicaiton seeks to account for these different variables and provide accurate price quoting for parts.

  Although this software was designed as a business applicaiton particular to truck parts, it could technically be used in a wide variety of business applications. You wouldd only need to change what kinds of pricing variables you use, and the particular numbers behind the pricing modifiers to suit the needs of your specific busienss.

1. How-To

  The use of the software is relatively straightforward. There are two major features - a pricing page and an admin page. 

1a. The admin page

  On the Admin page, a password protected portion of the software (optional), users with privildged access can add, update, and delete customers from the customer database table. Each customer in the customer table has 3 properties: a customer number, a name, and a pricing modifier. The table is set so that the customer number is also automatically used as the unique key for the row. The customer pricing modifier is a percentage that is used as a multipier in the pricing algoirthm. I.e. a 1.25 price multipliter for customer 123 adds a 25% markup to the base price of the product.
  
  1b. The pricing page
    
    On the pricing page, any user can enter a customer number and various variables to get pricing on a part. The pricing variables are shipping costs, time spent, list price, competitor price, and further modifiers like hot item, expidited deliery, and a truck-down situation. All of these variables are technically optional, and the pricing algorithm will calculate a price for the part based upon the variables that are used by the user. On this page, it is also possible for a user to look up a customer by their number and see the information saved on them in the db table, including their pricing modifier.
