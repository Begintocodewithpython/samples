import unittest

class TestShop(unittest.TestCase):

    def test_StockItem_init(self):
        item = StockItem(stock_ref='Test', price=10, tags='test:tag')
        self.assertEqual(item.stock_ref, 'Test')
        self.assertEqual(item.price, 10)
        self.assertEqual(item.stock_level, 0)

    def failing_test(self):
        self.assertEqual(1, 0)


        
    def ztest_StockItem_add_stock(self):
        item = StockItem(stock_ref='Test', price=10, tags='test:tag')
        self.assertEqual(item.stock_level, 0)
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)

    def ztest_StockItem_sell_stock(self):
        item = StockItem(stock_ref='Test', price=10, tags='test:tag')
        self.assertEqual(item.stock_level, 0)
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)
        item.sell_stock(2)
        self.assertEqual(item.stock_level, 8)



print('bazinga')        
unittest.main()

