#coding=utf-8
from Fractorization import MatrixFractorization as mf
import Tools
from copy import deepcopy
import math

class HouseholderReduction(mf):

	def __init__(self, A):
		super(HouseholderReduction, self).__init__(A)
		
	def fractorization(self):
		super(HouseholderReduction, self).fractorization()

		self.R = deepcopy(self.A)
		self.Q = Tools.getIMatrix(max(self.n, self.m))

		for j in range(max(self.n, self.m)-1):
			lenth = 0.0
			for i in range(j, self.m):
				lenth += self.R[i][j] * self.R[i][j]
			lenth = math.sqrt(lenth)
			u = [[self.R[ii][j] ] for ii in range(j, self.m)]
			u[0][0] -= lenth
			temp = Tools.matrixMultiplication(u, Tools.matrixTranspose(u))
			#print u
			u = Tools.matrixScale(temp, -2.0/Tools.dotMultiplication(u, 0, u, 0))
			
			u = Tools.iMatrixAddition(u)

			tempQ = Tools.getIMatrix(max(self.n, self.m))
			for i in range(j, max(self.n, self.m)):
				for k in range(j, max(self.n, self.m)):
					tempQ[i][k] = u[i-j][k-j]

			self.Q = Tools.matrixMultiplication(tempQ, self.Q)
			self.R = Tools.matrixMultiplication(tempQ, self.R)
			#print self.R

		self.Q = Tools.matrixTranspose(self.Q)

	def show(self):
		content = '\n'+super(HouseholderReduction, self).show()+'\n\n'
		content += 'Q:'
		content += Tools.outputAMatrix(self.Q)
		content += '\nR:'
		content += Tools.outputAMatrix(self.R)
		content += '--'*44+'\n'
		return content




