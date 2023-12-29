# steps
# 1. find the book by isbn using google books api
# 2. get a bibtex file of the book for citation
# 3. generate the citation
# 4. (later) use this as backend for a website

"""
python -m unittest discover -v -s tests/ -p 'test_*.py'
"""

import sys
import os
from book_information import BookRequest
from citation import Citation

def main():
    # get input
    input = BookRequest(sys.argv[1:])

    if input.valid:
        input.requestAndWriteBookInformation()

    citation = Citation(input.style)

    cited_book = citation.generateCitation()
    print(cited_book)

    os.remove(".temp")

if (__name__ == "__main__"):
    main()