import random


class Card:

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f'{self.value}:{self.suit}'


class Deck:

	def __init__(self):
		self.deck = []
		suits = ['H', 'S', 'D', 'C']
		values = ['a', '1', '2', '3', '4', 'j']
		for s in suits:
			for v in values:
				self.deck.append(Card(v, s))

	def deal(self, n):
		if n > len(self.deck):
			print('no more cards')
			return

		cards = []
		for i in range(n):
			cards.append(self.deck.pop(0))
		return cards

	def shuffle(self):
		random.shuffle(self.deck)


if __name__ == '__main__':
	deck = Deck()
	print(deck.deck)
	deck.shuffle()
	print(deck.deck)
	print(deck.deal(5))
	print(deck.deck)




	print(deck.deal(10))
	print(deck.deal(100))
	deck.shuffle()

	print('yo')