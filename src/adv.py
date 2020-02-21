from room import Room
from player import Player
from item import Item

import textwrap
import time
import asyncio

# Declare all the rooms

lantern = Item('lantern', 'It\'s an old gas lantern.')
lighter = Item('lighter', 'Nice! A Zippo.')

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [lantern, lighter]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ),

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
location = room['outside']
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
player.name = input('\nWelcome Adventurer! What is your name? --->  ')

while player.current_room:
  room_items = f'Room Items: '
  for i in player.current_room.items:
    room_items += f' -{i.name}- '

  your_items = f'Your Items: '
  for i in player.items:
    your_items += f' -{i.name}- '


  print(f'\n-----------------------------------------------------------\n---{player.current_room.name}---')
  print(f'{textwrap.fill(player.current_room.description, 40)}')
  print(f'\n{room_items}')
  print(f'\n{your_items}')
  user_input = input("""   
                                                                  To move:              'n' for North
  Enter 'take item_name' to take/get an item from the room,                'w' for West        +      'e' for East
  Enter 'drop item_name' to drop/leave an item from your inventory,                     's' for South

What would you like to do? (enter 'q' to quit) ---> """).lower()
  print('\n-----------------------------------------------------------')

  room_items_names = [i.name for i in player.current_room.items]
  player_items_names = [i.name for i in player.items]

# handle quitting and movement requirements
  if len(user_input.split()) == 1:
    if user_input == 'q':
      print(f'\nGood bye {player.name}, until next time!')      
      break
    elif 'lantern' not in player_items_names and 'lighter' not in player_items_names:
      print('\nIt is way too dark in there.\nIf only there was a way to create enough light to see...')
    elif 'lantern' in player_items_names and 'lighter' not in player_items_names:
      print('\nYou have a lantern and the gas is full,\nbut there must be something else you need.')
    elif 'lantern' not in player_items_names and 'lighter' in player_items_names:
      print('\nYou have a lighter, but that won\'t be enough light by it\'s self.\nThere must be something else you need.')
    else:

# handle movements
      if user_input == 'n':
        if player.current_room.n_to:
          player.current_room = player.current_room.n_to
          print(f'\nYou have moved North to the {player.current_room.name}')
        else:
          print('\nThere is nothing in this direction!')      
          continue
      elif user_input == 's':
        if player.current_room.s_to:
          player.current_room = player.current_room.s_to
          print(f'\nYou have moved South to the {player.current_room.name}')
        else:
          print('\nThere is nothing in this direction!')      
          continue
      elif user_input == 'e':
        if player.current_room.e_to:
          player.current_room = player.current_room.e_to
          print(f'\nYou have moved East to the {player.current_room.name}')
        else:
          print('\nThere is nothing in this direction!')      
          continue
      elif user_input == 'w':
        if player.current_room.w_to:
          player.current_room = player.current_room.w_to
          print(f'\nYou have moved West to the {player.current_room.name}')
        else:
          print('\nThere is nothing in this direction!')      
          continue
      else:
        print(f'\nYou entered {user_input}, that does nothing. Sorry')      
        continue

# handle actions
  elif len(user_input.split()) == 2:
    picked_item = user_input.split()[1]

    if user_input.split()[0] in ['take', 'get']:
      if picked_item in room_items_names:
        for i in player.current_room.items:
          if i.name == picked_item:
            player.current_room.items.remove(i)
            player.items.append(i)
            i.on_take()      
      else:
        print(f'\nThere is no such item in this room!')      
        continue

    elif user_input.split()[0] in ['drop', 'leave']:
      if picked_item in player_items_names:
        for i in player.items:
          if i.name == picked_item:
            player.items.remove(i)
            player.current_room.items.append(i)
            i.on_drop()      
      else:
        print(f'\nYou do not posses that item!')      
        continue
    else:
      print(f'\n{user_input.split()[0]} is not a valid action!')      
      continue

  else:
    print(f'\n{user_input} is not a valid action!')      
    continue