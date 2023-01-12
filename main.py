# This is a sample Python script.
import logging
import random
import psycopg2
from db_exceptions import UserException, PlaceException

DATABASE = "training_bot"
USER = "postgres"
PASSWORD = "0000"
HOST = "127.0.0.1"
PORT = "5432"


def init_database():
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(open("init.sql", "r").read())


def create_place(name: str):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO places(name) VALUES (%s)",
                    (name,))
        logging.info(f"place created ")


def create_training(name: str, lvl: int, gender: str, type: str,
                    description: str, muscle_group: str, places_id: list):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO trainings(name, lvl,gender,type,description,muscle_group) "
                    f"VALUES (%s, %s,%s, %s,%s, %s) RETURNING id;",
                    (name, lvl, gender, type, description, muscle_group))
        training_id = cur.fetchone()[0]
        logging.info(f"training with id =  {training_id} created ")
        for place_id in places_id:
            cur.execute(f"SELECT id FROM places WHERE id = {place_id}")
            if cur.fetchone() is None:
                raise ValueError(f"Place with id = {place_id} not found")
            else:
                cur.execute(f"INSERT INTO place_and_training(place_id,training_id) VALUES (%s, %s)",
                            (place_id, training_id))


def create_user(user_id, user_name):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:

            cur.execute(f"INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, user_name))
            logging.info(f"User with id = {user_id} successfully registered")
        else:
            logging.info(f"User with id = {user_id} already registered")


def get_user_info(user_id):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"select  name, age, weight, gender, lvl, "
                        f"training_goal, place_id from users where id = {user_id}")
            user = cur.fetchone()
            return {
                "name": user[0],
                "age": user[1],
                "weight": user[2],
                "gender": user[3],
                "lvl": user[4],
                "training_goal": user[5],
                "place_id": user[6],
            }

def get_trainings(lvl: int, gender: str, type: str,
    muscle_group: str, place_id: id=1, count=1):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM place_and_training WHERE place_id = {place_id}")
        place_ids = []
        while True: 
            row = cur.fetchone() 
            if row == None: 
                break
            else:
                place_ids.append(row[1])
        cur.execute("SELECT * FROM trainings WHERE lvl = {} and gender = '{}' and type = '{}' and muscle_group = '{}' and id in {}".format(lvl, gender, type, muscle_group, tuple(place_ids)))
        trainings = []
        while True: 
            row = cur.fetchone()
            if row == None: 
                break
            else:
                trainings.append("<a href='{}'>{}</a>".format(row[5], row[1]))
        random.shuffle(trainings)
        return trainings[0:count]

def set_user_name(user_id, name):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"update users set name = %s where id = %s", (name, user_id))
            logging.info(f"User with id = {user_id} updated")


def set_user_age(user_id, age: int):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"update users set age = %s where id = %s", (age, user_id))
            logging.info(f"User with id = {user_id} updated")


def set_user_lvl(user_id, lvl: int):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"update users set lvl = %s where id = %s", (lvl, user_id))
            logging.info(f"User with id = {user_id} updated")


def set_user_gender(user_id, gender: str):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"update users set gender = %s where id = %s", (gender, user_id))
            logging.info(f"User with id = {user_id} updated")


def set_user_training_task(user_id, training_goal: str):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"update users set training_goal = %s where id = %s", (training_goal, user_id))
            logging.info(f"User with id = {user_id} updated")


def set_user_weight(user_id, weight: float):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"update users set weight = %s where id = %s", (weight, user_id))
            logging.info(f"User with id = {user_id} updated")


def set_user_place(user_id, place_id: id):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:
            raise UserException()
        else:
            cur.execute(f"SELECT * FROM places WHERE id = {place_id}")
            if cur.fetchone() is None:
                raise PlaceException(f"place with id = {place_id} not found")
            else:
                cur.execute(f"update users set place_id = %s where id = %s", (place_id, user_id))
                logging.info(f"User with id = {user_id} updated")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_user(12121, "viktor")
    # create_place("Тренажерный Зал")
    # create_place("Спортивная площадка на улице")
    # create_place("Дом")
    # create_training("Австралийские подтягивания", 1, "M/F", 'база', 'https://t.me/trainigazbuka/23',
    #                 "спина", [1])
    # set_user_name(12121, "lox")
    # set_user_age(12121, 45)
    # set_user_weight(12121, 55.5)
    # set_user_lvl(12121, 1)
    # set_user_gender(12121, "male")
    # set_user_training_task(12121,"сдать опп")
    # set_user_place(12121,1)
    print(get_trainings(1, 'М/Ж', 'вспом', 'Спина',1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
