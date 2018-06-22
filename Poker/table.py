from Deck import Deck
from Player import Player


class Table:

	players=[]
	deck=None


	def __init__(self,number_of_players,buyin):
		self.deck=Deck()
		for i in range(0,number_of_players):
			players=append(Player(buyin))

	def turn(self):
		hand=new Hand(Player)



