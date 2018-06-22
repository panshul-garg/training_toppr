class Hand:
	potMoney=0
	player_turn=0
	state=0
	table=None

	table_cards=[]

	def __init__():


	def deal(self):
		j=0
		for i in self.table.players:
			if i.active:
				i.deal_card1(self.table.deck.cards[j])
				j+=1
		for i in self.table.players:
			if i.active:
				i.deal_card2(self.table.deck.cards[j])
				j+=1
		for i in range(0,5):
			table_cards.append(self.table.deck.cards[j])
			j+=1

	def play(self):
		








