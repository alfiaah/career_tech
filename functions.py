import PyPDF2
import spacy

def pdfreader(path):

	pdfFileObj = open(path, 'rb')
	# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pdfReader = PyPDF2.PdfReader(pdfFileObj)
	# pdfReader.numPages
	len(pdfReader.pages)

	# pageObj = pdfReader.getPage(0)
	pageObj=pdfReader.pages[0] 
	# pageObj.extractText()
	pageObj.extract_text()

	# return pageObj.extractText()
	return pageObj.extract_text()
def docreader(path):
	out=""
	from docx import Document
	document = Document(path)
	for para in document.paragraphs:
		out=out+para.text
	return out
def txtreader(path):
	
	filepath =path
	data = ""
	with open(filepath) as fp:
		line = fp.readline()
	# print(line)
		cnt = 1
		while line:
		# print(line)
			data = data + line
			line = fp.readline()
			cnt += 1

		return data
