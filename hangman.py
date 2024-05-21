import random
import string


def get_random_word():
    with open("words.txt", "r") as words:
        word_list = words.readlines()
    return random.choice(word_list).strip()


def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if (player_input not in guessed_letters) and (len(player_input) == 1):
            return player_input


def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))


def show_guessed_word(rand_word, guessed_letters):
    current_letters = []
    for letter in rand_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("-")
    return " ".join(current_letters)


if __name__ == "__main__":
    rand_word = get_random_word()
    guessed_letters = set()
    player_input = get_player_input(guessed_letters)
