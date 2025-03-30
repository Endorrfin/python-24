class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        # return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # current_difficulty = self.question_list[self]
        self.question_number += 1
        user_answer = input(f"Level 🧠: {current_question.level}, \n"
                            f"Category 🔤: {current_question.category} \n"
                            f"🙋‍♂️🙋🏼‍♀️.{self.question_number}: {current_question.text}, \n"
                            f"Choose ⏳: (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅ You got it right!")
        else:
            print("❌ That's wrong")
        print(f"The correct answer was 🎯: {correct_answer}")
        print(f"You current score is: {self.score}/{self.question_number}")
        print("\n ⏭️")