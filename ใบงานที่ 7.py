import tkinter as tk

def calculate_area():
    base = float(entry_base.get())  #อย่าใส่ตัวอักษรเด้อเดี๋ยวโค้ดระเบิด
    height = float(entry_height.get())
    area = 0.5 * base * height
    result_label.config(text=f"พื้นที่สามเหลี่ยม: {area:.2f} ตารางหน่วย")

window = tk.Tk()
window.title("คำนวณพื้นที่สามเหลี่ยม")
window.geometry("300x200")

tk.Label(window, text="ความยาวฐาน:").pack(pady=5)
entry_base = tk.Entry(window)
entry_base.pack()

tk.Label(window, text="ความสูง:").pack(pady=5)
entry_height = tk.Entry(window)
entry_height.pack()

tk.Button(window, text="คำนวณ", command=calculate_area).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

