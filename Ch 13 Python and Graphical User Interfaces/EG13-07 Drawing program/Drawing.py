'''
Provides a simple drawing app
Hold down the left button to draw
Provides some single key commands:
R-red G-green B-blue
C-clear
'''

from tkinter import *

class Drawing(object):

    def display(self):
        root = Tk()

        canvas = Canvas(root, width=500, height=500)
        canvas.grid(row=0, column=0)

        draw_color = 'red'

        def mouse_move(event):
            '''
            Draws a 10 pixel rectangle centered about the mouse
            position
            '''
            canvas.create_rectangle(event.x-5, event.y-5,
            event.x+5, event.y+5, fill=draw_color, outline=draw_color)

        canvas.bind('<B1-Motion>', mouse_move)

        def key_press(event):
            nonlocal draw_color
            ch = event.char.upper()
            if ch == 'C':
                canvas.delete("all")
            elif ch == 'R':
                draw_color = 'red'
            elif ch == 'G':
                draw_color = 'green'
            elif ch == 'B':
                draw_color = 'blue'
            

        canvas.bind('<KeyPress>', key_press)
        canvas.focus_set()

        root.mainloop()





if __name__ == '__main__':
    app = Drawing()
    app.display()     