datatype_name = "PDF Button"

import genericDatatype
import cgi

from . import cell


class Column(genericDatatype.Column):
	def __init__(self, table, data):
		super().__init__(table, data)
		if not self.metadata:
			self.metadata = {}

		self.cellClass = cell.Cell
		self.retriveCode = """
			return {}
		"""
		
	@property
	def editHTML(self):
		return ""
		
		
	
	
