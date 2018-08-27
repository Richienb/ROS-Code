import unittest as ut
import ros.main

class TestCode(ut.TestCase):

    def test_colourcode(self):
        self.assertEqual(ros.main.colourcode('#212121', 'hex', True), '#212121')

    def test_changecolour(self):
        self.assertEqual(str(ros.main.changecolour('#212121', 'red', 10)), '#192121')

    def test_catwalk(self):
        self.assertEqual(
            ros.string.catwalk('this     is    some    text'), 'this is some text')

    def test_isprime(self):
        self.assertEqual(ros.math.isprime(1), False)
        self.assertEqual(ros.math.isprime(27), False)
        self.assertEqual(ros.math.isprime(52), False)
        self.assertEqual(ros.math.isprime(7), True)
        self.assertEqual(ros.math.isprime(3), True)

    def test_absolutenum(self):
        self.assertEqual(ros.math.absolutenum(-54.26), 54.26)
        self.assertEqual(ros.math.absolutenum(-94), 94)
        self.assertEqual(ros.math.absolutenum(3 - 4j), 5.0)

    def test_splitstring(self):
        self.assertEqual(
            ros.main.splitstring('hello my name'), ['hello', 'my', 'name'])
        self.assertEqual(ros.main.splitstring('hello my name', '-'), ['hello my name'])
        self.assertEqual(
            ros.main.splitstring('hello-my-name', '-'), ['hello', 'my', 'name'])
        self.assertEqual(ros.main.splitstring('hello-my-name', '-', 0), 'hello')

    def test_sort(self):
        self.assertEqual(ros.main.sort(['d', 'a', 'c', 'b']), ['a', 'b', 'c', 'd'])
        self.assertEqual(
            ros.main.sort(['d', 'a', 'c', 'b'], None, True), ['d', 'c', 'b', 'a'])

    def test_pykeyword(self):
        self.assertEqual(ros.main.pykeyword('check', 'None'), True)
        self.assertEqual(ros.main.pykeyword('check', 'and'), True)
        self.assertEqual(ros.main.pykeyword('check', 'assert'), True)
        self.assertEqual(ros.main.pykeyword('check', 'blahblah'), False)

    def test_isfib(self):
        self.assertEqual(ros.maths.isfib(1), True)
        self.assertEqual(ros.maths.isfib(2), True)
        self.assertEqual(ros.maths.isfib(8), True)
        self.assertEqual(ros.maths.isfib(13), True)
        self.assertEqual(ros.maths.isfib(89), True)
        self.assertEqual(ros.maths.isfib(385), False)

    def test_psrgame(self):
        results = ["Tie", "Win", "Loose"]
        self.assertEqual(ros.fun.psrgame("paper") in results, True)
        self.assertEqual(ros.fun.psrgame("scissor") in results, True)
        self.assertEqual(ros.fun.psrgame("rock") in results, True)
        self.assertEqual(ros.fun.psrgame("papers") in results, True)
        self.assertEqual(ros.fun.psrgame("scissors") in results, True)
        self.assertEqual(ros.fun.psrgame("rocks") in results, True)

    def test_diceroll(self):
        results = [1, 2, 3, 4, 5, 6]
        resultsext = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(ros.fun.diceroll() in results, True)
        self.assertEqual(ros.fun.diceroll() in results, True)
        self.assertEqual(ros.fun.diceroll() in results, True)
        self.assertEqual(ros.fun.diceroll(1, 10) in resultsext, True)
        self.assertEqual(ros.fun.diceroll(1, 10) in resultsext, True)
        self.assertEqual(ros.fun.diceroll(1, 10) in resultsext, True)
        self.assertEqual(isinstance(ros.fun.diceroll(5), list), True)

    def test_yesnogame(self):
        results = ["Yes", "No"]
        resultsext = ["Yes", "No", "Maybe"]
        self.assertEqual(ros.fun.yesnogame() in results, True)
        self.assertEqual(ros.fun.yesnogame() in results, True)
        self.assertEqual(ros.fun.yesnogame() in results, True)
        self.assertEqual(ros.fun.yesnogame(True) in resultsext, True)
        self.assertEqual(ros.fun.yesnogame(True) in resultsext, True)
        self.assertEqual(ros.fun.yesnogame(True) in resultsext, True)

    def test_truthorliegame(self):
        results = ["Truth", "Maybe", "Lie"]
        self.assertEqual(ros.fun.truthorliegame() in results, True)
        self.assertEqual(ros.fun.truthorliegame() in results, True)
        self.assertEqual(ros.fun.truthorliegame() in results, True)

    def test_bintobool(self):
        self.assertEqual(ros.math.bintobool(0), False)
        self.assertEqual(ros.math.bintobool(1), True)

    def test_autosolve(self):
        self.assertEqual(ros.math.autosolve("1 + 1"), 2)
        self.assertEqual(ros.math.autosolve("1 plus 1"), 2)
        self.assertEqual(ros.math.autosolve("1 add 1"), 2)
        self.assertEqual(ros.math.autosolve("1 - 1"), 0)
        self.assertEqual(ros.math.autosolve("1 minus 1"), 0)
        self.assertEqual(ros.math.autosolve("1 subtract 1"), 0)
        self.assertEqual(ros.math.autosolve("1 * 1"), 1)
        self.assertEqual(ros.math.autosolve("1 times 1"), 1)
        self.assertEqual(ros.math.autosolve("1 multiply 1"), 1)
        self.assertEqual(ros.math.autosolve("1 / 1"), 1)
        self.assertEqual(ros.math.autosolve("1 divide 1"), 1)
        self.assertEqual(ros.math.autosolve("1 quotient 1"), 1)
        self.assertEqual(ros.math.autosolve("1 % 1"), 0)
        self.assertEqual(ros.math.autosolve("1 remainder 1"), 0)
        self.assertEqual(ros.math.autosolve("1 rem 1"), 0)

    def test_equation(self):
        self.assertEqual(ros.math.equation("plus", 2, 5), 7)
        self.assertEqual(ros.math.equation("plus", 365, 164), 529)
        self.assertEqual(ros.math.equation("minus", 5, 2), 3)
        self.assertEqual(ros.math.equation("minus", 976, 245), 731)
        self.assertEqual(ros.math.equation("multiply", 2, 5), 10)
        self.assertEqual(ros.math.equation("multiply", 5, 2), 10)
        self.assertEqual(ros.math.equation("multiply", 56, 15), 840)
        self.assertEqual(ros.math.equation("divide", 5, 2), 2.5)
        self.assertEqual(ros.math.equation("divide", 125, 5), 25)

    def test_scientific(self):
        self.assertAlmostEqual(ros.math.scientific(5, "log"), 0.69897000433)
        self.assertAlmostEqual(ros.math.scientific(0.5, "acos"), 1.0471975511965979)
        self.assertAlmostEqual(ros.math.scientific(0.5, "asin"), 0.5235987755982989)
        self.assertAlmostEqual(ros.math.scientific(0.5, "atan"), 0.4636476090008061)
        self.assertAlmostEqual(ros.math.scientific(5, "cos"), 0.28366218546)
        self.assertEqual(ros.math.scientific(5, "hypot", 12), 13)
        self.assertAlmostEqual(ros.math.scientific(5, "sin"), -0.95892427466)
        self.assertAlmostEqual(ros.math.scientific(5, "tan"), -3.38051500625)

    def test_lcm(self):
        self.assertEqual(ros.math.lcm(7, 9), 63)
        self.assertEqual(ros.math.lcm(10, 9), 90)
        self.assertEqual(ros.math.lcm(9, 8), 72)
        self.assertEqual(ros.math.lcm(6, 5), 30)
        self.assertEqual(ros.math.lcm(5, 4), 20)

    def test_hcf(self):
        self.assertEqual(ros.math.hcf(30, 10), 10)
        self.assertEqual(ros.math.hcf(78, 26), 26)
        self.assertEqual(ros.math.hcf(60, 68), 4)
        self.assertEqual(ros.math.hcf(70, 20), 10)
        self.assertEqual(ros.math.hcf(40, 24), 8)

    def test_factors(self):
        self.assertEqual(ros.math.factors(1), [1])
        self.assertEqual(ros.math.factors(2), [1, 2])
        self.assertEqual(ros.math.factors(4), [1, 2, 4])
        self.assertEqual(ros.math.factors(18), [1, 2, 3, 6, 9, 18])
        self.assertEqual(ros.math.factors(42), [1, 2, 3, 6, 7, 14, 21, 42])

    def test_randstring(self):
        self.assertEqual(len(ros.secure.randstring(5)), 5)
        self.assertEqual(type(ros.secure.randstring(5)), str)
        self.assertEqual(len(ros.secure.randstring()), 1)
        self.assertEqual(type(ros.secure.randstring()), str)

    def test_compare(self):
        self.assertEqual(ros.main.compare(1, 1, "and"), True)
        self.assertEqual(ros.main.compare(0, 1, "and"), False)
        self.assertEqual(ros.main.compare(True, True, "and"), True)
        self.assertEqual(ros.main.compare(False, False, "and"), False)
        self.assertEqual(ros.main.compare(True, False, "and"), False)
        self.assertEqual(ros.main.compare(1, 1, "or"), True)
        self.assertEqual(ros.main.compare(0, 1, "or"), True)
        self.assertEqual(ros.main.compare(True, False, "or"), True)
        self.assertEqual(ros.main.compare(1, 1, "is"), True)
        self.assertEqual(ros.main.compare(0, 1, "is"), False)


if __name__ == '__main__':
    ut.main()
