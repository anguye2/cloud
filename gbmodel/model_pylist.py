"""
Python list model
"""
from .Model import Model

class model(Model):
    def __init__(self):
        """
        Create an empty dictionary and then calls the populateDict function 
        """
        self.foodcart = {}
        self.populateDict()
                

    def select(self):
        """
        Get all rows from the food cart database
        Each row contains: name, address, city, state, zipcode, hour, phone, rating
        :return a dic
        """
        return self.foodcart
    
    def populateDict(self):
        """
        Function to populate a food cart into the dic
        """
        self.foodcart['esan'] = {
            "name": "esan",
            "address": "123 SE",
            "city": "Portland",
            "state": "OR",
            "zipcode": "97223",
            "hour": "8 AM - 9 PM!",
            "rating": "3",
        }
        
        return True
