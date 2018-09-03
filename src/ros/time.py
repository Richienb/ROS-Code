"""

All commands based around time functions

"""
import datetime
import time
import calendar


def dayofweek(day, month, year, formatresult=True):
    """
    
    Get the day of the week for a specific day
    
    day:
    The day to include in the search
    
    month:
    The month to include in the search
    
    year:
    The year to include in the search
    
    formatresult:
    Whether or not to format the result.
    A formatted date would look like: "Monday".
    A non formatted date would look like: 1.
    Default is True.
    
    """
    if formatresult is False:
        return calendar.weekday(year, month, day) + 1
    else:
        days = {
            0: 'Monday',
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return days[calendar.weekday(year, month, day)]


def leapyear(year):
    """
    
    Check if a year in particular is a leap year
    
    year:
    The year to check for
    
    """
    return bool(calendar.isleap(year))


def closeyear(year):
    """
    
    Find how many years away was the closest leap year to a specific year
    
    """
    return int(year % 4)


def converttime(time, currentformat, newformat):
    """
    
    Convert a specific time format to another type
    
    time:
    The time to convert
    
    currentformat:
    The current format of the time.
    Can be seconds, milliseconds, minutes, hours, days, weeks, fortnights, years, decades, centuaries or millenniums.
    
    newformat:
    The new format of the time.
    Can be seconds, milliseconds, minutes, hours, days, weeks, fortnights, years, decades, centuaries or millenniums.
    
    """
    currentformat = currentformat.lower()
    newformat = newformat.lower()
    if currentformat == newformat:
        return time
    if currentformat == 'seconds':
        if newformat == 'milliseconds':
            return time * 1000
        elif newformat == 'minutes':
            return time / 60
        elif newformat == 'hours':
            return time / 60 / 60
        elif newformat == 'days':
            return time / 60 / 60 / 24
        elif newformat == 'weeks':
            return time / 60 / 60 / 24 / 7
        elif newformat == 'fortnights':
            return time / 60 / 60 / 24 / 14
        elif newformat == 'years':
            return time / 60 / 60 / 24 / 365
        elif newformat == 'decades':
            return time / 60 / 60 / 24 / 365 / 10
        elif newformat == 'centuaries':
            return time / 60 / 60 / 24 / 365 / 100
        elif newformat == 'millenniums':
            return time / 60 / 60 / 24 / 365 / 1000
    elif currentformat == 'minutes':
        if newformat == 'milliseconds':
            return time * 60 * 1000
        elif newformat == 'seconds':
            return time * 60
        elif newformat == 'hours':
            return time / 60
        elif newformat == 'days':
            return time / 60 / 24
        elif newformat == 'weeks':
            return time / 60 / 24 / 7
        elif newformat == 'fortnights':
            return time / 60 / 24 / 14
        elif newformat == 'years':
            return time / 60 / 24 / 365
        elif newformat == 'decades':
            return time / 60 / 24 / 365 / 10
        elif newformat == 'centuaries':
            return time / 60 / 24 / 365 / 100
        elif newformat == 'millenniums':
            return time / 60 / 24 / 365 / 1000
    elif currentformat == 'hours':
        if newformat == 'milliseconds':
            return time * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 60 * 60
        elif newformat == 'minutes':
            return time / 60
        elif newformat == 'days':
            return time / 24
        elif newformat == 'weeks':
            return time / 24 / 7
        elif newformat == 'fortnights':
            return time / 24 / 14
        elif newformat == 'years':
            return time / 24 / 7 / 365
        elif newformat == 'decades':
            return time / 24 / 365 / 10
        elif newformat == 'centuaries':
            return time / 24 / 365 / 100
        elif newformat == 'millenniums':
            return time / 24 / 365 / 1000
    elif currentformat == 'days':
        if newformat == 'milliseconds':
            return time * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 24 * 60
        elif newformat == 'hours':
            return time * 24
        elif newformat == 'weeks':
            return time / 24 / 7
        elif newformat == 'fortnights':
            return time / 60 / 24 / 14
        elif newformat == 'years':
            return time / 60 / 24 / 7 / 365
        elif newformat == 'decades':
            return time / 7 / 365 / 10
        elif newformat == 'centuaries':
            return time / 7 / 365 / 100
        elif newformat == 'millenniums':
            return time / 7 / 365 / 1000
    elif currentformat == 'weeks':
        if newformat == 'milliseconds':
            return time * 7 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 7 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 7 * 24 * 60
        elif newformat == 'hours':
            return time * 7 * 24
        elif newformat == 'fortnights':
            return time * 7 / 14
        elif newformat == 'years':
            return time * 7 / 365
        elif newformat == 'decades':
            return time * 7 / 365 / 10
        elif newformat == 'centuaries':
            return time * 7 / 365 / 100
        elif newformat == 'millenniums':
            return time * 7 / 365 / 1000
    elif currentformat == 'fortnights':
        if newformat == 'milliseconds':
            return time * 14 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 14 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 14 * 24 * 60
        elif newformat == 'hours':
            return time * 14 * 24
        elif newformat == 'weeks':
            return time * 14
        elif newformat == 'years':
            return time * 14 / 365
        elif newformat == 'decades':
            return time * 14 / 365 / 10
        elif newformat == 'centuaries':
            return time * 14 / 365 / 100
        elif newformat == 'millenniums':
            return time * 14 / 365 / 1000
    elif currentformat == 'years':
        if newformat == 'milliseconds':
            return time * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 365 * 24
        elif newformat == 'days':
            return time * 365
        elif newformat == 'weeks':
            return time * 365 / 7
        elif newformat == 'fortnights':
            return time * 365 / 14
        elif newformat == 'decades':
            return time / 10
        elif newformat == 'centuaries':
            return time / 100
        elif newformat == 'millenniums':
            return time / 1000
    elif currentformat == 'decades':
        if newformat == 'milliseconds':
            return time * 10 * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 10 * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 10 * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 10 * 365 * 24
        elif newformat == 'days':
            return time * 10 * 365
        elif newformat == 'weeks':
            return time * 10 * 365 / 7
        elif newformat == 'fortnights':
            return time * 10 * 365 / 14
        elif newformat == 'years':
            return time * 10
        elif newformat == 'centuaries':
            return time * 10 / 100
        elif newformat == 'millenniums':
            return time * 10 / 1000
    elif currentformat == 'centuaries':
        if newformat == 'milliseconds':
            return time * 100 * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 100 * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 100 * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 100 * 365 * 24
        elif newformat == 'days':
            return time * 100 * 365
        elif newformat == 'weeks':
            return time * 100 * 365 / 7
        elif newformat == 'fortnights':
            return time * 100 * 365 / 14
        elif newformat == 'years':
            return time * 100
        elif newformat == 'decades':
            return time * 100 / 10
        elif newformat == 'millenniums':
            return time * 100 / 1000
    elif currentformat == 'millenniums':
        if newformat == 'milliseconds':
            return time * 1000 * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 1000 * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 1000 * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 1000 * 365 * 24
        elif newformat == 'days':
            return time * 1000 * 365
        elif newformat == 'weeks':
            return time * 1000 * 365 / 7
        elif newformat == 'fortnights':
            return time * 1000 * 365 / 14
        elif newformat == 'years':
            return time * 1000
        elif newformat == 'decades':
            return time * 1000 / 10
        elif newformat == 'centuaries':
            return time * 1000 / 100


def minyear():
    """
    
    Get the minimum year allowed by the current OS.
    
    """
    return datetime.MINYEAR


def maxyear():
    """
    
    Get the maxiumum year allowed by the current OS.
    
    """
    return datetime.MAXYEAR


def timezone():
    """
    
    Get the current timezone code.
    
    """
    return time.timezone


def timesince():
    """
    
    Get the amount of time since 00:00 on 1 January 1970, the raw date before formatting by computers.
    
    """
    return time.time()


def getdatetime(timedateformat='complete'):
    """
    
    Get the current date or time in a specific format
    
    timedateformat:
    The type of date to query for.
    Can be day, month, year, hour, minute, second, millisecond, yearmonthday, daymonthyear, hourminutesecond, secondminutehour, complete, datetime or timedate.
    Default is "complete".
    
    """
    timedateformat = timedateformat.lower()
    if timedateformat == 'day':
        return ((str(datetime.datetime.now())).split(' ')[0]).split('-')[2]
    elif timedateformat == 'month':
        return ((str(datetime.datetime.now())).split(' ')[0]).split('-')[1]
    elif timedateformat == 'year':
        return ((str(datetime.datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hour':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[0]
    elif timedateformat == 'minute':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[1]
    elif timedateformat == 'second':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[2]
    elif timedateformat == 'millisecond':
        return (str(datetime.datetime.now())).split('.')[1]
    elif timedateformat == 'yearmonthday':
        return (str(datetime.datetime.now())).split(' ')[0]
    elif timedateformat == 'daymonthyear':
        return ((str(datetime.datetime.now())).split(' ')[0]).split(
            '-')[2] + '-' + ((str(
                datetime.datetime.now())).split(' ')[0]).split('-')[1] + '-' + (
                    (str(datetime.datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hourminutesecond':
        return ((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
    elif timedateformat == 'secondminutehour':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[2] + ':' + (((str(datetime.datetime.now())).split(
                   ' ')[1]).split('.')[0]).split(':')[1] + ':' + (
                       ((str(datetime.datetime.now())).split(' ')[1]
                       ).split('.')[0]).split(':')[0]
    elif timedateformat == 'complete':
        return str(datetime.datetime.now())
    elif timedateformat == 'datetime':
        return (str(datetime.datetime.now())).split('.')[0]
    elif timedateformat == 'timedate':
        return ((str(
            datetime.datetime.now())).split('.')[0]).split(' ')[1] + ' ' + (
                (str(datetime.datetime.now())).split('.')[0]).split(' ')[0]


def timeit(command, round=True):
    """
    
    Time how long a command takes to execute
    
    command:
    The command to time.
    
    round:
    Whether or not to round the number to an integer. Default is True.
    
    """
    t1 = time.clock()
    exec(command)
    t2 = time.clock()
    if round == True:
        return int(t2 - t1)
    return t2 - t1
