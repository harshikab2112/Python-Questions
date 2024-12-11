char = input("Enter a Character: ")

if char.isalpha() and len(char) == 1:
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    if char in vowel:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")
else:
    print("Please enter a valid single alphabet character.")
