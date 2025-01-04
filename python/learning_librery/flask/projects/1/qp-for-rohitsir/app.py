from flask import Flask, request, render_template
import pandas as pd

data = pd.read_csv('question.csv')
data = pd.DataFrame(data)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)










question_paper/
├── app.py
├── templates/
│   ├── index.html
│   ├── admin.html
│   ├── result.html
│   └── question_paper.html
├── static/
├── models.py
├── forms.py
├── database.db
