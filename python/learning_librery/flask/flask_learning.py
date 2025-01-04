from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# CSV file se data read karna
data = pd.read_csv('data.csv')
# Flask route
@app.route('/', methods=['POST', 'GET'])
def index():
    data_convert_into_dict = data.to_dict(orient='records')

    if request.method=='POST':
        ID = request.form['ID']
        passw = request.form['pass']
        data.loc[len(data)] = [ID,passw]
        data.to_csv('data.csv', index=False)
    return render_template("index.html", data=data_convert_into_dict)

@app.route('/data')
def get_data():
    # Data ko response me bhejna
    return data.to_html()  # Pandas DataFrame ko HTML table me convert karna

if __name__ == '__main__':
    app.run(debug=True, port=8000)
  