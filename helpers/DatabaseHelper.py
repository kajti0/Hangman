import random
from singleton.Singleton import Singleton
import mysql.connector


class DatabaseHelper(metaclass=Singleton):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def __del__(self):
        self.mydb.close()

    def getmydb(self):
        return self.mydb

    def addWordToDatabase(self, word):
        sql = "select word from words"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if (word, ) in result:
            print("This element already exists in database!\n")
        else:
            sql = "INSERT INTO words (word) VALUES (%s)"
            val = (word, )
            self.cursor.execute(sql, val)
            self.mydb.commit()
            print("Added your word successfully")

    def randomWord(self):
        sql = "select count(*) from words"
        self.cursor.execute(sql)
        max = int(self.cursor.fetchall()[0][0])
        index = random.randint(1, max-1)
        sql = "select word from words where word_id = %s"
        val = (index, )
        self.cursor.execute(sql, val)
        word = self.cursor.fetchall()[0][0]
        return word


