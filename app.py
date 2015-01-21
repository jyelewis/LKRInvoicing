import tornado.ioloop
import tornado.web
import tornado
import urllib
import dataModel
import sys

import viewControllers.tableVC
import viewControllers.tableEditVC
import viewControllers.landingVC
import viewControllers.columnEditVC
import viewControllers.newColumnVC
import viewControllers.rowEditVC
import viewControllers.rowViewVC
import viewControllers.invoiceDisplay
import columnAjaxRouting
import appManager

portNumber = sys.argv[1] if len(sys.argv) > 1 else 8888


application = tornado.web.Application([
    (r"/", viewControllers.landingVC.route),
    
    (r"/table/([^\/]+?)\/?$", viewControllers.tableVC.route),
    (r"/table/([^\/]+?)\/?edit$", viewControllers.tableEditVC.route),
    (r"/table/([^\/]+?)\/?new-column$", viewControllers.newColumnVC.route),
    (r"/table/([^\/]+?)\/?column/([^\/]+?)\/?$", viewControllers.columnEditVC.route),
    (r"/table/([^\/]+?)\/?column/([^\/]+?)\/ajax$", columnAjaxRouting.route),
    (r"/table/([^\/]+?)\/?row/([^\/]+?)\/edit\/?$", viewControllers.rowEditVC.route),
    (r"/table/([^\/]+?)\/?row/([^\/]+?)\/view\/?$", viewControllers.rowViewVC.route),
    (r"/table/([^\/]+?)\/?new-row", viewControllers.rowEditVC.route),
    (r"/new-table", viewControllers.tableEditVC.route),

    (r"/invoice/([^\/]+?)\.pdf$", viewControllers.invoiceDisplay.route),
    
    (r"/app/([^\/]+?)\/?$", appManager.appRouter),
    
    (r"/Resources/(.*)", tornado.web.StaticFileHandler, {'path': "GUI/Resources"}),
])

if __name__ == "__main__":
    application.listen(portNumber)
    print("Running LKRInvoicing at port", portNumber)
    tornado.ioloop.IOLoop.instance().start()
    	




