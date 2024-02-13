import tkinter as tk
from tkinter import messagebox
import random

class QuizApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz")
        self.geometry("400x300")
        self.configure(background="#f0f0f0")
        
        self.questions = self.load_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        self.current_question_index = 0
        
        self.setup_ui()
        self.show_question()
        
    def load_questions(self):
        questions = [
            {"query": "What is the capital of France?", "options": ["New York", "Paris", "London", "Dublin"], "answer": "Paris"},
            {"query": "Who is the CEO of Tesla?", "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"], "answer": "Elon Musk"},
            {"query": "Which company created the iPhone?", "options": ["Apple", "Intel", "Amazon", "Microsoft"], "answer": "Apple"},
            {"query": "How many Harry Potter books are there?", "options": ["1", "4", "6", "7"], "answer": "7"}
        ]
        return questions
        
    def setup_ui(self):
        self.question_label = tk.Label(self, text="", wraplength=380, bg="#f0f0f0", fg="#333333")
        self.question_label.pack(pady=10)
        
        self.options_frame = tk.Frame(self, bg="#f0f0f0")
        self.options_frame.pack(pady=5)
        
        self.answer_var = tk.StringVar()
        self.options = []
        for _ in range(2):
            row_frame = tk.Frame(self.options_frame, bg="#f0f0f0")
            row_frame.pack()
            for _ in range(2):
                option = tk.Radiobutton(row_frame, text="", variable=self.answer_var, value="", indicatoron=0, bg="#f0f0f0", fg="#333333", activebackground="#cccccc", activeforeground="#333333")
                option.pack(side=tk.LEFT, padx=10)
                self.options.append(option)
            tk.Label(self.options_frame, text="", bg="#f0f0f0").pack()
        
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer, bg="#4caf50", fg="#ffffff", activebackground="#388e3c")
        self.submit_button.pack(pady=10)
        
        self.feedback_label = tk.Label(self, text="", bg="#f0f0f0", fg="#333333")
        self.feedback_label.pack(pady=5)
        
        self.next_button = tk.Button(self, text="Next", command=self.show_question, state=tk.DISABLED, bg="#2196f3", fg="#ffffff", activebackground="#1976d2")
        self.next_button.pack(pady=5)
        
    def show_question(self):
        if self.current_question_index < self.total_questions:
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["query"])
            self.answer_var.set("")
            options = random.sample(question_data["options"], len(question_data["options"]))
            for i in range(4):
                self.options[i].config(text=options[i], value=options[i])
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.show_results()
    
    def check_answer(self):
        user_answer = self.answer_var.get()
        correct_answer = self.questions[self.current_question_index]["answer"]
        
        if user_answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg="#4caf50")
            self.score += 1
        else:
            self.feedback_label.config(text="Incorrect. Correct answer: " + correct_answer, fg="#f44336")
        
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        
        self.current_question_index += 1
    
    def show_results(self):
        messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{self.total_questions}")
        self.quit()
        
if __name__ == "__main__":
    app = QuizApplication()
    app.mainloop()
