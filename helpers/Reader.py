from os import system, name
from subprocess import call
import os


class Reader:
    alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuwxyzźż"
    def readLetter(self, guessed):
        again = True
        letter = ""
        while again:
            letter = input("Enter a letter: ")
            if len(letter) > 1 or len(letter) < 1:
                print("Wpisz JEDEN znak!")
            elif letter not in self.alphabet:
                print("Podaj LITERĘ!")
            elif letter in guessed:
                print("Już użyłeś tej litery, podaj inną!")
            else:
                again = False
        return letter
