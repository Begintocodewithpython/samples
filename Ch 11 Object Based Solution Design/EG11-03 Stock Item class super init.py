# EG11-03 Stock Item class super init


class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    def __init__(self, stock_ref, price, color):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color

    @property
    def price(self):
        return self.__price

    @property
    def stock_level(self):
        return self.__stock_level


class Dress(StockItem):

    def __init__(self, stock_ref, price, color, pattern, size):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.pattern = pattern
        self.size = size

x = Dress(stock_ref='D001', price=100, color='red', pattern='swirly', size=12)
print(x.pattern)
print(x.price)
