import sys
PDFa = sys.argv[1]
PDFb = sys.argv[2]
destination = sys.argv[3]


from PyPDF2 import PdfFileWriter, PdfFileReader

existing_pdf = PdfFileReader(open(PDFa, "rb"))
new_pdf = PdfFileReader(open(PDFb, "rb"))

output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open(destination, "wb")
output.write(outputStream)
outputStream.close()
