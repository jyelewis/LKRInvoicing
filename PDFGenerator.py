from __future__ import division

import io
from reportlab.pdfgen import canvas
import random
import subprocess
import dataModel

def tryInt(value):
	retValue = 0;
	try:
		retValue = int(value);
	except ValueError:
		retValue = float(value);
	
	return retValue

def generateInvoice(invoice):
	overlayFilename = "/tmp/pdfOverlay"+str(random.randint(100000,999999))+".pdf"

	packet = io.StringIO()
	# create a new PDF with Reportlab
	can = canvas.Canvas(overlayFilename)
	can.setFont("Helvetica", 11)
	#can.setFillColorRGB(73/255,98/255,145/255) #73 98 145
	can.setFillColorRGB(23/255,58/255,95/255) #73 98 145

	#draw all text

	#print(dir())

	#LEFT COLUMN
	leftColAlign = 290
	can.drawRightString(leftColAlign, 621, invoice.cellByColumnName("Client").selectedRow.cellByColumnName("Contact name").rawData) #contact name
	can.drawRightString(leftColAlign, 605, invoice.cellByColumnName("Client").selectedRow.cellByColumnName("Contact name 2").rawData) #company name

	can.drawRightString(leftColAlign, 585, invoice.cellByColumnName("Client").selectedRow.cellByColumnName("Business Name").rawData) #Company name
	can.drawRightString(leftColAlign, 570, invoice.cellByColumnName("Client").selectedRow.cellByColumnName("Email").rawData) #Email address

	can.drawRightString(leftColAlign, 550, invoice.cellByColumnName("Client").selectedRow.cellByColumnName("Phone number").rawData) #Phone number
	
	can.drawRightString(leftColAlign, 535, str(invoice.cellByColumnName("Date issued"))) #Date issued

	#RIGHT COLUMN
	rightColAlign = 480
	can.drawRightString(rightColAlign, 621, invoice.cellByColumnName("Project Title").rawData) #project title
	can.drawString(310, 588, invoice.cellByColumnName("Project Description").rawData) #project Description

	can.drawRightString(rightColAlign, 567, invoice.cellByColumnName("Invoice Number").rawData) #Invoice number
	can.drawRightString(rightColAlign, 553, invoice.cellByColumnName("Term").rawData) #Term

	#Draw table
	tableTopOffset = 505

	TotalCost = 0

	#description column
	descOffset = 63
	quantityOffset = 290
	priceOffset = 375
	costOffset = 455
	for i in range(1,11):
		product = invoice.cellByColumnName("Product "+str(i)).selectedRow
		if product is not None:
			try:
				quantity = tryInt(invoice.cellByColumnName("Quantity "+str(i)).rawData)
			except:
				quantity = 1
			unitPrice = tryInt(product.cellByColumnName("Unit Price").rawData)

			#description
			can.drawString(descOffset, tableTopOffset-(i*17), product.cellByColumnName("Description").rawData)

			#quantitiy
			can.drawString(quantityOffset, tableTopOffset-(i*17), str("%.2f" % quantity))

			#unit price
			can.drawString(priceOffset, tableTopOffset-(i*17), "$"+str("%.2f" % unitPrice))

			#cost
			can.drawString(costOffset, tableTopOffset-(i*17), "$"+str("%.2f" % (quantity*unitPrice)))

			TotalCost += quantity*unitPrice



	#total
	can.drawString(costOffset, 315, "$"+str("%.2f" % TotalCost)) #Term


	can.save()

	

	templateLoc = "/tmp/pdfTemplate"+str(random.randint(100000,999999))+".pdf"
	resultFile = "/tmp/pdfResult"+str(random.randint(100000,999999))+".pdf"

	#load up template
	with open(templateLoc, 'wb') as f:
		templateRow = invoice.cellByColumnName("Template").selectedRow
		if templateRow is None:
			templateRow = dataModel.Table("Templates").getRow(1)
		f.write(templateRow.cellByColumnName("File").fileData)

	subprocess.call(["python", "mergePDF.py", templateLoc, overlayFilename, resultFile])

	return resultFile





