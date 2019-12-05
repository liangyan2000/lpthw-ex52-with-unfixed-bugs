from nose.tools import *
from gothonweb.planisphere import *

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a 
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room ("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up':start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    room1 = load_room(START)
    assert_equal(room1.go('shoot!'), generic_death)
    assert_equal(room1.go('dodge!'), generic_death)

    room2 = room1.go('tell a joke')
    assert_equal(room2, laser_weapon_armory)

    assert_equal(room2.go(***), generic_death)
    room3 = room2.go('520')
    assert_equal(room3, the_bridge)

    assert_equal(room3.go('throw the bomb'), generic_death)
    room4 = room3.go('slowly place the bomb')
    assert_equal(room4, escape_pod)

    assert_equal(room4.go('4'), the_end_loser)
    room5 = room4.go('2')
    assert_equal(room5, the_end_winner)

    
    