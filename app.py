from flask import Flask, render_template, request, redirect, url_for
from engine import TestEngine, Question

app = Flask(__name__)
# We use a global engine instance for this simple, single-user demonstration.
# In a real app with multiple users, we'd use session storage or a database.
engine = TestEngine()

# Sample questions for the test
SAMPLE_QUESTIONS = [
    Question(1, "What keyword is used to define a function in Python?", ["func", "def", "lambda", "function"], "def"),
    Question(2, "Which data structure in Python is mutable and uses square brackets?", ["Tuple", "Dictionary", "Set", "List"], "List"),
    Question(3, "What module gives us access to current dates and times in Python standard library?", ["time", "datetime", "calendar", "moment"], "datetime"),
    Question(4, "In Object-Oriented Programming, what refers to bundling data and methods that work on that data within one unit?", ["Inheritance", "Polymorphism", "Encapsulation", "Abstraction"], "Encapsulation"),
    Question(5, "Which Flask method is used to render an HTML template?", ["return_template", "render_file", "render_template", "show_html"], "render_template"),
    Question(6, "Which of the following is NOT a core data type in Python?", ["Class", "Dictionary", "Tuple", "List"], "Class"),
    Question(7, "What is the output of `print(2 ** 3)`?", ["5", "6", "8", "9"], "8"),
    Question(8, "How do you start a comment in Python?", ["//", "/*", "<!--", "#"], "#"),
    Question(9, "Which of the following is used to handle exceptions in Python?", ["try/except", "catch/throw", "handle/error", "try/catch"], "try/except"),
    Question(10, "What is the purpose of the `__init__` method in a Python class?", ["It initializes the class properties", "It runs when the object is deleted", "It creates a new class", "It prints the object"], "It initializes the class properties")
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Re-initialize engine and load questions for a new session
        global engine
        engine = TestEngine()
        engine.load_questions(SAMPLE_QUESTIONS)
        
        # Load the first question
        engine.get_next_question()
        return redirect(url_for('question'))
        
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    try:
        if not engine.current_question and not engine.question_queue:
            return redirect(url_for('home'))

        if request.method == 'POST':
            user_answer = request.form.get('answer')
            if user_answer:
                engine.check_answer(user_answer)
                # Advance to the next question
                engine.get_next_question()

        if engine.current_question:
            # Calculate current question number for the UI
            current_num = engine.total_questions - len(engine.question_queue)
            # Pre-calculate progress percentage for the progress bar
            progress_percent = (current_num / engine.total_questions * 100) if engine.total_questions > 0 else 0
            
            return render_template(
                'question.html', 
                question=engine.current_question, 
                current_num=current_num, 
                total_num=engine.total_questions,
                progress_percent=progress_percent
            )
        else:
            # No more questions, finish the test
            engine.finish_test()
            return redirect(url_for('result'))
    except Exception as e:
        print(f"Error in /question: {e}")
        return f"Internal Server Error: {e}", 500

@app.route('/result')
def result():
    try:
        if not engine.end_time: # Test hasn't finished properly
            return redirect(url_for('home'))
        
        # Pre-calculate score percentage for the UI
        score_percent = (engine.score / engine.total_questions * 100) if engine.total_questions > 0 else 0
            
        return render_template(
            'result.html', 
            score=engine.score, 
            total=engine.total_questions, 
            completion_time=engine.end_time,
            score_percent=round(score_percent, 1)
        )
    except Exception as e:
        print(f"Error in /result: {e}")
        return f"Internal Server Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
