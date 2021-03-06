#coding=utf-8
import wx

from core import PLUFractorization as plu
from core import GramSchmidtQR as gsqr
from core import HouseholderReduction as hhr
from core import GivensReduction as gir


class Frame(wx.Frame):
	"""docstring for Frame"""
	def __init__(self, parent=None, title='Matrix Fractorization', size=(500, 700)):
		super(Frame, self).__init__(parent, title=title, size=size, style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX))


class  App(wx.App):
	"""docstring for  App"""
	def OnInit(self):
		self.Frame = Frame()
		#self.bkg = wx.Panel(self.Frame)
		self.inputState = True
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

		self.Frame.Show()

	def clearText(self, event):
		self.textCtrl.Clear()

	def inputMatrix(self, event):
		self.textCtrl.SetEditable(True)
		introduceContent = "**"*48 + '\n'
		introduceContent += "Please input 2 integers with respect to matrix's size(rows and columns) separates by one space or tab in the first row."
		introduceContent += " Then input the matrix one row one line, separate by one space or tab."
		introduceContent += " For example:\n"
		introduceContent += '4\t4\n1\t2\t-3\t4\n4\t8\t12\t-8\n2\t3\t2\t1\n-3\t-1\t1\t-4\n'
		introduceContent += "**"*48 + '\n'

		self.textCtrl.AppendText(introduceContent)
		self.introduceLineNum = self.textCtrl.GetNumberOfLines()-1

	def getMatrix(self):
		try:
			if not hasattr(self, 'introduceLineNum'):
				self.inputState = False
				return 

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
			return A
		except Exception, e:
			self.inputState = False
			return 
		

	def raiseDialog(self, message):
		dlg = wx.MessageDialog(None, message, caption='Excute error!', style=wx.ICON_ERROR|wx.OK)
		dlg.ShowModal()
		#self.clearText('')
		#self.inputMatrix('')
		self.textCtrl.SetEditable(True)
		dlg.Destroy()

	def checkInput(self):
		if not self.inputState:
			self.raiseDialog('Matrix input error, please input again!')
			self.inputState = True
			return False
		return True

	def calculation(self):
		self.oneFractor.fractorization()
		if not self.oneFractor.state:
			self.raiseDialog(self.oneFractor.errorMessage)
			return 
		resultContent = self.oneFractor.show()
		self.textCtrl.AppendText(resultContent)

	def pluCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix()
		if not self.checkInput():
			return

		self.oneFractor = plu.PLUFractorization(A)
		self.calculation()
	

	def gsqrCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 
		if not self.checkInput():
			return

		self.oneFractor = gsqr.GramSchmidtQR(A)
		self.calculation()

	def hhrCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 
		if not self.checkInput():
			return

		self.oneFractor = hhr.HouseholderReduction(A)
		self.calculation()

	def girCalculation(self, event):
		self.textCtrl.SetEditable(False)
		A = self.getMatrix() 
		if not self.checkInput():
			return

		self.oneFractor = gir.GivensReduction(A)
		self.calculation()


def layout():
	app = App()
	app.layout()
	app.MainLoop()


if __name__ == '__main__':
	layout()