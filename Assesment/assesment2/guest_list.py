'''import tkinter
from tkinter import ttk,messagebox
def show():
      
    win=tkinter.Tk()
    win.title("CHECK IN ")
    win.geometry("800x600")
    win.config(bg="lavender")
    

    tkinter.Label(text=" CURRENT GUEST LIST ",bg="lavender",font="Century 20 bold underline").place(x=300,y=40)

    cols = ('ID', 'Name', 'Address', 'Phone', 'Days', 'Room Type', 'Payment Method')
    tree = ttk.Treeview(win, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill=tkinter.BOTH, expand=True)
    
    try:
        from db_con import fetch_all_guests
        rows = fetch_all_guests()
        for row in rows:
            tree.insert("", tkinter.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load guest data:\n{e}")

'''


import tkinter
from tkinter import ttk, messagebox
from db_con import fetch_all_guests
import main

def show():
    win = tkinter.Tk()
    win.title("CURRENT GUEST LIST")
    win.geometry("800x600")
    win.config(bg="lavender")

    tkinter.Label(text=" CURRENT GUEST LIST ", bg="lavender", font="Century 20 bold underline").place(x=250, y=30)

    cols = ('ID', 'Name', 'Address', 'Phone', 'Days', 'Room Type', 'Payment Method')
    tree = ttk.Treeview(win, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.place(x=50, y=100, width=700, height=400)

    try:
        rows = fetch_all_guests()
        for row in rows:
            tree.insert("", tkinter.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data:\n{e}")

    def back():
        win.destroy()     
        main.main_screen()

    tkinter.Button(text="BACK", font="Constantia 14 bold", bg="tomato", command=back).place(x=13-0, y=530, height=50, width=160)

    win.mainloop()
