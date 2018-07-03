# line 1
'A module docstring.'

import sys
import inspect
# line 5

# line 7


def spam(a, b, c, d=3, xxx_todo_changeme=(4, (5,)), *g, **h):
    (e, (f,)) = xxx_todo_changeme
    eggs(b + d, c + f)

# line 11


def eggs(x, y):
    "A docstring."
    global fr, st
    fr = inspect.currentframe()
    st = inspect.stack()
    p = x
    q = y // 0

# line 20


class StupidGit:
    """A longer,

    indented

    docstring."""
# line 27

    def abuse(self, a, b, c):
        """Another

\tdocstring

        containing

\ttabs
\t
        """
        self.argue(a, b, c)
# line 40

    def argue(self, a, b, c):
        try:
            spam(a, b, c)
        except BaseException:
            self.ex = sys.exc_info()
            self.tr = inspect.trace()

# line 48


class MalodorousPervert(StupidGit):
    pass


class ParrotDroppings:
    pass


class FesteringGob(MalodorousPervert, ParrotDroppings):
    pass
