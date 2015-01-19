import tornado
import dataModel
import appManager

template = tornado.template.Loader("GUI").load("template.html")

def render(responce, code, renderSidebar = True):
	tables = dataModel.allTables()
	apps = list(appManager.apps)
	apps.sort()
	if renderSidebar and responce.get_argument("Modal", False):
		renderSidebar = False
	responce.write(template.generate(tables=tables, apps=apps, CPH=code, url=responce.request.uri, sidebar = renderSidebar))