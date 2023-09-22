class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text  # This stores the text of the question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer
