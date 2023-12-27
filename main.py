# steps
# 1. find the book by isbn using google books api
# 2. get a bibtex file of the book for citation
# 3. generate the citation
# 4. (later) use this as backend for a website

import sys
import parse_input as parse
import request_information as req

def main():
    # get input
    input = parse.parseAndValidateInput(sys.argv[1:])
    book_data = None

    if (input != {}):
        book_data = req.requestBookInformation(input["ISBN"])

    print(book_data.text)

if (__name__ == "__main__"):
    main()