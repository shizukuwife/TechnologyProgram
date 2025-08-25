from tkinter import *
import qrcode
from PIL import ImageTk, Image

root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

app_label = Label(root, text="QRCode Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200, 100, window=name_label)

Link_label = Label(root, text="URL")
canvas.create_window(200, 140, window=Link_label)

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)

link_entry = Entry(root)
canvas.create_window(200, 180, window=link_entry)

def generate_qr():
    name = name_entry.get()
    url = link_entry.get()

    if name and url:
        qr = qrcode.make(url)
        qr.save(f"{name}.png")

        img = Image.open(f"{name}.png")
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)

        canvas.create_image(200, 350, image=img_tk)
        canvas.image = img_tk 

button = Button(text="สร้างคิวอาร์โค้ด", command=generate_qr)
canvas.create_window(200, 230, window=button)

root.mainloop()
