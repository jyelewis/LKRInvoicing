import tornado
import template
import dataModel
import base64
import json

class route(tornado.web.RequestHandler):
	def get(self, tableName, rowID = False):
		table = dataModel.Table(tableName)
		row = table.getRow(rowID)
		code = tornado.template.Loader("viewControllers").load("rowEditVC.html").generate(row=row, isInsert=not rowID, base64=base64)
		template.render(self, code)

			
	def post(self, tableName, rowID = False):
		table = dataModel.Table(tableName)
		row = table.getRow(rowID)
		if (self.get_argument("Delete", 0)):
			row.delete()
		else:		
			newData = json.loads(self.get_argument("jsonValues"))
			for columnDbName in newData:
				updateCell(row, columnDbName, newData[columnDbName])
			
			row.save()
			
		if self.get_argument("Modal", False):
			self.write('<script type="text/javascript">top.location.reload();</script>')
		else:
			self.redirect(self.get_argument("returnURL", "/table/"+table.name))
		
		

def updateCell(row, columnDbName, dataObj):
	for cell in row.cells:
		if cell.column.dbname == columnDbName:
			cell.setValue(dataObj)
			break