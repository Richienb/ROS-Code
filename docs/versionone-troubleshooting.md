# Troubleshooting ROS Code

### ROS Code Error Code Explanations:
#### View The Explanations For All Error Codes Given By ROS Code.

|Error Code|Causing Functions|What Happened|How To Fix|
|:---------|:----------------|:------------|:---------|
|0001|throwerror(errortext)|An error was forced by the user.|Nothing. This error code (0001) must be provided so people know it was a custom-defined error.|
|0002|equation(operation, firstnum, secondnum)|Either the first number (firstnum) or the second number (secondnum) is not a number.|Ensure you are providing an actual number to the firstnum and secondnum variables.|
|0003|equation(operation, firstnum, secondnum)|The operation that you specified does not exist.|Ensure you use *plus*, *minus*, *multiply* or *divide* in the operation variable.|
|0004|randomstr(valuelist)|You haven't specified a list.|Make sure you've specified a list.|
|0005|debugstate(state)|You entered an invalid debug state.|Ensure you use *Enable* or *Disable* in the state variable.|
|0006|debug_varglobal() or debug_supresswarnings()|You tried to use a debug command when debug mode was disabled.|Enable debug mode by typing *ros.debugstate('Enable')*.|
|0007|dirtool(operation, directory)|The directory you specified doesn't exist.|Enter a directory that doesn't exist.|
|0008|dirtool(operation, directory) or convertsymbol(value, command)|An invalid operation has been entered.|Enter Either *exists* or *delete* in the operation variable.|
|0009|dirtool(operation, directory)|The directory you entered doesn't exist.|Enter a directory that exists.|
|0010|filedownload(source, destination)|An error has occurred while downloading the file.|Check the download URL.|
|0011|filedownload(source, destination)|The source or destination you entered is invalid.|Check the source or destination.|
|0012|file(operation, path)|The file you specified doesn't exist.|Check that the file actually exists.|
|0013|file(operation, path)|The file you specified already exists.|Check that the file doesn't exists.|
|0014|convertsymbol(value, command)|You entered an invalid symbol value.|Try another value.|
|0015|convertsymbol(value, command)|You entered an invalid symbol.|Try another symbol.|
|0016|randomnum(minimum, maximum)|You entered an invalid number.|Make sure the value is actually a number.|
|0017|openurl(url), newwindow(url) or newtab(url)|The URL was unable to open.|Check The URL or try another one.|
