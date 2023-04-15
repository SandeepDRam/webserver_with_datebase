import unittest

string_to_test = 'hello world'

class TestHelloWorld(unittest.TestCase):

    def test_upper(self):
        assert string_to_test.upper() == 'HELLO WORLD'
     
    def test_islower(self):
        assert string_to_test.islower()
        assert not string_to_test.upper().islower()

    def test_split(self):
        assert string_to_test.split() == ['hello', 'world']
        with self.assertRaises(TypeError):
            string_to_test.split(2)

if __name__ == '__main__':
    unittest.main()
