DEFAULT, MLA, APA, CHICAGO = range(0, 4)

def displayUsage():
    print("Usage: python main.py -f <ISBN> [-s <style>]")

def validateISBN(isbn: str):
    valid = True
    errmsg = ""

    if isbn == "":
        valid = False
        errmsg = "No ISBN found"
    elif len(isbn) != 13:
        valid = False
        errmsg = "ISBN must have 13 digits"

    for digit in isbn:
        try:
            int(digit)
        except ValueError:
            valid = False
            errmsg = "Invalid characters found. Use digits 0-9 only"

    return valid, errmsg

def setStyle(style: str):
    if (style.lower() == "mla"):
        return MLA
    elif (style.lower() == "apa"):
        return APA
    elif (style.lower() == "chicago"):
        return CHICAGO
    elif (style == "" or style.lower() == "default"):
        return DEFAULT
    else:
        print("Warning: Invalid parameter. Style set to DEFAULT.")
        return DEFAULT

def parseInput(input: list[str]):
    input_parameters = {}
    valid = True
    errmsg = ""

    index = 0

    number_of_parameters = len(input)
    if number_of_parameters == 0:
        errmsg = "No input found"
        valid = False
        return valid, input_parameters, errmsg

    option_1 = input[index]
    if option_1 == "-f":
        try:
            input_parameters["ISBN"] = input[index + 1]
        except IndexError:
            valid = False
            errmsg = "No ISBN given: -f must be followed by ISBN number"
            return valid, input_parameters, errmsg
        
        if input_parameters["ISBN"] == "-s":
            valid = False
            errmsg = "No ISBN found: -f must be followed by ISBN number"
            return valid, input_parameters, errmsg
        
    elif option_1 == "-s":
        try:
            input_parameters["Style"] = setStyle(input[index + 1])
        except IndexError:
            valid = False
            errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
            return valid, input_parameters, errmsg
        
        if input[index + 1] == "-f":
            valid = False
            errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
            return valid, input_parameters, errmsg
    else:
        valid = False
        errmsg = "Invalid input parameters"
        return valid, input_parameters, errmsg
        
    if number_of_parameters > 2:
        index = 2
        option_2 = input[index]
        if option_2 == "-f":
            try:
                input_parameters["ISBN"] = input[index + 1]
            except IndexError:
                valid = False
                errmsg = "No ISBN given: -f must be followed by ISBN number"
                return valid, input_parameters, errmsg
            
            if input_parameters["ISBN"] == "-s":
                valid = False
                errmsg = "No ISBN found: -f must be followed by ISBN number"
                return valid, input_parameters, errmsg
            
        elif option_2 == "-s":
            try:
                input_parameters["Style"] = setStyle(input[index + 1])
            except IndexError:
                valid = False
                errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
                return valid, input_parameters, errmsg
            
            if input[index + 1] == "-f":
                valid = False
                errmsg = "No Style given: -s must be follow by one of [mla, apa, chicago, default]"
                return valid, input_parameters, errmsg
        else:
            valid = False
            errmsg = "Invalid input parameters"
            return valid, input_parameters, errmsg

    if not "ISBN" in input_parameters.keys():
        valid = False
        errmsg = "No ISBN given: -f is required"
    
    if not "Style" in input_parameters.keys():
        input_parameters["Style"] = DEFAULT
            
    return valid, input_parameters, errmsg

def parseAndValidateInput(input: list[str]):
    
    valid, input_parameters, errmsg = parseInput(input)

    if not valid:
        print("Error: ", errmsg)
        displayUsage()
    else:
        valid, errmsg = validateISBN(input_parameters["ISBN"])

        if not valid:
            print("Error: ", errmsg)
            displayUsage()
        else:
            return input_parameters
    return {}
