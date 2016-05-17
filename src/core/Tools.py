#coding=utf-8
from copy import deepcopy

def matrixMultiplication(A, B):
	m = len(A)
	kk = len(B)
	n = len(B[0])

	result = [[0.0 for i in range(n) ] for i in range(m)]

	for i in range(m):
		for j in range(n):
			for k in range(kk):
				result[i][j] += A[i][k] * B[k][j]

	return result

def matrixTranspose(A):
	m = len(A)
	n = len(A[0])

	result = [[0.0 for i in range(m)] for i in range(n)]

	for i in range(m):
		for j in range(n):
			result[j][i] = A[i][j]

	return result

def matrixScale(A, a):
	m = len(A)
	n = len(A[0])

	result = deepcopy(A)

	for i in range(m):
		for j in range(n):
			result[i][j] *= a

	return result

def dotMultiplication(A, i, B, j):
	result = 0.0
	for ii in range(len(A)):
		result += A[ii][i] * B[ii][j]
	return result

def iMatrixAddition(A):
	result = deepcopy(A)
	for i in range(len(result)):
		result[i][i] = 1 + result[i][i]
	return result

def getIMatrix(n):
	result = [[0.0 for i in range(n)] for j in range(n)]
	for i in range(n):
		result[i][i] = 1.0
	return result

def outputAMatrix(A):
	result = '[\n'
	for i in range(len(A)):
		result += '\t' + '\t\t'.join(map(lambda x: ('%.5f' % x), A[i]))+'\n'
	result += ']\n'

	return result



