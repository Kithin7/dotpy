import tkinter as tk
window = tk.Tk()
window.rowconfigure([0, 1, 2, 3, 4], minsize=50)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50)
window.geometry("200x150")

cards = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

def b1():
    clickon = str(button1["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b2():
    clickon = str(button2["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b3():
    clickon = str(button3["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b4():
    clickon = str(button4["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b5():
    clickon = str(button5["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b6():
    clickon = str(button6["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b7():
    clickon = str(button7["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b8():
    clickon = str(button8["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b9():
    clickon = str(button9["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b10():
    clickon = str(button10["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b11():
    clickon = str(button11["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass
def b12():
    clickon = str(button12["text"])
    if info_["text"] == "1":
        last_click["text"] = clickon
        info_["text"] = "2"
    elif info_["text"] == "2":
        last_click2["text"] = clickon
        info_["text"] = "3"
    elif info_["text"] == "3":
        last_click3["text"] = clickon
        info_["text"] = "1"
    else:
        pass

frame = tk.Frame(master=window, borderwidth=1,bg="black")
frame.pack(side=tk.LEFT)

button1 = tk.Button(master=frame, text=cards[0], command=b1)
button1.grid(row=0,column=0,sticky="nsew")
button2 = tk.Button(master=frame, text=cards[1], command=b2)
button2.grid(row=0,column=1,sticky="nsew")
button3 = tk.Button(master=frame, text=cards[2], command=b3)
button3.grid(row=0,column=2,sticky="nsew")
button4 = tk.Button(master=frame, text=cards[3], command=b4)
button4.grid(row=0,column=3,sticky="nsew")
button5 = tk.Button(master=frame, text=cards[4], command=b5)
button5.grid(row=1,column=0,sticky="nsew")
button6 = tk.Button(master=frame, text=cards[5], command=b6)
button6.grid(row=1,column=1,sticky="nsew")
button7 = tk.Button(master=frame, text=cards[6], command=b7)
button7.grid(row=1,column=2,sticky="nsew")
button8 = tk.Button(master=frame, text=cards[7], command=b8)
button8.grid(row=1,column=3,sticky="nsew")
button9 = tk.Button(master=frame, text=cards[8], command=b9)
button9.grid(row=2,column=0,sticky="nsew")
button10 = tk.Button(master=frame, text=cards[9], command=b10)
button10.grid(row=2,column=1,sticky="nsew")
button11 = tk.Button(master=frame, text=cards[10], command=b11)
button11.grid(row=2,column=2,sticky="nsew")
button12 = tk.Button(master=frame, text=cards[11], command=b12)
button12.grid(row=2,column=3,sticky="nsew")

infoside = tk.Frame(master=window, borderwidth=1,bg="black")
infoside.pack(side=tk.RIGHT)
clickon=""
info_ = tk.Label(master=infoside, text="1",bg="black", fg="white")
info_.pack()
info_a = tk.Label(master=infoside,text="First:",bg="black", fg="white")
info_a.pack()
last_click = tk.Label(master=infoside,text=f"{clickon}",bg="black", fg="white")
last_click.pack()
info_b = tk.Label(master=infoside,text="Second:",bg="black", fg="white")
info_b.pack()
last_click2 = tk.Label(master=infoside,text=f"{clickon}",bg="black", fg="white")
last_click2.pack()
info_c = tk.Label(master=infoside,text="Third:",bg="black", fg="white")
info_c.pack()
last_click3 = tk.Label(master=infoside,text=f"{clickon}",bg="black", fg="white")
last_click3.pack()

window.mainloop()