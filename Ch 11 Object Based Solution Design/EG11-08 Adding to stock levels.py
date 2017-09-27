# EG11-08 Adding to stock levels

from BTCInput import *


class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    show_instrumentation = False
    
    min_price = 0.5
    max_price = 500.0

    max_stock_add = 10

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
        '''
        if count < 0 or count > StockItem.max_stock_add:
            raise Exception('Invalid add amount')

        self.__stock_level = self.__stock_level + count


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

d = Dress(stock_ref='D01', price=100, color='red', pattern='swirly',
          size=12, location='Shop Window')

d.add_stock(5)

print(d)


