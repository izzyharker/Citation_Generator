# generate a citation in one of three styles from the request
import requests
import parse_input as parse

class Book():
    def __init__(self):
        self.volume_info = {"authors": [], "title": ""}
        self.publisher = ""
        self.published_date = ""
        self.page_count = 0
        self.isbn = {"type": 13, "isbn": ""}

    def citeAPA(self):
        pass

    def citeMLA(self):
        pass

    def citeChicago(self):
        pass

    def citeDefault(self):
        return self.citeMLA()
    
    def generateCitation(self, style):
        if style == parse.APA:
            return self.citeAPA()
        elif style == parse.MLA:
            return self.citeMLA()
        elif style == parse.CHICAGO:
            return self.citeChicago()
        elif style == parse.DEFAULT:
            return self.citeDefault()
        else:
            raise Warning("Style undefined")

    def parseBookInformation(self, filename = ".temp"):
        pass


    def readAndGenerateCitation(self, style: int):
        self.parseBookInformation()

        citation = self.generateCitation(style)
        return citation




