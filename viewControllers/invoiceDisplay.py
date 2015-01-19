import tornado
import PDFGenerator
import dataModel

class route(tornado.web.RequestHandler):
	def get(self, rowID):
		tblInvoices = dataModel.Table("Invoices")
		invoice = tblInvoices.getRow(rowID)
		resultPath = PDFGenerator.generateInvoice(invoice)

		self.set_header('Content-Type', 'application/octet-stream')
		self.set_header('Content-Disposition', 'attachment; filename=Invoice%20'+str(invoice.cellByColumnName("Invoice Number").rawData + ".pdf"))

		#send file
		with open(resultPath, 'rb') as f:
			while 1:
				data = f.read(16384) # or some other nice-sized chunk
				if not data: break
				self.write(data)
			self.finish()