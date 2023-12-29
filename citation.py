# generate a citation in one of three styles from the request
import json
from book_information import BookRequest
import os

class Citation():
    def __init__(self, style: int = BookRequest.DEFAULT, filename: str = ".temp"):
        self.style = style

        book_data = open(filename, "r")

        book = json.load(book_data)["items"][0]["volumeInfo"]

        self.title = book["title"]
        try:
            self.subtitle = book["subtitle"]
        except KeyError:
            self.subtitle = ""

        self.authors = book["authors"]
        self.publisher = book["publisher"]
        self.published_date = book["publishedDate"]
        self.published_year = self.published_date.split("-")[0]

    def generateCitation(self):
        if self.style == BookRequest.APA:
            self.citeAPA()
        elif self.style == BookRequest.MLA:
            self.citeMLA()
        elif self.style == BookRequest.CHICAGO:
            self.citeChicago()
        elif self.style == BookRequest.DEFAULT:
            self.citeDefault()
        else:
            raise Warning("Style undefined")
        
        os.remove(".temp")

    @staticmethod
    def generateAuthorString(authors: list[str]):
        if len(authors) == 0:
            return 
        elif len(authors) == 1:
            return authors[0]
        elif len(authors) == 2:
            return authors[0] + " and " + Citation.generateAuthorString(authors[1:])
        else:
            return authors[0] + ", " + Citation.generateAuthorString(authors[1:])

    def citeAPA(self):
        pass

    def citeMLA(self):
        pass

    def citeChicago(self):
        pass

    def citeDefault(self):
        return self.citeMLA()



