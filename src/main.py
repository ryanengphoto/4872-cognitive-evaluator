import json
from gui import GUI
from decision_tree import DecisionTree
import tkinter as tk

knowledge_base_file = "knowledge_base.json"

def main():
    tree = DecisionTree(knowledge_base_file)
    root = tk.Tk()
    gui = GUI(root, tree)
    gui.run()

if __name__ == "__main__":
    main()
