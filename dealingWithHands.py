def updateHand(hand, word):
handCopy = hand.copy()
    for letter in word:
        if letter in handCopy.keys():
            handCopy[letter] -= 1
    return handCopy 
