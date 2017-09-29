# EG11-04 Stock Items with str

from BTCInput import *

class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    min_price = 0.5
    max_price = 500.0
    
    def __init__(self, stock_ref, price, color):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color

    @property
    def item_name(self):
        return 'Stock Item'

    def __str__(self): 
        template = '''Stock Reference: {0}
Type: {1}
Price: {2}
Stock level: {3}
Color: {4}''' 
        return template.format(self.stock_ref, self.item_name,
                              self.price, self.stock_level, self.color) 

    @property
    def price(self):
        return self.__price

    @property
    def stock_level(self):
        return self.__stock_level

class Dress(StockItem):

    def __init__(self, stock_ref, price, color, pattern, size):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.name = 'Dress'
        self.pattern = pattern
        self.size = size

    @property
    def item_name(self):
        return 'Dress'

    def __str__(self):
        stock_details = super().__str__()
        template = '''{0}
Pattern: {1}
Size: {2}'''
        return template.format(stock_details, self.pattern,
                               self.size)

class Pants(StockItem):

    def __init__(self, stock_ref, price, color, pattern, length, waist):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.pattern = pattern
        self.length = length
        self.waist = waist

    @property
    def item_name(self):
        return 'Trousers'

    def __str__(self):
        stock_details = super().__str__()
        template = '''{0}
Pattern: {1}
Length: {2}
Waist: {3}'''
        return template.format(stock_details, self.pattern,
                               self.length, self.waist)
class Hat(StockItem):

    def __init__(self, stock_ref, price, color, size):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.size = size

    @property
    def item_name(self):
        return 'Hat'


    def __str__(self):
        stock_details = super().__str__()
        template = '''{0}
Size: {1}'''
        return template.format(stock_details, self.size)

class Blouse(StockItem):
    
    def __init__(self, stock_ref, price, color, size, style, pattern):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.size = size
        self.style = style
        self.pattern = pattern

    @property
    def item_name(self):
        return 'Blouse'

    def __str__(self):
        stock_details = super().__str__()
        template = '''{0}
Size: {1}
Style: {2}
Pattern: {3}'''
        return template.format(stock_details, self.size,
                               self.style, self.pattern)
x = Dress(stock_ref='D001', price=100, color='red', pattern='swirly', size=12)
print(x)
