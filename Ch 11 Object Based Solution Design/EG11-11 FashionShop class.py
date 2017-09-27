# EG11-11 FashionShop class

import pickle

from BTCInput import *

class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    show_instrumentation = False
    
    min_price = 0.5
    max_price = 500.0

    max_stock_add = 50

    def __init__(self, stock_ref, price, color, location):
        if StockItem.show_instrumentation:
            print('** StockItem __init__ called')
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.StockItem_version = 1
        self.color = color
        self.location = location

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** StockItem get item_name called')
        return 'Stock Item'
        
    def check_version(self):
        if StockItem.show_instrumentation:
            print('** StockItem check_version called')
        # This is version 1 - no need to update anything
        pass

    def __str__(self): 
        if StockItem.show_instrumentation:
            print('** StockItem __str__ called')
        template = '''Stock Reference: {0}
Type: {1}
Location: {2}
Price: {3}
Stock level: {4}
Color: {5}''' 

        return template.format(self.stock_ref, self.item_name, self.location,
                                self.price, self.stock_level, self.color) 

    def add_stock(self,count):
        '''
        Adds stock for this item. 
        Count gives the amount of stock to add
        Will raise exceptions if the number is invalid
        '''
        if StockItem.show_instrumentation:
            print('** StockItem add_stock called')
        if count < 0 or count > StockItem.max_stock_add:
            raise Exception('Invalid add amount')

        self.__stock_level = self.__stock_level + count

    def sell_stock(self, count):
        '''
        Sells stock for this item.
        count gives the number of items to sell
        Will raise exceptions if the number is invalid
        '''
        if StockItem.show_instrumentation:
            print('** StockItem sell_stock called')
        if count < 1:
            raise Exception('Invalid number of items to sell')

        if count > self.stock_level:
            raise Exception('Not enough stock to sell')

        self.__stock_level = self.__stock_level - count

    def set_price(self, new_price):
        if StockItem.show_instrumentation:
            print('** StockItem set_price called')
        if price < StockItem.min_price or price > StockItem.max_price:
            raise Exception('Price out of range')
        self.__price = new_price

    @property
    def price(self):
        if StockItem.show_instrumentation:
            print('** StockItem get price called')
        return self.__price

    @property
    def stock_level(self):
        if StockItem.show_instrumentation:
            print('** StockItem get stock level called')
        return self.__stock_level


class Dress(StockItem):

    def __init__(self, stock_ref, price, color, pattern, size, location):
        if StockItem.show_instrumentation:
            print('** Dress __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, location=location)
        self.pattern = pattern
        self.size = size
        self.Dress_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Dress get item_name called')
        return 'Dress'
        
    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Dress check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Dress __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Pattern: {1}
Size: {2}'''
        return template.format(stock_details, self.pattern,
                               self.size)
 

class Trousers(StockItem):

    def __init__(self, stock_ref, price, color, pattern, length, waist, location):
        if StockItem.show_instrumentation:
            print('** Trousers __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, location=location)
        self.pattern = pattern
        self.length = length
        self.waist = waist
        self.trousers_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Trousers get item_name called')
        return 'Trousers'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Trousers check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Trousers __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Pattern: {1}
Length: {2}
Waist: {3}'''
        return template.format(stock_details, self.pattern,
                               self.length, self.waist)


class Jeans(Trousers):

    def __init__(self, stock_ref, price, color, pattern, length, waist, style, location):
        if StockItem.show_instrumentation:
            print('** Jeans __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, pattern=pattern, length=length,
                         waist=waist, location=location)
        self.style = style
        self.jeans_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Jeans get item_name called')
        return 'Jeans'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Jeans check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Jeans __str__ called')
        trousers_details = super().__str__()
        template = '''{0}
Style: {1}'''
        return template.format(trousers_details, self.style)


class Hat(StockItem):

    def __init__(self, stock_ref, price, color, size, location):
        if StockItem.show_instrumentation:
            print('** Hat __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, location=location)
        self.size = size
        self.Hat_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Hat get item_name called')
        return 'Hat'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Hat check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Hat __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Size: {1}'''
        return template.format(stock_details, self.size)

    @staticmethod
    def make_test_data():
        '''
        Retuns hat test items one at a time
        '''
        stock_id = 1
        for price in [50,100,200,500]:
            for color in ['red', 'green', 'blue', 'yellow', 'pink']:
                for pattern in ['plain', 'check', 'lines']:
                    for size in [6, 7, 8, 9]:
                        id_string = 'HA' + str(stock_id)
                        h = Hat(id_string, price, color, size, 'hat shelf')
                        stock_id = stock_id + 1
                        yield h

class Blouse(StockItem):
    
    def __init__(self, stock_ref, price, color, size, style, pattern, location):
        if StockItem.show_instrumentation:
            print('** Blouse __init__ called')
        super().__init__(stock_ref, price, color, location)
        self.size = size
        self.style = style
        self.pattern = pattern
        self.Hat_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Blouse get item_name called')
        return 'Blouse'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Blouse check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Blouse __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Size: {1}
Style: {2}
Pattern: {3}'''
        return template.format(stock_details, self.size,
                               self.style, self.pattern)

import pickle


class FashionShop:

    show_instrumentation = False

    def __init__(self):
        if FashionShop.show_instrumentation:
            print('** FashionShop __init__ called')
        self.__stock_dictionary = {}

    def save(self, filename):
        '''
        Saves the fashion shop to the given filename
        Data is stored in binary as pickled file
        Exceptions will be raised if the save fails
        '''
        if FashionShop.show_instrumentation:
            print('** FashionShop save called')
        with open(filename,'wb') as out_file:
            pickle.dump(self,out_file)

    @staticmethod
    def load(filename):
        '''
        Loads the fashion shop from the given filename
        Data are stored in binary as pickled file
        Exceptions will be raised if the load fails
        '''
        if FashionShop.show_instrumentation:
            print('** FashionShop load called')
        with open(filename,'rb') as input_file:
            result = pickle.load(input_file)

        # Now update the versions of the loaded stock items
        for stock_item in result.__stock_dictionary.values():
            stock_item.check_version()
        return result


    def store_new_stock_item(self, stock_item):
        '''
        Create a new item in the fashion shop
        The item is indexed on the stock_ref value
        Raises an exception if the item already 
        exists
        '''
        if FashionShop.show_instrumentation:
            print('** FashionShop store_new_stock_item called')
        if stock_item.stock_ref in self.__stock_dictionary:
            raise Exception('Item already present') 
        self.__stock_dictionary[stock_item.stock_ref] = stock_item


    def find_stock_item(self, stock_ref):
        '''
        Gets an item from the stock dictionary
        Returns None if there is no item for
        this key
        '''
        if FashionShop.show_instrumentation:
            print('** FashionShop find_stock_item called')
        if stock_ref in self.__stock_dictionary:
            return self.__stock_dictionary[stock_ref]
        else:
            return None

    def __str__(self):
        if FashionShop.show_instrumentation:
            print('** FashionShop __str__ called')
        stock = map(str,self.__stock_dictionary.values())
        stock_list = '\n'.join(stock)
        template = '''Items in Stock

{0}
'''
        return template.format(stock_list)


# Create a new Fashion Shop
shop = FashionShop()

# Save it in a file 
shop.save('FashionShop.pickle')

# Load a copy back from teh file
loaded_shop = FashionShop.load('FashionShop.pickle')

# Create a new dress
dress = Dress(stock_ref='D001', price=100, color='red', pattern='swirly', size=12, location='front')

# Store the dress in the Fashion Shop
shop. store_new_stock_item(dress)

# Find the dress
item = shop.find_stock_item('D001')

# Print out an error if the dress is not found
if item == None:
    print('Item not found')
else:
    print(item)

# Print out the entire fashion shop
print(shop)

        
        
