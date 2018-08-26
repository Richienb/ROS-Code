# Math modules
import math
import operator
import statistics
import random

from roserrors import *

# Automatically solve a simple maths problem


def autosolve(equation):
    try:
        num1 = int(equation.split(" ")[0])
    except ValueError:
        num1 = float(equation.split(" ")[0])
    try:
        num2 = int(equation.split(" ")[2])
    except ValueError:
        num2 = float(equation.split(" ")[2])
    if equation.split(" ")[1] in ["+", "plus", "add"]:
        return num1 + num2
    elif equation.split(" ")[1] in ["-", "minus", "subtract"]:
        return num1 - num2
    elif equation.split(" ")[1] in ["*", "times", "multiply"]:
        return num1 * num2
    elif equation.split(" ")[1] in ["/", "divide", "quotient"]:
        return num1 / num2
    elif equation.split(" ")[1] in ["%", "remainder", "rem"]:
        return num1 % num2


# Automatically solve a hard maths problem


def autohard(equation):
    try:
        num1 = int(equation.split(" ")[1])
    except ValueError:
        num1 = float(equation.split(" ")[1])
    if equation.split(" ")[0] == "log":
        return math.log(num1)
    elif equation.split(" ")[0] == "acos":
        return math.acos(num1)
    elif equation.split(" ")[0] == "asin":
        return math.asin(num1)
    elif equation.split(" ")[0] == "atan":
        return math.atan(num1)
    elif equation.split(" ")[0] == "cos":
        return math.cos(num1)
    elif equation.split(" ")[0] == "hypot":
        try:
            num2 = int(equation.split(" ")[2])
        except ValueError:
            num2 = float(equation.split(" ")[2])
        return math.hypot(num1, num2)
    elif equation.split(" ")[0] == "sin":
        return math.sin(num1)
    elif equation.split(" ")[0] == "tan":
        return math.tan(num1)

# Solve a simple maths equation manually (May be deprecated)


def equation(operation, firstnum, secondnum):
    if not isnum(firstnum) and isnum(secondnum):
        raise RuntimeError(
            'An Error Has Occured: One Of The Values Specified Is Not A Number (0002)'
        )
    if operation == 'plus':
        return (firstnum + secondnum)
    elif operation == 'minus':
        return (firstnum - secondnum)
    elif operation == 'multiply':
        return (firstnum * secondnum)
    elif operation == 'divide':
        if not secondnum == 0:
            return (firstnum / secondnum)
    else:
        raise RuntimeError(
            'An Error Has Occured: You Entered An Invalid Operation (0003)')


# Solve scientific operations manually (May be deprecated)


def scientific(number, operation, number2=None, logbase=10):
    if operation == 'log':
        return math.log(number, logbase)
    elif operation == 'acos':
        return math.acos(number)
    elif operation == 'asin':
        return math.asin(number)
    elif operation == 'atan':
        return math.atan(number)
    elif operation == 'cos':
        return math.cos(number)
    elif operation == 'hypot':
        return math.hypot(number, number2)
    elif operation == 'sin':
        return math.sin(number)
    elif operation == 'tan':
        return math.tan(number)

# Simplify A Fraction


def fracsimplify(numerator, denominator):
    if numerator == denominator:
        return '1/1'
    elif numerator > denominator:
        limit = int(numerator / 2)
    elif numerator < denominator:
        limit = int(denominator / 2)
    for i in range(2, limit):
        checknum = limit - i
        if numerator % checknum == 0 and denominator % checknum == 0:
            numerator = numerator / checknum
            denominator = denominator / checknum
    return str(int(numerator)) + '/' + str(int(denominator))


# Convert A Circle Measurement


def circleconvert(amount, currentformat, newformat):
    currentformat = currentformat.lower()
    newformat = newformat.lower()
    if currentformat == newformat:
        return amount
    if currentformat == 'radius':
        if newformat == 'diameter':
            return amount * 2
        elif newformat == 'circumference':
            return amount * 2 * math.pi
    elif currentformat == 'diameter':
        if newformat == 'radius':
            return amount / 2
        elif newformat == 'circumference':
            return amount * math.pi
    elif currentformat == 'circumference':
        if newformat == 'radius':
            return amount / math.pi / 2
        elif newformat == 'diameter':
            return amount / math.pi


# Get The Amount Of Numbers Divisible By A Number


def amountdiv(number, minnum, maxnum):
    amount = 0
    for i in range(minnum, maxnum + 1):
        if number % i == 0:
            amount += 1
    return amount


# Get A Constant


def constant(constanttype):
    constanttype = constanttype.lower()
    if constanttype == 'pi':
        return math.pi
    elif constanttype == 'e':
        return math.e
    elif constanttype == 'tau':
        return math.tau
    elif constanttype == 'inf':
        return math.inf
    elif constanttype == 'nan':
        return math.nan
    elif constanttype in ['phi', 'golden']:
        return (1 + 5**0.5) / 2


# Find The Power Of A Number


def power(number, power):
    return math.pow(number, power)


# Find The Square Root Of A number


def squareroot(number):
    return math.sqrt(number)


# Find the factorial of a number


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Do An Average Command


def average(numbers, averagetype='mean'):
    averagetype = averagetype.lower()
    try:
        statistics.mean(numbers)
    except BaseException:
        raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
    if averagetype == 'mean':
        return statistics.mean(numbers)
    elif averagetype == 'mode':
        return statistics.mode(numbers)
    elif averagetype == 'median':
        return statistics.median(numbers)
    elif averagetype == 'min':
        return min(numbers)
    elif averagetype == 'max':
        return max(numbers)
    elif averagetype == 'range':
        return max(numbers) - min(numbers)
    else:
        raise RuntimeError(
            'An Error Has Occured: You Entered An Invalid Operation (0003)')

# Check If A Number Is A Type


def numprop(value, propertyexpected):
    if propertyexpected == 'triangular':
        x = (math.sqrt(8 * value + 1) - 1) / 2
        return bool(x - int(x) > 0)
    elif propertyexpected == 'square':
        return math.sqrt(value).is_integer()
    elif propertyexpected == 'cube':
        x = value**(1 / 3)
        x = int(round(x))
        return bool(x**3 == value)
    elif propertyexpected == 'even':
        return value % 2 == 0
    elif propertyexpected == 'odd':
        return not value % 2 == 0
    elif propertyexpected == 'positive':
        return bool(value > 0)
    elif propertyexpected == 'negative':
        return bool(value < 0)
    elif propertyexpected == 'zero':
        return bool(value == 0)


# Toggle A Number Between Positive And Negative


def posnegtoggle(number):
    if bool(number > 0):
        return number - number * 2
    elif bool(number < 0):
        return number + abs(number) * 2
    elif bool(number == 0):
        return number

# Check If A Variable Is Infinite


def isinfinite(variable):
    return bool(math.isfinite(variable))


# Check if a variable is essetially "False"


def isfalse(variable):
    if variable in [0, 0.0, False, [], {}, math.nan, ""]:
        return True
    return False


# Get The Largest Integer Less Than Or Equal To


def less_or_equal(number):
    try:
        return math.floor(number)
    except BaseException:
        raise RuntimeError('An Error Has Occured: Number Not Provided (0016)')

# Compare 2 Values


def compare(value1, value2, comparison):
    if not isinstance(comparison, str):
        raise WrongInput("ERROR: comparison argument must be a string")
    if comparison not in ['is', 'or', 'and']:
        raise WrongInput(
            "ERROR: comparison argument must be 'is', 'or' or 'and'")
    if comparison == 'is':
        return operator.is_(value1, value2)
    elif comparison == 'or':
        return operator.or_(value1, value2)
    elif comparison == 'and':
        return operator.and_(value1, value2)

# Find all the factors of a number


def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


# Use Euler's Formula


def eulercalc(faces, edges, verticies):
    return verticies + edges - faces

# Get A Random Number


def randomnum(minimum, maximum):
    if isnum(minimum):
        if isnum(maximum):
            return random.randint(minimum, maximum)
        else:
            raise RuntimeError('Invalid Value (0016)')
    else:
        raise RuntimeError('Invalid Value (0016)')

# Check if a number is in the Fibonacci sequence


def isfib(number):
    num1 = 1
    num2 = 1
    while True:
        if num2 < number:
            tempnum = num2
            num2 += num1
            num1 = tempnum
        elif num2 == number:
            return True
        else:
            return False


def isprime(number):
    """

    Check if a number is a prime number

    number:
    The number to check

    """

    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Convert A Base 10 Number To A Custom Base


def convertbase(number, base=10):
    integer = number
    if not integer:
        return '0'
    sign = 1 if integer > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    integer *= sign
    while integer:
        integer, mod = divmod(integer, base)
        res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]

# Check If A Value Is Able To Be Converted To A Number (Decimal And Integer)


def isnum(value):
    try:
        return bool(isinstance(value, int) or isinstance(value, float))
    except BaseException:
        return False

# Get The Quadrant Of Coordinates


def quadrant(xcoord, ycoord):
    xneg = bool(xcoord < 0)
    yneg = bool(ycoord < 0)
    if xneg is True:
        if yneg is False:
            return 2
        return 3
    elif xneg is False:
        if yneg is False:
            return 1
        return 4


# Flip Coordinates Over A Specific Axis


def flipcoords(xcoord, ycoord, axis):
    axis = axis.lower()
    if axis == 'y':
        if xcoord > 0:
            return str(xcoord - xcoord - xcoord) + ', ' + str(ycoord)
        elif xcoord < 0:
            return str(xcoord + abs(xcoord) * 2) + ', ' + str(ycoord)
        elif xcoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
    elif axis == 'x':
        if ycoord > 0:
            return str(xcoord) + ', ' + str(ycoord - ycoord - ycoord)
        elif ycoord < 0:
            return str(ycoord + abs(ycoord) * 2) + ', ' + str(xcoord)
        elif ycoord == 0:
            return str(xcoord) + ', ' + str(ycoord)

# Find the lowest common multiple of 2 numbers


def lcm(num1, num2):
    if num1 > num2:
        bigger = num1
    else:
        bigger = num2
    while True:
        if bigger % num1 == 0 and bigger % num2 == 0:
            return bigger
        bigger += 1


# Find the lowest common multiple of 2 numbers


def hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            return i
