import unittest
from ship import Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship('testShip', 3, 1)

    def test_get_ship_name(self):
        self.assertEqual(self.ship.get_name(), 'testShip')

    def test_get_ship_length(self):
        self.assertEqual(self.ship.get_length(), 3)

    def test_get_ship_orientation(self):
        self.assertEqual(self.ship.get_orientation(), 1)

    def test_set_ship_name(self):
        self.ship.set_name('uusi_nimi')
        self.assertEqual(self.ship.name, 'uusi_nimi')

    def test_set_ship_length(self):
        self.ship.set_length(4)
        self.assertEqual(self.ship.length, 4)

    def test_set_ship_length_zero(self):
        self.ship.set_length(0)
        self.assertEqual(self.ship.length, 3)

    def test_set_ship_orientation(self):
        self.ship.set_orientation(0)
        self.assertEqual(self.ship.orientation, 0)

    def test_set_ship_status(self):
        self.ship.set_status(True)
        self.assertEqual(self.ship.status, True)

    def test_set_ship_status_no_changes(self):
        self.ship.set_status(False)
        self.assertEqual(self.ship.status, False)

    def test_is_sunk(self):
        self.assertEqual(self.ship.is_sunk(), False)
