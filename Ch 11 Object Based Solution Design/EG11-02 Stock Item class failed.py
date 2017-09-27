# EG11-02 Stock Item class failed


class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    def __init__(self, stock_ref,  price, color):
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
        self.item_name = 'Dress'
        self.pattern = pattern
        self.size = size


x = Dress(stork_ref='D01', price=100, color='red', pattern='swirly', size=12)
print(x.pattern)
print(x.price)
