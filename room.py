# Gonna need this to parse the json files
# Which will basically serve as the database of rooms
import json


def get_room(id="startscreen"):
# This is basically the loader
# Takes the name of a json file and loades it into a dic to be used
	ret = None
	with open("rooms/" + id + ".json", 'r') as f:
		jsontext = f.read()
		d = json.loads(jsontext)

		d['id'] = id
		ret = Room(**d)

	return ret


class Room():
# This calls implements a room in the game world
# It's more or less a graph of rooms and their connections

	def __init__(self, id="void", name="A Room", description="An Empty Room.", directions="You are stuck here.", neighbors={}):
		self.id = id
		self.name = name
		self.description = description
		self.directions = directions
		self.neighbors = neighbors # This is the list of connected rooms (like a graph)
		
		# As a possible expansion we could include lists for these things
		# - Items
		# - NPCs

	def _neighbor(self, direction):
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None

	def north(self):
		return self._neighbor('north')

	def south(self):
		return self._neighbor('south')

	def east(self):
		return self._neighbor('east')

	def west(self):
		return self._neighbor('west')