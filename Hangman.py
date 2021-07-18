import random
print('Type the word to guess, with a space between every letter')
play_type = input('1p or 2p: ')
play_type.lower()
predetermined_words = ('h e l l o', 't a b l e', 'c h a i r', 's k y', 'b a c k _ p a c k', 'w h i t e b o a r d',
                       ' f a c e', 'm o b i l e', 'w a t e r', 'm o n e y', 's k i r t', 'f l o o r', 'h u n g e r',
                       'e a t i n g', 'c o m p u t e r', 'p y t h o n', 'd r a g o n', 'n e r d', 'f a c e _ m a s k',
                       'i c o n', 'p e r s o n', 'b o o k', 'r e a d', 'l i b r a r y', 'r e c e p t i o n',
                       'h o m e w o r k', 'j o k e', 'b u y e r', 'e s t a b l i s h m e n t', 'g i r l f r i e n d',
                       'd i s t r i b u t i o n')
if play_type == '2p':
    correct_word_str = input('> ')
else:
    correct_word_str = random.choice(predetermined_words)
correct_word_str = correct_word_str.lower()
correct_word = list(correct_word_str)
allowed_tries = input('Select the number of tries: ')
tries = 0
good_tries = 0
tries_left = 0
tried_letters = []
word_display = [['_'] * len(correct_word)]
position_of_letter = 0
# Space to not let the player see the correct word


def whiteSpace():
    print("""











    """)


print(word_display)
while tries < int(allowed_tries):

    guess = input('> ')
    whiteSpace()
    # Correct try
    if good_tries != len(correct_word) - 1:
        if guess in correct_word and guess not in tried_letters:
            tried_letters.insert(0, guess)
            print(f'{guess} was a correct letter!')
            good_tries += 1
            position_of_letter = correct_word.index(guess)
            word_display[0][position_of_letter] = guess
            print(word_display)
            print(f'You have tried: {tried_letters}')

        # Repeated correct try
        elif guess in correct_word and guess in tried_letters:
            print(f'You already had tried the letter {guess}')
            print(f'You now have {tries_left} tries left')

        #Incorrect Try
        elif guess not in correct_word and guess not in tried_letters:
            print(f'{guess} is not a correct letter')
            tries += 1
            tries_left = int(allowed_tries) - tries
            print(f'You now have {tries_left} tries left')
            print(word_display)
            print(f'You have tried: {tried_letters}')
            tried_letters.insert(0, guess)


        # Incorrect repeated try
        elif guess not in correct_word and guess  not in tried_letters:
            print(f'You already had tried the letter {guess}')
            print(word_display)
            print(f'You have tried: {tried_letters}')

    else:
        #Victory
        print(f'You guess it! The correct word was: {correct_word_str}')

print(f'You ran out of tries, the correct word was: {correct_word_str}')
