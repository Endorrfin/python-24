from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    level = question["difficulty"]
    category = question["category"]
    new_question = Question(question_text, question_answer, level, category)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz 🤔")
print(f"You final score was 💡: {quiz.score}/{quiz.question_number}")