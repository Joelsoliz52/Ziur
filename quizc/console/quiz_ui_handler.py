from quizc.console.quiz_input_handler import QuestionInputHandler
from quizc.console.quiz_ui_menu import QuizUIMenu
from quizc.model.quiz import Quiz
from quizc.model.quiz_answers import QuizAnswer, Answer
from json import JSONEncoder

class MyClass:
    def __init__(self, value):
        self.value = value


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class QuizUIHandler(object):


    @staticmethod
    def create_quiz() -> Quiz:
        menu = QuizUIMenu()
        return menu.handle_create_quiz()

    @staticmethod
    def fill_quiz(quiz) -> QuizAnswer:
        quiz_answer = QuizAnswer(quiz)
        question_handler = QuestionInputHandler()
        print("Quiz:" + quiz.title)
        for question in quiz.questions:
            answers = question_handler.ask_question_value(question)
            answer = Answer(question, answers)
            quiz_answer.add_answer(answer)

        return quiz_answer

        myclass = MyClass(quiz_answer)
        json = MyEncoder().encode(myclass)
        f = open("myform.json", "w")
        f.write(json)
        f.close()

    @staticmethod
    def show_quiz(quiz_answer):
        print(quiz_answer.quiz.title)
        print("=============================================")
        for answer in quiz_answer.answers:
            print(answer)


        return quiz_answer
