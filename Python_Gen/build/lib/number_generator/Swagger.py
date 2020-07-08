
# Implementing the three service in swagger and exposing as a service

from flask import Flask
from flask_restplus import Api, Resource, reqparse
from fib import fibonacci_optimised
from fib import fibonacci
from ackermann_func import ackermann
from factorial_func import factorial_optimised
import timeit
from functools import partial
from matplotlib import pyplot

flask_app = Flask(__name__)
api = Api(app=flask_app)

fibonacci_ns = api.namespace('Fibonacci_API', description="Fibonacci series will be calculated for the Input Number")
factorials_ns = api.namespace('Factorials_API', description="Factorial will be calculated for provided Input Number")
Ackermann_ns = api.namespace('Ackermann_API', description="Ackermann Calculations for 2 numbers provided")
dashboard_ns = api.namespace('Efficiency Dashboard',
                             description="Compare the efficiency of naive and effieicent approach for factorial")

single_number_parser = reqparse.RequestParser()
single_number_parser.add_argument('Number', type=int, required=True, help='Integers Only')

two_number_parser = reqparse.RequestParser()
two_number_parser.add_argument('M', type=int, required=True, help='Integers Only')
two_number_parser.add_argument('N', type=int, required=True, help='Integers Only')


@fibonacci_ns.route("/fibonacci")
@fibonacci_ns.expect(single_number_parser)
class MainClass(Resource):
    def get(self):
        n = single_number_parser.parse_args()['Number']
        try:
            return fibonacci_optimised(n)
        except ValueError:
            return "Please Enter a positive Integer Value > 0"
        except Exception as e:
            return str(e)


@factorials_ns.route("/Factorial")
@fibonacci_ns.expect(single_number_parser)
class MainClass(Resource):
    def get(self):
        n = single_number_parser.parse_args()['Number']
        try:
            return factorial_optimised(n)
        except ValueError:
            return "Please Enter a positive Integer Value > 0"
        except Exception as e:
            return str(e)


@Ackermann_ns.route("/Ackermann")
@Ackermann_ns.expect(two_number_parser)
class MainClass(Resource):
    def get(self):
        args = two_number_parser.parse_args()
        m = args['M']
        n = args['N']
        print(m)
        print(n)
        try:
            return ackermann(m, n)
        except ValueError:
            return "Please Enter a positive Integer Value > 0"
        except Exception as e:
            return str(e)
        return str(m) + '&' + str(n)


flask_app.run()