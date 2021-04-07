import re

class InvalidPostcodeError(Exception):
    pass

def is_valid(postcode):
    regex = re.compile('[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}')
    match = regex.match(str(postcode))
    return bool(match)

def format(postcode):
    postcode = postcode.upper()
    if postcode[-4] != ' ':
        postcode = postcode[:-3] + ' ' + postcode[-3:]

    if is_valid(postcode):
        return(postcode)
    else:
        raise InvalidPostcodeError
