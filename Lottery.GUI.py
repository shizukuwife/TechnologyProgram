import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#ด้วยความกรุณาอย่าลืม pip install requests, beautifulsoup4, selenium และ webdriver-manager และเมื่อรันได้ โปรดเปิดเต็มจอ 

def get_lottery_results():
    url = "https://www.lottery.co.th/small"
    results = {}
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(url)
        time.sleep(3)

        numbers = [el.text for el in driver.find_elements(By.TAG_NAME, "strong")]

        driver.quit()

        if len(numbers) >= 10:
            results["รางวัลที่ 1"] = numbers[1]
            results["เลขท้าย 2 ตัว"] = numbers[3]
            results["เลขหน้า 3 ตัว"] = f"{numbers[5]} {numbers[6]}"
            results["เลขท้าย 3 ตัว"] = f"{numbers[8]} {numbers[9]}"
        else:
            results["Error"] = "ไม่พบข้อมูลครบถ้วน"

        return results

    except Exception as e:
        messagebox.showerror("Error", f"ไม่สามารถดึงข้อมูลได้\n{e}")
        return {}


def show_results():
    text_box.delete("1.0", tk.END)
    results = get_lottery_results()
    if results:
        for k, v in results.items():
            line = f"{k} : {v}\n\n"
            text_box.insert(tk.END, line, "center")  # ใส่ tag "center"
    else:
        text_box.insert(tk.END, "ไม่มีข้อมูล", "center")


root = tk.Tk()
root.title("ผลสลากกินแบ่งรัฐบาล")
root.geometry("700x550")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.theme_use("default")

style.configure("TFrame", background="#f0f4f7")
style.configure("TLabel", background="#f0f4f7", font=("Arial", 20, "bold"), foreground="#333")
style.configure("TButton", font=("Arial", 14), padding=10)
style.map("TButton",
          foreground=[('pressed', 'white'), ('active', '#003366')],
          background=[('pressed', '#336699'), ('active', '#cce6ff')])

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

label = ttk.Label(frame, text="ผลสลากกินแบ่งรัฐบาล")
label.pack(pady=10)

text_frame = ttk.Frame(frame)
text_frame.pack(fill="both", expand=True, pady=10)

scrollbar = ttk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(
    text_frame,
    width=60,
    height=20,
    font=("Arial", 24),   # เพิ่มขนาดฟอนต์
    yscrollcommand=scrollbar.set,
    bg="#ffffff",
    fg="#000000",
    relief="flat",
    bd=1,
    padx=10,
    pady=10
)
text_box.pack(side="left", fill="both", expand=True)
scrollbar.config(command=text_box.yview)

text_box.tag_configure("center", justify="center")

button = ttk.Button(frame, text="ดึงผลล่าสุด", command=show_results)
button.pack(pady=10)

root.mainloop()
