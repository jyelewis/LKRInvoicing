import tornado

class route(tornado.web.RequestHandler):
	def get(self):
		self.redirect("/table/Invoices")