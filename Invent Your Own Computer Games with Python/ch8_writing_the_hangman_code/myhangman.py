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

def randomWord(wordList):
  word = wordList[random.randint(0, len(wordList) -1)]
  return word

def getWord(enteredWords):
  while True:
    word = input('Enter a word : ').lower()
    if len(word) > 1:
      print('You can only enter one word')
    elif word in enteredWords:
      print('You already entered this word')
    elif word not in 'abcdefghijklmnopqrstuvwxyz':
      print('You can only enter a word')
    else:
      return word

answer = randomWord(words)
correctWords = ''
incorrectWords = ''

print('H A N G M A N')
endGame = False
while True:
  print(HANGMAN_PICS[len(incorrectWords)])
  print('Missed letters: ', end='')
  for word in incorrectWords:
    print(word, end=' ')
  print()
  
  blanks = '_'*len(answer)

  for i in range(len(answer)):
    if answer[i] in correctWords:
      blanks = blanks[:i] + answer[i] + blanks[i+1:]
  print(*blanks, sep=' ')

  word = getWord(correctWords + incorrectWords)

  if word in answer:
    correctWords += word
    
    foundAllLetters = True
    for i in range(len(answer)):
      if answer[i] not in correctWords:
        foundAllLetters = False
        break
    if foundAllLetters:
      print('Yes! The secret word is "{}"! You have won'.format(answer))
      endGame = True
  else:
    incorrectWords += word
    if len(incorrectWords) == len(HANGMAN_PICS)-1:
      print(HANGMAN_PICS[len(incorrectWords)])
      print('You failed! Answer was {}'.format(answer))
      endGame = True

  if endGame:    
    q = input('Do you want to play angain? (yes or no) ')

    if q.lower() in ['yes', 'y']:
      endGame = False
      answer = randomWord(words)
      correctWords = ''
      incorrectWords = ''
    else:
      break
