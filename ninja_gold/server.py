import random, time
from flask import Flask, render_template, redirect, request, Markup, session
app = Flask(__name__)
app.secret_key = 'Dojo'

@app.route('/', methods=['POST', 'GET'])
def index():
    session['gold'] = 0
    print session['gold']
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    message = ''
    if 'farm' in request.form: 
        amount = random.randint(10,20)
        session['gold'] += amount
    elif 'cave' in request.form:
        amount = random.randint(5,10)
        session['gold'] += amount
    elif 'house' in request.form:
        amount = random.randint(2,5)
        session['gold'] += amount
    elif 'casino' in request.form:
        amount = random.randint(0,50)
        chance = random.choice([0,1])
        if chance == 0:
            session['gold'] += amount
        elif chance == 1:
            session['gold'] -= amount
    return render_template('index.html', gold=session['gold'], amount=amount, message=message)

app.run(debug=True)
