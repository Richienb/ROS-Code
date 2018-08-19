def parse(inputtext):

    # If text starts with imp

    if inputtext.startswith("imp"):
        return "import " + inputtext.split(" ")[1]
