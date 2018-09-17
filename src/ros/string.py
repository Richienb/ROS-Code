def catwalk(text):
    """

    Replace multiple spaces with a single space
    For example replace 'this  is    a long  sentence' with 'this is a long sentence'

    text:
    Specify the text to fix

    """

    return ' '.join(text.split())


def converttabs(text, spaces=4):
    """

    Convert all the tabs to a specific amount of spaces

    text:
    The text to convert tabs to spaces on

    spaces:
    The amount of spaces to replace tabs to. Default is 4.

    """

    return text.replace('\t', ' ' * spaces)


def shortentext(text, minlength, placeholder='...'):
    """

    Shorten some text by replacing the last part with a placeholder (such as '...')

    text:
    The text to shorten

    minlength:
    The minimum length before a shortening will occur

    placeholder:
    The text to append after removing protruding text. Default is '...'.

    """

    return textwrap.shorten(text, minlength, placeholder=str(placeholder))


def wraptext(text, maxlength):
    """

    Wrap text around the execution window according to a given size

    text:
    The text to be wraped

    maxlength:
    The amount of text until a wrap will be added

    """

    return textwrap.wrap(text, maxlength)


def unindent(text):
    """

    Remove indention for some text

    text:
    The text to unindent

    """

    return textwrap.dedent(text)


def paraspace(paragraphspaces=1):
    """

    Print 1 or more paragraph spaces in the terminal output

    paragraphspaces:
    The amount of paragraph spaces to print. Default is 1.

    """

    for _ in range(paragraphspaces):
        print('', end='\n')


# Choose A Random Item From A List


def randomstr(valuelist):
    try:
        return random.choice(valuelist)
    except IndexError:
        raise RuntimeError('An Error Has Occured: List Not Specified (0018)')


def case(text, format='sentence'):
    """
    
    Change the casing of some text
    
    text:
    The text to change the casing of
    
    format:
    The format of casing to apply to the text. Default is sentence.
    
    """
    if format == 'uppercase':
        return str(text.upper())
    elif format == 'lowercase':
        return str(text.lower())
    elif format == 'sentence':
        return str(text[0].upper()) + str(text[1:])
    elif format == 'caterpillar':
        return str(text.lower().replace(" ", "_"))
