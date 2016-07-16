import unittest
from deride import Deride

class Person(object):

    def __init__(self, name):
        self.name = name

    def greet(self, other):
        return 'hello ' + other.name

class TestDeride(unittest.TestCase):

    def setUp(self):
        self.deride = Deride()

    def test_called_times(self):
        andy = self.deride.wrap(Person('Andy'))
        bob = self.deride.wrap(Person('Bob'))

        self.assertEquals('hello Bob', andy.greet(bob))

        andy.expect.greet.called.times(1)

    def test_called_times_fails(self):
        andy = self.deride.wrap(Person('Andy'))
        bob = self.deride.wrap(Person('Bob'))

        self.assertEquals('hello Bob', andy.greet(bob))

        with self.assertRaises(AssertionError):
            andy.expect.greet.called.times(2)

    def test_called_once(self):
        andy = self.deride.wrap(Person('Andy'))
        bob = self.deride.wrap(Person('Bob'))

        self.assertEquals('hello Bob', andy.greet(bob))

        andy.expect.greet.called.once()

    def test_called_once_fails(self):
        andy = self.deride.wrap(Person('Andy'))
        bob = self.deride.wrap(Person('Bob'))

        self.assertEquals('hello Bob', andy.greet(bob))
        self.assertEquals('hello Bob', andy.greet(bob))

        with self.assertRaises(AssertionError):
            andy.expect.greet.called.once()


    def test_called_twice(self):
        andy = self.deride.wrap(Person('Andy'))
        bob = self.deride.wrap(Person('Bob'))

        self.assertEquals('hello Bob', andy.greet(bob))
        self.assertEquals('hello Bob', andy.greet(bob))

        andy.expect.greet.called.twice()

    def test_called_twice_fails(self):
        andy = self.deride.wrap(Person('Andy'))
        bob = self.deride.wrap(Person('Bob'))

        self.assertEquals('hello Bob', andy.greet(bob))

        with self.assertRaises(AssertionError):
            andy.expect.greet.called.twice()

    def test_called_range(self):
        bob = self.deride.wrap(Person('Bob'))
        alice = Person('Alice')
        bob.greet(alice)
        bob.greet(alice)
        bob.greet(alice)

        bob.expect.greet.called.lt(4);
        bob.expect.greet.called.lte(3);
        bob.expect.greet.called.gt(2);
        bob.expect.greet.called.gte(3);

    def test_called_range_fails(self):
        bob = self.deride.wrap(Person('Bob'))
        alice = Person('Alice')
        bob.greet(alice)
        bob.greet(alice)
        bob.greet(alice)

        with self.assertRaises(AssertionError):
            bob.expect.greet.called.lt(3);
        with self.assertRaises(AssertionError):
            bob.expect.greet.called.lte(2);
        with self.assertRaises(AssertionError):
            bob.expect.greet.called.gt(3);
        with self.assertRaises(AssertionError):
            bob.expect.greet.called.gte(4);

    def test_called_never(self):
        bob = Person('bob')
        bob = self.deride.wrap(bob)
        bob.expect.greet.called.never();

    def test_called_never_fails(self):
        bob = Person('bob')
        bob = self.deride.wrap(bob)
        bob.greet(Person('alice'))
        with self.assertRaises(AssertionError):
            bob.expect.greet.called.never();

    def test_reset_call_counts(self):
        bob = Person('bob')
        bob = self.deride.wrap(bob)
        alice = Person('alice')
        bob.greet(alice)

        bob.expect.greet.called.once()

        bob.expect.reset()

        bob.expect.greet.called.never()


if __name__ == '__main__':
    unittest.main()
