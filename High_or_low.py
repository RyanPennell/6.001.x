#!/usr/bin/ry4n python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:04:39 2019

@author: user
"""
low = 0
high = 100
guesses = 0
guess = int( (high + low)/2.0)
print("Please think of a number between 0 and 100!")
print("Is your secret number ", guess,"?")
ans=str(input(("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")))
while ans != "c":
    if ans == "h":
        high = guess
        guess = int((low + guess)/2)
        guesses += 1
        print("Is your secret number ", guess,"?")
        ans=str(input(("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")))
        
    elif ans == "l":
        low = guess
        guess = int((high + guess)/2)
        guesses +=1
        print("Is your secret number ", guess,"?")
        ans=str(input(("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")))
    
    else: 
        print("Sorry, I did not understand your input.")
        print("Is your secret number ", guess,"?")
        ans=str(input(("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")))
        
    
        
print("Game over. Your secret number was: ", guess)       

