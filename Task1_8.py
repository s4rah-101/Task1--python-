#Accept a word from the user. Create a dictionary with key as the letter and value as the number of occurrences.

word = input("Enter a word: ")
value = {}

for letter in word:
    if letter in value:
        value[letter] += 1
    else:
        value[letter] = 1

print("Letter occurrences are:", value)
