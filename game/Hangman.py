from typing import Dict
from time import sleep
from helpers.Reader import Reader
import os

class Hangman:
    alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuwxyzźż"

    stages: Dict = {0: "",
                    1:  " \n"
                        " ||        \n"
                        " ||         \n"
                        " ||         \n"
                        "//\\\\       ",
                    2:  " +========+\n"
                        " ||         \n"
                        " ||         \n"
                        " ||        \n"
                        "//\\\\       ",
                    3:  " +========+\n"
                        " ||       O\n"
                        " ||       | \n"
                        " ||        \n"
                        "//\\\\       ",
                    4:  " +========+\n"
                        " ||       O\n"
                        " ||      /| \n"
                        " ||        \n"
                        "//\\\\       ",
                    5:  " +========+\n"
                        " ||       O\n"
                        " ||      /|\\\n"
                        " ||         \n"
                        "//\\\\        ",
                    6:  " +========+\n"
                        " ||       O\n"
                        " ||      /|\\\n"
                        " ||      /\n"
                        "//\\\\      ",
                    7:  " +========+\n"
                        " ||       O\n"
                        " ||      /|\\\n"
                        " ||      / \\\n"
                        "//\\\\       "}

    def __init__(self):
        self.lettersToGuess = []
        self.Reader = Reader()
        self.clear = lambda: os.system('cls')
        self.score = 0
        self.play = True
        self.guessed = []
        self.word = ""

    def start(self):
        for i in range(1, 8):
            print(self.stages[i])
            sleep(1)

    def get_word(self):
        result = ""
        for letter in self.word:
            if letter in self.guessed:
                result += letter + " "
            else:
                result += "_ "
        return result

    def get_hangman(self):
        return self.stages[self.score]

    def game(self, word):
        self.word = word
        self.score = 0
        self.play = True
        self.guessed = []
        self.lettersToGuess = list(dict.fromkeys(list(word)))

    def guess(self, letter):
        if letter in self.word:
            self.guessed.append(letter)
            if len(self.guessed) == len(self.lettersToGuess):
                return "WYGRAŁEŚ"
            return "Zgadłeś!"
        else:
            self.score += 1
            if self.score >= 7:
                self.play = False
                raise Exception("GAME END - wszystkie życia wykorzystane!")
            return "Nie zgadłeś!"


    def read_guess(self):
        again = True
        letter = ""
        while again:
            letter = input("Enter a letter: ")
            if len(letter) > 1 or len(letter) < 1:
                print("Wpisz JEDEN znak!")
            elif letter not in self.alphabet:
                print("Podaj LITERĘ!")
            elif letter in self.guessed:
                print("Już użyłeś tej litery, podaj inną!")
            else:
                again = False
        return letter

