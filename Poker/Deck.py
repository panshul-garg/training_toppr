from Card import Card
from suits import Suit
import random
class Deck:
	cards=[]
	def __init__(self):
		for i in range(1,5):
			for j in range(1,14):
				self.cards.append(Card(j,Suit(i)))
		
		for i in range(0,50):
			self.shuffle_2()
			self.shuffle_1()
		



	def shuffle(self):
		for i in Range(0,10):
			self.shuffle_2()
			self.shuffle_1()



	def shuffle_1(self):
		half_cards1=self.cards[:26]
		half_cards2=self.cards[-26:]
		j=0
		for i in range(0,26):
			self.cards[j]=half_cards2[i]
			j+=1
			self.cards[j]=half_cards1[i]
			j+=1


	def shuffle_2(self):
		random_number=random.randint(0,52)
		break1=self.cards[0:random_number]
		break2=self.cards[random_number:]
		self.cards=break2+break1



	def test_check(self):
		check=[]

		for i in range(0,52):
			check.append(False)
		
		for i in self.cards:
			value=13*(i.suit.value-1)+(i.number-1)
			check[value]=True

		for i in check:
			if not i:
				return False
		return True



	def __str__(self):
		ret=""
		for i in self.cards:
			ret += str(i.number) + str(i.suit) + '\n'
		return ret









#deck=Deck()
#print deck.shuffle_2()
#print deck
#print deck.test_check()
'''
first=deck.cards[:26]
second=deck.cards[-26:]
#deck.shuffle_1()

for i in first:
	print i.number
	print i.suit


print ""
print ""

for i in second:
	print i.number
	print i.suit

'''



