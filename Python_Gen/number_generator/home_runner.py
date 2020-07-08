# Runner class to call the methods and run as a service

import flask
from flask import Flask
from flask import request, render_template

from ackermann_func import ackermann
from factorial_func import factorial_optimised
from fib import fibonacci_optimised

app = Flask(__name__)


# HTML form for user input
@app.route('/ackermann')
def my_form():
    return render_template('ackermann_input.html')


@app.route('/ackermann', methods=['POST'])
def my_form_post():
    fnum1 = request.form['fnum']
    fnum2 = request.form['lnum']
    return str(ackermann(fnum1, fnum2))


@app.route('/nfactorial')
def my_form1():
    return render_template('factorial_input.html')


@app.route('/nfactorial', methods=['POST'])
def my_form_post1():
    text = request.form['text']
    return str(factorial_optimised(text))


@app.route('/fibonacci')
def my_form2():
    return flask.render_template('fib_input.html')


@app.route('/fibonacci', methods=['POST'])
def my_form_post2():
    text = flask.request.form['text']
    print(type(text))
    return str(fibonacci_optimised(text))


if __name__ == "__main__":
    app.run(debug=False)
