import tkinter
from tkinter import messagebox
from db_con import con
import main

def get_info_form():
    win = tkinter.Tk()
    win.title("Get Guest Info")
    win.geometry("800x400")
    win.config(bg="lavender")

    tkinter.Label(text="GET GUEST INFO", bg="lavender", font="Century 20 bold underline").place(x=260, y=40)
    tkinter.Label(text="ENTER GUEST ID:", bg="lavender", font="Century 15 bold").place(x=100, y=120)

    id_entry = tkinter.Entry(font="Constantia 12", width=30)
    id_entry.place(x=400, y=125)

    guest_info = tkinter.Label(win, text="", bg="lavender", font="Constantia 12", justify="left")
    guest_info.place(x=100, y=200)

    def search_info():
        guest_id = id_entry.get().strip()
        if not guest_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric Guest ID.")
            return

        try:
            db = con()
            cr = db.cursor()
            cr.execute("SELECT * FROM check_in WHERE id = %s", (guest_id,))
            guest = cr.fetchone()
            db.close()

            if guest:
                guest_info.config(text=(
                    f"ID: {guest[0]}\n"
                    f"Name: {guest[1]}\n"
                    f"Address: {guest[2]}\n"
                    f"Phone: {guest[3]}\n"
                    f"Days: {guest[4]}\n"
                    f"Room: {guest[5]}\n"
                    f"Payment Method: {guest[6]}"
                ))
            else:
                guest_info.config(text="")
                messagebox.showerror("Not Found", "No guest found with this ID.")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def go_back():
        win.destroy()
        main.main_screen()

    tkinter.Button(text="SEARCH", font="Constantia 12 bold", bg="lightgreen", command=search_info).place(x=300, y=170)
    tkinter.Button(text="BACK", font="Constantia 12 bold", bg="tomato", command=go_back).place(x=420, y=170)

    win.mainloop()
