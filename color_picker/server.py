from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    return render_template('index.html',red=red,green=green,blue=blue)

app.run(debug=True)