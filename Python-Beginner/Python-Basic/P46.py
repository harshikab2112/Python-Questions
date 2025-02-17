# Accept a string and print the count of vowels and consonants in it.

string = input("Enter a string: ")
vowel = set("AEIOUaeiou")
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():
        if char in vowel:
            vowel_count += 1
        else:
            consonant_count += 1

print(
    f"No. of vowels in {string} is {vowel_count}.\nNo. of consonants in {string} is {consonant_count}."
)
