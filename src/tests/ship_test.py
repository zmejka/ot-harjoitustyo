import unittest
from ship import Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship('testShip', 3, 1)

    def test_get_ship_name(self):
        self.assertEqual(self.ship.getName(), 'testShip')

    def test_get_ship_length(self):
        self.assertEqual(self.ship.getLength(), 3)

    def test_get_ship_orientation(self):
        self.assertEqual(self.ship.getOrientation(), 1)

    def test_set_ship_name(self):
        self.ship.setName('uusi_nimi')
        self.assertEqual(self.ship.name, 'uusi_nimi')

    def test_set_ship_length(self):
        self.ship.setLength(4)
        self.assertEqual(self.ship.length, 4)

    def test_set_ship_length_zero(self):
        self.ship.setLength(0)
        self.assertEqual(self.ship.length, 3)

    def test_set_ship_orientation(self):
        self.ship.setOrientation(0)
        self.assertEqual(self.ship.orientation, 0)
