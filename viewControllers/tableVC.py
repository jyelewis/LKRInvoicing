import tornado
import dataModel
import urllib
import template
import math

class route(tornado.web.RequestHandler):
	def get(self, tableName):
		
		table = dataModel.Table(tableName)
		dataset = table.dataset
		orderColumn = self.get_argument("OrderBy", False)
		
		isSelectModal = (self.get_argument("Select", None) != None)
		
		if orderColumn:
			orderColumn = orderColumn.replace("+", " ")
			dataset.sort(orderColumn)
			
		#pagination code
		pag = {}
		pag['numPerPage'] = 10
		pag['totalPages'] = math.ceil(table.rowCount/pag['numPerPage'])
		try:
			pag['page'] = int(self.get_argument("Page", 1))
			if pag['page'] > pag['totalPages']:
				raise Exception
		except:
			pag['page'] = 1
		pag['fromRows'] = pag['numPerPage'] * (pag['page']-1)
		pag['toRows'] = min(pag['fromRows'] + pag['numPerPage'], table.rowCount)
		
		
		code = tornado.template.Loader("viewControllers").load("tableVC.html").generate(
			 dataset=dataset
			,table=table
			,orderColumn=orderColumn
			,pag=pag
			,getURL = getURLFunc(self)
			,isSelectModal=isSelectModal
			,editURL = ("?Modal=1&" if self.get_argument("Modal", False) else '?') + 'returnURL=' + tornado.escape.url_escape(self.request.uri)
		)
		
		template.render(self, code, not isSelectModal)



def getURLFunc(webRequest):
	def getURL(overwriteDict):
		arguments = {}
		for key, argument in webRequest.request.arguments.items():
			arguments[key] = argument[0]
	
		for key, argument in overwriteDict.items():
			if argument is not None:
				arguments[key] = argument
			else:
				arguments[key] = ""
				del arguments[key]
			
		return "?" + urllib.parse.urlencode(arguments)
	
	return getURL
		







