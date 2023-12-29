import requests
import os

class BookRequest():
    DEFAULT, MLA, APA, CHICAGO = range(0, 4)

    def __init__(self, input: list[str] = []):
        self.errmsg = ""
        self.valid = True
        self.data_filename = ".temp"
        self.style = BookRequest.DEFAULT
        self.isbn = ""

        # temporary
        self.request = None
        self.request_url = ""

        self.parseAndValidateInput(input)

    def validateISBN(self):
        # sometimes isbn numbers are given with a dash (like 978-1476730776)
        self.isbn = self.isbn.strip("-")

        if self.isbn == "":
            self.valid = False
            self.errmsg = "No ISBN found"
        elif len(self.isbn) != 13 and len(self.isbn) != 10:
            self.valid = False
            self.errmsg = "ISBN must have 13 or 10 digits"

        if self.valid:
            for digit in self.isbn:
                try:
                    int(digit)
                except ValueError:
                    self.valid = False
                    self.errmsg = "Invalid characters found. Use digits 0-9 only"

        return self.valid

    def setStyle(self, style: str):
        if (style.lower() == "mla"):
            self.style = BookRequest.MLA
        elif (style.lower() == "apa"):
            self.style = BookRequest.APA
        elif (style.lower() == "chicago"):
            self.style = BookRequest.CHICAGO
        elif (style == "" or style.lower() == "default"):
            self.style = BookRequest.DEFAULT
        else:
            print("Warning: Invalid parameter. Style set to DEFAULT.")
            self.style = BookRequest.DEFAULT

    def parseInput(self, input: list[str]):
        self.valid = True
        index = 0

        number_of_parameters = len(input)
        if number_of_parameters == 0:
            self.errmsg = "No input found"
            self.valid = False
            self.isbn = ""
        else:
            option_1 = input[index]

        if self.valid and option_1 == "-f":
            try:
                self.isbn = input[index + 1]
            except IndexError:
                self.valid = False
                self.errmsg = "No ISBN given: -f must be followed by ISBN number"
            
            if self.valid and  self.isbn == "-s":
                self.valid = False
                self.errmsg = "No ISBN found: -f must be followed by ISBN number"   
        elif self.valid and option_1 == "-s":
            try:
                self.setStyle(input[index + 1])
            except IndexError:
                self.valid = False
                self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
            
            if self.valid and input[index + 1] == "-f":
                self.valid = False
                self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
        elif self.valid:
            self.valid = False
            self.errmsg = "Invalid input parameters"
            
        if self.valid and number_of_parameters > 2:
            index = 2
            option_2 = input[index]
            if self.valid and option_2 == "-f":
                try:
                    self.isbn = input[index + 1]
                except IndexError:
                    self.valid = False
                    self.errmsg = "No ISBN given: -f must be followed by ISBN number"
                
                if self.valid and self.isbn == "-s":
                    self.valid = False
                    self.errmsg = "No ISBN found: -f must be followed by ISBN number"
                
            elif self.valid and option_2 == "-s":
                try:
                    self.setStyle(input[index + 1])
                except IndexError:
                    self.valid = False
                    self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
                    
                
                if self.valid and input[index + 1] == "-f":
                    self.valid = False
                    self.errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
            elif self.valid:
                self.valid = False
                self.errmsg = "Invalid input parameters"

        if self.valid and self.isbn == "":
            self.valid = False
            self.errmsg = "No ISBN given: -f is required"

        return self.valid
    
    # temporary
    def displayUsage(self):
        print("Usage: python main.py -f <ISBN> [-s <style>]")    

    def parseAndValidateInput(self, input: list[str] or str):

        if type(input) == str:
            input = input.split(" ")
        
        self.parseInput(input)

        if not self.valid:
            print("Error: ", self.errmsg)
            self.displayUsage()
        else:
            self.valid = self.validateISBN()

            if not self.valid:
                print("Error: ", self.errmsg)
                self.displayUsage()

        return self.valid

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

    def writeBookInformation(self):
        temp_file = open(self.data_filename, "w+")
        temp_file.write(self.response.text)
        temp_file.close()

    def requestAndWriteBookInformation(self):
        self.requestBookInformation()
        self.writeBookInformation()