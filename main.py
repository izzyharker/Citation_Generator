# steps
# 1. find the book by isbn using google books api
# 2. get a bibtex file of the book for citation
# 3. generate the citation
# 4. (later) use this as backend for a website

# google API key: AIzaSyAbR6PPNAkWuLD46_pivjj4RF6bYwIkud0
import requests
import sys
import parse_input as parse

def getAPIKey():
    api_file = open("googleAPI", "r")
    
    for line in api_file:
        print(line)


def send_and_get_request(url_string):
    response = requests.get(url_string)

    if (response.status_code != 200):
        # print some error message
        print("request failed")
        return False
    else:
        return response
    
def configure_book_url(search_params: dict):
    request_url = "https://www.googleapis.com/books/v1/volumes?q="

    api_key = "&key=" + getAPIKey()

    return request_url
            

def main():
    # get input
    input = parse.parseAndValidateInput(sys.argv[1:])

    if (input.keys() == None):
        print("input is empty")
    else:
        print(input)
    # configure url

if (__name__ == "__main__"):
    main()