from Tools import tools_v000 as tools
import os
from os.path import dirname
from base64 import b64decode
from base64 import b64encode

import requests, PyPDF2


# -20 for the name of this project base64_pdf_generator
save_path = dirname(__file__)[ : -20]
propertiesFolder_path = save_path + "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'base64_pdf_generator', 'user_text=')


# Encode in base64

def encodeBase64(pathIn, pathOut):
    # Encode in base64
    with open(pathIn, "rb") as pdf_file:
        encoded_string = b64encode(pdf_file.read())
        f = open(pathOut, 'wb')
        f.write(encoded_string)
        f.close()

# Import only b64decode function from the base64 module
# Define the Base64 string of the PDF file

def decodeBase64(pathIn, pathOut):
    # Import only b64decode function from the base64 module
    # Define the Base64 string of the PDF file
    file = open(pathIn, 'rb') 

    b64 = file.read()

    # Decode the Base64 string, making sure that it contains only valid characters
    bytes = b64decode(b64)

    # Perform a basic validation to make sure that the result is a valid PDF file
    # Be aware! The magic number (file signature) is not 100% reliable solution to validate PDF files
    # Moreover, if you get Base64 from an untrusted source, you must sanitizpipe the PDF contents
    if bytes[0:4] != b'%PDF':
      raise ValueError('Missing the PDF file signature')

    # Write the PDF contents to a local file
    f = open(pathOut, 'wb')
    f.write(bytes)
    f.close()

def readPdf(url, pathOutTemp) :

    response = requests.get(url)
    my_raw_data = response.content

    with open(pathOutTemp, 'wb') as my_data:
        my_data.write(my_raw_data)

    open_pdf_file = open(pathOutTemp, 'rb')
    read_pdf = PyPDF2.PdfFileReader(open_pdf_file)
    if read_pdf.isEncrypted:
        read_pdf.decrypt("")
        print(read_pdf.getPage(0).extractText())

    else:
        print(read_pdf.getPage(0).extractText())

encodeBase64("Projects\\base64_pdf_generator\\pdf\\Original\\my_pdf.pdf", "Projects\\base64_pdf_generator\\pdf\\my_pdf.txt")
decodeBase64("Projects\\base64_pdf_generator\\pdf\\my_pdf.txt", "Projects\\base64_pdf_generator\\pdf\\my_pdf.pdf")

readPdf('http://www.asx.com.au/asxpdf/20171103/pdf/43nyyw9r820c6r.pdf', "Projects\\base64_pdf_generator\\pdf\\my_pdf_internet.pdf")