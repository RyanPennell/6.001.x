#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print

s = 'azcbobobegghakl'
i=0
bobs = 0
for i in range(len(s)):
	if s[i:i+3]=='bob':
		bobs+=1
print("Number of times bob occurs is: " + str(bobs))
