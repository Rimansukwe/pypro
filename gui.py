import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog

def decompression(i,o):
    decompress(i,o)


window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window, text="File to be decompressed: ")
output_label = tk.Label(window, text="Name of the decompressed file: ")

decompress_button = tk.Button(window,text="Decompress",command=lambda:decompression(input_entry.get(),output_entry.get()))

input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)
output_label.grid(row=1, column=0)
output_entry.grid(row=1,column=1)
decompress_button.grid(row=2,column=1)

window.mainloop()