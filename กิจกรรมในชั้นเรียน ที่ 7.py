import tkinter as tk

root = tk.Tk()
root.title("Count Down")
root.geometry("400x300")

label = tk.Label(root, text="", font=("Arial", 30))
label.pack(pady=30)

info_label = tk.Label(root, text="", font=("Arial", 14))
info_label.pack(pady=10)

count = 10  # เริ่มถอยจาก 10

def countdown():
    global count
    if count > 0:
        label.config(text=f"{count}")
        count -= 1
        root.after(1000, countdown)  # หน่วงเวลา 1 วินาที แล้วเรียกตัวเองซ้ำ
    else:
        label.config(text="เวลา 0")
        show_info()

def show_info():
    info = (
        "ชื่อ-นามสกุล: อิษฎาอร โชคมงคลเสถียร\n"
        "ชื่อเล่น: วุ้นเส้น\n"
        "ห้องเรียน: ม.5/8\n"
        "แผนการเรียน: วิทย์-คณิต-เทคโน\n"
        "อยากเรียนคณะ: สาขาสถาปัตยกรรม และการออกแบบกลุ่มเอกแอนิเมชัน"
    )
    info_label.config(text=info)

countdown()
root.mainloop()
