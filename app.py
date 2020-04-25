##################################################
## Author: {Sayantan Biswas}
## Maintainer: {Sayantan Biswas}
## Email: {sayantanbiswas1002@gmail.com}
##################################################

from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_event', methods=['POST'])
def add_event():
    summary = request.form['summary']
    date = request.form['date']
    start_time = request.form['start']
    end_time = request.form['end']
    #num = request.form['num']
    email1 = request.form['invite1']
    email2 = request.form['invite2']
    email3 = request.form['invite3']
    # email4 = request.form['invite4']
    # email5 = request.form['invite5']
    description = request.form['description']
    location = request.form['location']

    response = (util.add_event(summary,date,start_time,end_time,email1,email2,email3,description,location))

    return render_template('index.html', result_text=response)

if __name__ =="__main__":
    print("Starting python Flask server...")
    app.run(debug=True)
