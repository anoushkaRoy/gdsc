# quiz.py

from random import shuffle
from question import Question
from questions import questions

class Quiz:
    def __init__(self):
        self.questions = [Question(q["question_text"], q["answer"]) for q in questions]
        self.score = 0
        self.current_question_index = 0

    def shuffle_questions(self):
        shuffle(self.questions)

    def next_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index].question_text
        else:
            return None

    def check_answer(self, user_answer):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            if question.check_answer(user_answer):
                self.score += 2  # Increment the score by 2 for a correct answer
            else:
                self.score -= 1  # Decrement the score by 1 for an incorrect answer
            self.current_question_index += 1
            return True
        else:
            return False

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def get_score(self):
        return self.score
