class Hand:
	potMoney=0
	potMoneyAfterFolding=0
	player_turn=0
	state=0
	table=None
	dealer=None
	table_cards=[]
	players_in_order=[]
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

	def make_players_in_order(self,start):
		first_half=self.players_in_order[0:start]
		second_half=self.players_in_order[start:]
		self.players_in_order=second_half+first_half

	def play(self):
		pass

	def pre_flop(self):
		pass

	def cycle(self,raiser,max_amount,starter):
		player_on_turn=starter

		while(True):
			if(player_on_turn>len(players)):
				player_on_turn=0;
			if(players[player_on_turn].amount_in_hand==max_amount):
				break

			else:
				currentPlayer=players[player_on_turn]
				turn=currentPlayer.turn()
				if(turn=Turn.Check):
					currentPlayer+=1

				elif(turn=Turn.Fold):
					players[currentPlayer].fold=True

				elif(turn=Turn.Call):
					players[currentPlayer].amount_in_hand=max_amount

				elif(turn=Turn.Raise):
					raise_amount=currentPlayer.getRaiseAmount()
					max_amount+=raise_amount
					raiser=player_on_turn

				elif(turn=Turn.AllIn):
					































