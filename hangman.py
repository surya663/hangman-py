import random
import string


def get_random_word():
    with open("words.txt", "r") as words:
        word_list = words.readlines()
    return random.choice(word_list).strip()


def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if (player_input not in guessed_letters) and (
            player_input in string.ascii_lowercase
        ):
            return player_input


def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))


def hangman():
    rand_word = get_random_word()


hangman()
