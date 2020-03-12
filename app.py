import PyPDF2
import argparse

parser = argparse.ArgumentParser(description='Extract data table from PDF')
parser.add_argument('--input',required=True)
parser.add_argument('--output',required=True)
args = parser.parse_args()

pdfFileObj = open(args.input, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(1)
	
print(pageObj.extractText().split('\n \n'))
	
elements = list(map(lambda x: x.replace(' \n', '').replace('\n', ''), pageObj.extractText().split('\n \n')))

	
try:
	i_t = elements.index("CCAA")
except:
	print("Oh crap!")
	
csv = open(args.output, 'w')
			
csv.write("CCAA,Casos,IA (c/100.000),UCI,Fallecidos\n") 
	
for c in range(19):

	csv.write("\""+elements[(i_t+5) + c * 5] + "\",\"" + elements[(i_t+5) + c * 5 +1] + "\",\"" + elements[(i_t+5) + c * 5 +2] + "\",\"" + elements[(i_t+5) + c * 5 +3] +  "\",\"" + elements[(i_t+5) + c * 5 +4]+"\"\n")

		
	
