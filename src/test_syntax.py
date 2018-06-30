import unittest as ut
import syntax as s


class TestCode(ut.TestCase):

    def test_colourcode(self):
        self.assertEqual(s.colourcode('#212121', 'hex', True), '#212121')

    def test_changecolour(self):
        self.assertEqual(str(s.changecolour('#212121', 'red', 10)), '#192121')

    def test_catwalk(self):
        self.assertEqual(
            s.catwalk('this     is    some    text'), 'this is some text')

    def test_isprime(self):
        self.assertEqual(s.isprime(1), False)
        self.assertEqual(s.isprime(27), False)
        self.assertEqual(s.isprime(52), False)
        self.assertEqual(s.isprime(7), True)
        self.assertEqual(s.isprime(3), True)

    def test_absolutenum(self):
        self.assertEqual(s.absolutenum(-54.26), 54.26)
        self.assertEqual(s.absolutenum(-94), 94)
        self.assertEqual(s.absolutenum(3 - 4j), 5.0)

    def test_splitstring(self):
        self.assertEqual(s.splitstring('hello my name'),
                         ['hello', 'my', 'name'])
        self.assertEqual(s.splitstring(
            'hello my name', '-'), ['hello my name'])
        self.assertEqual(s.splitstring('hello-my-name', '-'),
                         ['hello', 'my', 'name'])
        self.assertEqual(s.splitstring('hello-my-name', '-', 0), 'hello')

    def test_sort(self):
        self.assertEqual(s.sort(['d', 'a', 'c', 'b']), ['a', 'b', 'c', 'd'])
        self.assertEqual(s.sort(['d', 'a', 'c', 'b'], None, True), [
                         'd', 'c', 'b', 'a'])

    def test_pykeyword(self):
        import keyword
        self.assertEqual('None' in keyword.kwlist, True)
        self.assertEqual('and' in keyword.kwlist, True)
        self.assertEqual('assert' in keyword.kwlist, True)
        self.assertEqual('blahblah' in keyword.kwlist, False)
        self.assertEqual(s.pykeyword('check', 'None'), True)
        self.assertEqual(s.pykeyword('check', 'and'), True)
        self.assertEqual(s.pykeyword('check', 'assert'), True)
        self.assertEqual(s.pykeyword('check', 'blahblah'), False)

    def test_isfib(self):
        self.assertEqual(s.isfib(1), True)
        self.assertEqual(s.isfib(2), True)
        self.assertEqual(s.isfib(8), True)
        self.assertEqual(s.isfib(13), True)
        self.assertEqual(s.isfib(89), True)
        self.assertEqual(s.isfib(385), False)

    def test_psrgame(self):
        results = ["Tie", "Win", "Loose"]
        self.assertEqual(s.psrgame("paper") in results, True)
        self.assertEqual(s.psrgame("scissor") in results, True)
        self.assertEqual(s.psrgame("rock") in results, True)
        self.assertEqual(s.psrgame("papers") in results, True)
        self.assertEqual(s.psrgame("scissors") in results, True)
        self.assertEqual(s.psrgame("rocks") in results, True)

    def test_diceroll(self):
        results = [1, 2, 3, 4, 5, 6]
        resultsext = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(s.diceroll() in results, True)
        self.assertEqual(s.diceroll() in results, True)
        self.assertEqual(s.diceroll() in results, True)
        self.assertEqual(s.diceroll(1, 10) in resultsext, True)
        self.assertEqual(s.diceroll(1, 10) in resultsext, True)
        self.assertEqual(s.diceroll(1, 10) in resultsext, True)
        self.assertEqual(isinstance(s.diceroll(5), list), True)

    def test_yesnogame(self):
        results = ["Yes", "No"]
        resultsext = ["Yes", "No", "Maybe"]
        self.assertEqual(s.yesnogame() in results, True)
        self.assertEqual(s.yesnogame() in results, True)
        self.assertEqual(s.yesnogame() in results, True)
        self.assertEqual(s.yesnogame(True) in resultsext, True)
        self.assertEqual(s.yesnogame(True) in resultsext, True)
        self.assertEqual(s.yesnogame(True) in resultsext, True)

    def test_truthorliegame(self):
        results = ["Truth", "Maybe", "Lie"]
        self.assertEqual(s.truthorliegame() in results, True)
        self.assertEqual(s.truthorliegame() in results, True)
        self.assertEqual(s.truthorliegame() in results, True)

    def test_bintobool(self):
        self.assertEqual(s.bintobool(0), False)
        self.assertEqual(s.bintobool(1), True)

    def test_autosolve(self):
        self.assertEqual(s.autosolve("1 + 1"), 2)
        self.assertEqual(s.autosolve("1 plus 1"), 2)
        self.assertEqual(s.autosolve("1 add 1"), 2)
        self.assertEqual(s.autosolve("1 - 1"), 0)
        self.assertEqual(s.autosolve("1 minus 1"), 0)
        self.assertEqual(s.autosolve("1 subtract 1"), 0)
        self.assertEqual(s.autosolve("1 * 1"), 1)
        self.assertEqual(s.autosolve("1 times 1"), 1)
        self.assertEqual(s.autosolve("1 multiply 1"), 1)
        self.assertEqual(s.autosolve("1 / 1"), 1)
        self.assertEqual(s.autosolve("1 divide 1"), 1)
        self.assertEqual(s.autosolve("1 quotient 1"), 1)
        self.assertEqual(s.autosolve("1 % 1"), 0)
        self.assertEqual(s.autosolve("1 remainder 1"), 0)
        self.assertEqual(s.autosolve("1 rem 1"), 0)

    def test_equation(self):
        self.assertEqual(s.equation("plus", 2, 5), 7)
        self.assertEqual(s.equation("plus", 365, 164), 529)
        self.assertEqual(s.equation("minus", 5, 2), 3)
        self.assertEqual(s.equation("minus", 976, 245), 731)
        self.assertEqual(s.equation("multiply", 2, 5), 10)
        self.assertEqual(s.equation("multiply", 5, 2), 10)
        self.assertEqual(s.equation("multiply", 56, 15), 840)
        self.assertEqual(s.equation("divide", 5, 2), 2.5)
        self.assertEqual(s.equation("divide", 125, 5), 25)

    def test_scientific(self):
        self.assertAlmostEqual(s.scientific(5, "log"), 0.69897000433)
        self.assertAlmostEqual(s.scientific(0.5, "acos"), 1.0471975511965979)
        self.assertAlmostEqual(s.scientific(0.5, "asin"), 0.5235987755982989)
        self.assertAlmostEqual(s.scientific(0.5, "atan"), 0.4636476090008061)
        self.assertAlmostEqual(s.scientific(5, "cos"), 0.28366218546)
        self.assertEqual(s.scientific(5, "hypot", 12), 13)
        self.assertAlmostEqual(s.scientific(5, "sin"), -0.95892427466)
        self.assertAlmostEqual(s.scientific(5, "tan"), -3.38051500625)

    def test_lcm(self):
        self.assertEqual(s.lcm(7, 9), 63)
        self.assertEqual(s.lcm(10, 9), 90)
        self.assertEqual(s.lcm(9, 8), 72)
        self.assertEqual(s.lcm(6, 5), 30)
        self.assertEqual(s.lcm(5, 4), 20)

    def test_hcf(self):
        self.assertEqual(s.hcf(30, 10), 10)
        self.assertEqual(s.hcf(78, 26), 26)
        self.assertEqual(s.hcf(60, 68), 4)
        self.assertEqual(s.hcf(70, 20), 10)
        self.assertEqual(s.hcf(40, 24), 8)

    def test_factors(self):
        self.assertEqual(s.factors(1), [1])
        self.assertEqual(s.factors(2), [1, 2])
        self.assertEqual(s.factors(4), [1, 2, 4])
        self.assertEqual(s.factors(18), [1, 2, 3, 6, 9, 18])
        self.assertEqual(s.factors(42), [1, 2, 3, 6, 7, 14, 21, 42])

    def test_randstring(self):
        self.assertEqual(len(s.randstring(5)), 5)
        self.assertEqual((type(s.randstring(5)), "string")

if __name__ == '__main__':
    ut.main()
