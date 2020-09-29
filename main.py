import pyttsx3
import PyPDF2

 bookName = 'sample.pdf'

book = open(bookName, 'rb')
# read book into PyPDF obj
pdfObj = PyPDF2.PdfFileReader(book)
# no. of pages
pageCount = pdfObj.numPages
reader = pyttsx3.init()
if pageCount > 1:
    print("%s contains %s pages " % (bookName, pageCount))
    for pageNumber in range(0, pageCount):
        print("reading page %s" % pageNumber)
        page = pdfObj.getPage(pageNumber)
        text = page.extractText()
        reader.say(text)
        reader.runAndWait()

else:
    print("%s contains only one page" % bookName)
    page = pdfObj.getPage(0)
    text = page.extractText()
    reader.say(text)
    reader.runAndWait()

