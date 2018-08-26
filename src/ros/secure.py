
# Generate a completely random string


def randstring(length=1):
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
