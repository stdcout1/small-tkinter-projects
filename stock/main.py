from tkinter import *
import http.client
import stockgraph
from stockgraph import getstock



root = Tk()
root.title('Stocks')
root.iconbitmap('stock_ticker.ico')


e = Entry(root,width = 10)
e.grid(row = 0, column = 0)



def clicked():
    lable = Label(root, text = getstock(e.get().upper()))
    lable.grid(row = 0, column = 1)



button = Button(root,text = 'Get Stock Price',padx = 100, pady = 100, command = clicked, font = 100 )
button.grid(row = 2, column = 0, columnspan = 2)
button2 = Button(root,text = 'Show Graph',padx = 112, pady = 10, command = lambda:stockgraph.graph(e.get().upper()), font = 100 )
button2.grid(row = 1, column = 0, columnspan = 2)

root.mainloop()