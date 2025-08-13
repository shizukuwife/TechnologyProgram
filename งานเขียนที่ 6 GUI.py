import tkinter as tk

def update_label():
    my_label.config(text="ชื่อ : อิษฎาอร โชคมงคลเสถียร ,ชั้น 508 , เลขที่ 38",fg= "black")
    
root = tk.Tk()
root.title("EPT - Event Label Example")

my_label = tk.Label(root, text="กดปุ่มเพื่อเปลี่ยนข้อความ", fg="black")
my_label.pack()

my_button = tk.Button(root, text="Press here", command=update_label)
my_button.pack()

root.mainloop()