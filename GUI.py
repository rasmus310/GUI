import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles_input = entry_Int.get()
    km_output = miles_input * 1.60934
    output_string.set(km_output)

#window
window = ttk.Window(themename = 'darkly')
window.title("Demo")
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri, 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window) # create a frame to hold the input field and button
entry_Int = tk.IntVar() # create a variable to hold the value in the entry field
entry = ttk.Entry(
    master = input_frame,
    textvariable = entry_Int) # 
button = ttk.Button(
    master = input_frame, 
    text = 'Convert', 
    command = convert)
entry.pack(side = 'left', padx = 10) # places the entry field in the window
button.pack(side = 'left') # places the button in the window
input_frame.pack(pady = 10) # places widgets in the window

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text = 'output',
    font = 'Calibri, 24', 
    textvariable=output_string)
output_label.pack()

#run
window.mainloop()