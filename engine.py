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
    pass
