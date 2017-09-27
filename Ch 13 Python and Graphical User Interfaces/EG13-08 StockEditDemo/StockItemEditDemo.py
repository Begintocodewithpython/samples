# EG13-08 StockItemEditDemo

from tkinter import *
from StockItem import StockItem
from StockItemEditor import StockItemEditor

item = StockItem('D001', 120,
                 'dress,color:red,loc:shop window,pattern:swirly,size:12,evening,long')

root = Tk()

stock_frame = StockItemEditor(root)
stock_frame.frame.grid(row=0, column=0)

def save_edit():

    if not stock_frame.item_edited(item):
        print('not changed - no need to save')
        return

    stock_frame.get_from_editor(item)
    stock_frame.clear_editor()
    print(item)

save_button = Button(root,text='Save', command=save_edit)
save_button.grid(row=1, column=0)
stock_frame.load_into_editor(item)
root.mainloop()
