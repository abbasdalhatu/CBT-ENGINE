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
    Question(5, "Which Flask method is used to render an HTML template?", ["return_template", "render_file", "render_template", "show_html"], "render_template")
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
        if request.method == 'POST':
             # The queue is decreased, but current_num logic remains valid for display since current_question is popped
             pass
        else:
             pass 
        # Slightly more robust calculation
        current_num = engine.total_questions - len(engine.question_queue)
        
        return render_template(
            'question.html', 
            question=engine.current_question, 
            current_num=current_num, 
            total_num=engine.total_questions
        )
    else:
        # No more questions, finish the test
        engine.finish_test()
        return redirect(url_for('result'))

@app.route('/result')
def result():
    if not engine.end_time: # Test hasn't finished properly
        return redirect(url_for('home'))
        
    return render_template(
        'result.html', 
        score=engine.score, 
        total=engine.total_questions, 
        completion_time=engine.end_time
    )

if __name__ == '__main__':
    app.run(debug=True)
