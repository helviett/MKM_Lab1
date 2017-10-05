from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
from math import exp
import getopt
import threading

def f(x, y):
	return x ** 2 - 2 * y

class Table():

	def __init__(self):
		self.rows = []

	def AddCols(self, cols):
		self.cols = map(str, cols)

	def AddRow(self, row):
		_row = map(str, row)
		self.rows.append(list(_row))

	def RowCount(self):
		return len(self.rows)

	def ColCount(self):
		return len(self.cols)

	def Cols(self):
		return self.cols

	def __getitem__(self, index):
		return self.rows[index]


def AnaliticalSolution(x):
	return exp(-2 * x) * 3 / 4 + x ** 2 / 2 - x / 2 + 1 / 4

def EulerMethod(y0, xs, f):
	ys = [0] * len(xs)
	ys[0] = y0
	for i in range(1, len(ys)):
		ys[i] = ys[i - 1] + (xs[i] - xs[i - 1]) * f(xs[i - 1], ys[i - 1])
	return ys

def ImprovedEulerMethod(y0, xs, f):
	ys = [0] * len(xs)
	ys[0] = y0
	for i in range(1, len(ys)):
		h = xs[i] - xs[i - 1]
		deltaY = h * f(xs[i - 1] + h / 2, ys[i - 1] + h / 2 * f(xs[i - 1], ys[i - 1]))
		ys[i] = ys[i - 1] + deltaY
	return ys

def RungeKuttaMethod(y0, xs, f):
	ys = [0] * len(xs)
	ys[0] = y0
	for i in range(0, len(ys) - 1):
		h = xs[i + 1] - xs[i]
		k1 = f(xs[i], ys[i])
		k2 = f(xs[i] + h / 2, ys[i] + k1 * h / 2)
		k3 = f(xs[i] + h / 2, ys[i] + k2 * h / 2)
		k4 = f(xs[i] + h, ys[i] + h * k3)
		ys[i + 1] = ys[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
		print(h, ys[i])
	return ys

def CorrectedEulerMethod(y0, xs, f):
	ys = [0] * len(xs)
	ys[0] = y0
	for i in range(1, len(ys)):
		h = xs[i] - xs[i - 1]
		k1 = f(xs[i - 1], ys[i - 1]) * h
		k2 = f(xs[i - 1] + h, ys[i - 1] + k1) * h
		deltaY = (k1 + k2) / 2
		ys[i] = ys[i - 1] + deltaY
	return ys

class FirstTaskViewModel():

	def __init__(self):
		print("kek")

	def Plot(xs, yss, analitical, methodNames):
		print('lol')
		i = 1
		rows = len(yss)
		plt.figure(tight_layout=True)
		for j in range(len(yss)):
			plt.subplot(rows, 1, i)
			i += 1
			plt.xlabel('t')
			plt.ylabel('T')
			plt.grid(True)
			plt.title(methodNames[j])
			plt.plot(xs, yss[j], color='g')
			if not analitical is None:
				plt.plot(xs, analitical, color='b')
		if len(yss) == 0 and not analitical is None:
			plt.xlabel('t')
			plt.ylabel('T')
			plt.grid(True)
			plt.plot(xs, analitical)
			plt.show()
		else:
			plt.show()

	def CreateTable(xs, numerics, analitical, methodNames):
		t = Table()
		cols = []
		if not analitical is None:
			for mname in methodNames:
				cols = cols + [mname, 'Delta']
			cols = ['k', 't', 'Analitical']
		else:
			cols = ['k', 't'] + methodNames
		for i in range(len(xs)):
			row  = [str(i + 1), str(xs[i])]
			if not analitical is None:
				row.append(analitical[i])
				for j in numerics:
					row.append(j[i])
					row.append(abs(j[i] - analitical[i]))
			else:
				for j in numerics:
					row.append(j[i])
			t.AddRow(row)
		return t



	def ConductExperiment(self, T0, Tc, r, n, endOfInterval, analitical=False, euler=False, improved=False, rungekutte=False, table=False, graphics=False):
		methods = []
		methodNames = []
		analiticalSolution = None
		h = endOfInterval / (n - 1)
		xs =  [i * h for i in range(n)]
		yss = []
		analiticalYs = None
		if analitical:
			analiticalSolution = lambda t: Tc + (T0 - Tc) * exp(-r * t)
			analiticalYs = [analiticalSolution(x) for x in xs]
		if euler:
			methods.append(EulerMethod)
			methodNames.append("Euler")
		if improved:
			methods.append(ImprovedEulerMethod)
			methodNames.append("Improved Euler")
		if rungekutte:
			methods.append(RungeKuttaMethod)
			methodNames.append("Runge-Kutta")
		f = lambda t, T: -r * (T - Tc)
		for m in methods:
			yss.append(m(T0, xs, f))
		if graphics:
			FirstTaskViewModel.Plot(xs, yss, analiticalYs, methodNames)
		if table:
			return FirstTaskViewModel.CreateTable(xs, yss, analiticalYs, methodNames)
