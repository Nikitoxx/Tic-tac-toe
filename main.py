from tkinter import *

window = Tk()




def create_ui(column, row, text):
    Button(text=text, font=('Arial', 15), borderwidth=2,
           bg='white', width=10, 
           height=5).grid(column=column, row=row)
    
    
    
ui = (('x','',''),
      ('','x',''),
      ('','','x'))
    
for i in range(len(ui)):
    for x in range(len(ui[i])):
        create_ui(x, i, ui[i][x])



window.mainloop()
