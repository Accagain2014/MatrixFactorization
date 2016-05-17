#coding=utf-8
from Fractorization import MatrixFractorization as mf
from copy import deepcopy
import Tools

class PLUFractorization(mf):

	def __init__(self, A):
		super(PLUFractorization, self).__init__(A)
		if (self.n != self.m):
			print "Input matrix must be square matrix, but find (%d, %d) matrix." % (self.m, self.n)
			self.state = False

	def fractorization(self):
		super(PLUFractorization, self).fractorization()

		n = self.n
		A = deepcopy(self.A)
		'''
		LU fraction with row interchanges
		PA = LU
		return P, L, U
		'''
		P = [ ([0]*1) for i in range(n)]
		for i in range(n):
			P[i][0] = i
		for i in range(n):
			#Find pivot
			#Max = -float("inf")
			Max = abs(A[i][i])
			pivotRow = i
			
			for j in range(i+1, n):
				if abs(A[j][i]) > Max:
					Max = abs(A[j][i])
					pivotRow = j
			
			if abs(Max) < 2e-10:
				print "Pivot is zero: Wrong"
				return (None, None, None)
			if pivotRow != i:
				P[pivotRow], P[i] = P[i], P[pivotRow]
				A[pivotRow], A[i] = A[i], A[pivotRow]
			#Excute multiple row addtion
			for j in range(i+1, n):
				A[j][i] = A[j][i]/A[i][i]
				for k in range(i+1, n):
					A[j][k] = A[j][k] - A[j][i]*A[i][k]

		L = [([0.0]*n) for i in range(n)]
		U = [([0.0]*n) for i in range(n)]
		P1 = [([0.0]*n) for i in range(n)]

		for i in range(n):
			for j in range(n):
				if j < i:
					L[i][j] = A[i][j]
				elif j == i:
					L[i][j] = 1
					U[i][j] = A[i][j]
				else:
					U[i][j] = A[i][j]
			P1[i][P[i][0]] = 1
		self.P = P1
		self.L = L
		self.U = U
		#print 'Matrix fractorization is done successfully ...'

	def show(self):
		content = '\n'+super(PLUFractorization, self).show('PLUFractorization')+'\n\n'
		content += 'P:'
		content += Tools.outputAMatrix(self.P)
		content += '\nL:'
		content += Tools.outputAMatrix(self.L)
		content += '\nU:'
		content += Tools.outputAMatrix(self.U)
		content += '--'*44+'\n'

		return content