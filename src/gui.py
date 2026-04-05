import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from decision_tree import DecisionTree

class GUI:
    def __init__(self, root, tree):
        self.decision_tree = tree
        self.root = root
        self.root.title("Cognitive Evaluator")
        self.root.geometry("800x600")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.root.geometry("800x600")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid();
        self.widgets()

    def widgets(self):
        """
        Creates all the widgets for the gui.
        """
        """
        self.question_number =
        self.question = 
        self.answer_box =
        self.submit =
        self.score =
        self.final_score =
        """
        self.quit = ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=0);

    def run(self):
        """
        Runs the main loop of the gui.
        """
        self.root.mainloop()