import null as null
import pyttsx3
import PyPDF2

bookName = 'sample.pdf'

book = open(bookName, 'rb')
# read book into PyPDF obj
pdfObj = PyPDF2.PdfFileReader(book)
# no. of pages
pageCount = pdfObj.numPages
reader = pyttsx3.init()
pageCount = 0
total_calls = 0

def read_page(currentPage):
    print('Reading Page')
    text = currentPage.extractText()
    reader.say(text)
    reader.runAndWait()


def fib_rec(n):
    print('fib_rec (', n, ')')
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


mem_list = [None] * 11


def fib_memoize(n):
    print('fib_memoize (', n, ')')
    if n == 1 or n == 2:
        return 1
    elif mem_list[n] != None:
        return mem_list[n]
    else:
        mem_list[n] = fib_memoize(n - 1) + fib_memoize(n - 2)
        return mem_list[n]


print(fib_rec(10))
print(fib_memoize(10))

if pageCount > 1:
    print("%s contains %s pages " % (bookName, pageCount))
    for pageNumber in range(0, pageCount):
        print("reading page %s" % pageNumber)
        page = pdfObj.getPage(pageNumber)
        read_page(page)
elif pageCount == 1:
    print("%s contains only one page" % bookName)
    page = pdfObj.getPage(0)
    read_page(page)
else:
    print("nothing to read")
