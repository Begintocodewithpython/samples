from tkinter import *

from  StockItem import StockItem

class StockItemSelector(object):

    '''
    Provides a frame that can be used to select
    a given stock item reference from a list
    of stock items
    The stock item list is delivered to the 
    class via the populate_listbox method
    Selection events will trigger a call
    of got_selection in the object provided
    as the receiver of selection messages
    '''

    def __init__(self, root, receiver):
        '''
        Create an instance of the editor. root provides
        the Tkinter root frame for the editor
        receiver is a reference to the object that
        will receive messages when an item is selected
        The event will take the form of a call 
        to the got_selection method in the
        receiver
        '''

        assert hasattr(receiver, 'got_selection')

        self.receiver = receiver

        self.frame = Frame(root,borderwidth=5)

        self.listbox = Listbox(self.frame)
        self.listbox.grid(row=0, column=0)

        def on_select(event):
            '''
            Bound to the selection event in the Listbox
            Finds the selected text and calls
            the message receiver to deliver the name
            that has been selected
            '''
            lb = event.widget
            index = int(lb.curselection()[0])
            receiver.got_selection(lb.get(index))

        self.listbox.bind('<<ListboxSelect>>', on_select)
        
    def populate_listbox(self, items):
        '''
        Clears the selection Listbox and then 
        populates it with the stock_ref values 
        in the collection of items that have
        been supplied
        '''
        self.listbox.delete(0, END)
        for item in items:
            self.listbox.insert(END,item.stock_ref)


    