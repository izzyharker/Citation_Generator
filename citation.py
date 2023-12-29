# generate a citation in one of three styles from the request
import json
from book_information import BookRequest
import os

class Citation():
    def __init__(self, style: int = BookRequest.DEFAULT, filename: str = ".temp"):
        self.style = style

        book_data = open(filename, "r")

        book = json.load(book_data)["items"][0]["volumeInfo"]

        self.filename = filename
        self.title = book["title"]
        try:
            self.subtitle = book["subtitle"]
        except KeyError:
            self.subtitle = ""

        self.authors = book["authors"]
        self.publisher = book["publisher"]
        self.published_date = book["publishedDate"]
        self.published_year = self.published_date.split("-")[0]

    @staticmethod
    def generateAuthorString(authors: list[str]):
        if len(authors) == 0:
            return None
        elif len(authors) == 1:
            return authors[0]
        elif len(authors) == 2:
            return authors[0] + " and " + Citation.generateAuthorString(authors[1:])
        else:
            return authors[0] + ", " + Citation.generateAuthorString(authors[1:])

    @staticmethod
    def generateTitleString(title, subtitle = ""):
        if subtitle == "":
            return title
        else:
            return title + ": " + subtitle

    def generateCitation(self):
        if self.style == BookRequest.APA:
            citation = self.citeAPA()
        elif self.style == BookRequest.MLA:
            citation = self.citeMLA()
        elif self.style == BookRequest.CHICAGO:
            citation = self.citeChicago()
        elif self.style == BookRequest.DEFAULT:
            citation = self.citeDefault()
        else:
            raise Warning("Style undefined")
        
        os.remove(self.filename)
        return citation

    def citeAPA(self):
        authors = [item.split(" ")[1] + ", " + item.split(" ")[0][0] + "." for item in self.authors]
        book_authors = Citation.generateAuthorString(authors)
        book_authors.replace(" and ", " & ")
        book_title = Citation.generateTitleString(self.title, self.subtitle)

        citation = book_authors + " (" + self.published_year + "). \x1B[3m" + book_title + "\x1B[0m. " + self.publisher + "."
        return citation

    def citeMLA(self):
        authors = self.authors.copy()
        authors[0] = authors[0].split(" ")[1] + ", " + authors[0].split(" ")[0]
        book_authors = Citation.generateAuthorString(authors)
        book_title = Citation.generateTitleString(self.title, self.subtitle)

        citation = book_authors + ". \x1B[3m" + book_title + "\x1B[0m. " + self.publisher + ", " + self.published_year + "."
        return citation

    def citeChicago(self):
        authors = self.authors.copy()
        authors[0] = authors[0].split(" ")[1] + ", " + authors[0].split(" ")[0]
        book_authors = Citation.generateAuthorString(authors)
        book_title = Citation.generateTitleString(self.title, self.subtitle)

        citation = book_authors + ". \x1B[3m" + book_title + "\x1B[0m. " + self.publisher + ", " + self.published_year + "."
        return citation

    def citeDefault(self):
        return self.citeMLA()



