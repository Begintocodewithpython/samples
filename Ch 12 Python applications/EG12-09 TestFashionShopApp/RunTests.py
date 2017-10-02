
import unittest

from  Storage.StockItem import StockItem

class TestShop(unittest.TestCase):

    def test_StockItem_init(self):
        item = StockItem(stock_ref='Test', price=10, tags='test:tag')
        self.assertEqual(item.stock_ref, 'Test')
        self.assertEqual(item.price, 10)
        self.assertEqual(item.stock_level, 0)
        self.assertEqual(item.tags, 'test:tag')
        
    def test_StockItem_add_stock(self):
        item = StockItem(stock_ref='Test', price=10, tags='test:tag')
        self.assertEqual(item.stock_level, 0)
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)
        with self.assertRaises(Exception):
            item.add_stock(-1)

    def test_StockItem_sell_stock(self):
        item = StockItem(stock_ref='Test', price=10, tags='test:tag')
        self.assertEqual(item.stock_level, 0)
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)
        item.sell_stock(2)
        self.assertEqual(item.stock_level, 8)

        
unittest.main()

