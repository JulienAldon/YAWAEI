import re
from .constants import INTRA_LINK

def execRegex(regex, string):
    """Check if regex match in string

    :params regex: A regex
    :type regex: str
    :params string: A string to match the *regex*
    :returns: A boolean, True if *regex* is found in *string* False otherwise
    :rtype: bool
    """
    matches = re.finditer(regex, string, re.MULTILINE)
    for match in matches:
        if match:
            return True
    return False

def check_autologin(autologin):
    """Check Autologin format
    
    :param autologin: An Epitech Intranet autologin url (found under the administration tab on the Epitech intranet) 
    :type autologin: str
    :returns: A correctly formated autologin url if the format is correct, False otherwise
    :rtype: str
    """
    if execRegex(r'^http://', autologin):
        autologin = autologin.replace('http', 'https')
    if execRegex(rf'^{INTRA_LINK}/auth-[0-9a-fA-F]+$', autologin):
        autologin = 'https://' + autologin
        return autologin
    elif execRegex(r'^auth-[0-9a-fA-F]+$', autologin):
        return f'https://intra.epitech.eu/' + autologin
    elif execRegex(rf'^https://{INTRA_LINK}/auth-[0-9a-fA-F]+$', autologin):
        return autologin
    return False
