import tkinter as tk
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from roundBotton import CustomButton

root = tk.Tk()
root.title("PDF Text Extractor")

height = 300
width = 600

# app size
canvas = tk.Canvas(root, width=width, height=height, bg="purple")
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="purple")
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instruction
instruction = tk.Label(root, text="Select a PDF on your computer to extract all its text", font="Corbel", bg="purple", fg="white")
instruction.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("Loading")
    file = askopenfile(parent=root, mode="rb", title="Choose a file",
                       filetype=[("PDF file", "*.pdf")])
    if file:
        top = Toplevel()
        top.title("Text Extracted")
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # text box
        text_box = tk.Text(top, height=height//30, width=width//12, padx=width//40, pady=height//20)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="left")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


# button
browse_text = tk.StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Corbel",12),
                    bg="#20bebe", fg="white", height=height//height, width=width//40)

browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

# # padding of button
# canvas = tk.Canvas(root, width=600, height=250, bg="purple")
# canvas.grid(columnspan=3, rowspan=3)

root.mainloop()
