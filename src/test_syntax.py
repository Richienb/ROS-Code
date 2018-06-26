import unittest as ut
import syntax as s

class TestCode(ut.TestCase):

    def test_colourcode(self):
        self.assertEqual(s.colourcode('#212121', 'hex', True), '#212121')

    def test_changecolour(self):
        self.assertEqual(str(s.changecolour('#212121', 'red', 10)), '#192121')

    def test_catwalk(self):
        self.assertEqual(s.catwalk('this     is    some    text'), 'this is some text')

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
        self.assertEqual(s.splitstring('hello my name'), ['hello', 'my', 'name'])
        self.assertEqual(s.splitstring('hello my name', '-'), ['hello my name'])
        self.assertEqual(s.splitstring('hello-my-name', '-'), ['hello', 'my', 'name'])
        self.assertEqual(s.splitstring('hello-my-name', '-', 0), 'hello')

    def test_sort(self):
        self.assertEqual(s.sort(['d', 'a', 'c', 'b']), ['a', 'b', 'c', 'd'])
        self.assertEqual(s.sort(['d', 'a', 'c', 'b'], None, True), ['d', 'c', 'b', 'a'])

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
        results =  ["Tie", "Win", "Loose"]
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

    def test_equation(self):
<<<<<<< HEAD
        self.assertEqual(s.equation("plus", 2, 5), 7)
        self.assertEqual(s.equation("plus", 365, 164), 529)
        self.assertEqual(s.equation("minus", 5, 2), 3)
        self.assertEqual(s.equation("minus", 976, 245), 731)
        self.assertEqual(s.equation("multiply", 2, 5), 10)
        self.assertEqual(s.equation("multiply", 5, 2), 10)
        self.assertEqual(s.equation("multiply", 56, 15), 840)
        self.assertEqual(s.equation("divide", 5, 2), 2.5)
        self.assertEqual(s.equation("divide", 125, 5), 25)
=======
        self.assertEqual(equation("plus", 2, 5), 7)
        self.assertEqual(equation("plus", 365, 164), 520)
        self.assertEqual(equation("minus", 5, 2), 3)
        self.assertEqual(equation("minus", 976, 245), 731)
        self.assertEqual(equation("multiply", 2, 5), 10)
        self.assertEqual(equation("multiply", 5, 2), 10)
        self.assertEqual(equation("multiply", 56, 15), 840)
        self.assertEqual(equation("divide", 5, 2), 2.5)
        self.assertEqual(equation("divide", 125, 5), 25)
>>>>>>> 7b049c35384d197ec4d82d04e3c3e3255b413188

if __name__ == '__main__':
    ut.main()
