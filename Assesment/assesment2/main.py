import tkinter
import check_in
import guest_list
import check_out
import get_info

def main_screen():
    win=tkinter.Tk()
    win.title("Hotel Management")
    win.geometry("800x600")
    win.config(bg="lavender")

    tkinter.Label(text=" WELCOME TO OUR HOTEL ",bg="lavender",font="Century 20 bold underline").place(x=180,y=40)

    def ckn():
        win.destroy()
        check_in.form()

    def list():
        win.destroy()
        guest_list.show()

    def ckout():
        win.destroy()
        check_out.checkout_form()

    def info():
        win.destroy()
        get_info.get_info_form()
    
        

    btn1=tkinter.Button(win,text="CHECK IN",font="Century 14 bold",padx=100,command=ckn)
    btn1.place(x=225,y=120)

    btn2=tkinter.Button(text="SHOW GUEST LIST",font="Century 14 bold",padx=54,command=list)
    btn2.place(x=225,y=180)

    btn3=tkinter.Button(text="CHECK OUT",font="Century 14 bold",padx=90,command=ckout)
    btn3.place(x=225,y=240)

    btn4=tkinter.Button(text="GET INFO OF ANY GUEST",font="Century 14 bold",padx=19,command=info)
    btn4.place(x=225,y=300)

    btn5=tkinter.Button(text="EXIT",font="Century 14 bold",padx=130,command=win.destroy)
    btn5.place(x=225,y=360)

    win.mainloop()

# This ensures it's not auto-called when imported

if __name__ == "__main__":
    main_screen()