import re

class InvalidPostcodeError(Exception):
    pass

def is_valid(postcode):
    regex = re.compile('[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}')
    match = regex.match(str(postcode))
    return bool(match)

def format(postcode):    #Formats given string into valid postcode
    if not is_valid(postcode):   #Only complete steps if not already formatted
        postcode = postcode.upper()
        postcode = postcode.replace(" ", "")   #Reformats a postcode if the space(s) are in the incorrect place.
        postcode = postcode[:-3] + ' ' + postcode[-3:]   #Adds space into correct place.

        if not is_valid(postcode):   #If postcode is still invalid, the provided string cannot be formatted into a real postcode.
            raise InvalidPostcodeError

    return postcode
