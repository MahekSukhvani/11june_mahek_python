import tkinter
from tkinter import messagebox
from db_con import insert_guest 
import main

def form():
    win = tkinter.Tk()
    win.title("CHECK IN ")
    win.geometry("800x600")
    win.config(bg="lavender")
    

    tkinter.Label(text=" CHECK IN ", bg="lavender", font="Century 20 bold underline").place(x=300, y=40)


    tkinter.Label(text="ENTER YOUR NAME", bg="lavender", font="Century 15 bold").place(x=110, y=110)
    tkinter.Label(text="ENTER YOUR ADDRESS", bg="lavender", font="Century 15 bold").place(x=110, y=150)
    tkinter.Label(text="ENTER YOUR NUMBER", bg="lavender", font="Century 15 bold").place(x=110, y=190)
    tkinter.Label(text="NUMBER OF DAYS", bg="lavender", font="Century 14 bold").place(x=110, y=230)
    tkinter.Label(text="CHOOSE YOUR ROOM", bg="lavender", font="Century 14 bold").place(x=110, y=270)
    tkinter.Label(text="PAYMENT METHOD", bg="lavender", font="Century 14 bold").place(x=110, y=340)

    fnm = tkinter.Entry(font="Constantia 10 bold", width=30)
    fnm.place(x=400, y=115, height=20)
    lnm = tkinter.Entry(font="Constantia 10 bold", width=30)
    lnm.place(x=400, y=155, height=20)
    num = tkinter.Entry(font="Constantia 10 bold", width=30)
    num.place(x=400, y=195, height=20)
    dy = tkinter.Entry(font="Constantia 10 bold", width=30)
    dy.place(x=400, y=235, height=20)

    var = tkinter.StringVar(value="DELUXE")
    tkinter.Radiobutton(value="DELUXE", text="DELUXE", font="Constantia 12 bold", variable=var, bg="lavender").place(x=395, y=270)
    tkinter.Radiobutton(value="GENERAL", text="GENERAL", font="Constantia 12 bold", variable=var, bg="lavender").place(x=555, y=270)
    tkinter.Radiobutton(value="FULL DELUXE", text="FULL DELUXE", font="Constantia 12 bold", variable=var, bg="lavender").place(x=395, y=300)
    tkinter.Radiobutton(value="JOINT", text="JOINT", font="Constantia 12 bold", variable=var, bg="lavender").place(x=555, y=300)

    var1 = tkinter.StringVar(value="cash")
    tkinter.Radiobutton(value="cash", text="BY CASH", font="Constantia 12 bold", variable=var1, bg="lavender").place(x=395, y=340)
    tkinter.Radiobutton(value="card", text="BY CREDIT/DEBIT CARD", font="Constantia 12 bold", variable=var1, bg="lavender").place(x=555, y=340)

    def back():
        win.destroy()     
        main.main_screen()

    def submit():
        name = fnm.get()
        address = lnm.get()
        phone = num.get()
        days = dy.get()
        room = var.get()
        payment = var1.get()

        if not all([name, address, phone, days]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if insert_guest(name, address, phone, days, room, payment):
            messagebox.showinfo("Success", "Guest Checked In Successfully!")
            fnm.delete(0, 'end')
            lnm.delete(0, 'end')
            num.delete(0, 'end')
            dy.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Failed to insert guest data.")
        
    

    tkinter.Button(text="SUBMIT", font="Constantia 14 bold", bg="lightGreen", command=submit).place(x=380, y=430, height=50, width=160)
    tkinter.Button(text="BACK", font="Constantia 14 bold", bg="tomato", command=back).place(x=190, y=430, height=50, width=160)

    win.mainloop()
