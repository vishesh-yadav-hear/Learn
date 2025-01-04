from flask import Flask, render_template, redirect, url_for, request
import os
import pandas as pd
import datetime

app = Flask(__name__)

# Path to store the question papers
QUESTION_PAPER_FOLDER = 'data/questions'
if not os.path.exists(QUESTION_PAPER_FOLDER):
    os.makedirs(QUESTION_PAPER_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Get the form data
        question_text = request.form.get('question_text')
        option_a = request.form.get('option_a')
        option_b = request.form.get('option_b')
        option_c = request.form.get('option_c')
        option_d = request.form.get('option_d')
        correct_answer = request.form.get('correct_answer')

        # Create unique filename using current timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = f'questions_{timestamp}.csv'
        file_path = os.path.join(QUESTION_PAPER_FOLDER, file_name)

        # Save the question to a CSV file
        new_question = pd.DataFrame({
            'question_text': [question_text],
            'option_a': [option_a],
            'option_b': [option_b],
            'option_c': [option_c],
            'option_d': [option_d],
            'correct_answer': [correct_answer]
        })

        # If file exists, append the new question, else create new file
        if os.path.exists(file_path):
            new_question.to_csv(file_path, mode='a', header=False, index=False)
        else:
            new_question.to_csv(file_path, mode='w', header=True, index=False)

        # Return the unique file link
        return render_template('admin.html', file_link=url_for('serve_paper', file_name=file_name))

    return render_template('admin.html')

@app.route('/serve_paper/<file_name>')
def serve_paper(file_name):
    # Serve the question paper as a download link
    file_path = os.path.join(QUESTION_PAPER_FOLDER, file_name)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found!"
@app.route('/quiz/<file_name>', methods=['GET', 'POST'])
def quiz(file_name):
    # Your logic to serve the quiz
    
    file_path = os.path.join(QUESTION_PAPER_FOLDER, file_name)
    if os.path.exists(file_path):
        questions_df = pd.read_csv(file_path)
        if request.method == 'POST':
            score = 0
            for index, row in questions_df.iterrows():
                selected_answer = request.form.get(f"q{index}")
                if selected_answer == row['correct_answer']:
                    score += 1
                    
        return render_template('quiz.html', file_name=file_name)

    return "No question paper found!"

if __name__ == '__main__':
    app.run(debug=True)
