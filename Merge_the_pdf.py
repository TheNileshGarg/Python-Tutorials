## Write a program to merge pdf files in alphabetical order 

def merge_pdf(path):
    import os 
    os.chdir(path)
    pdf_li = []

    for file in os.listdir():
        # Check if the current file is a regular file
        if os.path.isfile(file):
            if file.endswith('pdf'):
                pdf_li.append(file)

    pdf_li.sort()

    from pypdf import PdfWriter
    merger = PdfWriter()

    for pdf in pdf_li:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()


## To test if the function works 

if __name__ == '__main__':

    path = '#########################'
    merge_pdf(path)
# It is tested and we know it works. 