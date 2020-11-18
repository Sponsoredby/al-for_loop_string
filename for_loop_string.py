#set the variable str & count
str = 'This is a test, testing for loops inside this string'
count = 0

	#for every defined letter search the above string and count it
for x in str:
	if (x == 't'):
		count +=1
		
#print the count		
print (count)

#SKILLS for loop & nested statement
#VERSION print text with count, let users  input a single letter and if that letter is in string print the count else print 'letter not in sentence' also need to be able to exit somehow