# EG11-10 FashionShop template

class FashionShop:

    def __init__(self, name):
        pass

    def save(self):
        '''
        Saves the fashion shop to the given filename
        Data is stored in binary as pickled file
        Exceptions will be raised if the save fails
        '''
        pass

    @staticmethod
    def load(filename):
        '''
        Loads the fashion shop from the given filename
        Data are stored in binary as pickled file
        Exceptions will be raised if the load fails
        '''
        return None

    def __str__(self):
        return ""

    def get_item(self,key):
        '''
        Gets an item from the stock dictionary
        Returns None if there is no item for
        this key
        '''
        return None

    def store_new_item(self,item):
        '''
        Store an item in the fashion shop
        The item is indexed on the stock_ref value
        Raises an exception if the item already 
        exists
        '''
        pass

