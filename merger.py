import PyPDF2
import sys

def merge_pdfs(pdf_list, output_filename):
    """
    Merges multiple PDF files into a single PDF.

    Parameters:
    pdf_list (list of str): A list of paths to PDF files to be merged.
    output_filename (str): The path where the merged PDF will be saved.

    The function initializes a PdfMerger object, iterates through all the provided
    PDF paths, appends them to the merger object, and finally writes the merged
    content to the specified output file.
    """
    # Initialize a PdfMerger object
    pdf_merger = PyPDF2.PdfMerger()

    # Iterate through each PDF file in the list and append it to the merger object
    for pdf in pdf_list:
        pdf_merger.append(pdf)
    
    # Create the output file in binary write mode (as PDFs are binary files)
    # and write the merged PDFs into this file
    with open(output_filename, 'wb') as output_pdf_file:
        pdf_merger.write(output_pdf_file)
    
if __name__ == '__main__':
    # Check for the correct number of command-line arguments
    if len(sys.argv) < 4:
        # If not enough arguments are provided, display usage instructions
        print('Usage: python merger.py <output_filename> <pdf1> <pdf2> ...')
        sys.exit(1)
    
    # Extract the output filename from the command-line arguments
    output_filename = sys.argv[1]
    # Extract the list of PDF files to merge from the command-line arguments
    pdf_list = sys.argv[2:]

    # Call the merge_pdfs function with the list of PDFs and the desired output filename
    merge_pdfs(pdf_list, output_filename)
    # Inform the user that the PDFs have been merged successfully
    print(f"PDFs merged successfully into {output_filename}!")


    
