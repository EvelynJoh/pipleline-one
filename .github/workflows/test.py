import unittest
from main import main

class TestMainknFuncion(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(none), "hello World!")

if __name__ == '__main__':
    unittest.main()