from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #question_bank.append(Question(question['text'], question['answer'])) # My initial way but unsure if it's really correct

    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")


