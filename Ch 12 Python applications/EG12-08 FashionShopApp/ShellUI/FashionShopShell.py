from ShellUI.BTCInput import *

from  Storage.StockItem import StockItem

class FashionShopShell:

    def __init__(self, filename, storage_class):
        '''
        Manages the fashion shop data
        Displays a message if the load fails and creates a new shop
        '''
        FashionShopShell.__filename = filename
        try:
            self.__shop = storage_class.load(filename)
        except:
            print('Fashion shop not loaded.')
            print('Creating an empty fashion shop')
            self.__shop = storage_class()

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
            command = read_int_ranged(prompt, 1, 7)
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
                self.__shop.save(FashionShopShell.__filename)
                print('Shop data saved')
                break
