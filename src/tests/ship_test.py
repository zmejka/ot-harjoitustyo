import unittest
from objects.ship import Ship

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
    
    def test_set_ship_length_to_long(self):
        self.ship.set_length(7)
        self.assertEqual(self.ship.length, 3)

    def test_set_ship_orientation_horizontal(self):
        self.ship.set_orientation(0)
        self.assertEqual(self.ship.orientation, 0)
    
    def test_set_ship_orientation_vertical(self):
        self.ship.set_orientation(1)
        self.assertEqual(self.ship.orientation, 1)

    def test_set_ship_orientation_wrong_value(self):
        self.ship.set_orientation('a')
        self.assertEqual(self.ship.orientation, 1) 

    def test_set_ship_status(self):
        self.ship.set_status(True)
        self.assertEqual(self.ship.status, True)

    def test_set_ship_status_no_changes(self):
        self.ship.set_status(False)
        self.assertEqual(self.ship.status, False)

    def test_set_ship_status_wrong_value(self):
        self.ship.set_status(5)
        self.assertEqual(self.ship.status, False)

    def test_is_sunk(self):
        self.assertEqual(self.ship.are_sunk(), False)

    def test_get_hits(self):
        self.ship.add_hit()
        self.ship.add_hit()
        self.assertEqual(self.ship.get_hits(), 2)
    
    def test_add_hits(self):
        self.ship.add_hit()
        self.assertEqual(self.ship.hits, 1)
    
    def test_ship_position_row(self):
        coordinates = self.ship.ship_position()
        self.assertTrue(0 <= coordinates[0] <=  9)
    
    def test_ship_position_column(self):
        coordinates = self.ship.ship_position()
        self.assertTrue(0 <= coordinates[1] <=  9)
   
    def test_are_sunk(self):
        self.ship.add_hit()
        self.ship.add_hit()
        self.ship.add_hit()
        self.assertEqual(self.ship.are_sunk(), True)

    def test_not_sunk(self):
        self.ship.add_hit()
        self.ship.add_hit()
        self.assertEqual(self.ship.are_sunk(), False)
