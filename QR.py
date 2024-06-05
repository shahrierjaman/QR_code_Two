def generate():
    txt = src_entry.get()
    qr = qrcode.QRCode(version=5,box_size=10,border=3)
    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#4e4e4c", back_color="white").convert("RGB")
    img = img.resize((300,300))
    img_tk = ImageTk.PhotoImage(img)
    qr_show_lbl.configure(image=img_tk)
    qr_show_lbl.image = img_tk


import tkinter as tk
from PIL import Image,ImageTk
import ttkbootstrap
from tkinter import ttk
import qrcode

win = ttkbootstrap.Window(themename='morph')
win.title("QR Code Generate")
win.geometry('400x450')

app_icon = ImageTk.PhotoImage(file = "image.png")
win.iconphoto(False, app_icon)


src_lbl = ttk.Label(win,text="Enter text to convert URL")
src_lbl.pack(pady=10)
src_entry = ttk.Entry(win,width=50)
src_entry.pack()
btn = ttkbootstrap.Button(win,text="Search",command=generate, bootstyle="success")
btn.pack(pady=10)
qr_show_lbl = ttk.Label(win)
qr_show_lbl.pack(pady=8)

win.mainloop()
