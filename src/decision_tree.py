import json

class DecisionTree:
    def __init__(self, knowledge_base_file):
        self.knowledge_base_file = knowledge_base_file
        self.knowledge_base = json.load(open(knowledge_base_file))
        self.questions = self.knowledge_base["questions"]

    def get_next_question(self, question_id, answer):
        """
        Computes and fetches the next question based on a correct or incorrect answer.
        """
        question = self.questions[question_id]
        if answer == question["answer"]:
            return question["correct_next"]
        else:
            return question["incorrect_next"]
    