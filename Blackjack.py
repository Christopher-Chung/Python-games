# (c) 2019 Christopher Chung
# Blackjack game

# Starts with $1000, can change bet before every round.
# Game ends when you hold more than $10000 at end of round.
# You earn the bet if you beat A.I.

import random

def createdeck():
	deck = []
	for i in range(2,11):
		deck.extend([i] * 4)
	deck.extend(['A'] * 4)
	deck.extend(['J'] * 4)
	deck.extend(['Q'] * 4)
	deck.extend(['K'] * 4)
	return deck

def deal(deck):
	card = random.choice(deck)
	deck.remove(card)
	return card

def builddict():
	d = {}
	for i in range(2,11):
		d[i] = i
	d['J'] = 10
	d['Q'] = 10
	d['K'] = 10
	d['A'] = [1,11]
	return d


def dealround():
	deck = createdeck()
	acard = []
	ucard = []
	for _ in range(2):
		acard.append(deal(deck))
		ucard.append(deal(deck))
	print("You are dealt: {} + {}".format(ucard[0],ucard[1]))
	if jack(ucard):
		print("You have a Blackjack!")
	return [acard,ucard,deck]

def change(bet,pystatus):
	print("You are currently betting on ${} and own ${}.".format(bet,pystatus))
	if pystatus < bet:
		print("As you do not hold enough money, you need to bet smaller.")
		ins = 'y'
	else:
		ins = input("Do you want to change bets? Press 'y' to change, or any other key to skip.")
	if ins == 'y':
		bet = setbet(pystatus)
		while not legal(bet,pystatus):
			bet = setbet(pystatus)
	else:
		pass
	return bet

def setbet(pystatus):
	bet = input("Please input how much you would like to bet: ")
	return int(bet)

def legal(bet,pystatus):
	if bet <= 0:
		print("You cannot bet so small!")
		return False
	elif bet > pystatus:
		print("You currently own ${}, enter a smaller bet.")
		return False
	else:
		return True

def score(cards,d):
	if overshoot(cards,d):
		return -1
	if len(cards) == 5:
		return 100
	if jack(cards):
		return 200
	total = 0
	for i in cards:
		if i == 'A':
			total += 10
		else:
			total += d[i]
	if total > 21:
		for _ in range(cards.count('A')):
			total -= 9
			if total <= 21:
				break
	return total


def overshoot(cards,d):
	total = 0
	for i in cards:
		if i == 'A':
			total += 1
		else:
			total += d[i]
	if total > 21:
		return True
	return False

def uadd(ucard,deck,d):
	if jack(ucard):
		return ucard
	ins = input("Do you want to add cards? Press 'y' to add, or any other key to skip.")
	if ins == 'y':
		n = 0
		for a in range(3):
			ucard.append(deal(deck))
			print("Your current hand is: ", ucard)
			if overshoot(ucard,d):
				print("You have exceeded 21!")
				return ucard
			else:
				if a == 2:
					print("Five dragons! You win")
					return ucard
				ins = input("Do you want to keep adding cards? Press 'y' to add, or any other key to skip.")
				if ins != 'y':
					break
				else:
					pass
		return ucard
	else:
		return ucard

def jack(ucard):
	if set(ucard) == {'J','A'} or set(ucard) == {10,'A'} or set(ucard) == {'Q','A'} or set(ucard) == {'K','A'}:
		return True
	else:
		return False

def updatest(status,pystatus,bet):
	pystatus = pystatus + status*bet
	return pystatus

#AI strategy

def average(deck,d):
	total = 0
	for u in deck:
		if u == "A":
			total += 5.5
		else:
			total += d[u]
	avg = total/len(deck)
	return avg

def decide(acard,deck,d):
	posn = []
	total = 0
	q = acard.count('A')

	for u in acard:
		if u == 'A':
			pass
		else:
			total += d[u]
	for i in range(q + 1):
		posn.append(total + q + i * 9)
	posy = [a + average(deck,d) for a in posn]

	i = 0
	for j in posy:
		if j <= 21 and j > i:
			i = j
			k = 1
	for j in posn:
		if j <= 21 and j > i:
			i = j
			k = 0

	return bool(k)


def cadd(acard,deck,d):
	if jack(acard):
		return acard
	n = 0
	for a in range(3):
		if decide(acard,deck,d):
			acard.append(deal(deck))
			if overshoot(acard,d):
				return acard
		else:
			return acard

def comparison(acard,ucard,d):
	ai = score(acard,d)
	user = score(ucard,d)
	print("The AI has cards:", acard)
	if ai > user:
		print("You lose!")
		return -1
	elif user > ai:
		print("You win!")
		return 1
	else:
		print("It is a draw!")
		return 0


def main():
	print("Let's start the game!")
	money = 1000
	d = builddict()
	bet = 50
	while money in range(10000):
		ins = input("Do you want to keep playing? Press 'y' to keep playing:")
		if ins != 'y':
			print("Aww, let's play some other time!")
			return
		else:
			print("")
			bet = change(bet,money)
			k = dealround()
			ucard = uadd(k[1],k[2],d)
			acard = cadd(k[0],k[2],d)
			status = comparison(acard,ucard,d)
			money = updatest(status,money,bet)

	if money <= 0:
		print("You lose! Try again.")
	else:
		print("You win!")
if __name__ == "__main__":
	main()
