from flask import Flask, render_template, send_from_directory, url_for, request
import os
import datetime
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Directory to save generated files
OUTPUT_DIR = 'templates/DPPs/htmls'
OUTPUT_DIR_CSV = 'templates/DPPs/csvs'
OUTPUT_DIR_CSV_question = 'templates/DPPs/csvs'
CSV_FILE = 'data/paper_file_path.csv'

# Create directories and initialize CSV if not exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=['file_name']).to_csv(CSV_FILE, index=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")


@app.route('/create_paper', methods=['POST'])
def create_paper():
    file_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated File</title>
    </head>
    <body>
        <h1>Hello</h1>
    </body>
    </html>
    '''
    file_content_csv = '''id,question,option-a,option-b,option-c,option-d,answer'''

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'hello_{timestamp}.html'
    file_path = os.path.join(OUTPUT_DIR, file_name)
    file_name_csv = f'hello_{timestamp}.csv'
    file_path_csv = os.path.join(OUTPUT_DIR_CSV, file_name_csv)

    # Create HTML file
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    # Create CSV file
    with open(file_path_csv, 'w') as file:
        file.write(file_content_csv)

    # Read existing CSV and append new data
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=['file_name', 'csv_file_name'])

    # Create a new row with file paths
    new_row = pd.DataFrame({'file_name': [file_path], 'csv_file_name': [file_path_csv]})
    
    # Append the new row to the DataFrame
    updated_df = pd.concat([df, new_row], ignore_index=True)

    # Save the updated DataFrame to CSV
    updated_df.to_csv(CSV_FILE, index=False)

    return render_template('input_paper.html')

@app.route('/show_paper', methods=['POST'])
def show_paper():
    paper_path_data = pd.read_csv(CSV_FILE)
    data = pd.DataFrame(paper_path_data)
    data = data['file_name']
    print(data)
    data_convert_into_dict = data.to_dict(orient='records')
    return render_template('show_paper.html', data=data_convert_into_dict)

@app.route('/input_paper', methods=['GET', 'POST'])
def input_paper():

    data = pd.read_csv('data/paper_file_path.csv')

    data = pd.DataFrame(data)
    data_last_line = data['csv_file_name'].tail(1)
    data_last_index = data.index[-1]
    data = data_last_line.to_dict()
    path_data = data[data_last_index]

    if request.method == 'POST':
        # Form inputs ko fetch karna
        question_text = request.form.get('question_text')
        option_a = request.form.get('option_a')
        option_b = request.form.get('option_b')
        option_c = request.form.get('option_c')
        option_d = request.form.get('option_d')
        correct_answer = request.form.get('correct_answer')

        # Naya row prepare karna
        new_row = pd.DataFrame([{
            'id': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
            'question': question_text,
            'option-a': option_a,
            'option-b': option_b,
            'option-c': option_c,
            'option-d': option_d,
            'answer': correct_answer
        }])

        # Existing data ko load karke append karna
        existing_data = pd.read_csv(path_data)
        updated_data = pd.concat([existing_data, new_row], ignore_index=True)

        # Updated data ko save karna
        updated_data.to_csv(path_data, index=False)

        return render_template('input_paper.html', message="Question added successfully!")

    return render_template('input_paper.html')



if __name__ == '__main__':
    app.run(debug=True)      