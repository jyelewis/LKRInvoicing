import os
app_name = "Testing app"
app_path = os.path.dirname(os.path.realpath(__file__))

import tornado
import template
import dataModel




def app_get(request):
	quotesTbl = dataModel.Table("Quotes")
	quoteCount = quotesTbl.rowCount
	code = tornado.template.Loader(app_path).load("view.html").generate(quoteCount = quoteCount)
	template.render(request, code)

		
def app_post(request):
	app_get(request)