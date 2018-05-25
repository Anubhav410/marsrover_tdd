import pytest
from marsrover import Rover


def test_move_step():
    rover = Rover(x=0, y=0, direction='N')
    rover.move()
    assert rover.x == 0 and rover.y == 1 and rover.direction == 'N'


# def test_turn_left_from_north_faces_west():
#     rover = Rover(x=0, y=0, direction='N')
#     rover.turn('L')
#     assert rover.direction == 'W'
#
#
# def test_turn_left_from_west_faces_south():
#     rover = Rover(x=0, y=0, direction='W')
#     rover.turn('L')
#     assert rover.direction == 'S'
#
#
# def test_turn_left_from_south_faces_east():
#     rover = Rover(x=0, y=0, direction='S')
#     rover.turn('L')
#     assert rover.direction == 'E'
#
#
# def test_turn_left_from_east_faces_north():
#     rover = Rover(x=0, y=0, direction='E')
#     rover.turn('L')
#     assert rover.direction == 'N'

def test_left_turns():
    test_cases = {"N": "W", 'W': 'S', 'S': 'E', 'E': 'N'}
    for key, value in test_cases.iteritems():
        rover = Rover(x=0, y=0, direction=key)
        rover.turn('L')
        assert rover.direction == value


def test_right_turns():
    test_cases = {"N": "E", 'E': 'S', 'S': 'W', 'W': 'N'}
    for key, value in test_cases.iteritems():
        rover = Rover(x=0, y=0, direction=key)
        rover.turn('R')
        assert rover.direction == value


def test_complex_movements():
    rover = Rover(x=1, y=2, direction='N')
    movements = 'LMLMLMLMM'
    rover.execute(movements)
    assert rover.x == 1
    assert rover.y == 3
    assert rover.direction == 'N'

    rover = Rover(x=3, y=3, direction='E')
    movements = 'MMRMMRMRRM'
    rover.execute(movements)
    assert rover.x == 5
    assert rover.y == 1
    assert rover.direction == 'E'
