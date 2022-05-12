import unittest
from objects.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('testPlayer', True)

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), 'testPlayer')

    def test_get_status(self):
        self.assertEqual(self.player.get_status(), True)

    def test_set_name(self):
        self.assertEqual(self.player.set_name('another'), True)

    def test_set_name_short(self):
        self.assertEqual(self.player.set_name('an'), False)

    def test_set_name_long(self):
        self.assertEqual(self.player.set_name('anananananananananananananananananananan'), False)
    
    def test_set_status(self):
        self.player.set_status(False)
        self.assertEqual(self.player._status, False)
    
    def test_set_wrong_status(self):
        self.player.set_status('false')
        self.assertEqual(self.player._status, True)