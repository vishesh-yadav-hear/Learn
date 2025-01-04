# for downloads


#@app.route('/download/<path:file_name>')
#def download_paper(file_name):
#    directory, filename = os.path.split(file_name)
#    return send_from_directory(directory, filename)
import pandas as pd
data = pd.read_csv('data/paper_file_path.csv')

data = pd.DataFrame(data)
data_last_line = data['csv_file_name'].tail(1)
data_last_index = data.index[-1]
data = data_last_line.to_dict()
data = data[data_last_index]
print(data)