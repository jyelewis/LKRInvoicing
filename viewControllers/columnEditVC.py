import tornado
import template
import dataModel
import urllib
import base64
import json
from database import db

class route(tornado.web.RequestHandler):
	def get(self, tableName, columnName):
		try:
			table = dataModel.Table(tableName)
			column = table.getColumn(columnName)
		except:
			self.redirect("/table/"+tableName+"/edit")
		code = tornado.template.Loader("viewControllers").load("columnEditVC.html").generate(column=column, base64 = base64)
		template.render(self, code)
		

			
	def post(self, tableName, columnName):
		table = dataModel.Table(tableName)
		column = table.getColumn(columnName)
		if self.get_argument("delete", 0):
			column.delete()
			self.redirect("/table/" + urllib.parse.quote(tableName) + "/edit")
			return
		else:
			column.name = self.get_argument("Name")
			column.visible = bool(self.get_argument("Visible", 0))
			if column.setMetadata(json.loads(self.get_argument("columnMetadata"))) == False:
				self.redirect(self.request.uri) #if returns true, continue editing			
				column.save()
				return
				
			column.save()
				

		self.redirect("/table/" + urllib.parse.quote(tableName))