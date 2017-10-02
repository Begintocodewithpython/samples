import pickle

class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    show_instrumentation = False

    min_price = 0.5
    max_price = 500.0

    max_stock_add = 50
    
    @staticmethod
    def get_tag_set_from_text(tag_string):
        '''
        Converts a comma separated list into a set 
        of individual items
        Converts the text to lower case and trims each
        word
        '''
        # Convert the string to lower case
        tag_string = str.lower(tag_string)

        # Make a list of all the words in the string
        # separated by the comma character
        tag_list = str.split(tag_string, sep=',')

        # Remove any spaces at the start or the
        # end of each string in the list
        tag_list = map(str.strip,tag_list)

        # return a set created from the list
        return set(tag_list)


    def __init__(self, stock_ref, price, tags):
        if StockItem.show_instrumentation:
            print('** StockItem __init__ called')
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.StockItem_version = 1
        self.tags = tags

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** StockItem check_version called')
        # This is version 1 - no need to update anything
        pass

    def __str__(self): 
        if StockItem.show_instrumentation:
            print('** StockItem __str__ called')
        template = '''Stock Reference: {0}
Price: {1}
Stock Level: {2}
Tags: {3}''' 

        return template.format(self.stock_ref, 
                               self.price, self.stock_level, 
                               self.tags) 

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

