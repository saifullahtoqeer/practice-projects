from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()
print(word)

turns = 9
letters_used = []
letters = ""
p = ""
for i in word:
    if i not in p:
        p = p + i

# print(p, len(p))
while turns!=0:
    input_char = input("Enter a character: ")
    if len(input_char) > 1 or not isinstance(input_char, str):
        print("You entered something wrong...")
        continue

    if input_char in letters_used:
        print(f'You\'ve already used {input_char}')
        continue

    if input_char in word:
        # letters.append(input_char)
        letters = letters + input_char
        letters_used.append(input_char)
        for i in word:
            if i in letters:
                print(i, end="")
            else:
                print("_", end="")
        print()
        if len(letters) == len(p):
            print("Congratulations. You've win the game. ")
            exit()
        continue
    else:
        letters_used.append(input_char)
        turns = turns - 1
        print("Wrong Guess")
        print(f"{turns} turns left.")
        if turns == 0:
            print(f"Oh. Game Over. You lost. The actual word that you had to guess was: {word}")


