import tornado
import dataModel
import json
import urllib
import template
from database import db

class route(tornado.web.RequestHandler):
	def get(self, tableName = False):
		template.render(self, renderView(self, tableName))
	def post(self, tableName = False):
		if tableName:
			tableName = tableName.replace("+", " ")
		
		if self.get_argument("delete", 0):
			table = dataModel.Table(tableName)
			table.delete()
			self.redirect("/")
			return
		else:
			saveChanges(self, tableName)

def renderView(netRequest, tableName, error = None):
	try:
		table = dataModel.Table(tableName)
	except:
		netRequest.redirect("/")
		return
	
	code = tornado.template.Loader("viewControllers").load("tableEditVC.html").generate(table=table, error = error)
	return code
	
	
def saveChanges(netRequest, tableName = False):
	try:
		table = dataModel.Table(tableName)
	except:
		netRequest.redirect("/")
		return
		
	c = db.cursor();
	error = None
	table.name = netRequest.get_argument("Name")
	
	if table.name == "":
		error = "Table names must not be blank"
	
	if ('/' in table.name or '\\' in table.name) and not error:
		error = "Table names must not contain slashes"
	else:
		try:
			table.save()
		except:
			error = "Error creating table, Does that table already exist?"
	
	#submission
	if not error:
		if tableName: #updating existing table
			for (key, columnName) in enumerate(json.loads(netRequest.get_argument("columnOrdering"))):
				column = table.getColumn(columnName)
				column.ordering = key+1
				column.save()
			
		if tableName:
			netRequest.redirect("/table/" + urllib.parse.quote(table.name))
		else:
			netRequest.redirect("/table/" + urllib.parse.quote(table.name) + "/edit")
	else:
		template.render(netRequest, renderView(netRequest, tableName, error))










