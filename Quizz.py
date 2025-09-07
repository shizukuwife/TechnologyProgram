import tkinter as tk
from tkinter import messagebox

#ข้อมูลคำถามและตัวเลือก
questions = [
    {
        "question": "1 + 1 = ?",
        "options": ["1", "2", "3", "11"],
        "answer": "2"
    },
    {
        "question": "สีของท้องฟ้าเป็นสีอะไร?",
        "options": ["แดง", "ฟ้า", "เขียว", "เหลือง"],
        "answer": "ฟ้า"
    },
    {
        "question": "ชื่อจริงของครูเกดชื่อ?",
        "options": ["ภัทรานี ไชยสุวรรณ", "ภัทราณี ไชสุวรรณ", "ภัทรานี ไชสุรรณ", "ภัทราณี ไชญสุวรรณ"],
        "answer": "ภัทรานี ไชยสุวรรณ"
    },
    {
        "question": "4!",
        "options": ["22", "24", "28", "30"],
        "answer": "24"
    },
    {
        "question": "อะไรขึ้นแต่ไม่เคยลง?",
        "options": ["อายุ", "อีโก้", "ลิฟต์", "อากาศ"],
        "answer": "อายุ"
    },
    {
        "question": "Sin(30)=x?",
        "options": ["0.707", "0", "0.866", "0.5"],
        "answer": "0.5"
    },
    {
        "question": "Arccot(x)=2/1.732?",
        "options": ["60 องศา", "30 องศา", "45 องศา", "0 องศา"],
        "answer": "30 องศา"
    },
    {
        "question": "ไก่กับไข่อะไรเกิดก่อนกัน?",
        "options": ["ไก่", "ไข่", "ไดโนเสาร์", "ไม่รู้"],
        "answer": "ไม่รู้"
    },
    {
        "question": "มหาสมุทรใดที่ใหญ่ที่สุดในโลก?",
        "options": ["มหาสมุทรอินเดีย", "มหาสมุทรแอตแลนติก", "มหาสมุทรแปซิฟิก", "มหาสมุทรอาร์กติก"],
        "answer": "มหาสมุทรแปซิฟิก"
    },
    {
        "question": "รากที่สองของ 144 คืออะไร?",
        "options": ["12", "11", "13", "14"],
        "answer": "12"
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 แบบทดสอบความรู้ทั่วไป")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f4f7")

        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar()
        self.user_answers = []

        #หัวข้อ
        title = tk.Label(
            root, text="แบบทดสอบความรู้ 📝", font=("Helvetica", 26, "bold"),
            bg="#f0f4f7", fg="#2c3e50"
        )
        title.pack(pady=20)

        #กรอบแสดงคำถามและตัวเลือก
        self.card = tk.Frame(root, bg="white", bd=2, relief="groove", padx=20, pady=20)
        self.card.pack(pady=10, padx=30, fill="both", expand=True)

        self.question_label = tk.Label(
            self.card, text="", font=("Helvetica", 18, "bold"),
            wraplength=600, bg="white", fg="#34495e", justify="center"
        )
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.card, bg="white")
        self.options_frame.pack(pady=10)

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame, text="", variable=self.selected_option, value="",
                font=("Helvetica", 14), bg="white", anchor="w", padx=10,
                activebackground="#ecf0f1", selectcolor="#dff9fb"
            )
            rb.pack(fill="x", pady=5)
            self.options.append(rb)

        #ปุ่มส่ง
        self.submit_btn = tk.Button(
            root, text="✅ ส่งคำตอบ", font=("Helvetica", 14, "bold"),
            bg="#27ae60", fg="white", padx=20, pady=10, command=self.submit_answer
        )
        self.submit_btn.pack(pady=20)

        self.show_question()

    def show_question(self):
        q = questions[self.current_question]
        self.question_label.config(text=f"ข้อที่ {self.current_question + 1}: {q['question']}")
        self.selected_option.set(None)
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def submit_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("คำเตือน", "โปรดเลือกคำตอบก่อนส่ง")
            return

        q = questions[self.current_question]
        correct = q["answer"]
        self.user_answers.append({
            "question": q["question"],
            "selected": selected,
            "correct": correct,
            "is_correct": selected == correct
        })

        if selected == correct:
            self.score += 1

        self.current_question += 1
        if self.current_question == len(questions):
            self.show_summary()
        else:
            self.show_question()

    def show_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("📊 สรุปผล")
        summary_window.geometry("650x600")
        summary_window.configure(bg="#fefefe")

        tk.Label(summary_window, text=f"คุณได้ {self.score} จาก {len(questions)} คะแนน",
                 font=("Helvetica", 18, "bold"), fg="#2980b9", bg="#fefefe").pack(pady=15)

        canvas = tk.Canvas(summary_window, bg="#fefefe", highlightthickness=0)
        scrollbar = tk.Scrollbar(summary_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#fefefe")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for i, answer in enumerate(self.user_answers, start=1):
            result = "✅ ถูก" if answer["is_correct"] else "❌ ผิด"
            color = "green" if answer["is_correct"] else "red"
            summary_text = (
                f"ข้อ {i}: {answer['question']}\n"
                f"คำตอบของคุณ: {answer['selected']}\n"
                f"คำตอบที่ถูกต้อง: {answer['correct']}\n"
                f"ผลลัพธ์: {result}"
            )
            tk.Label(scrollable_frame, text=summary_text, justify="left",
                     fg=color, wraplength=580, anchor="w", bg="#fefefe",
                     font=("Helvetica", 12)).pack(pady=10, anchor="w")

        tk.Button(summary_window, text="ปิด", command=self.root.destroy,
                  font=("Helvetica", 12), bg="#c0392b", fg="white", padx=15, pady=5).pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
