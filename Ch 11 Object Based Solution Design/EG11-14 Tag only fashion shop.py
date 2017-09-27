# EG11-14 Tag only fashion shop

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

    def find_matching_with_tags(self, search_tags):
        '''
        Returns the stock items that contain
        the search_tags as a subset of their tags
        '''
        if FashionShop.show_instrumentation:
            print('** FashionShop find_matching_tags called', search_tags)

        def match_tags(item):
            '''
            Returns True if the tags in the item
            contain the search tags
            '''
            return search_tags.issubset(item.tags)

        return filter(match_tags, self.__stock_dictionary.values())



class FashionShopShellApplication:

    def __init__(self, filename):
        '''
        Manages the fashion shop data
        Displays a message if the load fails and creates a new shop
        '''
        FashionShopShellApplication.__filename = filename
        try:
            self.__shop = FashionShop.load(filename)
        except:
            print('Fashion shop not loaded.')
            print('Creating an empty fashion shop')
            self.__shop = FashionShop()

    def create_new_stock_item(self):
        '''
        Creates a new stock item. Gets the details of the item, 
        creates it and then stores it in the shop
        '''

        stock_ref = read_text('Enter stock reference: ')
        price = read_float_ranged(prompt='Enter price: ',
                                    min_value=StockItem.min_price,
                                    max_value=StockItem.max_price)
        tag_string = read_text('Enter tags (separated by commas): ')

        tags = StockItem.get_tag_set_from_text(tag_string)

        new_item = StockItem(stock_ref=stock_ref, price=price, tags=tags)

        try:
            self.__shop.store_new_stock_item(new_item)
            print('Item stored')
        except Exception as e:
            print('Item not stored ')
            print(e)

    def add_stock(self):
        '''
        Adds stock to an existing stock item
        Searches for the item first, and then gets the 
        number of stock items to add
        '''
        print('Add stock')

        item_stock_ref = read_text('Enter the stock reference: ')

        item = self.__shop.find_stock_item(item_stock_ref)
        
        if item == None:
            print('This stock item was not found')
            return

        print(item)

        number_to_add = read_int_ranged('Number to add (0 to abandon): ',
                                        0, StockItem.max_stock_add)

        if number_to_add == 0:
            print('No items added')
        else:
            item.add_stock(number_to_add)
            print(item)

    def sell_stock(self):
        '''
        Sells stock. Searches for the item and then reads the
        number of items that are being sold.
        Will not allow more items to be sold than are in stock
        '''
        print('Sell item')

        item_stock_ref = read_text('Enter the stock reference: ')

        item = self.__shop.find_stock_item(item_stock_ref)

        if item == None:
            print('This item was not found')
            return

        print('Selling')
        print(item)

        if item.stock_level == 0:
            print('There are none in stock')
            return

        number_sold = read_int_ranged('How many sold (0 to abandon): ',
                                      0,
                                      item.stock_level)

        if number_sold == 0:
            print('Sell item abandoned')
            return

        item.sell_stock(number_sold)

        print('Items sold')

    def do_report(self):
        print('Stock report')
        print(self.__shop)

    def do_tag_filter(self):
        print('Filter on tags')
        tag_string = read_text('Enter the tags to look for (separated by commas): ')
        search_tags = StockItem.get_tag_set_from_text(tag_string)
        items = self.__shop.find_matching_with_tags(search_tags)
        stock = map(str,items)
        stock_list = '\n'.join(stock)
        template = '''Matching items

{0}
'''
        print(stock_list)

    def main_menu(self):

        prompt = '''Mary's Fashion Shop

1: Create new stock item
2: Add stock to existing item
3: Sell stock
4: Stock report
5: Find on tags
6: Exit

Enter your command: '''

        while(True):
            command = read_int_ranged(prompt, 1, 6)
            if command == 1:
                self.create_new_stock_item()
            elif command == 2:
                self.add_stock()
            elif command == 3:
                self.sell_stock()
            elif command == 4:
                self.do_report()
            elif command == 5:
                self.do_tag_filter()
            elif command == 6:
                self.__shop.save(FashionShopShellApplication.__filename)
                print('Shop data saved')
                break

ui = FashionShopShellApplication('simplefashionshop.pickle')
ui.main_menu()

