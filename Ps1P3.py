#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

s = input('input string: ')
string = s[0]
tempstring = string

for i in range (1, len(s)):
    if ord(s[i]) >= ord(tempstring[-1]):
        tempstring += s[i]
        if len(tempstring) > len(string):
            string = tempstring
    else:
        tempstring = s[i]

print('Longest substring in alphabetical order is: ' + string)
