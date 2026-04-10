import json


class DecisionTree:
    def __init__(self, knowledge_base_file):
        self.knowledge_base_file = knowledge_base_file
        self.knowledge_base = json.load(open(knowledge_base_file))
        # Store as a dict keyed by question id for string-based lookup
        self.questions = {
            q["id"]: q for q in self.knowledge_base["questions"]
        }

    def get_next_question(self, question_id, answer):
        """
        Computes and fetches the next question based on a correct or incorrect answer.
        """
        question = self.questions[question_id]
        if answer.strip().lower() == question["answer"].strip().lower():
            return question["correct_next"]
        else:
            return question["incorrect_next"]