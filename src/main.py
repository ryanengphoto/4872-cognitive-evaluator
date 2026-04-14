import tkinter as tk
from tkinter import messagebox, ttk
import math
import random

KNOWLEDGE_BASE = {
    "questions": [
        {
            "id": "1",
            "question": "What is the capital of France?",
            "answer": "Paris",
            "difficulty": "medium",
            "correct_next": "4",
            "incorrect_next": "2",
        },
        {
            "id": "2",
            "question": "What is the capital of Germany?",
            "answer": "Berlin",
            "difficulty": "easy",
            "correct_next": "3",
            "incorrect_next": "5",
        },
        {
            "id": "3",
            "question": "What is the capital of Italy?",
            "answer": "Rome",
            "difficulty": "medium",
            "correct_next": None,
            "incorrect_next": None,
        },
        {
            "id": "4",
            "question": "What is the capital of Spain?",
            "answer": "Madrid",
            "difficulty": "hard",
            "correct_next": "2",
            "incorrect_next": "5",
        },
        {
            "id": "6",
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon",
            "difficulty": "easy",
            "correct_next": None,
            "incorrect_next": None,
        },
                {
            "id": "7",
            "question": "What is the capital of France?",
            "answer": "Paris",
            "difficulty": "medium",
            "correct_next": "2",
            "incorrect_next": "4",
        },
        {
            "id": "8",
            "question": "What is the capital of Germany?",
            "answer": "Berlin",
            "difficulty": "hard",
            "correct_next": "3",
            "incorrect_next": "5",
        },
        {
            "id": "9",
            "question": "What is the capital of Italy?",
            "answer": "Rome",
            "difficulty": "easy",
            "correct_next": None,
            "incorrect_next": None,
        },
        {
            "id": "10",
            "question": "What is the capital of Spain?",
            "answer": "Madrid",
            "difficulty": "medium",
            "correct_next": "2",
            "incorrect_next": "5",
        },
        {
            "id": "11",
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon",
            "difficulty": "hard",
            "correct_next": None,
            "incorrect_next": None,
        },
                {
            "id": "12",
            "question": "What is the capital of France?",
            "answer": "Paris",
            "difficulty": "easy",
            "correct_next": "2",
            "incorrect_next": "4",
        },
        {
            "id": "13",
            "question": "What is the capital of Germany?",
            "answer": "Berlin",
            "difficulty": "medium",
            "correct_next": "3",
            "incorrect_next": "5",
        },
        {
            "id": "14",
            "question": "What is the capital of Italy?",
            "answer": "Rome",
            "difficulty": "hard",
            "correct_next": None,
            "incorrect_next": None,
        },
        {
            "id": "15",
            "question": "What is the capital of Spain?",
            "answer": "Madrid",
            "difficulty": "easy",
            "correct_next": "2",
            "incorrect_next": "5",
        },
        {
            "id": "16",
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon",
            "difficulty": "medium",
            "correct_next": None,
            "incorrect_next": None,
        },
                {
            "id": "17",
            "question": "What is the capital of France?",
            "answer": "Paris",
            "difficulty": "hard",
            "correct_next": "2",
            "incorrect_next": "4",
        },
        {
            "id": "18",
            "question": "What is the capital of Germany?",
            "answer": "Berlin",
            "difficulty": "easy",
            "correct_next": "3",
            "incorrect_next": "5",
        },
        {
            "id": "19",
            "question": "What is the capital of Italy?",
            "answer": "Rome",
            "difficulty": "medium",
            "correct_next": None,
            "incorrect_next": None,
        },
        {
            "id": "20",
            "question": "What is the capital of Spain?",
            "answer": "Madrid",
            "difficulty": "hard",
            "correct_next": "2",
            "incorrect_next": "5",
        }
    ]
}


class DecisionTree:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.questions = {q["id"]: q for q in self.knowledge_base["questions"]}
        self.score = 0
        self.max_questions = math.floor(len(self.questions)/3)

    def update_score(self, question, correct):
        if not correct:
            return
        if question["difficulty"] == "easy":
            self.score += 1
        elif question["difficulty"] == "medium":
            self.score += 2
        elif question["difficulty"] == "hard":
            self.score += 3

    def get_random_medium_question(self):
        medium_questions = [q for q in self.questions.values() if q["difficulty"] == "medium"]
        return random.choice(medium_questions)["id"]
        
    def get_random_hard_question(self):
        hard_questions = [q for q in self.questions.values() if q["difficulty"] == "hard"]
        return random.choice(hard_questions)["id"]

    def get_random_easy_question(self):
        easy_questions = [q for q in self.questions.values() if q["difficulty"] == "easy"]
        return random.choice(easy_questions)["id"]

    def get_next_question(self, question_id, answer):
        question = self.questions[question_id]
        correct = answer.strip().lower() == question["answer"].strip().lower()
        self.update_score(question, correct)

        # remove the question from the list so it isn't used again
        self.questions.pop(question["id"], None)
        if correct:
            if question["difficulty"] == "easy":
                return self.get_random_medium_question()
            elif question["difficulty"] == "medium":
                return self.get_random_hard_question()
            elif question["difficulty"] == "hard":
                return self.get_random_hard_question()
        else:
            if question["difficulty"] == "easy":
                return self.get_random_easy_question()
            elif question["difficulty"] == "medium":
                return self.get_random_easy_question()
            elif question["difficulty"] == "hard":
                return self.get_random_medium_question()

    def get_score(self):
        return self.score

    def get_result(self):
        if self.score < 3:
            return "Low cognitive ability"
        if self.score < 6:
            return "Average cognitive ability"
        return "High cognitive ability"


class GUI:
    def __init__(self, root, tree):
        self.decision_tree = tree
        self.root = root
        self.root.title("Cognitive Evaluator")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f4f8")
        self.root.resizable(False, False)

        self.current_question_id = "1"
        self.score = 0
        self.questions_answered = 0
        self.max_questions = self.decision_tree.max_questions
        self.questions_dict = self.decision_tree.questions

        self._build_styles()
        self._build_layout()
        self._load_question()

    def _build_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Submit.TButton", background="#2563eb", foreground="#ffffff")
        style.configure("Quit.TButton", background="#e5e7eb", foreground="#374151")
        style.configure("Restart.TButton", background="#059669", foreground="#ffffff")

    def _build_layout(self):
        self.content_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=20)

        self.score_label = tk.Label(
            self.content_frame,
            text="Score: 0",
            bg="#f0f4f8",
            fg="#1a2a4a",
            font=("Helvetica", 13, "bold"),
        )
        self.score_label.pack(anchor="w")

        self.progress_label = tk.Label(
            self.content_frame,
            text=f"Question 1 of {self.max_questions}",
            bg="#f0f4f8",
            fg="#6b7280",
            font=("Helvetica", 11),
        )
        self.progress_label.pack(anchor="e")

        self.question_label = tk.Label(
            self.content_frame,
            text="",
            bg="#ffffff",
            fg="#1a2a4a",
            font=("Georgia", 14),
            wraplength=620,
            justify="left",
            anchor="w",
            padx=16,
            pady=16,
        )
        self.question_label.pack(fill="x", pady=8)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(
            self.content_frame,
            textvariable=self.answer_var,
            font=("Helvetica", 13),
        )
        self.answer_entry.pack(fill="x", ipady=8, pady=8)
        self.answer_entry.bind("<Return>", lambda e: self._submit())

        self.feedback_label = tk.Label(
            self.content_frame, text="", bg="#f0f4f8", font=("Helvetica", 11, "bold")
        )
        self.feedback_label.pack(fill="x", pady=8)

        btn_row = tk.Frame(self.content_frame, bg="#f0f4f8")
        btn_row.pack(fill="x", pady=8)
        ttk.Button(btn_row, text="Quit", style="Quit.TButton", command=self._confirm_quit).pack(
            side="right", padx=(8, 0)
        )
        self.submit_btn = ttk.Button(
            btn_row, text="Submit Answer", style="Submit.TButton", command=self._submit
        )
        self.submit_btn.pack(side="right")

    def _load_question(self):
        if (
            self.current_question_id not in self.questions_dict
            or self.questions_answered >= self.max_questions
        ):
            self._show_results()
            return

        q = self.questions_dict[self.current_question_id]
        num = self.questions_answered + 1
        self.progress_label.config(text=f"Question {num} of {self.max_questions}")
        self.question_label.config(text=q["question"])
        self.feedback_label.config(text="")
        self.answer_var.set("")
        self.answer_entry.config(state="normal")
        self.submit_btn.config(state="normal")
        self.answer_entry.focus()

    def _submit(self):
        raw = self.answer_var.get().strip()
        if not raw:
            messagebox.showwarning("No answer", "Please type an answer before submitting.")
            return

        q = self.questions_dict[self.current_question_id]
        correct = raw.lower() == q["answer"].lower()
        if correct:
            self.score += 1
            self.feedback_label.config(text=f"Correct! The answer is {q['answer']}.", fg="#059669")
        else:
            self.feedback_label.config(
                text=f"Incorrect. The correct answer is {q['answer']}.", fg="#dc2626"
            )

        self.score_label.config(text=f"Score: {self.score}")
        self.answer_entry.config(state="disabled")
        self.submit_btn.config(state="disabled")
        self.current_question_id = self.decision_tree.get_next_question(self.current_question_id, raw)
        self.questions_answered += 1
        self.root.after(1000, self._load_question)

    def _show_results(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        score = self.decision_tree.get_score()
        tk.Label(
            self.content_frame,
            text=f"Quiz complete! You earned {score} points.",
            bg="#f0f4f8",
            fg="#1a2a4a",
            font=("Georgia", 18, "bold"),
        ).pack(pady=12)
        tk.Label(
            self.content_frame,
            text=self.decision_tree.get_result(),
            bg="#f0f4f8",
            fg="#4b5563",
            font=("Helvetica", 13),
        ).pack(pady=8)
        ttk.Button(
            self.content_frame, text="Play Again", style="Restart.TButton", command=self._restart
        ).pack(pady=6)
        ttk.Button(
            self.content_frame, text="Quit", style="Quit.TButton", command=self.root.destroy
        ).pack(pady=6)

    def _restart(self):
        self.current_question_id = "1"
        self.score = 0
        self.questions_answered = 0
        self.questions_dict = self.decision_tree.questions
        self.decision_tree.score = 0
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self._build_layout()
        self._load_question()

    def _confirm_quit(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


def main():
    tree = DecisionTree(KNOWLEDGE_BASE)
    root = tk.Tk()
    gui = GUI(root, tree)
    gui.run()


if __name__ == "__main__":
    main()
