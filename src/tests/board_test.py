import unittest
from board import Board

class TestShip(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_game_over(self):
        self.board.game_status = True
        self.assertEqual(self.board.game_status, True)

    def test_game_not_over(self):
        self.assertEqual(self.board.game_status, False)

    def test_place_the_ship_horizontal(self):
        coordinates = (3,4)
        orientation = 0
        length = 4
        self.assertEqual(self.board.place_the_ship(coordinates, orientation, length), True)

    def test_place_the_ship_horizontal_over_board(self):
        coordinates = (3,8)
        orientation = 0
        length = 4
        self.assertEqual(self.board.place_the_ship(coordinates, orientation, length), False)

    def test_place_the_ship_vertical(self):
        coordinates = (3,4)
        orientation = 1
        length = 4
        self.assertEqual(self.board.place_the_ship(coordinates, orientation, length), True)

    def test_place_the_ship_vertical_over_board(self):
        coordinates = (8,4)
        orientation = 1
        length = 4
        self.assertEqual(self.board.place_the_ship(coordinates, orientation, length), False)

    def test_no_overlap_horizontal(self):
        self.board.place_the_ship((3,4), 0, 4)
        self.assertEqual(self.board.overlap_check((5,2), 0, 3), True)

    def test_overlap_horizontal(self):
        self.board.place_the_ship((3,4), 0, 4)
        self.assertEqual(self.board.overlap_check((3,2), 0, 3), False)

    def test_no_overlap_vertical(self):
        self.board.place_the_ship((3,4), 0, 4)
        self.assertEqual(self.board.overlap_check((5,2), 1, 3), True)

    def test_overlap_vertical(self):
        self.board.place_the_ship((3,4), 0, 4)
        self.assertEqual(self.board.overlap_check((2,4), 1, 3), False)

