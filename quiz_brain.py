class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return current_question.text

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number - 1].answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        return False
