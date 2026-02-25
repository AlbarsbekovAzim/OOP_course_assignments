import unittest
from src.device import Device


class TestDevice(unittest.TestCase):

    def test_discount(self):
        d = Device("Test", 100, 5, 12)
        d.apply_discount(10)
        self.assertEqual(d.price, 90)

    def test_stock(self):
        d = Device("Test", 100, 5, 12)
        self.assertTrue(d.is_available(3))
        d.reduce_stock(3)
        self.assertEqual(d.stock, 2)


if __name__ == "__main__":
    unittest.main()