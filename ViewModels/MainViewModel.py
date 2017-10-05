from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
from math import exp
import getopt
import sys
try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:e:", ["help", "file=", "expression="])
except getopt.GetoptError as err:
	print(err)
	sys.exit(2)
for o, a in opts:
	if o in ('-h', '--help'):
		print("""
-h or --help\tDisplay this message
-f or --filename\tName of the file with expression as input
-e or --expression\tExpression to parse
and - Conjunction
or  - Disjunction
->  - Implicatio
=   - Equality
not - Inversion
			""")
		sys.exit(0)
	elif o in ('-f', '--file'):
		expr = " " + open(a, 'r').read()
	elif o in ('-e', '--epression'):
		expr = " " + a
	else:
		assert False, "unhandled option"

def f(x, y):
	return x ** 2 - 2 * y

def AnaliticalSolution(x):
	return exp(-2 * x) * 3 / 4 + x ** 2 / 2 - x / 2 + 1 / 4

def EulerMethod(y0, xs, f):
	ys = [0] * n
	ys[0] = y0
	for i in range(1, len(ys)):
		ys[i] = ys[i - 1] + (xs[i] - xs[i - 1]) * f(xs[i - 1], ys[i - 1])
	return ys

def ImprovedEulerMethod(y0, xs, f):
	ys = [0] * n
	ys[0] = y0
	for i in range(1, len(ys)):
		h = xs[i] - xs[i - 1]
		deltaY = h * f(xs[i - 1] + h / 2, ys[i - 1] + h / 2 * f(xs[i - 1], ys[i - 1]))
		ys[i] = ys[i - 1] + deltaY
	return ys

def RungeKuttaMethod(y0, xs, f):
	ys = [0] * n
	ys[0] = y0
	for i in range(0, len(ys) - 1):
		h = xs[i + 1] - xs[i]
		k1 = f(xs[i], ys[i])
		k2 = f(xs[i] + h / 2, ys[i] + k1 * h / 2)
		k3 = f(xs[i] + h / 2, ys[i] + k2 * h / 2)
		k4 = f(xs[i] + h, ys[i] + h * k3)
		ys[i + 1] = ys[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
	return ys

def CorrectedEulerMethod(y0, xs, f):
	ys = [0] * n
	ys[0] = y0
	for i in range(1, len(ys)):
		h = xs[i] - xs[i - 1]
		k1 = f(xs[i - 1], ys[i - 1]) * h
		k2 = f(xs[i - 1] + h, ys[i - 1] + k1) * h
		deltaY = (k1 + k2) / 2
		ys[i] = ys[i - 1] + deltaY
	return ys	

