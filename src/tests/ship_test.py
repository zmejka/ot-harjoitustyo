import unittest
from objects.ship import Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship('testShip', 3, 1)
        self.ship._notice = 'Text'

    def test_get_ship_name(self):
        self.assertEqual(self.ship.get_name(), 'testShip')

    def test_get_notice(self):
        self.assertEqual(self.ship.get_notice(), 'Text')

    def test_get_ship_length(self):
        self.assertEqual(self.ship.get_length(), 3)

    def test_get_ship_orientation(self):
        self.assertEqual(self.ship.get_orientation(), 1)

    def test_set_ship_status(self):
        self.ship._set_status(True)
        self.assertEqual(self.ship._status, True)

    def test_set_ship_status_no_changes(self):
        self.ship._set_status(False)
        self.assertEqual(self.ship._status, False)

    def test_set_ship_status_wrong_value(self):
        self.ship._set_status(5)
        self.assertEqual(self.ship._status, False)

    def test_is_sunk(self):
        self.assertEqual(self.ship.are_sunk(), False)
    
    def test_add_hits(self):
        self.ship.add_hit()
        self.assertEqual(self.ship._hits, 1)
    
    def test_ship_position_row(self):
        coordinates = self.ship.ship_random_position()
        self.assertTrue(0 <= coordinates[0] <=  9)
    
    def test_ship_position_column(self):
        coordinates = self.ship.ship_random_position()
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
