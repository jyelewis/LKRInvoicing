import tornado
import template
import dataModel
import base64
import json

class route(tornado.web.RequestHandler):
	def get(self, tableName, rowID = False):
		table = dataModel.Table(tableName)
		row = table.getRow(rowID)
		code = tornado.template.Loader("viewControllers").load("rowViewVC.html").generate(row=row, isInsert=not rowID, base64=base64)
		template.render(self, code, False)