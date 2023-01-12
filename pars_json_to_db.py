from main import *
from json import dumps, load

with open('test.json', 'r+', encoding='utf-8') as file:
    workout = load(file)
    if workout == {}:
        print(1)
    cls_workout = {}
    for workout_key in workout.keys():
        clworkout = workout[workout_key]
        places = []
        if "Дом" in clworkout["Место"]:
            places.append(3)
        if "Спортивная площадка на улице" in clworkout["Место"]:
            places.append(2)
        if "Тренажерный Зал" in clworkout["Место"]:
            places.append(1)
        print(places)
        print(workout_key)
        create_training(workout_key, clworkout["Уровень"], clworkout["Пол"], clworkout["Тип"], clworkout["Описание"], clworkout["Группа мышц"],places)
