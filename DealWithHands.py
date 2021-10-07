import words.txt
f = open('words.txt', 'r')
content = f.read()
hand = {'h':1, 'e':1, 'l':2, 'm':1, 'o':1, 'i':1}
def updateHand(hand, word):
    """ function takes random hand given by program and a word chosen by player and checks if the word is in the 
     txt file. If the word is in the txt file then the funtion checks if the letters in the word are in the hand. 
     If the letters are in the hand, function checks if player has a letters needed if duplicates are needed using
     keys. 
    """
    if word.upper() in content:
         for letter in word:
              if letter in hand:
                      handcopy = hand.copy()
                              for letter in word:
                                      if letter in handCopy.keys():
                                          handCopy[letter] -=1
                              return handCopy
    else: return 'nope'

