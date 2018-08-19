import importlib
def parse(inputtext):
 if inputtext.startswith("imp"):
  return "import "+inputtext.split(" ")[1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
