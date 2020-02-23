class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def on_take(self):
    print(f'\nYou have picked up a {self.name}, {self.description}')

  def on_drop(self):
    print(f'\nYou have dropped your {self.name}!!!')