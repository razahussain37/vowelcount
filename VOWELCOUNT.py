# FIRST I WILL CREAT A VARIABLE WITH THE REQUIRED value
vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
#THAN I WILL ASK THE USER TO WRITE A WORD
word = input("Enter a word: ")
# SET THE COUNTER TO 0 SO THAT IF THE WORD HAS NOW VOEWL/S THE OUTPUT SHALL BE "your word has  0 vowel/s."
count = 0
#THAN I WILL SET THE CONDITIONAL STATEMENT
for letter in word:
    if letter in vowels:
        count += 1
# FINALLY GIVE AN OUTPUT WITH THE NUMBER OF VOWELS
print("your word has " ,count, "vowel/s.")

