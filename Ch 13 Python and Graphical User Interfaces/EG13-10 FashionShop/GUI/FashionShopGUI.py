from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Storage.StockItem import StockItem
from GUI.StockItemEditor import StockItemEditor
from GUI.StockItemSelector import StockItemSelector

class FashionShopGUI:
    '''
    Provides a Command Shell interface for use by
    the Fashion Shop application
    '''

    def __init__(self, filename, storage_class):
        '''
        Manages the fashion shop gui
        Records the filename and storage class for later use
        '''
        FashionShopGUI.__filename = filename
        FashionShopGUI.__storage_class = storage_class

    def _move_off_item(self):
        '''
        Called when the editor moves off an item.
        If the __active_item attribute is not None, we
        save the current edit window into the active item.
        If the __active_item attribute is None, and we have a
        stock item in the editor, we try to save it
        '''
        if self.__active_item != None:
            # moving off an active item
            # Might have changed the stock reference
            self.__stock_item_editor.get_from_editor(self.__active_item)
        else:
            # creating a new item 
            try:
                # make an empty stock item
                new_item = StockItem('empty',10,'empty')
                try :
                    self.__stock_item_editor.get_from_editor(new_item)
                except:
                    return
                self.__shop.store_new_stock_item(new_item)
                self.__stock_item_selector.populate_listbox(self.__shop.find_matching_with_tags(self.__search_set))
            except:
                messagebox.showwarning('Save entry', 'Entry not saved')


    def _create_new_stock_item(self):
        self._move_off_item()
        self.__stock_item_editor.clear_editor()
        self.__active_item = None
        

    def _add_stock(self):
        if self.__active_item == None:
            messagebox.showinfo('Add stock', 'No item selected')
            return
        try:
            amount_string = self.addStockAmountEntry.get()
            amount =int(amount_string)
            self.__active_item.add_stock(amount)
            self.__stock_item_editor.load_into_editor(self.__active_item)
        except:
            messagebox.showerror('Add stock', 'Add stock failed')
        pass

    def _sell_stock(self):
        if self.__active_item == None:
            messagebox.showinfo('Sell stock', 'No item selected')
            return
        try:
            amount_string = self.sellStockAmountEntry.get()
            print(self.__active_item)
            amount =int(amount_string)
            self.__active_item.sell_stock(amount)
            self.__stock_item_editor.load_into_editor(self.__active_item)
        except:
            messagebox.showerror('Sell stock', 'Sell stock failed')

    def got_selection(self,stock_ref):
        '''
        Called when an item is selected by the stock item 
        selector
        '''

        self._move_off_item()

        self.__active_item = self.__shop.find_stock_item(stock_ref)
        self.__active_item_stock_ref = stock_ref
        
        self.__stock_item_editor.load_into_editor(self.__active_item)

    def do_tag_search(self):
        search_string = self.__tagSearchEnty.get()
        self.__search_set = StockItem.get_tag_set_from_text(search_string)
        self.__stock_item_selector.populate_listbox(self.__shop.find_matching_with_tags(self.__search_set))
        
    def main_menu(self):
        '''
        Manages the fashion shop data
        Displays a message if the load fails and creates a new shop
        '''

        root=Tk()

        try:
            self.__shop = FashionShopGUI.__storage_class.load(FashionShopGUI.__filename)
        except:
            messagebox.showwarning('Fashion Shop Load', 
            'Fashion shop not loaded. Creating an empty fashion shop')
            self.__shop = FashionShopGUI.__storage_class()
            self.__shop.make_test_dresses()

        self.__active_item = None

        self.__search_set = set()

        titleLabel = Label(root,text="Mary's Fahion Shop")
        titleLabel.grid(row=0, column=0, columnspan=2)

        tagSearchButton = Button(root, text='Tag Search', command=self.do_tag_search)
        tagSearchButton.grid(sticky=E, row=1, column=0)
        self.__tagSearchEnty = Entry(root,width=60)
        self.__tagSearchEnty.grid(sticky=W,row=1,column=1)


        self.__stock_item_selector = StockItemSelector(root,self)
        self.__stock_item_selector.frame.grid(row=2, column=0, rowspan=2)
        self.__stock_item_selector.populate_listbox(self.__shop.find_matching_with_tags(self.__search_set))

        self.__stock_item_editor = StockItemEditor(root)
        self.__stock_item_editor.frame.grid(row=2,column=1)

        button_frame = Frame(root, height=500,width=100)

        newStockItemButton=Button(button_frame,text='Create New Stock Item',command=self._create_new_stock_item)
        newStockItemButton.grid(sticky=E+W, padx=5, pady=5, row=0, column=0)
        addStockItemButton=Button(button_frame,text='Add Stock',command=self._add_stock)
        addStockItemButton.grid(sticky=E+W,padx=5, pady=5, row=1, column=0)
        self.addStockAmountEntry = Entry(button_frame)
        self.addStockAmountEntry.grid(row=1,column=1)
        sellStockButton=Button(button_frame,text='Sell Stock',command=self._sell_stock)
        sellStockButton.grid(sticky=E+W, padx=5, pady=5, row=2, column=0)
        self.sellStockAmountEntry = Entry(button_frame)
        self.sellStockAmountEntry.grid(row=2,column=1)
        button_frame.grid(sticky=E,row=3, column=0, columnspan=2)

        root.mainloop()

        #self._move_off_item()

        self.__shop.save(FashionShopGUI.__filename)

        return

