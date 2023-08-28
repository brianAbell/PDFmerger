import PyPDF2
import sys

def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    #iterate thru given pdfs, combine
    for pdf in pdf_list:
        pdf_merger.append(pdf)
    
    #open file in binary write mode (pdfs are binary not text), then write all pdfs to
    with open(output_filename, 'wb') as output_pdf_file:
        pdf_merger.write(output_pdf_file)
    
if __name__ == '__main__':
    #take command line args
    if len(sys.argv) < 4:
        print('Usage: python merger.py <output_filename> <pdf1> <pdf2> ...')
        sys.exit(1)
    
    output_filename = sys.argv[1]
    pdf_list = sys.argv[2:]

    merge_pdfs(pdf_list, output_filename)
    print(f"PDFs merged successfully into {output_filename}!")

    
