# line 1
def wrap(foo=None):
    def wrapper(func):
        return func
    return wrapper

# line 7


def replace(func):
    def insteadfunc():
        print 'hello'
    return insteadfunc

# line 13


@wrap()
@wrap(wrap)
def wrapped():
    pass

# line 19


@replace
def gone():
    pass


# line 24
def oll(m):
    return m

# line 27


def tll(g):
    return g and \
        g and \
        g

# line 32


def tlli(d):
    return d and \
        d

# line 36


def onelinefunc():
    pass

# line 39


def manyargs(arg1, arg2,
             arg3, arg4): pass

# line 43


def twolinefunc(m):
    return m and \
        m


# line 47
a = [None,
     lambda x: x,
     None]

# line 52


def setfunc(func):
    globals()["anonymous"] = func


setfunc(lambda x, y: x * y)

# line 57


def with_comment():  # hello
    world


# line 61
multiline_sig = [
    lambda x_y: x_y[0] + x_y[1],
    None,
]

# line 68


def func69():
    class cls70:
        def func71():
            pass
    return cls70


extra74 = 74

# line 76


def func77():
    pass


(extra78, stuff78) = 'xy'
extra79 = 'stop'

# line 81


class cls82:
    def func83(): pass


(extra84, stuff84) = 'xy'
extra85 = 'stop'

# line 87


def func88():
    # comment
    return 90

# line 92


def f():
    class X:
        def g():
            "doc"
            return 42
    return X


method_in_dynamic_class = f().g.im_func
