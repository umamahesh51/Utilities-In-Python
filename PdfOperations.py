from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import glob
import FileOperations as fo
def merge_pdfs(pdfs_location):
    merged_pdf = PdfFileWriter()
    for pdf in os.listdir(pdfs_location):
        pdf_file = PdfFileReader(pdfs_location+"\\"+pdf)
        for i in range(pdf_file.getNumPages()):
            page = pdf_file.getPage(i)
            merged_pdf.addPage(page)
        merged_pdf_file = open(pdfs_location+"\\mergedpdf.pdf", "wb")   
        merged_pdf.write(merged_pdf_file)
        merged_pdf.encrypt("uma12", "badri12") #encryption
file_path = "C:\\Users\\utumma\\Desktop\\pdfs"
merge_pdfs(file_path)

#Watermarking is similar


