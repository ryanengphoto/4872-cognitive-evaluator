
import tkinter as tk
from tkinter import ttk, messagebox, font
from decision_tree import DecisionTree


class GUI:
    def __init__(self, root, tree):
        self.decision_tree = tree
        self.root = root
        self.root.title("Cognitive Evaluator")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f4f8")
        self.root.resizable(False, False)

        # game state
        self.current_question_id = "1"
        self.score = 0
        self.questions_answered = 0
        self.max_questions = 10

        # decision_tree.questions is already a dict keyed by id
        self.questions_dict = self.decision_tree.questions

        self._build_styles()
        self._build_layout()
        self._load_question()

    # styling
    def _build_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")

        # frame
        style.configure("Card.TFrame", background="#ffffff",
                         relief="flat", borderwidth=0)
        style.configure("BG.TFrame", background="#f0f4f8")

        # labels
        style.configure("Header.TLabel",
                         background="#1a2a4a", foreground="#ffffff",
                         font=("Georgia", 18, "bold"), anchor="center")
        style.configure("Sub.TLabel",
                         background="#1a2a4a", foreground="#a8c4e0",
                         font=("Georgia", 10), anchor="center")
        style.configure("QNum.TLabel",
                         background="#ffffff", foreground="#6b7280",
                         font=("Helvetica", 11))
        style.configure("Question.TLabel",
                         background="#ffffff", foreground="#1a2a4a",
                         font=("Georgia", 14), wraplength=620,
                         justify="left")
        style.configure("Score.TLabel",
                         background="#f0f4f8", foreground="#1a2a4a",
                         font=("Helvetica", 13, "bold"))
        style.configure("Diff.TLabel",
                         background="#ffffff", foreground="#9ca3af",
                         font=("Helvetica", 10, "italic"))
        style.configure("Result.TLabel",
                         background="#f0f4f8", foreground="#1a2a4a",
                         font=("Georgia", 26, "bold"), anchor="center")
        style.configure("ResultSub.TLabel",
                         background="#f0f4f8", foreground="#4b5563",
                         font=("Helvetica", 13), anchor="center")

        # buttons
        style.configure("Submit.TButton",
                         background="#2563eb", foreground="#ffffff",
                         font=("Helvetica", 12, "bold"),
                         padding=(20, 10), relief="flat")
        style.map("Submit.TButton",
                  background=[("active", "#1d4ed8"), ("disabled", "#93c5fd")],
                  foreground=[("disabled", "#ffffff")])

        style.configure("Quit.TButton",
                         background="#e5e7eb", foreground="#374151",
                         font=("Helvetica", 10), padding=(10, 6), relief="flat")
        style.map("Quit.TButton",
                  background=[("active", "#d1d5db")])

        style.configure("Restart.TButton",
                         background="#059669", foreground="#ffffff",
                         font=("Helvetica", 12, "bold"),
                         padding=(20, 10), relief="flat")
        style.map("Restart.TButton",
                  background=[("active", "#047857")])

    # layout
    def _build_layout(self):
        # header
        self.header_frame = tk.Frame(self.root, bg="#1a2a4a", height=80)
        self.header_frame.pack(fill="x")
        self.header_frame.pack_propagate(False)

        tk.Label(self.header_frame, text="Cognitive Evaluator",
                 bg="#1a2a4a", fg="#ffffff",
                 font=("Georgia", 20, "bold")).pack(pady=(16, 0))
        tk.Label(self.header_frame, text="Test your knowledge — answer wisely",
                 bg="#1a2a4a", fg="#a8c4e0",
                 font=("Helvetica", 9)).pack()

        # main content
        self.content_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=20)

        # score bar
        score_bar = tk.Frame(self.content_frame, bg="#f0f4f8")
        score_bar.pack(fill="x", pady=(0, 12))

        self.score_label = tk.Label(score_bar, text="Score: 0",
                                     bg="#f0f4f8", fg="#1a2a4a",
                                     font=("Helvetica", 13, "bold"))
        self.score_label.pack(side="left")

        self.progress_label = tk.Label(score_bar, text="Question 1 of 10",
                                        bg="#f0f4f8", fg="#6b7280",
                                        font=("Helvetica", 11))
        self.progress_label.pack(side="right")

        # progress bar
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(self.content_frame,
                                             variable=self.progress_var,
                                             maximum=self.max_questions,
                                             length=720, mode="determinate")
        self.progress_bar.pack(fill="x", pady=(0, 16))

        # question card
        self.card = tk.Frame(self.content_frame, bg="#ffffff",
                              relief="flat", bd=0,
                              highlightthickness=1,
                              highlightbackground="#e5e7eb")
        self.card.pack(fill="x")

        card_inner = tk.Frame(self.card, bg="#ffffff")
        card_inner.pack(fill="both", padx=24, pady=20)

        # question metadata
        meta_row = tk.Frame(card_inner, bg="#ffffff")
        meta_row.pack(fill="x", pady=(0, 10))

        self.question_number_label = tk.Label(meta_row,
                                               text="Question 1",
                                               bg="#ffffff", fg="#6b7280",
                                               font=("Helvetica", 11))
        self.question_number_label.pack(side="left")

        self.difficulty_label = tk.Label(meta_row, text="",
                                          bg="#ffffff", fg="#9ca3af",
                                          font=("Helvetica", 10, "italic"))
        self.difficulty_label.pack(side="right")

        tk.Frame(card_inner, bg="#e5e7eb", height=1).pack(fill="x", pady=(0, 14))

        # question text
        self.question_label = tk.Label(card_inner, text="",
                                        bg="#ffffff", fg="#1a2a4a",
                                        font=("Georgia", 14),
                                        wraplength=620, justify="left",
                                        anchor="w")
        self.question_label.pack(fill="x", pady=(0, 20))

        # answer
        entry_frame = tk.Frame(card_inner, bg="#ffffff")
        entry_frame.pack(fill="x", pady=(0, 6))

        tk.Label(entry_frame, text="Your answer:",
                 bg="#ffffff", fg="#374151",
                 font=("Helvetica", 11)).pack(anchor="w", pady=(0, 6))

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(entry_frame,
                                     textvariable=self.answer_var,
                                     font=("Helvetica", 13),
                                     relief="solid", bd=1,
                                     fg="#1a2a4a", bg="#f9fafb",
                                     insertbackground="#2563eb")
        self.answer_entry.pack(fill="x", ipady=8)
        self.answer_entry.bind("<Return>", lambda e: self._submit())

        # feedback label
        self.feedback_label = tk.Label(card_inner, text="",
                                        bg="#ffffff",
                                        font=("Helvetica", 11, "bold"),
                                        anchor="w")
        self.feedback_label.pack(fill="x", pady=(8, 0))

        btn_row = tk.Frame(self.content_frame, bg="#f0f4f8")
        btn_row.pack(fill="x", pady=(16, 0))

        ttk.Button(btn_row, text="Quit", style="Quit.TButton",
                   command=self._confirm_quit).pack(side="right", padx=(8, 0))

        self.submit_btn = ttk.Button(btn_row, text="Submit Answer",
                                      style="Submit.TButton",
                                      command=self._submit)
        self.submit_btn.pack(side="right")

    # game logic
    def _load_question(self):
        """Populate all widgets with the current question data."""
        questions = self.questions_dict

        if (self.current_question_id not in questions
                or self.questions_answered >= self.max_questions):
            self._show_results()
            return

        q = questions[self.current_question_id]
        num = self.questions_answered + 1

        self.question_number_label.config(text=f"Question {num}")
        self.progress_label.config(text=f"Question {num} of {self.max_questions}")
        self.difficulty_label.config(
            text=f"Difficulty: {q.get('difficulty', 'unknown').capitalize()}")
        self.question_label.config(text=q["question"])
        self.feedback_label.config(text="", bg="#ffffff")
        self.answer_var.set("")
        self.answer_entry.config(state="normal")
        self.submit_btn.config(state="normal")
        self.progress_var.set(self.questions_answered)
        self.answer_entry.focus()

    def _submit(self):
        """Evaluate the submitted answer."""
        raw = self.answer_var.get().strip()
        if not raw:
            messagebox.showwarning("No answer",
                                   "Please type an answer before submitting.")
            return

        questions = self.questions_dict
        q = questions[self.current_question_id]
        correct = raw.lower() == q["answer"].lower()

        if correct:
            self.score += 1
            self.feedback_label.config(
                text=f"  Correct!  The answer is {q['answer']}.",
                fg="#059669", bg="#f0fdf4")
        else:
            self.feedback_label.config(
                text=f"  Incorrect.  The correct answer is {q['answer']}.",
                fg="#dc2626", bg="#fef2f2")

        self.score_label.config(text=f"Score: {self.score}")
        self.answer_entry.config(state="disabled")
        self.submit_btn.config(state="disabled")

        next_id = self.decision_tree.get_next_question(
            self.current_question_id, raw)
        self.current_question_id = next_id
        self.questions_answered += 1
        self.progress_var.set(self.questions_answered)

        # short delay
        self.root.after(1400, self._load_question)

    def _show_results(self):
        """Replace the content area with a results screen."""
        self.progress_bar.pack_forget()
        self.card.pack_forget()

        # clear frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        pct = int((self.score / self.max_questions) * 100)
        grade, colour, fill = self._grade(pct)

        # results
        res_card = tk.Frame(self.content_frame, bg="#ffffff",
                             highlightthickness=1,
                             highlightbackground="#e5e7eb")
        res_card.pack(fill="both", expand=True, pady=10)

        inner = tk.Frame(res_card, bg="#ffffff")
        inner.pack(expand=True, pady=30, padx=40)

        tk.Label(inner, text="Quiz Complete!",
                 bg="#ffffff", fg="#1a2a4a",
                 font=("Georgia", 22, "bold")).pack(pady=(0, 6))

        tk.Label(inner, text=f"{self.score} / {self.max_questions} correct",
                 bg="#ffffff", fg="#6b7280",
                 font=("Helvetica", 13)).pack(pady=(0, 20))

        # score circle
        canvas = tk.Canvas(inner, width=130, height=130,
                            bg="#ffffff", highlightthickness=0)
        canvas.pack(pady=(0, 16))
        canvas.create_oval(10, 10, 120, 120, outline=colour,
                            fill=fill, width=5)
        canvas.create_text(65, 58, text=f"{pct}%",
                            font=("Georgia", 22, "bold"), fill=colour)
        canvas.create_text(65, 84, text="score",
                            font=("Helvetica", 10), fill="#9ca3af")

        tk.Label(inner, text=grade,
                 bg="#ffffff", fg=colour,
                 font=("Georgia", 16, "bold")).pack(pady=(0, 24))

        btn_row = tk.Frame(inner, bg="#ffffff")
        btn_row.pack()

        ttk.Button(btn_row, text="Play Again",
                   style="Restart.TButton",
                   command=self._restart).pack(side="left", padx=6)
        ttk.Button(btn_row, text="Quit",
                   style="Quit.TButton",
                   command=self.root.destroy).pack(side="left", padx=6)

    def _grade(self, pct):
        if pct == 100:
            return "Perfect Score — Outstanding!", "#059669", "#d1fae5"
        elif pct >= 80:
            return "Excellent performance", "#2563eb", "#dbeafe"
        elif pct >= 60:
            return "Good — keep practising!", "#d97706", "#fef3c7"
        elif pct >= 40:
            return "Fair — room to improve", "#ea580c", "#ffedd5"
        else:
            return "Keep trying — you can do it!", "#dc2626", "#fee2e2"

    def _restart(self):
        """Reset state and restart the quiz."""
        self.current_question_id = "1"
        self.score = 0
        self.questions_answered = 0
        self.questions_dict = self.decision_tree.questions

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self._build_layout()
        self._load_question()

    def _confirm_quit(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()
