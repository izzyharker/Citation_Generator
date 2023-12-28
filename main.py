# steps
# 1. find the book by isbn using google books api
# 2. get a bibtex file of the book for citation
# 3. generate the citation
# 4. (later) use this as backend for a website

import sys
import os
from citation import Citation
from book import Book
import requests

def main():
    # get input
    input = Citation()
    valid = input.parseAndValidateInput(sys.argv[1:])

    if valid:
        input.requestBookInformation()

    # citation = gen.readAndGenerateCitation(input["Style"])

    os.remove(".temp")
    # print(citation)
    print(input.response.text)
    return 0

if (__name__ == "__main__"):
    main()