#coding=utf-8
import wx

from core import PLUFractorization as plu
from core import GramSchmidtQR as gsqr
from core import HouseholderReduction as hhr
from core import GivensReduction as gir


class Frame(wx.Frame):
	"""docstring for Frame"""
	def __init__(self, parent=None, title='Matrix Fractorization', size=(500, 700)):
		super(Frame, self).__init__(parent, title=title, size=size)


class  App(wx.App):
	"""docstring for  App"""
	def OnInit(self):
		self.Frame = Frame()
		self.bkg = wx.Panel(self.Frame)
		self.Frame.Show()
		return True

	def layout(self):
		self.pluButton = wx.Button(self.Frame, label='PLUFractorization', pos=(5, 5) ,size=(160, 25))
		self.gsqrButton = wx.Button(self.Frame, label='GramSchmidtQR', pos=(175, 5), size=(160, 25))
		self.inputButton = wx.Button(self.Frame, label='Input', pos=(345, 5), size=(150, 25))

		self.hhrButton = wx.Button(self.Frame, label='HouseholderReduction', pos=(5, 35), size=(160, 25))
		self.girButton = wx.Button(self.Frame, label='GivensReduction', pos=(175, 35), size=(160, 25))
		self.clearButton = wx.Button(self.Frame, label='Clear', pos=(345, 35), size=(150, 25))
		
		self.textCtrl = wx.TextCtrl(self.Frame, pos=(5, 70), size=(490, 600), style = wx.TE_MULTILINE | wx.HSCROLL)
		
		self.Frame.Bind(wx.EVT_BUTTON, self.inputMatrix, self.inputButton)
		self.Frame.Bind(wx.EVT_BUTTON, self.clearText, self.clearButton)
		
		self.Frame.Bind(wx.EVT_BUTTON, self.pluCalculation, self.pluButton)
		self.Frame.Bind(wx.EVT_BUTTON, self.gsqrCalculation, self.gsqrButton)
		self.Frame.Bind(wx.EVT_BUTTON, self.hhrCalculation, self.hhrButton)
		self.Frame.Bind(wx.EVT_BUTTON, self.girCalculation, self.girButton)

	def clearText(self, event):
		self.textCtrl.Clear()

	def inputMatrix(self, event):
		self.textCtrl.SetEditable(True)
		introduceContent = "**"*48 + '\n'
		introduceContent += "Please input 2 integers with respect to matrix's size(rows and columns) separates by one space or tab in the first row."
		introduceContent += " Then input the matrix one row one line, separate by one space or tab."
		introduceContent += " For example:\n"
		introduceContent += '3\t3\n1\t19\t-34\n-2\t-5\t20\n2\t8\t37\n'
		introduceContent += "**"*48 + '\n'

		self.textCtrl.AppendText(introduceContent)
		self.introduceLineNum = self.textCtrl.GetNumberOfLines()-1

	def getMatrix(self):
		aLine = self.textCtrl.GetLineText(self.introduceLineNum).strip()
		aLine = map(lambda x: x.strip(), aLine.split())
		aLine = map(int, aLine)
		n = aLine[1]
		m = aLine[0]

		A = []

		for i in range(m):
			aLine = self.textCtrl.GetLineText(self.introduceLineNum+i+1).strip()
			if(aLine == ""):
				self.inputState = False
			aLine = map(lambda x: x.strip(), aLine.split())
			aLine = map(float, aLine)
			if(len(aLine) != n):
				self.inputState = False
			A.append(aLine)
		#print A
		return A

	def calculation(self):
		self.oneFractor.fractorization()
		resultContent = self.oneFractor.show()
		self.textCtrl.AppendText(resultContent)

	def pluCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 
		self.oneFractor = plu.PLUFractorization(A)
		self.calculation()
	

	def gsqrCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 

		self.oneFractor = gsqr.GramSchmidtQR(A)
		self.calculation()

	def hhrCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 

		self.oneFractor = hhr.HouseholderReduction(A)
		self.calculation()

	def girCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 

		self.oneFractor = gir.GivensReduction(A)
		self.calculation()


def layout():
	app = App()
	app.layout()
	app.MainLoop()


if __name__ == '__main__':
	layout()