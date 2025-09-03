import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#กรุณาอย่าลืมดาวน์โหลด requests, beautifulsoup4, selenium เพิ่มเพราะหนูดึงข้อมูลไม่ได้ 
def get_lottery_results():
    url = "https://www.lottery.co.th/small"
    results = {}
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(url)
        time.sleep(3)  # รอให้ JS โหลดเสร็จ

        numbers = [el.text for el in driver.find_elements(By.TAG_NAME, "strong")]

        driver.quit()

        if len(numbers) >= 4:
            results["รางวัลที่ 1"] = numbers[1]
            results["เลขท้าย 2 ตัว"] = numbers[3]
            results["เลขหน้า 3 ตัว"] = str(numbers[5] + " " + numbers[6])
            results["เลขท้าย 3 ตัว"] = str(numbers[8] + " " + numbers[9])
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
root.geometry("650x500")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

label = ttk.Label(frame, text="ผลสลากกินแบ่งรัฐบาล", font=("Arial", 20, "bold"))
label.pack(pady=10)

text_frame = ttk.Frame(frame)
text_frame.pack(fill="both", expand=True, pady=10)

scrollbar = ttk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(text_frame, width=60, height=20, font=("Arial", 14), yscrollcommand=scrollbar.set)
text_box.pack(side="left", fill="both", expand=True)
scrollbar.config(command=text_box.yview)

button = ttk.Button(frame, text="ดึงผลล่าสุด", command=show_results)
button.pack(pady=10)

root.mainloop()