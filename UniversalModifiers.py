
''' Modual that provides universal pricing modifiers for customers.'''

class UniversalModifiers():
    '''This class provides universal pricing modifiers. These are modifiers which are true
     indpednent of the customer or part (i.e. we had to run to automann and deliver same day.)'''
	
    def __init__(self, automannPickup, localDelivery, nonLocalDelivery):
        self.automannPickup = automannPickup
        self.localDelivery = localDelivery
        self.nonLocalDelivery = nonLocalDelivery
    
    def expiditedDeliveryMod(deliveryFee):
        '''Takes a delivery cost (i.e. automannPickup) as input and returns 
		  a modified value for expidited same day delivery '''

        expiditedFee = (deliveryFee * 1.20)
        return expiditedFee
    
    def timeSinkFee(days, price):
        '''Takes a number of days spent on an order and the current price of the part,
        upcharging it based on the time investment of aquiring the part'''
        if days == 1:
            newPrice = price * 1.10
        elif days == 2: 
            newPrice = price * 1.20
        elif days >= 3: 
            newPrice = price *1.30
        return newPrice
    
    def rareProductFee(listPrice):
        '''Provides an upcharge for a high demand product/product that cant be found
        elsewhere/product that customer will buy no matter what'''
        return listPrice*2.0