import sqlite3


class Person:

    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.first = first
        self.last = last
        self.age = age
        self.id_number = id_number
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute(f"""
        SELECT * FROM persons
        WHERE id = {id_number}""")
        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute(f"""
        INSERT INTO persons VALUES ( {self.id_number},'{self.first}','{self.last}',{self.age})
        """)
        self.connection.commit()
        self.connection.close()


# connection = sqlite3.connect('mydata.db')
# cursor = connection.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
# )
# """)
#
# cursor.execute("""
# INSERT INTO persons VALUES(1,'Paul','Smith',24),(2,'Mark','Johnson',42),(3,'Anna','Smith',34)
# """
#                )
#
# cursor.execute("""
# SELECT * FROM persons
# WHERE last_name = 'Smith'
# """)
#
# rows = cursor.fetchall()
# print(rows)
# connection.commit()
# connection.close()

if __name__ == '__main__':
    person = Person()
    person.load_person(3)
    print(person.first)
    print(person.age)
    new_person = Person(4,"Pranav","Arora",26)
    new_person.insert_person()
    connection = sqlite3.connect('mydata.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM persons")
    result = cursor.fetchall()
    print(result)
    connection.close()
