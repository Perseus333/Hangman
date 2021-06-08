print('Type the word to guess, with a space between every letter')
correct_word_str = input('> ')
correct_word_str = correct_word_str.lower()
correct_word = correct_word_str.split(" ")
allowed_tries = input('Select the number of tries: ')
tries = 0
good_tries = 0
tried_letters = []
word_display = [['_'] * len(correct_word)]
position_of_letter = 0
# Space to not let the player see the correct word
print("""











""")

print(word_display)
while tries < int(allowed_tries):

    guess = input('> ')


    if guess in correct_word and guess not in tried_letters:
        print(f'{guess} was a correct letter!')
        good_tries += 1
        position_of_letter = correct_word.index(guess)
        word_display[0][position_of_letter] = guess
        print(word_display)

    elif guess in correct_word and guess in tried_letters:
        print(f'You already had tried the letter {guess}')
        if good_tries == len(correct_word):
            print(f'You guess it!, the correct word was {correct_word_str}')

    elif guess not in correct_word and guess not in tried_letters:
        print(f'{guess} is not a correct letter')
        tries += 1
    elif guess not in correct_word and guess in tried_letters:
        print(f'You already had tried the letter {guess}')

    tried_letters.insert(0, guess)

print(f'You ran out of tries, the correct word was: {correct_word_str}')
