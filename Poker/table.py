from Deck import Deck
from Player import Player


class Table:

	players=[]
	deck=None
	small_blind=0
	dealer=0


	def __init__(self,number_of_players,buyin,small_blind):
		self.deck=Deck()
		self.small_blind=small_blind
		for i in range(0,number_of_players):
			players=append(Player(buyin))

	def turn(self):
		hand=new Hand(Player)



