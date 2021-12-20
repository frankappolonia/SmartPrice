
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

        expiditedFee = deliveryFee + (deliveryFee * 0.50)
        return expiditedFee
    
    def timeSinkFee(days):
        '''Takes a number of days spent on an order and the current price of the part,
        upcharging it based on the time investment of aquiring the part'''
        mod = 1
        if days == 1:
            mod = 1.10
        elif days == 2: 
            mod =  1.20
        elif days >= 3: 
            mod = 1.30
        return mod
    
    def rareProductFee(price):
        '''Provides an upcharge for a high demand product/product that cant be found
        elsewhere/product that customer will buy no matter what'''
        return price*2.0
    
    def truckDownFee(self):
        return 50