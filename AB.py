# (c) 2019 Christopher
# Bulls and cows

# No repeating digits

import random

def create():
	x = []
	for i in range(120,10000):
		if len(str(i)) < 4:
			j = '0' * (4 - len(str(i))) + str(i)
			if len(set(j)) == len(j):
				x.append(j)
		else:
			if len(set(str(i))) == len(str(i)):
				x.append(str(i))
	return x

def compare(i,num,comp):
	if int(i[0]) == count(num,comp)[0] and int(i[1]) == count(num,comp)[1]:
		return True
	else:
		return False

def delete(i,num,poss):
	""" i = right place wrong place """
	d = []
	for element in poss:
		if compare(i,num,element):
			d.append(element)
	return d

def pick(poss):
	return poss[len(poss)//2]

def guess(num,n):
	print('')
	print("This is my {} guess: {}".format(n,num))
	ins = input("Enter two digit number ab to indicate result of guess: ")
	return ins

def choose(x):
	return random.choice(x)

def count(num,comp):
	a, b = 0, 0
	for k in range(4):
		if num[k] in comp:
			if num[k] == comp[k]:
				a += 1
			else:
				b += 1
	return [a,b]	

if __name__ == '__main__':
	poss = create()
	q = input("Press G to guess, or B to be guessed: ")
	a = 0
	if q == 'B':
		print("Let's start the game! Think of a random 4-digit number, with all unique digits.")
		print("My first guess is 1234")
		ins = input("Enter two digit number ab to indicate result of guess: ")
		num = '1234'
		for i in range(2,11):
			k = poss.copy()
			poss = delete(ins,num,k)
			if len(poss) == 1:
				print("I win! The number is {}".format(pick(poss)))
				a = 1
				break
			elif not poss:
				print("You are being fickle, huh?")
				a = 1
				break
			else:
				num = pick(poss)
				ins = guess(num,i)
		if a != 1:
			print("You win!")
	elif q == 'G':
		print("I've done coming up with a number! Start your guess.")
		num = input("Your first guess is....  ")
		comp = str(choose(poss))
		for i in range(2,11):
			if count(num,comp)[0] < 4:
				print("Your guess of {} yielded {}A, {}B.".format(num,count(num,comp)[0],count(num,comp)[1]))
				print('')
				num = input("Your {} guess is...  ".format(i))
			else:
				print("You win!")
				a = 1
				break
		if a != 1:
			print("I win! The number is {}".format(comp))
	else:
		print("Don't wanna play? Such a shame...")