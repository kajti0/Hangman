from helpers.PasswordHelper import PasswordHelper


class User:
    def __init__(self, login, password, name=None, surname=None):
        self.__login = login
        self.__name = name
        self.__surname = surname
        self.__password = password
        self.__helper = PasswordHelper()

    def register(self, cursor):
        sql = "SELECT * from user where login = '" + self.__login + "'"
        cursor.execute(sql)
        if len(cursor.fetchall()) > 0:
            print("Podany login jest zajęty, spróbuj ponownie")
            return
        sql = "INSERT INTO user (login, name, surname, password) VALUES (%s, %s, %s, %s)"
        val = (self.__login, self.__name, self.__surname, self.__helper.generate_hash(self.__password))
        cursor.execute(sql, val)

    def login(self, cursor):
        sql = "SELECT password from user where login = '" + self.__login + "'"
        cursor.execute(sql)
        try:
            if self.__helper.check_password(self.__password, cursor.fetchall()[0][0]):
                sql = "SELECT user_id from user where login = '" + self.__login + "'"
                cursor.execute(sql)
                print(cursor.fetchall()[0][0])
            else:
                print("Password incorrect")
        except IndexError:
            print("There's no account with that username")