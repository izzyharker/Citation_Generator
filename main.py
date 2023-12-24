# steps
# 1. find the book using some api - start with ISBN probably
# 2. get a bibtex file of the book for citation
# 3. generate the citation
# 4. (later) use this as backend for a website

# google API key: AIzaSyAbR6PPNAkWuLD46_pivjj4RF6bYwIkud0
import requests

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
    api_key = "&key=AIzaSyAbR6PPNAkWuLD46_pivjj4RF6bYwIkud0"

    return request_url