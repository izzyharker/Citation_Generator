import requests

def getAPIKey(api_key_filename: str = "APIKey"):
    try: 
        f = open("APIKey", "r")
    except FileNotFoundError:
        filename = input('API File not found under default name ("APIKey"). Please enter the name of the file containg the API key: ')
        f = open(filename, "r")

    api_key = f.readline()
    f.close()

    return api_key

def generateRequest(url_string):
    response = requests.get(url_string)

    # TODO: do something if request fails
    return response
    
def configureBookUrl(isbn: str):
    default_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    # do i even need an api key???
    # api_key = "&key=" + getAPIKey()
    api_key = ""

    url_for_isbn_request = default_url + isbn + api_key

    return url_for_isbn_request

def requestBookInformation(isbn: str) -> requests.Response:
    request_url = configureBookUrl(isbn)
    response = generateRequest(request_url)

    return response