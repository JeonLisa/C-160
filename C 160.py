from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.title("Note Pad Editor")
root.geometry("650x650")
close_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
def open_gmi():
    print("high")
def close_gmi():
    print("high")
def save_gmi():
    print("high")
button_opn=Button(root,image=open_img,command=open_gmi)
button_cls=Button(root,image=close_img,command=close_gmi)
button_sve=Button(root,image=save_img,command=save_gmi)
button_opn.place(relx=0.05,rely=0.03,anchor=CENTER)
button_cls.place(relx=0.11,rely=0.03,anchor=CENTER)
button_sve.place(relx=0.17,rely=0.03,anchor=CENTER)
label_1=Label(root,text="File Name")
label_1.place(relx=0.24,rely=0.03,anchor=CENTER)
input_1=Entry(root)
input_1.place(relx=0.42,rely=0.03,anchor=CENTER)
text_area=Text(root,height=35,width=80)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)
root.mainloop()