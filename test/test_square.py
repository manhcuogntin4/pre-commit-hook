import unittest

from code.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)


if __name__ == "__main__":
    unittest.main()