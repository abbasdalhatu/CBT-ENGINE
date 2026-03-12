# Mini CBT Engine

A simple Computer-Based Test (CBT) engine using Flask, demonstrating Object-Oriented Programming and Data Structures (Queue/FIFO).

## Prerequisites
- Python 3.6 or higher installed on your computer.

## Setup Instructions
1. Open your terminal or command prompt.
2. Navigate to the project directory where you downloaded/cloned the code.
3. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
5. Install Flask:
   ```bash
   pip install Flask
   ```

## Running the Application
1. In the terminal, ensure you are in the project folder (`CBT ENGINE`).
2. Run the application:
   ```bash
   python app.py
   ```
3. Open a web browser and go to `http://127.0.0.1:5000/`.
4. Click "Start Test" and answer the questions.

## Project Structure
- `app.py`: Flask web application and routes.
- `engine.py`: Contains OOP logic (`TestEngine` and `Question` classes).
- `templates/`: Contains HTML files (`index.html`, `question.html`, `result.html`).
