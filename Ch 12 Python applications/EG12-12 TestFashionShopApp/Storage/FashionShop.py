
import pickle

from  Storage.StockItem import StockItem

class FashionShop:

    show_instrumentation = False

    min_price = 0.5
    max_price = 500.0

    max_stock_add = 50

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

        return filter(lambda item:search_tags.issubset(item.tags), self.__stock_dictionary.values())
#        return filter(match_tags, self.__stock_dictionary.values())
