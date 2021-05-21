import tkinter as tk
from Grammar import *
from Variable import *
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.geometry("800x800")

#Initialize a matrix to keep track of all the widgets (buttons, entry fields, etc.)
widgets = [ [ 0 for i in range(50) ] for j in range(50) ]

#Will trigger every time the user clicks the "+" button
def clickAddSymbol(x, y):

    if x > 48 or y > 48:
        return

    #Destroy the button and replace it with an input field
    widgets[x][y].destroy()
    widgets[x][y] = tk.Entry(root, width=5)
    widgets[x][y].grid(row=x,column=y)

    #Create a new button to the right (index: x, y+1)
    widgets[x][y+1] = tk.Button(root, text="+", command=lambda i=x,j=y+1: clickAddSymbol(i,j))
    widgets[x][y+1].grid(row=x, column=y+1)

#Will trigger every time the user clicks the "Add row" button
def clickAddRow(index):
    widgets[index][0].destroy()
    widgets[index+1][0].destroy()
    addRow(index)

def clickVerify():

    msg = "Error"

    input = simpledialog.askstring("Input", "Please enter the string", parent=root)

    try:
        vars = createVariables()
        grammar = Grammar(vars)
        msg = grammar.stringVerifier("cacab")
        print(grammar.stringVerifier("a"))
        result = grammar.stringVerifier(input)

        if (result == True):
            msg = "The string is generated by the grammar!"
        else:
            msg = "The string is NOT generated by the grammar!"

    except IndexError:
        msg = "Please enter a valid string"

    except Exception as e:
        msg = e
        
    messagebox.showinfo("Message", msg)

def createVariables():

    vars = []

    for i in range(0, len(widgets)):

        print("-------------------")

        row = widgets[i]

        if isinstance(row[0], tk.Entry):
            vars.append([row[0].get(), []])
        else:
            break

        for x in range(2, len(row)):
            
            if isinstance(row[x], tk.Entry):
                vars[i][1].append(row[x].get())
    
    ret = []

    for x in range(0, len(vars)):
        ret.append(Variable(vars[x][0], vars[x][1]))

    return ret


#Adds a row in the window
def addRow(index):

    widgets[index][0] = tk.Entry(root, width=5)
    widgets[index][0].grid(row=index, column=0)

    widgets[index][1] = tk.Label(root, text="->")
    widgets[index][1].grid(row=index, column=1)

    widgets[index][2] = tk.Entry(root, width=5)
    widgets[index][2].grid(row=index, column=2)

    widgets[index][3] = tk.Button(root, text="+", command=lambda i=index,j=3: clickAddSymbol(i,j))
    widgets[index][3].grid(row=index, column=3)

    #Add a button to add a new row below the current row
    widgets[index+1][0] = tk.Button(root, text="Add Row", command= lambda i=index+1 : clickAddRow(i))
    widgets[index+1][0].grid(row=index+1, column=0)
    
    widgets[index+2][0] = tk.Button(root, text="Verify", padx=10, command=clickVerify)
    widgets[index+2][0].grid(row=index+2, column=0)

addRow(0)

if __name__ == "__main__":
    root.mainloop()