# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:09:05 2020

@author: anuj
"""

import timeit
from functools import partial
from matplotlib import pyplot
from fib import fibonacci_optimised
from fib import fibonacci
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True

app = Flask(__name__)


@app.route('/efficiency')
def my_form():
    return render_template('efficiency_input.html')


@app.route('/efficiency', methods=['POST'])
def my_form_post():
    fnum = request.form['min']
    lnum = request.form['max']

    if fnum.isdigit() & lnum.isdigit():
        m = int(fnum)
        n = int(lnum)
        if m < n:
            plotTC(fibonacci, m, n)
            plotTC(fibonacci_optimised, m, n)
            return render_template("image.html", image="C:/Users/anuj/PycharmProjects/number_generator/templates/image.png")
        else:
            return "Input Error! Second number should be greater than the first number"
    else:
        return "Input Error! Please input a positive integer number in both inputs"


# Run timer and plot time complexity
def plotTC(fn, nMin, nMax):
    x = []
    y = []

    color1 = [0, 0, 1]
    color2 = [1, 0, 0]

    for i in range(nMin, nMax):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=1)
        t = t * 10000
        x.append(i)
        y.append(t)

    pyplot.plot(x, y, 'o')
    pyplot.title("Efficient Vs Naive solution", fontsize=20)
    patch1 = pyplot.Rectangle((0, 0), 1, 1, fc=color1)
    patch2 = pyplot.Rectangle((0, 0), 1, 1, fc=color2)
    pyplot.legend([patch1, patch2], [r'Fibonacci', r'fibonacci_optimised'], loc='upper left')
    pyplot.xlabel("Input")
    pyplot.ylabel("Time")
    pyplot.tight_layout()
    pyplot.savefig("static/images/image.png")


if __name__ == "__main__":
    app.run(debug=True)
