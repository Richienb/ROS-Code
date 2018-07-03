import sys
print sys.platform
try:
    try:
        raise KeyError
    except KeyError:
        # no bug
        print 'Your JVM seems to be working'
except BaseException:
    print 'Your JVM seems broken'
