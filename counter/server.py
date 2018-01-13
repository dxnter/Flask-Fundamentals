from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'DannyFoster'
app.count = 0

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html', counter = session['counter'])

app.run(debug=True)