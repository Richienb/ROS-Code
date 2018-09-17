"""

Secure functions.

"""

def randstring(length=1):
    """
    
    Generate a random string consisting of letters, digits and punctuation
    
    length:
    The length of the generated string. Default is 1
    
    """
    charstouse = string.ascii_letters + string.digits + string.punctuation
    newpass = ''
    for _ in range(length):
        newpass += str(charstouse[random.randint(0, len(charstouse) - 1)])
    return newpass


# Return A Random String In Hexadecimal


def tokhex(length=10, urlsafe=False):
    if urlsafe is True:
        return secrets.token_urlsafe(length)
    return secrets.token_hex(length)
