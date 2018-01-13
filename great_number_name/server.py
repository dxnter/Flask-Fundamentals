import os, random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['POST', 'GET'])
def index():
    session['number'] = random.randrange(0, 101)
    print session['number']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def result():
    if int(request.form['guess']) == session['number']:
        answer = "Correct"
        return render_template("index.html", answer = answer)
    elif int(request.form['guess']) < session['number']:
        answer = "Too Low"
        return render_template("index.html", answer = answer)
    else:
        answer = "Too High"
        return render_template("index.html", answer = answer)

app.run(debug=True)

app.run(debug=True)