from room import Room
from player import Player
from item import Item

import textwrap
import time
import asyncio

# Declare all the rooms

lantern = Item('lantern', 'It\'s an old gas lantern.')
lighter = Item('lighter', 'Oh? You must have dropped this.')

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
room_items = f'Room Items: '
for i in player.current_room.items:
  room_items += f' -{i.name}- '

your_items = f'Your Items: '
for i in player.items:
  your_items += f' -{i.name}- '

while player.current_room:
  print(f'\n---{player.current_room.name}---')
  print(f'{textwrap.fill(player.current_room.description, 40)}')
  print(f'\n{room_items}')
  print(your_items)
  user_input = input("""
What would you like to do? (enter 'q' to quit)
  Enter 'take item_name' to take an item from the room,
  To move use: 'n' for North, 's' for South, 'e' for East, 'w' for West,
and press enter ---> """).lower()
  if len(user_input.split()) == 1:
    if user_input == 'n':
      if player.current_room.n_to:
        player.current_room = player.current_room.n_to
      else:
        async def response():
          print('\nThere is nothing in this direction!')
          await asyncio.sleep(3)

        asyncio.run(response())
        continue
    elif user_input == 's':
      if player.current_room.s_to:
        player.current_room = player.current_room.s_to
      else:
        async def response():
          print('\nThere is nothing in this direction!')
          await asyncio.sleep(3)

        asyncio.run(response())
        continue
    elif user_input == 'e':
      if player.current_room.e_to:
        player.current_room = player.current_room.e_to
      else:
        async def response():
          print('\nThere is nothing in this direction!')
          await asyncio.sleep(3)

        asyncio.run(response())
        continue
    elif user_input == 'w':
      if player.current_room.w_to:
        player.current_room = player.current_room.w_to
      else:
        async def response():
          print('\nThere is nothing in this direction!')
          await asyncio.sleep(3)

        asyncio.run(response())
        continue
    elif user_input == 'q':
      async def response():
        print(f'\nGood bye {player.name}, until next time!')
        await asyncio.sleep(3)

      asyncio.run(response())
      break
    else:
      async def response():
        print(f'\nYou entered {user_input}, that does nothing. Sorry')
        await asyncio.sleep(3)
        
      asyncio.run(response())
      continue

  elif len(user_input.split()) == 2:
    picked_item = user_input.split()[1]
    current_items_names = [i.name for i in player.current_room.items]

    if user_input.split()[0] == 'take':
      if picked_item in current_items_names:
        for i in player.current_room.items:
          if i.name == picked_item:
            picked_item = i
      else:
        async def response():
          print(f'\nThere is no such item in this room!')
          await asyncio.sleep(3)
          
        asyncio.run(response())
        continue
    
  else:
    async def response():
      print(f'\nYou must enter a valid command!')
      await asyncio.sleep(3)
        
    asyncio.run(response())
    continue