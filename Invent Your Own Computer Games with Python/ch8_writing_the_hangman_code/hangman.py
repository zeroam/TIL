import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
    =====''',
'''
  +---+
  O   |
      |
      |
    =====''',
'''
  +---+
  O   |
  |   |
      |
    =====''',
'''
  +---+
  O   |
 /|   |
      |
    =====''',
'''
  +---+
  O   |
 /|\  |
      |
    =====''',
'''
  +---+
  O   |
 /|\  |
 /    |
    =====''', 
'''
  +---+
  O   |
 /|\  |
 / \  |
    =====''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar \
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk \
       lion lizard llama mole monkey moose mouse mule newt otter owl panda \
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep \
       skunk sloth snake spider stork swan tiger toad trout turkey turtle \
       weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
  # This function returns a random string from the passwd list of strings.
  wordIndex = random.randint(0, len(wordList) -1)
  return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
  print(HANGMAN_PICS[len(missedLetters)])
  print()

  print('Missed letters:', end=' ')
  for letter in missedLetters:
    print(letter, end=' ')
  print()

  blanks = '_'*len(secretWord)

  for i in range(len(secretWord)):
    if secretWord[i] in correctLetters:
      blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

  print(*blanks, sep=' ')

def getGuess(alreadyGuessed):
  while True:
    print('Guess a letter')
    guess = input().lower()
    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in alreadyGuessed:
      print('You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print('Please enter a LETTER')
    else:
      return guess

def playAgain():
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
  displayBoard(missedLetters, correctLetters, secretWord)

  guess = getGuess(missedLetters + correctLetters)

  if guess in secretWord:
    correctLetters += guess

    foundAllLetters = True
    for word in secretWord:
      if word not in correctLetters:
        print('word {}, correctLetters {}'.format(word, correctLetters))
        foundAllLetters = False
        break
    if foundAllLetters:
      print('Yes! The secret word is "{}"! You have won!'.format(secretWord))
      gameIsDone = True
  else:
    missedLetters += guess

    if len(missedLetters) == len(HANGMAN_PICS) - 1:
      displayBoard(missedLetters, correctLetters, secretWord)
      print('You have run out of guesses!\nAfter {} missed guesses and {} correct guesses, the word was "{}"'.format(len(missedLetters), len(correctLetters), secretWord))
      gameIsDone = True
  
  if gameIsDone:
    if playAgain():
      missedLetters = ''
      correctLetters = ''
      gameIsDone = False
      secretWord = getRandomWord(words)
    else:
      break

