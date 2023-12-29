import sys
import os
from book_information import BookRequest
from citation import Citation

def main():
    # get input
    input = BookRequest(sys.argv[1:])

    if input.valid:
        input.requestAndWriteBookInformation()

    citation = Citation(input.style, input.data_filename)

    cited_book = citation.generateCitation()
    print(cited_book)

if (__name__ == "__main__"):
    main()