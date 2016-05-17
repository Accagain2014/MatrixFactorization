#coding=utf-8

from core import PLUFractorization as plu
from core import GramSchmidtQR as gsqr
from core import HouseholderReduction as hhr
from core import GivensReduction as gir
from core import Tools
from gui import Layout as ly

if __name__ == '__main__':
	'''
	A = [[1, 2, -3, 4],
	[4, 8, 12, -8],
	[2, 3, 2, 1],
	[-3, -1, 1, -4]
	]


	A = [[0, -20, -14],
	[3, 27, -4],
	[4, 11, -2]
	]
	
	A = [[4, -3, 4],
	[2, -14, -3],
	[-2, 14, 0],
	[1, -7, 15]]
	
	A = [[1, 19, -34],
	[-2, -5, 20],
	[2, 8, 37]]
	
	'''
	ly.layout()
