sentence=input('Enter a sentence:')
words=sentence.split()                  #split into words 
words.sort()                            #sort alphabetically
print("Sorted words:")                  #Uppercase is sorted before the lower case(Upper case has lower ASCII value than lower case)
for word in words:
    print(word)
