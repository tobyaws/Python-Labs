vowels = "aeiou"
user_word = input("Please enter a word: ").lower()
count = 0
for letter in user_word:
    if letter in vowels:
        count += 1
print(count)
