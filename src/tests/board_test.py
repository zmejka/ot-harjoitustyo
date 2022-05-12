import unittest
import itertools
from objects.board import Board
from objects.ship import Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.ship = Ship('testShip', 3, 1)

    def test_game_over(self):
        self.board._game_status = True
        self.assertEqual(self.board._game_status, True)

    def test_game_not_over(self):
        self.assertEqual(self.board._game_status, False)

    def test_place_the_ship_horizontal(self):
        coordinates = (3,4)
        orientation = 0
        length = 4
        self.assertEqual(self.board.place_the_ship(self.ship, coordinates, orientation, length), True)

    def test_place_the_ship_horizontal_over_board(self):
        coordinates = (3,8)
        orientation = 0
        length = 4
        self.assertEqual(self.board.place_the_ship(self.ship, coordinates, orientation, length), False)

    def test_place_the_ship_vertical(self):
        coordinates = (3,4)
        orientation = 1
        length = 4
        self.assertEqual(self.board.place_the_ship(self.ship, coordinates, orientation, length), True)

    def test_place_the_ship_vertical_over_board(self):
        coordinates = (8,4)
        orientation = 1
        length = 4
        self.assertEqual(self.board.place_the_ship(self.ship, coordinates, orientation, length), False)

    def test_place_the_ship_overlap_horizontal(self):
        first_ship = Ship('first', 0, 4)
        horizontal_ship = Ship('ship', 0, 3)
        self.board.place_the_ship(horizontal_ship, (3,2), 0, 3)
        self.assertEqual(self.board.place_the_ship(first_ship,(3,3), 0, 4), False)

    def test_place_the_ship_overlap_vertical(self):
        vertical_ship = Ship('ship', 1, 3)
        self.board.place_the_ship(vertical_ship, (3,4), 1, 3)
        self.assertEqual(self.board.place_the_ship(self.ship, (2,4), 1, 3), False)      

    def test_no_overlap_horizontal(self):
        first_ship = Ship('first', 0, 4)
        self.board.place_the_ship(self.ship, (3,4), 0, 3)
        self.assertEqual(self.board.place_the_ship(first_ship,(4,3), 0, 4), True)

    def test_overlap_horizontal(self):
        first_ship = Ship('first', 0, 4)
        self.board.place_the_ship(self.ship, (3,4), 0, 4)
        self.assertEqual(self.board.place_the_ship(first_ship,(3,2), 0, 4), False)

    def test_no_overlap_vertical(self):
        first_ship = Ship('first', 1, 4)
        self.board.place_the_ship(self.ship, (3,4), 0, 4)
        self.assertEqual(self.board.place_the_ship(first_ship,(5,2), 1, 4), True)

    def test_overlap_vertical(self):
        first_ship = Ship('first', 1, 3)
        self.board.place_the_ship(self.ship, (3,4), 0, 4)
        self.assertEqual(self.board.place_the_ship(first_ship,(2,4), 1, 4), False)

    def test_set_ammo(self):
        self.board.set_ammo(100)
        self.assertEqual(self.board._ammo, 100)
    
    def test_set_ammo_wrong_type_no_changes(self):
        self.board.set_ammo('Ammo')
        self.assertEqual(self.board._ammo, 40)

    def test_get_ammo(self):
        self.assertEqual(self.board.get_ammo(), 40)

    def test_ship_class(self):
        self.board.create_ships()
        self.assertIsInstance(self.board.ships[0], Ship)
        self.assertIsInstance(self.board.ships[1], Ship)
        self.assertIsInstance(self.board.ships[2], Ship)
        self.assertIsInstance(self.board.ships[3], Ship)
        self.assertIsInstance(self.board.ships[4], Ship)

    def test_shot_without_ammo(self):
        self.board.set_ammo(0)
        self.assertEqual(self.board.shot(2,3), False)
    
    def test_shot_with_ammos(self):
        self.assertEqual(self.board.shot(2,3), True)

    def test_shot_ammos_decreases_new_cell(self):
        self.board.shot(2,3)
        self.assertEqual(self.board._ammo, 39)

    def test_shot_ammos_decreases_same_cell(self):
        self.board.shot(2,3)
        self.board.shot(2,3)
        self.assertEqual(self.board._ammo, 38)

    def test_check_game_over(self):
        ship1 = Ship('1', 3, 0)
        ship2 = Ship('2', 3, 0)
        ship3 = Ship('3', 3, 0)
        ship4 = Ship('4', 3, 0)
        self.board.ships.append(ship1)
        self.board.ships.append(ship2)
        self.board.ships.append(ship3)
        self.board.ships.append(ship4)
        self.board.ships.append(self.ship)
        self.board._check_game_over()
        self.assertEqual(self.board._game_status, False)

    def test_randomize_ships(self):
        ship1 = Ship('1', 3, 0)
        ship2 = Ship('2', 3, 0)
        ship3 = Ship('3', 3, 0)
        ship4 = Ship('4', 3, 0)
        self.board.ships.append(ship1)
        self.board.ships.append(ship2)
        self.board.ships.append(ship3)
        self.board.ships.append(ship4)
        self.board.ships.append(self.ship)
        self.board.randomize_ships()
        self.assertTrue(self.ship.position)

    def test_comp_shot_row(self):
        self._coordinates = []
        for row, col in itertools.product(range(10), range(10)):
            self._coordinates.append((row,col))
        self.assertTrue(0 <= self.board.comp_shot()[0] <=  9)
    
    def test_comp_shot_column(self):
        self._coordinates = []
        for row, col in itertools.product(range(10), range(10)):
            self._coordinates.append((row,col))
        self.assertTrue(0 <= self.board.comp_shot()[1] <=  9)
