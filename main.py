from random import randint
import json

with open('words.json', 'r') as f:
    words = json.load(f)['data']


def hangman_game():
    current_word = words[randint(0, len(words) - 1)]
    secret_current_word = ['_'] * len(current_word)
    letters_current_word = [letter for letter in current_word]

    guessed_letters = []
    inputs_to_hang = round((len(current_word) / 26) * 100)

    print("let's play hangman\n".upper())

    while True:
        if inputs_to_hang != 0 and '_' in secret_current_word:
            print(' '.join(secret_current_word))
            print(f'you can make {inputs_to_hang} mistakes')
            player_input = input('enter a letter\n').lower()

            if player_input in letters_current_word:
                if player_input not in guessed_letters:
                    for letter in range(0, len(letters_current_word)):
                        if letters_current_word[letter] == player_input:
                            secret_current_word[letter] = player_input
                            guessed_letters.append(player_input)
                    continue
                else:
                    print('you have already guessed that!\n')
                    continue
            else:
                print('wrong guess buddy\n')
                inputs_to_hang = inputs_to_hang - 1
        elif '_' not in secret_current_word:
            print('\nyou won! congrats')
            break
        elif inputs_to_hang == 0:
            print('\nyou got hanged! game over')
            print(f'password was: {current_word}')
            break


hangman_game()
