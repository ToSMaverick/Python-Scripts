from glob import glob
from PyPDF2 import PdfMerger, PdfReader

def pdf_merge(password):
    ''' Merges all the pdf files in current directory '''
    merger = PdfMerger()
    allpdfs = [a for a in glob("*.pdf")]
    
    for pdf in allpdfs:
        reader = PdfReader(pdf)
        if reader.is_encrypted:
            reader.decrypt(password)
        merger.append(reader)
    
    with open("Merged_pdfs.pdf", "wb") as new_file:
        merger.write(new_file)

if __name__ == "__main__":
    password = input("Enter the password for the PDFs: ")
    pdf_merge(password)