from random import choice
from re import findall # Initiating packages that i need
deathcounter = 0
with open("dictionaryCode.csv","r") as f:
	dictionary = findall("([\w' ]*)\,([\w& ]*)\,([\w', ]*)",f.read()) # stores each word, word type, and word definition into a tuple
while 1:
	word, word_type, word_def = choice(dictionary) # Choosing a random word
	spaces = ["_"]*len(word)
	print("_"*160) # because it looks neat
	while 1:
		if word_type != "" or " ": # Some word types are blanks or spaces
			print("The word is a: " + word_type +
				  " (Noun, Article, Adjective, Verb, Adverb, Plural, Participle, Conjunction, Determiner, Exclamation, Interjection, ).\n",
				  "The definition is: " + word_def + ".\n") # displays the word type and definition
		else:
			print("This word does not have a type" + ".\n",
				  "The definition is: " + word_def + ".\n")  # displays the word type and definition
		guess = input("Guess the word or letter: ") # Guess a letter or word
		for i, char in enumerate(word):
			if guess.lower() == char.lower(): # lowers the letters because capitalization makes life fun
				spaces[i] = guess # Changes the corresponding space to the correct guess
		print(" ".join(spaces)) # prints current guessed word
		if guess.lower() not in word.lower(): # checks to see if the letter is in the list. if not adds 1 to your failures
			deathcounter += 1
			print("Wrong.\n")
		if "".join(spaces).replace(" ","").lower() == word.lower(): # checks to see if your guess is right
			deathcounter = 0
			print("Correct! Good job!\n")
			break
		elif guess.lower() == word.lower(): #checks to see if the word you guess is right
			print("Correct! Good job!\n")
			deathcounter = 0
			break
		if deathcounter >= 9: # if you die you exit the game. 9 Guesses, 1 for every vowel, and 3. Makes short words easy, and makes long words possible
			print("You lost, better luck next time!")
			print("The word was: " + word)
			input("")
			exit()
		print("You have {0} guesses left.".format(9-deathcounter)) # displays how many guesses you have left.
