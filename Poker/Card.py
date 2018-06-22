from suits import Suit
class Card:
	def __init__(self,number,suit):
		if number>=14 or number<=0:
			raise Exception("Not a valid card")
		else:
			self.number=number
		if isinstance(suit,Suit):
			self.suit=suit
		else:
			raise Exception("Not a valid card")


#card=Card(5,Suit.Spade)

#print card.number
#print card.suit	
