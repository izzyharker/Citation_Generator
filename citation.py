from book import Book
import requests
import os

class Citation():
    DEFAULT, MLA, APA, CHICAGO = range(0, 4)

    def __init__(self):
        self.errmsg = ""
        self.data_filename = ".temp"
        self.style = Citation.DEFAULT
        self.isbn = ""

        # temporary
        self.request = None
        self.request_url = ""

    def validateISBN(self):
        valid = True

        if self.isbn == "":
            valid = False
            self.errmsg = "No ISBN found"
        elif len(self.isbn) != 13 and len(self.isbn) != 10:
            valid = False
            self.errmsg = "ISBN must have 13 or 10 digits"

        for digit in self.isbn:
            try:
                int(digit)
            except ValueError:
                valid = False
                self.errmsg = "Invalid characters found. Use digits 0-9 only"

        return valid

    def setStyle(self, style: str):
        if (style.lower() == "mla"):
            self.style = Citation.MLA
        elif (style.lower() == "apa"):
            self.style = Citation.APA
        elif (style.lower() == "chicago"):
            self.style = Citation.CHICAGO
        elif (style == "" or style.lower() == "default"):
            self.style = Citation.DEFAULT
        else:
            print("Warning: Invalid parameter. Style set to DEFAULT.")
            self.style = Citation.DEFAULT

    def parseInput(self, input: list[str]):
        valid = True

        index = 0

        number_of_parameters = len(input)
        if number_of_parameters == 0:
            self.errmsg = "No input found"
            valid = False
            self.isbn = ""
        else:
            option_1 = input[index]

        if valid and option_1 == "-f":
            try:
                self.isbn = input[index + 1]
            except IndexError:
                valid = False
                self.errmsg = "No ISBN given: -f must be followed by ISBN number"
            
            if valid and  self.isbn == "-s":
                valid = False
                self.errmsg = "No ISBN found: -f must be followed by ISBN number"   
        elif valid and option_1 == "-s":
            try:
                self.setStyle(input[index + 1])
            except IndexError:
                valid = False
                self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
            
            if valid and input[index + 1] == "-f":
                valid = False
                self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
        elif valid:
            valid = False
            self.errmsg = "Invalid input parameters"
            
        if valid and number_of_parameters > 2:
            index = 2
            option_2 = input[index]
            if valid and option_2 == "-f":
                try:
                    self.isbn = input[index + 1]
                except IndexError:
                    valid = False
                    self.errmsg = "No ISBN given: -f must be followed by ISBN number"
                
                if valid and self.isbn == "-s":
                    valid = False
                    self.errmsg = "No ISBN found: -f must be followed by ISBN number"
                
            elif valid and option_2 == "-s":
                try:
                    self.setStyle(input[index + 1])
                except IndexError:
                    valid = False
                    self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
                    
                
                if valid and input[index + 1] == "-f":
                    valid = False
                    self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
            elif valid:
                valid = False
                self.errmsg = "Invalid input parameters"

        if valid and self.isbn == "":
            valid = False
            self.errmsg = "No ISBN given: -f is required"

        return valid
    
    # temporary
    def displayUsage(self):
        print("Usage: python main.py -f <ISBN> [-s <style>]")    

    def parseAndValidateInput(self, input: list[str] or str):

        if type(input) == str:
            input = input.split(" ")
        
        valid = self.parseInput(input)

        if not valid:
            print("Error: ", self.errmsg)
            self.displayUsage()
        else:
            valid = self.validateISBN()

            if not valid:
                print("Error: ", self.errmsg)
                self.displayUsage()

        return valid

    def getAPIKey(api_key_filename: str = "APIKey"):
        try: 
            f = open("APIKey", "r")
        except FileNotFoundError:
            filename = input('API File not found under default name ("APIKey"). Please enter the name of the file containg the API key: ')
            f = open(filename, "r")

        api_key = f.readline()
        f.close()

        return api_key

    def generateRequest(self):
        self.response = requests.get(self.request_url)
        
    def configureBookUrl(self):
        default_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

        # do i even need an api key???
        # api_key = "&key=" + getAPIKey()
        api_key = ""

        self.request_url = default_url + self.isbn + api_key

    def requestBookInformation(self):
        self.configureBookUrl()
        self.generateRequest()

        # TODO: do something if request fails
        temp_file = open(self.data_filename, "w+")
        temp_file.write(self.response.text)
        temp_file.close()
    
    def generateCitation(self):
        book_to_cite = Book.readBookInformation(self.response.text)

        if self.style == Citation.APA:
            self.citeAPA(book_to_cite)
        elif self.style == Citation.MLA:
            self.citeMLA(book_to_cite)
        elif self.style == Citation.CHICAGO:
            self.citeChicago(book_to_cite)
        elif self.style == Citation.DEFAULT:
            self.citeDefault(book_to_cite)
        else:
            raise Warning("Style undefined")
        
        os.remove(".temp")
        
    def citeAPA(self, book: Book):
        pass

    def citeMLA(self, book: Book):
        pass

    def citeChicago(self, book: Book):
        pass

    def citeDefault(self, book: Book):
        return self.citeMLA(book)