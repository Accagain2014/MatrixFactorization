#coding=utf-8

from Fractorization import MatrixFractorization as mf 
from copy import deepcopy
import Tools
import math


class GivensReduction(mf):
	"""docstring for GivensReduction"""
	def __init__(self, A):
		super(GivensReduction, self).__init__(A)
	
	def fractorization(self):
		try:
			maxNM = max(self.n, self.m)
			self.R = deepcopy(self.A)
			self.Q = Tools.getIMatrix(maxNM)

			for j in range(maxNM):
				for i in range(j+1, self.m):
					P = Tools.getIMatrix(self.m)
					temp = self.R[j][j]*self.R[j][j] + self.R[i][j]*self.R[i][j]
					temp = math.sqrt(temp)
					P[j][j] = self.R[j][j]/temp
					P[j][i] = self.R[i][j]/temp
					P[i][j] = -self.R[i][j]/temp
					P[i][i] = self.R[j][j]/temp
					self.R = Tools.matrixMultiplication(P, self.R)
					self.Q = Tools.matrixMultiplication(P, self.Q)
			self.Q = Tools.matrixTranspose(self.Q)
		except Exception, e:
			self.errorMessage += str(e)
			self.state = False

	def show(self):
		content = '\n'+super(GivensReduction, self).show('GivensReduction')+'\n\n'
		content += 'Q:'
		content += Tools.outputAMatrix(self.Q)
		content += '\nR:'
		content += Tools.outputAMatrix(self.R)
		content += '--'*44+'\n'

		return content
