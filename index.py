from tkinter import *

def click(event):
    global scvalue
    text1=event.widget.cget("text")
    if text1=="=":

       if scvalue.get().isdigit():
           value=int(scvalue.get())
       else:
           try:
               value=eval(scvalue.get())
           except Exception as e:
               value="ERROR"
       scvalue.set(value)
       screen.update()

    elif text1=="C":
        scvalue.set(" ")
    else:
        scvalue.set(str(scvalue.get())+str(text1))
        screen.update()


cal=Tk()

cal.geometry("325x495")
cal.title("Calculator")
cal.configure(background="lightseagreen")
# cal.wm_iconbitmap("icon.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(cal,textvariable=scvalue, font="lucida 30 bold",borderwidth=10,relief=SUNKEN,justify=RIGHT)
screen.pack(fill=X, ipadx=6, pady=8, padx=8)

# -------------------------------------------------------------------------------------------------------
f1=Frame(cal,bg='black')
b1=Button(f1, text="C",font="lucida 20 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey",fg="red")
b1.pack(anchor="nw",side=LEFT,ipadx=6)
b1.bind('<Button-1>',click)

b2=Button(f1, text="()",font="lucida 20 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b2.pack(anchor="nw",side=LEFT,ipadx=6)
b2.bind('<Button-1>',click)
b3=Button(f1, text="^",font="lucida 20 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b3.pack(anchor="nw",side=LEFT,ipadx=6)
b3.bind('<Button-1>',click)
b4=Button(f1, text="%",font="lucida 20 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b4.pack(anchor="nw",side=LEFT,ipadx=6)
b4.bind('<Button-1>',click)
f1.pack()

# --------------------------------------------------------------------------
f2=Frame(cal,bg='black')
b1=Button(f2, text="7",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b1.pack(anchor="nw",side=LEFT,ipadx=8)
b1.bind('<Button-1>',click)
b2=Button(f2, text="8",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b2.pack(anchor="nw",side=LEFT,ipadx=8)
b2.bind('<Button-1>',click)
b3=Button(f2, text="9",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b3.pack(anchor="nw",side=LEFT,ipadx=8)
b3.bind('<Button-1>',click)
b4=Button(f2, text="*",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b4.pack(anchor="nw",side=LEFT,ipadx=8)
b4.bind('<Button-1>',click)
f2.pack()
# -------------------------------------------------------------
f3=Frame(cal,bg='black')
b1=Button(f3, text="4",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b1.pack(anchor="nw",side=LEFT,ipadx=8)
b1.bind('<Button-1>',click)
b2=Button(f3, text="5",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b2.pack(anchor="nw",side=LEFT,ipadx=8)
b2.bind('<Button-1>',click)
b3=Button(f3, text="6",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b3.pack(anchor="nw",side=LEFT,ipadx=8)
b3.bind('<Button-1>',click)
b4=Button(f3, text="-",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b4.pack(anchor="nw",side=LEFT,ipadx=8)
b4.bind('<Button-1>',click)
f3.pack()
# --------------------------------------------
f4=Frame(cal,bg='black')
b1=Button(f4, text="1",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b1.pack(anchor="nw",side=LEFT,ipadx=8)
b1.bind('<Button-1>',click)
b2=Button(f4, text="2",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b2.pack(anchor="nw",side=LEFT,ipadx=8)
b2.bind('<Button-1>',click)
b3=Button(f4, text="3",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b3.pack(anchor="nw",side=LEFT,ipadx=8)
b3.bind('<Button-1>',click)
b4=Button(f4, text="+",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b4.pack(anchor="nw",side=LEFT,ipadx=6)
b4.bind('<Button-1>',click)
f4.pack()
# -----------------------------------------------
f5=Frame(cal,bg='black')
b1=Button(f5, text="0",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b1.pack(anchor="nw",side=LEFT,ipadx=9)
b1.bind('<Button-1>',click)

b2=Button(f5, text=".",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="whitesmoke")
b2.pack(anchor="nw",side=LEFT,ipadx=9)
b2.bind('<Button-1>',click)
b3=Button(f5, text="=",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="bisque")
b3.pack(anchor="nw",side=LEFT,ipadx=9)
b3.bind('<Button-1>',click)
b4=Button(f5, text="/",font="lucida 22 bold",borderwidth=5,relief=RAISED,padx=6,pady=6,bg="lightgrey")
b4.pack(anchor="nw",side=LEFT,ipadx=10)
b4.bind('<Button-1>',click)
f5.pack()
# -----------------------------------



cal.mainloop()
