# EG11-07 Creating Stock Items

from BTCInput import *

class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    show_instrumentation = False

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


class Trousers(StockItem):

    def __init__(self, stock_ref, price, color, pattern, length, waist, location):
        if StockItem.show_instrumentation:
            print('** Trousers __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, location=location)
        self.pattern = pattern
        self.length = length
        self.waist = waist
        self.Trousers_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Trousers get item_name called')
        return 'Trousers'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Trousers check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Trousers __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Pattern: {1}
Length: {2}
Waist: {3}'''
        return template.format(stock_details, self.pattern,
                               self.length, self.waist)

class Jeans(Trousers):

    def __init__(self, stock_ref, price, color, pattern, length, waist, style, location):
        if StockItem.show_instrumentation:
            print('** Jeans __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, pattern=pattern, length=length,
                         waist=waist, location=location)
        self.style = style
        self.Jeans_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Jeans get item_name called')
        return 'Jeans'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Jeans check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Jeans __str__ called')
        trousers_details = super().__str__()
        template = '''{0}
Style: {1}'''
        return template.format(trousers_details, self.style)

class Hat(StockItem):

    def __init__(self, stock_ref, price, color, size, location):
        if StockItem.show_instrumentation:
            print('** Hat __init__ called')
        super().__init__(stock_ref=stock_ref, price=price,
                         color=color, location=location)
        self.size = size
        self.Hat_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Hat get item_name called')
        return 'Hat'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Hat check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Hat __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Size: {1}'''
        return template.format(stock_details, self.size)

class Blouse(StockItem):
    
    def __init__(self, stock_ref, price, color, size, style, pattern, location):
        if StockItem.show_instrumentation:
            print('** Blouse __init__ called')
        super().__init__(stock_ref, price, color, location)
        self.size = size
        self.style = style
        self.pattern = pattern
        self.Hat_version = 1

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print('** Blouse get item_name called')
        return 'Blouse'

    def check_version(self):
        if StockItem.show_instrumentation:
            print('** Blouse check_version called')
        # This is version 1 - no need to update anything
        super().check_version()
        pass

    def __str__(self):
        if StockItem.show_instrumentation:
            print('** Blouse __str__ called')
        stock_details = super().__str__()
        template = '''{0}
Size: {1}
Style: {2}
Pattern: {3}'''
        return template.format(stock_details, self.size,
                               self.style, self.pattern)
    

menu = '''
Create new stock item 

1: Dress
2: Trousers
3: Hat
4: Blouse
5: Jeans

What kind of item do you want to add: '''

item = read_int_ranged(prompt=menu,min_value=1,max_value=5)

if item == 1:
    print('Creating a Dress')
    stock_ref = read_text('Enter stock reference: ')
    price = read_float_ranged(prompt='Enter price: ',
                              min_value=StockItem.min_price,
                              max_value=StockItem.max_price)
    color = read_text('Enter color: ')
    location = read_text('Enter location: ')
    pattern = read_text('Enter pattern: ')
    size = read_text('Enter size: ')
    stock_item =  Dress(stock_ref=stock_ref,
                        price=price,
                        color=color,
                        location=location,
                        pattern=pattern,    
                        size=size)
elif item == 2:
    print('Creating a pair of Trousers')
    stock_ref = read_text('Enter stock reference: ')
    price = read_float_ranged(prompt='Enter price: ',
                              min_value=StockItem.min_price,
                              max_value=StockItem.max_price)
    color = read_text('Enter color: ')
    location = read_text('Enter location: ')
    pattern = read_text('Enter pattern: ')
    length = read_text('Enter length: ')
    waist = read_text('Enter waist: ')
    stock_item = Trousers(stock_ref=stock_ref,
                          price=price,
                          color=color,
                          location=location,
                          pattern=pattern,
                          length=length,
                          waist=waist)
elif item == 3:
    print('Creating a Hat')
    stock_ref = read_text('Enter stock reference: ')
    price = read_float_ranged(prompt='Enter price: ',
                              min_value=StockItem.min_price,
                              max_value=StockItem.max_price)
    color = read_text('Enter color: ')
    location = read_text('Enter location: ')
    size = read_text('Enter size: ')
    stock_item = Hat(stock_ref=stock_ref,
                     price=price,
                     color=color,
                     location=location,
                     size=size)
elif item == 4:
    print('Creating a Blouse')
    stock_ref = read_text('Enter stock reference: ')
    price = read_float_ranged(prompt='Enter price: ',
                              min_value=StockItem.min_price,
                              max_value=StockItem.max_price)
    color = read_text('Enter color: ')
    location = read_text('Enter location: ')
    size = read_text('Enter size: ')
    style = read_text('Enter style: ')
    pattern = read_text('Enter pattern: ')
    stock_item = Blouse(stock_ref=stock_ref,
                        price=price,
                        color=color,
                        location=location,
                        pattern=pattern,
                        size=size,
                        style=style)
elif item == 5:
    print('Creating some jeans')
    stock_ref = read_text('Enter stock reference: ')
    price = read_float_ranged(prompt='Enter price: ',
                              min_value=StockItem.min_price,
                              max_value=StockItem.max_price)
    color = read_text('Enter color: ')
    location = read_text('Enter location: ')
    pattern = read_text('Enter pattern: ')
    length = read_text('Enter length: ')
    waist = read_text('Enter waist: ')
    style = read_text('Enter style: ')
    stock_item = Jeans(stock_ref=stock_ref,
                       price=price,
                       color=color,
                       location=location,
                       pattern=pattern,
                       length=length,
                       waist=waist,
                       style=style)

print(stock_item)


