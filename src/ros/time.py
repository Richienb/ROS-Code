# Time modules
import datetime
import time
import calendar

# Get The Day Of The Week For A Specific Day


def dayofweek(day, month, year, formatresult=True):
    if formatresult is False:
        return calendar.weekday(year, month, day) + 1
    else:
        days = {0: 'Monday', 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
        return days[calendar.weekday(year, month, day)]


# Check If A Year Is A Leap Year


def leapyear(year, querytype='is'):
    querytype = querytype.lower()
    if querytype == 'is':
        return calendar.isleap(year)
    elif querytype == 'closest':
        return year % 4

# Convert A Time Period To Another One


def converttime(time, currentformat, newformat):
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

# Get Maximum And Minimum Years


def yearlimit(limittype):
    if limittype == 'min':
        return datetime.MINYEAR
    elif limittype == 'max':
        return datetime.MAXYEAR
    else:
        raise RuntimeError(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Get The Timezone Code


def timezone():
    return time.timezone

# Get The Time Since 00:00 On 1 January 1970


def timesince():
    return time.time()

# Get The Current Date Or Time


def getdatetime(timedateformat='complete'):
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
