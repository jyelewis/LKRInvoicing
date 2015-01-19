import genericDatatype
import cgi

class Cell(genericDatatype.Cell):
	def __init__(self, table, column, rawData = None):
		super().__init__(table, column, rawData)
		self.rawData = ""
		self.retriveCode = """
			return "";
		"""
			
		self.initCode = ""
		
		
	
	@property
	def viewHTML(self):
		return '<a href="/invoice/'+str(self.row.id)+'.pdf"><button>Generate PDF</button></a>'
	
	
	@property
	def editHTML(self):
		return ""
		
		
	def setValue(self, newValue):
		pass


