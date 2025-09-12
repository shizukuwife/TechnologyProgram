import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#ดาวน์โหลด pip install selenium, pip install webdriver-manager

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
            text_box.insert(tk.END, f"{k} : {v}\n\n")
    else:
        text_box.insert(tk.END, "ไม่มีข้อมูล")

root = tk.Tk()
root.title("ผลสลากกินแบ่งรัฐบาล")
root.geometry("600x700")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Kanit", 16))
style.configure("TButton", font=("Kanit", 18), padding=10)

header = tk.Frame(root, bg="#007acc", height=80)
header.pack(fill="x")

title_label = tk.Label(header, text="ผลสลากกินแบ่งรัฐบาล", font=("Kanit", 28, "bold"), bg="#007acc", fg="white")
title_label.pack(pady=20)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

text_frame = ttk.Frame(main_frame)
text_frame.pack(fill="both", expand=True, pady=10)

scrollbar = ttk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(
    text_frame,
    font=("Consolas", 20),
    height=12,
    yscrollcommand=scrollbar.set,
    bg="#ffffff",
    fg="#000000",
    wrap="word",
    relief="solid",
    borderwidth=2
)
text_box.pack(fill="both", expand=True)
scrollbar.config(command=text_box.yview)

button = ttk.Button(main_frame, text="📥 ดึงผลล่าสุด", command=show_results)
button.pack(pady=20, ipadx=10, fill="x")

footer = tk.Label(root, text="สร้างโดย 38", font=("Kanit", 12), bg="#f0f0f0", fg="#888888")
footer.pack(pady=10)

root.mainloop()

#โค้ดหยุดระเบิดที แก้หลายรอบแล้ว :(