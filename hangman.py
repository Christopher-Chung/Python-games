# (c) 2019 Christopher Chung
# Play hangman

import random

def readfile():
	wordlist = []
	with open('words.txt') as f:
		for line in f:
			l = line.strip()
			if l.isalpha():
				l = l.lower()
				wordlist.append(l)
	return wordlist

def choose(wordlist):
	return random.choice(wordlist)

def draw(word,guesses):
	w = ''
	for char in word:
		if char in guesses:
			w += char
		else:
			w += '*'
	w = "The results is: " + w
	print(w)
	print('')

def legal(guesses,alp):
	if alp in guesses:
		print("You already guessed this before, please choose another letter.")
		return False
	elif not alp.isalpha():
		print("This is not a letter, please choose a letter.")
		return False
	elif len(alp) != 1:
		print("You entered more than a letter, please try again.")
		return False
	else:
		return True

def guess(word,n,guesses):
	alp = input("Please guess letter: ").lower()
	while legal(guesses,alp) == False:
		alp = input("Please guess letter: ").lower()
	guesses.append(alp)
	print("You guessed the letter {}; you have guessed {} times.".format(alp,n + 1))
	draw(word,guesses)
	if checkwin(word,guesses):
		print("You win! The word is {}.".format(word))
		return 1
	if n == 10:
		print("You lost. The word is {}.".format(word))
		return 1

def checkwin(word,guesses):
	for char in word:
		if char not in guesses:
			return False
	return True

def main():
	wordlist = readfile()
	word = choose(wordlist)
	guesses = []
	n = 1
	for i in range(11):
		a = guess(word,i,guesses)
		if a == 1:
			break

main()