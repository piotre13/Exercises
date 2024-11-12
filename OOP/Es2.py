class Deck():
	def __init__(self,suits,values):
		self.suits = suits
		self.values = values
		self.deck = []
		for s in self.suits:
			for v in self.values:
				self.deck.append(Card(s,v))

	def deal(self, number=1):
		cards =[]
		for i in range(number):
			card = self.deck.pop()
			cards.append(card)
		return cards
	def shuffle(self):
		tmp = set(self.deck)
		self.deck = list(tmp)


class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

	def __repr__(self):
		return f'{self.suit} {self.value}'

if __name__ == '__main__':
	suits = [ 'Q', 'C', 'F', 'P']
	values = [1,2,3,4,5]

	deck = Deck(suits, values)
	deck.shuffle()
	c = deck.deal()
	print(c)