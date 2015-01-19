import os
import tornado

apps = {}
for file in os.listdir("Apps"):
	if os.path.isfile(os.path.join("Apps",file)):
		continue
	if not (os.path.isfile(os.path.join("Apps", file, "__init__.py")) or os.path.isfile(os.path.join("Apps", file, "__init__.pyc"))):
		continue
	temp = __import__("Apps."+file, globals(), locals(), [], 0)
	
	try:
		typeName = temp.app_name
	except:
		typeName = file.lower()
	apps[typeName] = temp



class appRouter(tornado.web.RequestHandler):
	def get(self, appName):
		apps[appName].app_get(self)
		
	def post(self, appName):
		apps[appName].app_post(self)