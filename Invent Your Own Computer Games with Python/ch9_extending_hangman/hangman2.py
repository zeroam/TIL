import random

def hangmangDisplay():

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
      =====''',
  '''
    +---+
   [O   |
   /|\  |
   / \  |
      =====''',
  '''
    +---+
   [O]  |
   /|\  |
   / \  |
      =====''']
  
  difficulty = 'X' 
  while difficulty not in ['E', 'M', 'H']:
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
  if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
  if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

  return HANGMAN_PICS

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
      'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
      'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
      'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose \
       mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
  wordKey = random.choice(list(wordDict.keys()))
  wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

  return [wordDict[wordKey][wordIndex], wordKey]

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
HANGMAN_PICS = hangmangDisplay()
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
  print('The secret word is in the set: ' + secretSet)
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
      HANGMAN_PICS = hangmangDisplay()
      missedLetters = ''
      correctLetters = ''
      gameIsDone = False
      secretWord, secretSet = getRandomWord(words)
    else:
      break

