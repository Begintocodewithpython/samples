from tkinter import *

from StockItem import StockItem
from StockItemSelector import StockItemSelector

class MessageReceiver(object):

    def got_selection(self, stock_ref):
        print('Stock item selected :', stock_ref)


stock_list = []
item_number = 1

for i in range(1,100):
    stock_ref = 'D' + str(i)
    item = StockItem(stock_ref, 120,
                 'dress,color:red,loc:shop window,pattern:swirly,size:12,evening,long')
    stock_list.append(item)

receiver = MessageReceiver()

root = Tk()

stock_selector = StockItemSelector(root, receiver)
stock_selector.populate_listbox(stock_list)

stock_selector.frame.grid(row=0, column=0)

root.mainloop()