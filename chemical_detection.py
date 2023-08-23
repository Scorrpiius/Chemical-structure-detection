import sys
from document_processing import document_processing



def main():
    """
        This script segments chemical structures in documents and returns a list of the chemical structures detected and
        their number of occurences (if there are multiple documents). 
        The argument passed in the terminal is the folder containing the document(s) to be analysed
    """

    if len(sys.argv) == 2:
        document_processing(sys.argv[1])
    if len(sys.argv) == 3:
        document_processing(sys.argv[1], sys.argv[2])



if __name__ == "__main__":
    main()