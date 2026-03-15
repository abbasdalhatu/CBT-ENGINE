# Mini CBT Engine

A lightweight, premium Computer Based Test (CBT) engine built with Flask.

## Features
- **Premium UI**: Modern glassmorphism design with smooth transitions and animated backgrounds.
- **Dynamic Assessment**: Randomized questions and options for every session.
- **Timer & Progress**: Real-time duration tracking and animated progress bars.
- **Performance Feedback**: Score-based personalized messages on the results page.
- **Score History**: Persistent local tracking of previous attempts using `localStorage`.
- **Accessibility**: Keyboard shortcuts (Keys 1-4) for quick option selection.
- **Skip Logic**: Move difficult questions to the end of the queue for later review.

## Setup & Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`
3. Open `http://127.0.0.1:5000` in your browser.

## Project Structure
- `app.py`: Flask web application and routes.
- `engine.py`: Contains OOP logic (`TestEngine` and `Question` classes).
- `questions.json`: Externalized question repository.
- `templates/`: Jinja2 templates for index, question, and result pages.
