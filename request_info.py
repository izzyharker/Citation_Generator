import requests

def generateRequest(url_string):
    response = requests.get(url_string)

    if (response.status_code != 200):
        # print some error message
        print("request failed")
        return False
    else:
        return response
    
def configureBookUrl(isbn: str):
    default_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    api_key = "&key=AIzaSyAbR6PPNAkWuLD46_pivjj4RF6bYwIkud0"

    url_for_isbn_request = default_url + isbn + api_key

    return url_for_isbn_request

def requestBookInformation(isbn: str):
    request_url = configureBookUrl(isbn)

    response = generateRequest(request_url)

    return response