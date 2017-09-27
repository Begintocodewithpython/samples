from tkinter import *

from  Storage.StockItem import StockItem

class StockItemEditor(object):
    '''
    Provides an editor for a StockItem
    The frame property gives the Tkinter frame
    that is used to display the editor
    '''

    def __init__(self,root):
        '''
        Create an instance of the editor. root provides
        the Tkinter root frame for the editor
        '''
        self.frame = Frame(root,borderwidth=5)

        stock_ref_label = Label(self.frame,text='Stock ref:')
        stock_ref_label.grid(sticky=E, row=0, column=0, padx=5, pady=5)
        self._stock_ref_entry = Entry(self.frame, width=30)
        self._stock_ref_entry.grid(sticky=W, row=0, column=1, padx=5, pady=5)

        price_label = Label(self.frame,text='Price:')
        price_label.grid(sticky=E, row=1, column=0, padx=5, pady=5)
        self._price_entry = Entry(self.frame, width=30)
        self._price_entry.grid(sticky=W, row=1, column=1, padx=5, pady=5)

        self._stock_level_label = Label(self.frame,text='Stock level: 0')
        self._stock_level_label.grid( row=2, column=0, columnspan=2, padx=5, pady=5)

        tags_label = Label(self.frame,text='Tags:')
        tags_label.grid(sticky=E+N, row=3, column=0, padx=5, pady=5)

        self._tags_text = Text(self.frame, width=70, height=5)
        self._tags_text.grid(row=3, column=1, padx=5, pady=5)

    def load_into_editor(self, item):
        '''
        Loads a StockItem into the editor display
        item is a reference to the StockItem
        being loaded into the display
        '''
        self.clear_editor()
        self._stock_ref_entry.insert(0, item.stock_ref)
        self._price_entry.insert(0, str(item.price))
        self._stock_level_label.config(text = 'Stock level : ' + str(item.stock_level))
        self._tags_text.insert('0.0',item.text_tags)

    def get_from_editor(self,item):
        '''
        Gets updated values from the screen 
        item is a reference to the StockItem
        that will get the updated values
        Will raise an exception if the price entry
        cannot be converted into a number
        '''
        item.set_price(int(self._price_entry.get()))
        item.stock_ref = self._stock_ref_entry.get()
        item.text_tags = self._tags_text.get('1.0',END)

    def item_edited(self, item):
        '''
        Checks if there are any difference between the 
        item supplied as a parameter and the
        item displayed on the screen
        Returns True if the item has been changed
        '''
        if item.stock_ref != self._stock_ref_entry.get():
            return True
        if item.price != float(self._price_entry.get()):
            return True
        if item.text_tags.strip() != self._tags_text.get('1.0',END).strip():
            return True
        return False

    def clear_editor(self):
        '''
        Clears the editor window
        '''
        self._stock_ref_entry.delete(0, END) 
        self._price_entry.delete(0, END)
        self._tags_text.delete('0.0', END)
        self._stock_level_label.config(text = 'Empty')

