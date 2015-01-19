import tornado
import template
import dataModel
import urllib
from database import db

class route(tornado.web.RequestHandler):
	def get(self, tableName):
		render(self, tableName)

			
	def post(self, tableName):
		newColumnName = self.get_argument("Name", 0)
		newColumnDatatype = self.get_argument("Datatype", 0)
		
		try:
			table = dataModel.Table(tableName)
			column = table.createColumn(newColumnName, newColumnDatatype)
			column.save()
		except:
			render(self, tableName, "Column name already exists")
			return
	
			
		self.redirect("/table/" + urllib.parse.quote(tableName) + "/column/" + urllib.parse.quote(newColumnName))
		
		
def render(self, tableName, error = ""):
	datatypes = dataModel.datatypes.keys()
	try:
		table = dataModel.Table(tableName)
		code = tornado.template.Loader("viewControllers").load("newColumnVC.html").generate(table=table, datatypes=datatypes, error=error)
		template.render(self, code)
	except:
		self.redirect("/")