import tornado
import dataModel

class route(tornado.web.RequestHandler):
	def get(self, tableName, columnName):
		forwardRequest(self, tableName, columnName)
	
	def post(self, tableName, columnName):
		forwardRequest(self, tableName, columnName)

def forwardRequest(webRequest, tableNameOrig, columnNameOrig):
	tableName = tableNameOrig.replace("+", " ")
	columnName = columnNameOrig.replace("+", " ")
	
	handler = None
	try:
		table = dataModel.Table(tableName)
		column = table.getColumn(columnName)
		handler = column.ajaxHandler
	except:
		webRequest.redirect("/table/"+tableNameOrig+"/column/"+columnNameOrig)
	
	handler(webRequest)