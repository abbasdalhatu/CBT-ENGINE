import collections
from datetime import datetime

class Question:
    def __init__(self, id, text, options, answer):
        """
        Encapsulates a single test question.
        options is a list of strings.
        answer is the correct option string.
        """
        self.id = id
        self.text = text
        self.options = options
        self.answer = answer

class TestEngine:
    def __init__(self):
        self.question_queue = collections.deque()
        self.score = 0
        self.total_questions = 0
        self.start_time = None
        self.end_time = None
        self.current_question = None

    def load_questions(self, questions_list):
        """
        Loads a list of Question objects into the queue.
        """
        for q in questions_list:
            self.question_queue.append(q)
        self.total_questions = len(self.question_queue)
        self.start_time = datetime.now()

    def get_next_question(self):
        """
        Retrieves the next question from the queue (FIFO).
        Returns None if the queue is empty.
        """
        if self.question_queue:
            self.current_question = self.question_queue.popleft()
            return self.current_question
        self.current_question = None
        return None

    def check_answer(self, user_answer):
        """
        Checks the user's answer against the current question's correct answer.
        Updates the score if correct.
        """
        if self.current_question and user_answer == self.current_question.answer:
            self.score += 1

    def finish_test(self):
        """
        Marks the end time of the test using datetime.now().
        """
        self.end_time = datetime.now()
