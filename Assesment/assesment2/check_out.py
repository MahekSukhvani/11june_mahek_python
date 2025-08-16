import tkinter
from tkinter import messagebox
from db_con import  delete_guest,search_guest_id
import main

def checkout_form():
    win = tkinter.Tk()
    win.title("Guest Check-Out")
    win.geometry("800x400")
    win.config(bg="lavender")

    tkinter.Label(text="GUEST CHECK OUT", bg="lavender", font="Century 20 bold underline").place(x=250, y=40)
    tkinter.Label(text="ENTER GUEST ID:", bg="lavender", font="Century 15 bold").place(x=100, y=120)

    id_entry = tkinter.Entry(font="Constantia 12", width=30)
    id_entry.place(x=400, y=125)

    guest_info = tkinter.Label(win, text="", bg="lavender", font="Constantia 12", justify="left")
    guest_info.place(x=100, y=200)

    def search_guest():
        guest_id = id_entry.get().strip()
        if not guest_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric Guest ID.")
            return

        guest = search_guest_id(guest_id)

        if guest:
            guest_info.config(text=f"ID: {guest[0]}\nName: {guest[1]}\nRoom: {guest[5]}\nPayment: {guest[6]}")
            confirm = messagebox.askyesno("Confirm", f"Check out guest '{guest[1]}'?")
            if confirm:
                success = delete_guest(guest[0])
                if success:
                    messagebox.showinfo("Success", "Guest checked out successfully.")
                    guest_info.config(text="")
                    id_entry.delete(0, 'end')
                else:
                    messagebox.showerror("Error", "Failed to check out guest.")
        else:
            messagebox.showerror("Not Found", "No guest found with this ID.")

    def go_back():
        win.destroy()
        main.main_screen()

    tkinter.Button(text="SEARCH", font="Constantia 12 bold", bg="lightgreen", command=search_guest).place(x=300, y=170)
    tkinter.Button(text="BACK", font="Constantia 12 bold", bg="tomato", command=go_back).place(x=420, y=170)

    win.mainloop()
