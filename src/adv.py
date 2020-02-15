from room import Room
from player import Player

import textwrap
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
location = 'outside'
player = Player('Add Venturer', location)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while player.current_room:
  print(room[player.current_room].name)
  print(textwrap.fill(room[player.current_room].description, 40))
  user_input = input("""What would you like to do? (enter 'q' to quit)
  To move use:
  n for North,
  s for South,
  e for East,
  w for West,
  and press enter ---> """)
  if user_input == 'n':
    if player.current_room == 'outside':
      player.current_room = 'foyer'
    elif player.current_room == 'foyer':
      player.current_room = 'overlook'
    elif player.current_room == 'narrow':
      player.current_room = 'treasure'
    else:
      print('There is nothing in this direction!')
      time.sleep(2)
      continue
  elif user_input == 's':
    if player.current_room == 'foyer':
      player.current_room = 'outside'
    elif player.current_room == 'overlook':
      player.current_room = 'foyer'
    elif player.current_room == 'treasure':
      player.current_room = 'narrow'
    else:
      print('There is nothing in this direction!')
      time.sleep(2)
      continue
  elif user_input == 'e':
    if player.current_room == 'foyer':
      player.current_room = 'narrow'
    else:
      print('There is nothing in this direction!')
      time.sleep(3)
      continue
  elif user_input == 'w':
    if player.current_room == 'narrow':
      player.current_room = 'foyer'
    else:
      print('There is nothing in this direction!')
      time.sleep(3)
      continue
  elif user_input == 'q':
    print(f'Good bye {player.name}, until next time!')
    time.sleep(3)
  else:
    print(f'You entered {user_input}, that does nothing. Sorry')
    time.sleep(3)
    continue