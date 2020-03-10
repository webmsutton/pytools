import re

with open('insertpath') as f:
	content = f.readlines()
f.close

for s in content:
	m = re.search('[0-9]{12,16}',s)
	if m != None:
		#Take each number and perform Luhn check
		#Split number into array
		
		
		numberList = list(m.group(0))
		outputList = []
		
		reversedList = list(reversed(numberList))

		#Counting from right (Including Check Number) double each second number
		x = 0
		checknumber = reversedList[0]
		reversedList[0] = 0
		for i in reversedList:
			
			if x % 2 == 0: 
				outputList.append(int(i))
			else:
				i = 2 * int(i)
				#If number is greater than 9 then add together to form output
				if i > 9:
					iList = list(str(i))
					i = int(iList[0]) + int(iList[1])
					outputList.append(i)
				

			x += 1
		
		#Sum the output excluding the the check number
		numsum = sum(outputList)

		#Multiply by 9 the last digit is the check digit
		finalNumber = (numsum * 9)
		
		#Compare to original check digit
		finalNumberList = list(str(finalNumber))
		lenoflist = len(finalNumberList)
		lastDigit = finalNumberList[lenoflist - 1]

		
		if lastDigit == checknumber:
			print lastDigit
			print 'SUSPICIOUS :' + m.group(0)
			print s
			
	


