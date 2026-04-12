import json


class DecisionTree:
    def __init__(self, knowledge_base_file):
        with open(knowledge_base_file, 'r') as f:
            self.knowledge_base = json.load(f)
        # Store as a dict keyed by question id for string-based lookup
        self.questions = {
            q["id"]: q for q in self.knowledge_base["questions"]
        }
        self.score = 0
        
        self.max_questions = len(self.questions)
        
    def update_score(self, question, correct):
        """
        Updates the score based on whether the answer is correct or not.
        """
        if not correct:
            return
        
        if question["difficulty"] == "easy":
            self.score += 1
        elif question["difficulty"] == "medium":
            self.score += 2
        elif question["difficulty"] == "hard":
            self.score += 3

    def get_next_question(self, question_id, answer):
        """
        Computes and fetches the next question based on a correct or incorrect answer.
        """
        question = self.questions[question_id]
        
        correct = answer.strip().lower() == question["answer"].strip().lower()
        
        # update score
        self.update_score(question, correct)
        
        if correct:
            return question["correct_next"]
        else:
            return question["incorrect_next"]
        
    def get_score(self):
        """
        Returns the current score.
        """
        return self.score
    
    def get_result(self):
        """
        Returns the final result based on the score.
        """
        if self.score < 3:
            return "Low cognitive ability"
        elif self.score < 6:
            return "Average cognitive ability"
        else:
            return "High cognitive ability"