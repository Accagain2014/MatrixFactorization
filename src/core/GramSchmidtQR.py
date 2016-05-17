#coding=utf-8
from Fractorization import MatrixFractorization as mf
import math
import Tools


class GramSchmidtQR(mf):
	"""docstring for GramSchmidtQR"""
	def __init__(self, A):
		super(GramSchmidtQR, self).__init__(A)
		
	def fractorization(self):
		super(GramSchmidtQR, self).fractorization()
		self.Q = [[0.0 for i in range(self.n)] for i in range(self.m)]
		self.R = [[0.0 for i in range(self.n)] for i in range(self.n)]

		for i in range(self.m):
			self.R[0][0] += self.A[i][0] * self.A[i][0]
		self.R[0][0] = math.sqrt(self.R[0][0])

		for i in range(self.m):
			self.Q[i][0] = self.A[i][0]/self.R[0][0]

		for i in range(1, self.n):
			temp = [self.A[j][i] for j in range(self.m)]
		
			for j in range(i):
				self.R[j][i] = Tools.dotMultiplication(self.Q, j, self.A, i)
				for k in range(self.m):
					temp[k] += -self.R[j][i] * self.Q[k][j]
			
			self.R[i][i] = 0.0
			for k in range(self.m):
				self.Q[k][i] = temp[k]
				self.R[i][i] += temp[k] * temp[k]
			self.R[i][i] = math.sqrt(self.R[i][i])

			for k in range(self.m):
				self.Q[k][i]  = self.Q[k][i] / self.R[i][i]


	def show(self):
		content = '\n'+super(GramSchmidtQR, self).show('GramSchmidtQR')+'\n\n'
		content += 'Q:'
		content += Tools.outputAMatrix(self.Q)
		content += '\nR:'
		content += Tools.outputAMatrix(self.R)
		content += '--'*44+'\n'

		return content

		