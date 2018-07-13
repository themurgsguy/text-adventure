#! /usr/bin/python3

# This impoers the cmd module.
# Basically a basic command prompt system
import cmd
import textwrap
import os
import time

# This imports the loader function
from room import get_room


class Manager(cmd.Cmd):
# This is the game class, that controls the game
# Basically its the engine if you will
# The class inherist from the cmd module

	def __init__(self):
	# This is to inicialize the class
		cmd.Cmd.__init__(self)
		self.loc = get_room()
		self.look()

	def move(self, dir):
		new_room = self.loc._neighbor(dir)

		if new_room == None:
			print("There is nothing there.")
		else:
			self.loc = get_room(new_room)
			self.look()

	def look(self):
		os.system('clear')
		print("\n--" + self.loc.name + "--\n")
		#print("")
		for line in textwrap.wrap(self.loc.description, 72):
			print(line)

		print("")
		print(self.loc.directions + "\n")

		#for line in textwrap.wrap(self.loc.directions, 72):
		#	print(line)


	# These are basically the possible game commands
	def do_north(self, args):
		"""goes north"""
		self.move('north')

	def do_south(self, args):
		"""goes south"""
		self.move('south')

	def do_east(self, args):
		"""goes east"""
		self.move('east')

	def do_west(self, args):
		"""goes west"""
		self.move('west')

	def do_up(self, args):
		"""goes up"""
		self.move('up')

	def do_down(self, args):
		"""goes down"""
		self.move('down')

	def do_quit(self, args):
		"""
		Leaves the game
		"""
		os.system("clear")
		print("\n" + "Thank you for playing the METANOVEL.")
		print("There is definitly a better version, with losts more features on the horizon.\nStay tuned for updates\n")
		print("\nGoodbye.")
		time.sleep(4)
		os.system('clear')
		return True


if __name__ == "__main__":
# The requisit call on run
	game_manager = Manager()
	game_manager.cmdloop()