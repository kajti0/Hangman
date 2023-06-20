import customtkinter
from game.Hangman import Hangman
from tkinter import messagebox
from helpers.DatabaseHelper import DatabaseHelper


class View():
    alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuwxyzźż"
    def __init__(self):
        self.hangman = Hangman()
        self.mydb = DatabaseHelper("localhost", "root", "Venafro8", "pythonProject")
        self.hangman.game(self.mydb.randomWord())

    def login(self):
        customtkinter.set_default_color_theme("dark-blue")
        root = customtkinter.CTk()
        root.title("Formularz logowania")
        root.geometry("250x200")

        label_username = customtkinter.CTkLabel(root, text="Nazwa użytkownika:")
        label_username.pack()

        entry_username = customtkinter.CTkEntry(root)
        entry_username.pack()

        label_password = customtkinter.CTkLabel(root, text="Hasło:")
        label_password.pack()

        entry_password = customtkinter.CTkEntry(root, show="*")
        entry_password.pack()

        #button_login = customtkinter.CTkButton(root, text="Zaloguj", command=login)
        button_login = customtkinter.CTkButton(root, text="Zaloguj")
        button_login.pack()

        root.mainloop()

    def game(self):
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()
        root.geometry("500x500")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        lives = customtkinter.CTkLabel(master=frame, text="")
        lives.pack(pady=12, padx=10)

        label = customtkinter.CTkLabel(master=frame, text="HANGMAN")
        label.pack(pady=12, padx=10)

        word = customtkinter.CTkLabel(master=frame, text=self.hangman.get_word())
        word.pack(pady=12, padx=10)

        result = customtkinter.CTkLabel(master=frame, text='')
        result.pack(pady=12, padx=10)


        def entryguess(letter):
            again = True
            while again:
                if len(letter) > 1 or len(letter) < 1:
                    raise Exception("Wpisz JEDEN znak!")
                elif letter not in self.alphabet:
                    raise Exception("Podaj LITERĘ!")
                elif letter in self.hangman.guessed:
                    raise Exception("Już użyłeś tej litery, podaj inną!")
                else:
                    again = False
            return letter

        entry = customtkinter.CTkEntry(master=frame, placeholder_text="Your guess:")
        entry.pack(pady=12, padx=10)



        def guessbutton():
            if not self.hangman.play:
                messagebox.showerror("ERROR", "KONIEC GRY")
            message = ""
            try:
                letter = entryguess(entry.get())
            except Exception as e:
                messagebox.showerror("ERROR", e.args[0])
            else:
                try:
                    message = self.hangman.guess(letter)
                except Exception as e:
                    messagebox.showerror("ERROR", e.args[0])
            lives.configure(text=("Lives left: " + str(7-self.hangman.score)))
            label.configure(text=message)
            word.configure(text = self.hangman.get_word())
            result.configure(text=self.hangman.get_hangman())


        button = customtkinter.CTkButton(master=frame, text="Guess", command=guessbutton)
        button.pack(pady=12, padx=10)

        def newgame():
            self.hangman.game(self.mydb.randomWord())
            label.configure(text="HANGMAN")
            word.configure(text=self.hangman.get_word())
            result.configure(text=self.hangman.get_hangman())
            lives.configure(text=("Lives left: " + str(7-self.hangman.score)))

        reload = customtkinter.CTkButton(master=frame, text="New Game", command=newgame)
        reload.pack(pady=12, padx=10)
        root.mainloop()

