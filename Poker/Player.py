from Cards import Card
class Player:
	first_card=None
	second_card=None
	money=0
	active=False

	def __init__(self,buyin):
		self.money=buyin
		self.active=True



	def deal_card1(self,card1):
		self.first_card=card1

	def deal_card2(self,card2):
		self.second_card=card2


