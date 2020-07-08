
Version 1.0 - Wed 08 July 2020

Description 
------------

This service is based on Flask framework.
There are three functions whose outputs are to be caluclated.
The Fibonacci sequence generation, where it accepts a input number n and return the Fibonacci number.
The Factorial generation of a number based on user input.
Implementation of Ackermann function based on m and n integer values
The Package has 1 main runner program and has 2 optional implementations. One is swagger implementation of the above three functions and the other is an efficiency program to check performance of two functions

Requirements
------------
1. Python 3.6 or higher version
2. Flask version 1.0.0 or greater for Flask installation 
3. matplotlib3.0.0 or higher

Instruction 
-----------
This project includes the following files:
> home_runner.py
runs the flask application for the three functions

> fib.py
Generate N Fibonacci Numbers, N is a positive integer
 
> factorial_func.py
Generate factorial for N positive integer

> Ackermann_func.py
Generate Ackermann number for M and N positive integer

> efficiency-db.py
Compares the performance of 2 fibonacci functions and displays the graph with comparison 

> Swagger.py
Independent Swagger implementation of the three services


Instructions:

Once the project structure is copied to a location:

1. Run home_runner.py
-----------------
launch your Command Prompt to this directory. Then type the following command :

python home_runner.py
* Running on http://127.0.0.1:5000/

Now you can test out the service by hitting the below URL's from browser
http://127.0.0.1:5000/fibonacci
http://127.0.0.1:5000/nfactorial
http://127.0.0.1:5000/ackermann


You will get a User input page to enter valid number based on the endpoint called:


2. Compare the efficiency of two programs and display in dashboard
-------------------------------
in the project directory, run the below command:
python efficiency-db.py
Now you can test out the service by hitting the below URL's from browser:
http://127.0.0.1:5000/efficiency

You will get a User input page to enter numbers.
Based on the inputs a graph will be generated on an HTML page

The implementation is for fibonnaci numbers and has 2 approach:
1. The naive implementation using recursion
2. The memorisation approach for recursion which caches the values.

-----------------------------------------------------------------------
For all end points given a negative number or other illegal input, it will respond with an 
appropriate error.

3. Swagger Implementation:
=====================================================

I have implemented an additioanl Swagger implementation for the three functions and can be deployed by entering the below command:
python Swagger.py
Now you can test out the service by hitting the below URL's from browser:
http://127.0.0.1:5000/


