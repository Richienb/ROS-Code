import unittest as ut
import syntax as s

class TestCode(ut.TestCase):

    def test_colourcode(self):
        self.assertEqual(s.colourcode("#212121", "hex", True), '#212121')

    def test_changecolour(self):
        self.assertEqual(str(s.changecolour("#212121", "red", 10)), '#192121')

    def test_catwalk(self):
        self.assertEqual(s.catwalk("this     is    some    text"), "this is some text")

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
        self.assertEqual(s.splitstring("hello my name"), ["hello", "my", "name"])
        self.assertEqual(s.splitstring("hello my name", "-"), ["hello my name"])
        self.assertEqual(s.splitstring("hello-my-name", "-"), ["hello", "my", "name"])
        self.assertEqual(s.splitstring("hello-my-name", "-", 0), "hello")

if __name__ == '__main__':
    ut.main()
