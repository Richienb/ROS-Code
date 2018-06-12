# ROS Code Commands

!!! warning "Documentation Version"
    The current version of this documentation complies with ROS Code [v1.11.0-release](https://github.com/Richienb/ROS-Code/releases/tag/v1.11.0-release)

| Command | Usage | Tip |
|:--------|:------|:----|
|isprime(number)|Check If A Number Is A Prime Number| |
|paraspace(paragraphspaces=1)|Make A Paragraph Space|Change paragraphspaces=1 to the amount of paragraph spaces you want to make.|
|splitstring(string, split_character=' ')|Split A String|Change split_character=' ' to the character you want to split your string by.|
|sort(list, key=None)|Sort A List|Change key=None to customize the sorting otherwise it will be sorted in alphabetical order.|
|pykeyword(operation='list', keywordtotest=None)|Check If A Keyword Relates To Python|operation='list' can be changed to 'list' or 'check'. If You want to check if a keyword relates to python change the operation to 'check' and enter the keyword you want to check in keywordtotest=None.|
|isfib(number)|Check If A Number Is In The Fibonacci Sequence| |
|bintobool(integer)|Convert 0 Or 1 To False Or True|Change integer to 0 to get True And 1 to get False.|
|modulereload(modulename)|Reload A Module| |
|exitexecution(arguments=None)|Exit The Execution|Change arguments=None to use custom arguments.|
|warnconfig(action='default')|Configure Warnings|action='default' can be changed to default, error, ignore, always, module and once.|
|pycopyright()|Print Python Copyright Information| |
|message_print(text)|Print A Message| |
|equation(operation, firstnum, secondnum)|Solve A Maths Equation|operation can be changed to plus, minus, multiply and divide.|
|scientific(number, operation, logbase=10)|Preform Scientific Operations|operation can be changed to log, acos, asin, atan, cos, hypot, sin and tan. logbase=10 can be changed to the base of the number you are using for log-based operations.
|compare(value1, value2, comparision)|Compare 2 Values|comparison can be changed to or, is or and.|
|comparenum(value1, value2, comparison)|Compare 2 Numbers|comparison can be changed to equals, not equal, less than, greater than(or more than), less than or equal to and greater than or equal to(or more than or equal to).|
|dayofweek(day, month, year, format=True)|Get The Day Of The Week For A Specific Day|format=True can be changed to False to return the day id instead of the day name for example 1, 2, 3, 4, 5 for Monday, Tuesday, Wednesday, Thursday, Friday.|
|leapyear(year, querytype='is')|Check If A Year Is A Leap Year|querytype='is' can be changed to is to check if a year is a leap year and closest to find how many years after or before the closest leap year.|
|tokhex(length=10, urlsafe=False)|Return A Random String In Hexadecimal|Changing length=10 to another number changes the length of the random string and change urlsafe=False to True will make the random string URL-safe.|
|face(facetype='smiley')|Show A Type Of Face|facetype='smiley' can be changed to smiley, straight or sad|
|constant(constanttype)|Get A Constant|constanttype can be changed to pi, e, tau, inf or nan|
|power(number, power)|Find The Power Of A Number| |
|squareroot(number)|Find The Squareroot Of A Number| |
|average(numbers, type='mean')|Do An Average Command|mean can be changed to mean, mode, median, mix, max or range|
|throwerror(errortext)|Throw A Runtime Error| |
|store(value)|Store A Value In The ros_stored Variable| |
|delay(seconds)|Delay For A Specific Amount Of Seconds| |
|wait_enter()|Waits For The User To Press Enter| |
|convertstring(value)|Convert A Variable To A String| |
|opposite(boolean)|Return The Opposite Of A Boolean| |
|isdecimal(value)|Check If A Number Is A Decimal| |
|isstring(variable)|Check If A Variable Is A String| |
|istype(variable, typeexpected)|Check If A Variable Is A Specific Type|typeexpected can be changed to anything(string, integer, float...)|
|isinteger(value)|Check If A Number Is An Integer (Full Number)| |
|isboolean(value)|Check For A Boolean| |
|isnumber(value)|Check If A Value Is Convertable To A Number (Decimal And Integer)| |
|happybirthday(person)|Sing Happy Birthday| |
|case(variable, argument='uppercase')|Change The Casing Of Text|argument='uppercase' can be changed to uppercase, lowercase and sentence|
|numprop(value, propertyexpected)|Check If A Number Is A Type|propertyexpected can be changed to triangular, square, cube, even, odd, positive, negative and zero|
|posnegtoggle(number)|Toggle A Number Between Positive And Negative| |
|difference(num1, num2)|Find The Difference Between 2 Numbers| |
|isempty(variable)|Check If A Variable Is Empty| |
|isinfinite(variable)|Check If A Variable Is Infinite| |
|length(value)|Find The Length Of A Value| |
|cowsay(text='', align='centre')|Simulate A Cow Saying Text|align can be changed to left, centre(or center) and right.|
|getletter(variable, letternumber)|Get The Corresponding Letter In A String|Change letternumber to get the corresponding letter in that place for example if variable is Hello World and letternumber is 2 you will get e.|
|chancegame(gamename='dice')|Play A Chance Game|You can also play dice, coin, truth and yes.|
|onlist(list, item)|Check If Something Is On The List| |
|charlimit()|Get The Character Limit| |
|unilimit()|Get The Highest Unicode Value| |
|platform()|Get The Current Platform| |
|less_or_equal(number)|Get The Largest Integer Less Than Or Equal To| |
|jointext(firststring, secondstring)|Join Two Strings| |
|dirtool(operation, directory)|Tools For Directories (If Exists, Make And Delete)|operation can be changed to exists, make and delete.|
|filedownload(source, destination)|Download A File| |
|file(operation, path)|Tools For Files (If Exists, Make And Delete)|operation can be changed to exists, make and delete.|
|text(operation, path, argument)|Tools For Text Files|argument can be changed to the text you want to use and operation can be changed to write or append.|
|about()|About Information| |
|convertbinary(value, argument)|Convert Text To Binary Form|argument can be to or from.|
|reversetext(text, ignoretype=False)|Make The Text Forwards Or Backwards|If you change ignoretype=False to True you will be given a string even if your number is not a string(for example an integer).|
|convertbase(number, base=10)|Convert A Base 10 Number To A Custom Base| |
|convertsymbol(value, command)|Convert A ASCII Value To A Symbol|command can be changed to from and to.|
|gettype(value)|Get The Type Of A Value| |
|availchar(charactertype)|Get All Available Charaters For A Type|charactertype can be letters, lowercase, uppercase, digits, hexdigits, punctuation, printable and whitespace.|
|wordvalue(word)|Get The Value Of A Word| |
|textbetween(variable, firstnum=None, secondnum=None, type='regular')|Get The Text Between Two Parts|You can change type='regular' to regular, toend or tostart.|
|letternum(letter)|Get The Number Corresponding To A Letter| |
|yearlimit(limittype)|Get Maximum And Minimum Years|This is the maximum and minimum years your computer can handle before crashing. limittype can be changed to min and max.|
|timezone()|Get The Timezone Code| |
|randomnum(minimum, maximum)|Get A Random Number| |
|openurl(url)|Open A Link In A Webbrowser| |
|newwindow(url)|Open A Link In A New Window Of A Webbrowser| |
|newtab(url)|Open A Link In A New Tab Of A Webbrowser| |
|getbrowser()|Get The Name Of The Browser Currently Being Used| |
|randomstr(valuelist)|Choose A Random Item From A List| |
|timesince()|Get The Time Since 00:00 On 1 January 1970| |
|userinput(prompttext)|Get User input|The user will be prompted with prompttext and their response will be returned.|
|licence(raw=False)|Licence Information|If you change raw=False to True then icons will not be displayed.
