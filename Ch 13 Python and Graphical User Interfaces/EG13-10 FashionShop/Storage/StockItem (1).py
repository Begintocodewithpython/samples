'''
Storage for a single stock item in Fashion Shop
The item has a price, stock level and set of tags
that can be used to locate this item.
'''


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
        # Strip leading and trailing spaces
        tag_string = str.strip(tag_string)

        if tag_string == '':
            return set()

        # Convert the string to lower case
        tag_string = str.lower(tag_string)

        # Make a list of all the words in the string
        # separated by the comma character
        tag_list = str.split(tag_string, sep=',')

        # Remove any spaces at the start or the
        # end of each string in the list
        tag_list = map(str.strip,tag_list)

        # return a set created from the list

        result = set(tag_list)
        return result

    @staticmethod
    def get_text_from_tag_set(tag_set):
        tag_list = list(tag_set) 
        tag_list.sort()
        return ','.join(tag_list)
        
    @property
    def text_tags(self):
        '''
        Converts a set of items into a comma 
        separated text string for display or edit
        '''
        return StockItem.get_text_from_tag_set(self.tags) 

    @text_tags.setter
    def text_tags(self,tag_string):
        '''
        Converts a comma separated list into a set 
        of individual items
        Converts the text to lower case and trims each
        word
        '''
        self.tags = StockItem.get_tag_set_from_text(tag_string)

    def __init__(self, stock_ref, price, tags):
        if StockItem.show_instrumentation:
            print('** StockItem __init__ called')
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.StockItem_version = 1
        self.text_tags = tags

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
                               self.text_tags)

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
        if new_price < StockItem.min_price or new_price > StockItem.max_price:
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


