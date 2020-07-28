#This code converts vocabulary copied from quizlet to a format suitable
#for the memrise bulk add function, allowing you to import large amounts
#of words (up to 1000) at a time, with minimal human interaction.



#define variables
txt = ""
textList = []
temp = []
#var to store other phrases
invalid = ["Always correct","Sometimes Missed","Rarely Missed","Often Missed","No Answers Yet", "Select there"]

#open file to convert
txt = open("quizlet.txt", "r")
text = txt.read()
print(text)

#split by newlines
temp = text.split('\n')

#debug
print(temp)

#join english and french pairs, add comma and newline
for i in range(len(temp)-1):
	
	#check if temp[i] or temp[i+1] is blank, skip if true
	if temp[i] != "" and temp[i+1] != "":
		
		#check if temp[i] or temp[i+1] is a score, like +1
		if temp[i][0] != "+" and temp[i+1][0] != "+" and temp[i][0] != "-" and temp[i+1][0] != "-":
			
			#check if temp[i] or temp[i+1] is other
			if temp[i].split(" ")[:1] not in invalid:
				
				#add to answer list
				textList.append(temp[i] + " , " + temp[i+1] + "\n")
		
		#skip two so there are no repeats
		i += 1

#debug
print(textList)

#close input file
txt.close()

#open memrise file to write
txt = open("memrise.txt", "w")

#write all words in textList to output file
for i in range(len(textList)):
	txt.write(str(textList[i]))

#close output file file
txt.close()
