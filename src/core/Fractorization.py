#coding=utf-8
from copy import deepcopy

class MatrixFractorization(object):

	def __init__(self, A):
		for i in range(len(A)):
			A[i] = map(float, A[i])

		self.A = deepcopy(A)
		self.m = len(self.A)
		self.n = len(self.A[0])
		self.state = True
		self.errorMessage = ''

	def fractorization(self):
		#print 'Begin to do matrix fractorization ...'
		pass

	def show(self, method='matrix fractorization'):
		return 'Show ' + method + ' result ...'

	def check(self):
		return self.state

