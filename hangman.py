import random
words = ["office", "panda", "cabin", "ginger"]
random_word = random.choice(words)
hangman_draws = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''']
dashes = ["_"] * len(random_word)
print (" ".join(dashes))
tries = 6
guessed_letters = []
print (hangman_draws [0])
while "_" in dashes and tries > 0:
   letter = input("Please guess a letter: ").lower() 
   if letter in guessed_letters:
      print ("you already guessed that. Try again.")
      print(f"you have {tries} more tries")
      continue
   guessed_letters.append(letter)
   
   if letter not in random_word:
      tries -= 1 
      print (hangman_draws[6-tries]) 
   else: 
      for index in range(len(random_word)):
         if random_word[index] == letter:
            dashes[index] = letter
   print (" ".join(dashes))
   print(f"you have {tries} more tries")
     
if tries == 0:
   print("""
   ********
   You Lose
   ********
  +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  """)
else:
   print ("""
         *******
         YOU WIN
         *******
           """)