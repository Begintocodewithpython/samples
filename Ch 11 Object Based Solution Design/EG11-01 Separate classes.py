# EG11-01 Separate classes

class Dress:
    def __init__(self, stock_ref, price, color, pattern, size):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color
        self.pattern = pattern
        self.size = size

    @property
    def price(self):
        return self.__price

    @property
    def stock_level(self):
        return self.__stock_level
        
class Trousers:
    def __init__(self, stock_ref, price, color, pattern, length, waist):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color
        self.pattern = pattern
        self.length = length
        self.waist = waist

    @property
    def price(self):
        return self.__price

    @property
    def stock_level(self):
        return self.__stock_level
        
x = Dress(stock_ref='D01', price=100, color='red', pattern='swirly', size=12)
y = Trousers(stock_ref='T01', price=50, color='black', pattern='plain', length=30, waist=25)
print(x.price)
print(y.stock_level)
