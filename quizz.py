import tkinter as tk
from tkinter import messagebox
import random

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")
        self.configure(background="#f0f0f0")  # Set background color
        
        self.quiz_questions = self.load_quiz_questions()
        self.score = 0
        self.total_questions = len(self.quiz_questions)
        self.current_question_index = 0
        
        self.create_widgets()
        self.present_question()
        
    def load_quiz_questions(self):
        # Define your quiz questions here
        quiz_questions = [
            {"question": "What is the capital of France?", "options": ["New York", "Paris", "London", "Dublin"], "answer": "Paris"},
            {"question": "Who is CEO of Tesla?", "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"], "answer": "Elon Musk"},
            {"question": "The iPhone was created by which company?", "options": ["Apple", "Intel", "Amazon", "Microsoft"], "answer": "Apple"},
            {"question": "How many Harry Potter books are there?", "options": ["1", "4", "6", "7"], "answer": "7"}
        ]
        return quiz_questions
        
    def create_widgets(self):
        self.question_label = tk.Label(self, text="", wraplength=380, bg="#f0f0f0", fg="#333333")  # Set text and background color
        self.question_label.pack(pady=10)
        
        self.options_frame = tk.Frame(self, bg="#f0f0f0")  # Set background color
        self.options_frame.pack(pady=5)
        
        self.options_var = tk.StringVar()
        self.options = []
        for i in range(2):
            row_frame = tk.Frame(self.options_frame, bg="#f0f0f0")  # Set background color for each row
            row_frame.pack()
            for j in range(2):
                option = tk.Radiobutton(row_frame, text="", variable=self.options_var, value="", indicatoron=0, bg="#f0f0f0", fg="#333333", activebackground="#cccccc", activeforeground="#333333")  # Set colors
                option.pack(side=tk.LEFT, padx=10)  # Add padding between options
                self.options.append(option)
            # Add some vertical spacing between rows
            tk.Label(self.options_frame, text="", bg="#f0f0f0").pack()  # Add an empty label as spacer
        
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer, bg="#4caf50", fg="#ffffff", activebackground="#388e3c")  # Set colors
        self.submit_button.pack(pady=10)
        
        self.feedback_label = tk.Label(self, text="", bg="#f0f0f0", fg="#333333")  # Set text and background color
        self.feedback_label.pack(pady=5)
        
        self.next_button = tk.Button(self, text="Next", command=self.present_question, state=tk.DISABLED, bg="#2196f3", fg="#ffffff", activebackground="#1976d2")  # Set colors
        self.next_button.pack(pady=5)
        
    def present_question(self):
        if self.current_question_index < self.total_questions:
            question_data = self.quiz_questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            self.options_var.set("")
            options = random.sample(question_data["options"], len(question_data["options"]))
            for i in range(4):
                self.options[i].config(text=options[i], value=options[i])
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.display_final_results()
    
    def check_answer(self):
        user_answer = self.options_var.get()
        correct_answer = self.quiz_questions[self.current_question_index]["answer"]
        
        if user_answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg="#4caf50")  # Set text color
            self.score += 1
        else:
            self.feedback_label.config(text="Incorrect. Correct answer: " + correct_answer, fg="#f44336")  # Set text color
        
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        
        self.current_question_index += 1
    
    def display_final_results(self):
        messagebox.showinfo("Quiz Complete", f"You answered {self.score} out of {self.total_questions} questions correctly.")
        self.quit()
        
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
