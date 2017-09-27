''' 
Display a graphical user interface that lets users convert from temperature scales
'''

from tkinter import *
from tkinter import messagebox

class Converter(object):
    '''
    Displays a Tkinter user interface to convert between Fahrenheit and Centigrade
    Call the display function to display the converter on the screen
    '''

    def display(self):
        '''
        Displays the converter window
        When the window is closed this method completes
        '''

        root = Tk()

        cent_label = Label(root, text='Centigrade:')
        cent_label.grid(row=0, column=0, padx=5, pady=5, stick=E)

        cent_entry = Entry(root, width=5)
        cent_entry.grid(row=0, column=1, padx=5, pady=5)

        fah_label = Label(root, text='Fahrenheit:')
        fah_label.grid(row=2, column=0, padx=5, pady=5, stick=E)

        fah_entry = Entry(root, width=5)
        fah_entry.grid(row=2, column=1, padx=5, pady=5)

        def fah_to_cent():
            '''
            Convert from fahrenheit to centigrade and display the result
            '''
            fah_string = fah_entry.get()
            fah_float = float(fah_string)
            result = (fah_float - 32) / 1.89
            cent_entry.delete(0) # remove the old text
            cent_entry.insert(0, str(result)) # insert the new text

        def cent_to_fah():
            '''
            Convert from centigrade to fahrenheit and display the result
            '''
            cent_string = cent_entry.get()
            cent_float = float(cent_string)
            result = cent_float * 1.8 + 32


            fah_entry.delete(0) # remove the old text
            fah_entry.insert(0, str(result))

        fah_to_cent_button = Button(root, text="Fah to cent", command=fah_to_cent)
        fah_to_cent_button.grid(row=1, column=0, padx=5, pady=5)

        cent_to_fah_button = Button(root, text="Cent to fah", command=cent_to_fah)
        cent_to_fah_button.grid(row=1, column=1, padx=5, pady=5)
        
        root.mainloop()



if __name__ == '__main__':
    app = Converter()
    app.display()
