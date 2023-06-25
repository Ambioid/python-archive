import tkinter as tk

window = tk.Tk()
window.title("Unit 3 Revision")
window.resizable(width=False, height=False)

#Frame widget for organising layout
frame = tk.Frame(master=window, width=200, height=300)
frame.pack()

#Command funation for the button
def calcuate_file_size():
    variables=variable.get()
    chars=int(ent_charCount.get())
    if variables == "7-bit ASCII":
        label_result["text"] = chars*7
    elif variables == "8-bit ASCII":
        label_result["text"] = chars*8
    elif variables == "Unicode":
        label_result["text"] = chars*16
    else:
        label_result["text"] = 0

#Label for the title of the frame
label_1 = tk.Label(master=frame, text="Text encoding", font=("Arial Bold", 18), bg='#00FFFF')
label_1.place(x=0, y=0)


#Choose text encoding options (bits per character) from dropdown menu
label_2 = tk.Label(master=frame, text="Text encoding choice")
label_2.place(x=5, y=35)

variable = tk.StringVar(window)
variable.set("choose") # default value

w = tk.OptionMenu(window, variable, "7-bit ASCII", "8-bit ASCII", "Unicode")
w.place(x=15, y=55)



#Get number of character
label_3 = tk.Label(master=frame, text="Input number of characters")
label_3.place(x=5, y=100)

ent_charCount = tk.Entry(master=window, width=10)
ent_charCount.place(x=5, y=120)

label_4 = tk.Label(master=window, text="Characters")
label_4.place(x=80, y=120)



#Calculate the file size
label_5 = tk.Label(master=window, text="Calculate File size")
label_5.place(x=00, y=170)

btn_convert = tk.Button(
    master=window,
    text="Calcuate", command=calcuate_file_size
    )
btn_convert.place(x=50, y=190)

label_result = tk.Label(master=window, text="",font=("Arial Bold", 12),bg='#FFFFFF')
label_result.place(x=20, y=220)

label_6 = tk.Label(master=window, text="bits")
label_6.place(x=80, y=220)


window.mainloop()
