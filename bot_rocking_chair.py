import datetime
import logging
import aiogram
import random
from json import dumps, load
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ContentType
import asyncio
from main import *

#Bot_init
bot = aiogram.Bot(token="5510500493:AAEgGLG9UWJqHmGmgHewRuZUU0t0Cc5ZGvs", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.ERROR, filename="log/{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d")), filemode="w")

class Form(StatesGroup):
    change_key = State()
    value = State()
    workout_set = State()
    save = State()
    group_set = State()



#Handlers
@dp.message_handler(commands="start")
async def start_message(message : Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Быстрая тренировка", callback_data="fast_workout"))
    keyboard.add(InlineKeyboardMarkup(text="Персональная тренировка", callback_data="personal_workout"))
    keyboard.add(InlineKeyboardMarkup(text="Мои параметры", callback_data="characteristics"))
    keyboard.add(InlineKeyboardMarkup(text="Дневник тренировок", callback_data="diary_workout"))
    keyboard.add(InlineKeyboardMarkup(text="Описание кнопок", callback_data="description"))
    await message.answer(text="Добро пожаловать!\
                             \nВыберите пункт меню", reply_markup=keyboard, )


@dp.callback_query_handler(text='start')
async def start_call(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Быстрая тренировка", callback_data="fast_workout"))
    keyboard.add(InlineKeyboardMarkup(text="Персональная тренировка", callback_data="personal_workout"))
    keyboard.add(InlineKeyboardMarkup(text="Мои параметры", callback_data="characteristics"))
    keyboard.add(InlineKeyboardMarkup(text="Дневник тренировок", callback_data="diary_workout"))
    keyboard.add(InlineKeyboardMarkup(text="Описание кнопок", callback_data="description"))
    await call.message.answer(text="Добро пожаловать!\
                             \nВыберите пункт меню", reply_markup=keyboard)


@dp.callback_query_handler(text='description')
async def description_call(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Главное меню", callback_data="start"))
    await call.message.answer(text="Добро пожаловать!\
                                  \nЯ ваш персональный помощник по тренировкам.\n\
                                  \nВсе упражнения берутся из базы и каждый раз будут меняться, чтобы вам было не скучно заниматься.\n\
                                  \n«Быстрая тренировка» - тут доступны тренировки, не учитывающие ваши персональные параметры, но учитывающие место тренировки.\n\
                                  \n«Персональная тренировка» - тут доступны тренировки, учитывающие ваши параметры, цели и место проведения тренировки. Для упражнений будут рассчитаны количество подходов и необходимые веса.\n\
                                  \n«Мои параметры» - ваши персональные параметры, необходимые для подбора оптимальной тренировки.\n\
                                  \n«Дневник тренировок» – тут можно посмотреть историю занятий.", reply_markup=keyboard)


@dp.callback_query_handler(text='fast_workout')
async def fast_workout(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardMarkup(text="Силовая", callback_data="power")
    button_2 = InlineKeyboardMarkup(text="День ног", callback_data="Ноги")
    keyboard.row(button_1, button_2)
    keyboard.add(InlineKeyboardMarkup(text="Кардио", callback_data="Кардио"))
    keyboard.add(InlineKeyboardMarkup(text="Функциональная", callback_data="Функциональная"))
    keyboard.add(InlineKeyboardMarkup(text="Главное меню", callback_data="start"))
    await call.message.answer(text="Выберите тип тренировки:\
                                \n<b>Силовая тренировка</b>:\
                                  \n\t* Одно упражнение на разминку\
                                  \n\t* Три упражнения на одну группы мышц\
                                  \n\t* Три упражнения на другую группу мышц\
                                  \n\t* Одно упражнение на пресс\
                                \n<b>Тренировка на ноги</b>:\
                                  \n\t* Одно упражнение на разминку\
                                  \n\t* Пять упражнений на ноги\
                                  \n\t* Одно упражнение на пресс\
                                \n<b>Кардио тренировка</b>:\
                                  \n\t* 30 минут упражнения на кардио\
                                  \n\t* Одно упражнение на пресс\
                                \n<b>Функциональная тренировка</b>:\
                                  \n\t* Одно упражнение на разминку\
                                  \n\t* Пять функциональных упражнений\n\
                                \nВсе упражнения подбираются из базы и каждую новую тренировку меняются, чтобы вам было интересно заниматься.", reply_markup=keyboard)

@dp.callback_query_handler(text='power')
async def power(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Грудь", callback_data="Грудь_1"))
    keyboard.add(InlineKeyboardMarkup(text="Ноги", callback_data="Ноги_1"))
    keyboard.add(InlineKeyboardMarkup(text="Спина", callback_data="Спина_1"))
    keyboard.add(InlineKeyboardMarkup(text="Бицепс", callback_data="Бицепс_1"))
    keyboard.add(InlineKeyboardMarkup(text="Плечи", callback_data="Плечи_1"))
    keyboard.add(InlineKeyboardMarkup(text="Трицепс", callback_data="Трицепс_!"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="fast_workout"))
    await call.message.answer(text="Выберите первую группу мышц", reply_markup=keyboard)

@dp.callback_query_handler(text='Грудь_1')
@dp.callback_query_handler(text='Ноги_1')
@dp.callback_query_handler(text='Спина_1')
@dp.callback_query_handler(text='Бицепс_1')
@dp.callback_query_handler(text='Плечи_1')
@dp.callback_query_handler(text='Трицепс_1')
async def power_1(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(group_set=call.data[:-2])
    print(call.data[:-2])
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Грудь", callback_data="Грудь_2"))
    keyboard.add(InlineKeyboardMarkup(text="Ноги", callback_data="Ноги_2"))
    keyboard.add(InlineKeyboardMarkup(text="Спина", callback_data="Спина_2"))
    keyboard.add(InlineKeyboardMarkup(text="Бицепс", callback_data="Бицепс_2"))
    keyboard.add(InlineKeyboardMarkup(text="Плечи", callback_data="Плечи_2"))
    keyboard.add(InlineKeyboardMarkup(text="Трицепс", callback_data="Трицепс_2"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="fast_workout"))
    await call.message.answer(text="Выберите вторую группу мышц", reply_markup=keyboard)

@dp.callback_query_handler(text='Ноги')
async def power(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    workout_set = "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', 'Разминка'))
    workout_set += "\n\t* " + "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', 'Ноги', count=5))
    workout_set += "\n\t* " + "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', 'Пресс'))
    await state.update_data(workout_set=workout_set)
    await state.update_data(save=workout_set.split("\n\t* "))
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Начать тренировку", callback_data="workout"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="fast_workout"))
    await call.message.answer(text="Ваша программа тренировки на сегодня\n<b>{}</b>\n\n\t* {}".format(call.data, workout_set), reply_markup=keyboard, disable_web_page_preview=True)
    
@dp.callback_query_handler(text='Грудь_2')
@dp.callback_query_handler(text='Ноги_2')
@dp.callback_query_handler(text='Спина_2')
@dp.callback_query_handler(text='Бицепс_2')
@dp.callback_query_handler(text='Плечи_2')
@dp.callback_query_handler(text='Трицепс_2')
async def power(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    workout_sets = await state.get_data()
    group_set = workout_sets["group_set"] + " + " + call.data[:-2]
    workout_set = "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', 'Разминка'))
    workout_set += "\n\t* " + "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', call.data[:-2], count=3))
    workout_set += "\n\t* " + "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', str(workout_sets["group_set"]), count=3))
    workout_set += "\n\t* " + "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', 'Пресс'))
    await state.update_data(workout_set=workout_set)
    await state.update_data(save=workout_set.split("\n\t* "))
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Начать тренировку", callback_data="workout"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="power"))
    await call.message.answer(text="Ваша программа тренировки на сегодня\n<b>{}</b>\n\n\t* {}".format(group_set, workout_set), reply_markup=keyboard, disable_web_page_preview=True)

@dp.callback_query_handler(text='Кардио')
async def power(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    workout_set = get_trainings(1, 'М/Ж', 'база', 'Кардио')[0] +  " - выполнять 30 минут \n\t* " + get_trainings(1, 'М/Ж', 'база', 'Пресс')[0]
    await state.update_data(workout_set=workout_set)
    await state.update_data(save=workout_set.split("\n\t* "))
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Начать тренировку", callback_data="workout"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="fast_workout"))
    await call.message.answer(text="Ваша программа тренировки на сегодня\n<b>{}</b>\n\n\t*{}".format(call.data, workout_set), reply_markup=keyboard, disable_web_page_preview=True)

@dp.callback_query_handler(text='Функциональная')
async def power(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    workout_set = get_trainings(1, 'М/Ж', 'база', 'Разминка')[0] +  "\n\t* " + "\n\t* ".join(get_trainings(1, 'М/Ж', 'база', 'Функциональная', count=5))
    await state.update_data(workout_set=workout_set)
    await state.update_data(save=workout_set.split("\n\t* "))
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Начать тренировку", callback_data="workout"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="fast_workout"))
    await call.message.answer(text="Ваша программа тренировки на сегодня\n<b>{}</b>\n\n\t*{}".format(call.data, workout_set), reply_markup=keyboard, disable_web_page_preview=True)


@dp.callback_query_handler(text='workout')
async def workout_set(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    workout_set = await state.get_data()
    save = workout_set["save"]
    workout_set = workout_set["workout_set"]
    keyboard = InlineKeyboardMarkup()
    if isinstance(workout_set, str):
        workout_set = workout_set.split("\n\t* ")
    if len(workout_set) > 1:
        workout = workout_set.pop(0)
        await state.update_data(workout_set=workout_set)
        keyboard.add(InlineKeyboardMarkup(text="Следующее упражнение(без отдыха)", callback_data="workout"))
        keyboard.add(InlineKeyboardMarkup(text="Следующее упражнение(5 мин. отдыха)", callback_data="timer"))
        keyboard.add(InlineKeyboardMarkup(text="Прервать тренировку", callback_data="fast_workout"))
        await call.message.answer(text=workout, reply_markup=keyboard)
    else:
        workout = workout_set.pop(0)
        await state.update_data(workout_set=workout_set)
        keyboard.add(InlineKeyboardMarkup(text="Закончить тренировку", callback_data="fast_workout"))
        Users_diary.new_diary(call.from_user.id, save)
        await call.message.answer(text=workout, reply_markup=keyboard)


@dp.callback_query_handler(text='timer')
async def power(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Оставшееся время отдыха - 2:00")
    for sec in range(119, 0, -1):
        sec = sec % (24 * 3600) 
        sec %= 3600 
        min = sec // 60 
        sec %= 60 
        await bot.edit_message_text(text="Оставшееся время отдыха - {}:{}".format(min, sec), message_id=call.message.message_id+1, chat_id=call.message.chat.id)
        await asyncio.sleep(1)
    await bot.delete_message(call.message.chat.id, call.message.message_id+1)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Закончить отдыхать", callback_data="workout"))
    await call.message.answer(text="Время вышло!", reply_markup=keyboard)

class Diary:

    def __init__(self, date, workout_set):
        self.date = date
        self.workout_set = workout_set

    def __str__(self) -> str:
        workout_set =  "\n\t* ".join(self.workout_set)
        return "{}\
            \nВы сделали: \n\t* {}".format(self.date, workout_set)

    def to_dict(self):
        return self.__dict__

class Users_diary:

    def __init__(self) -> None:
        pass

    @classmethod
    def get_users_diary_dict(cls):
        with open('diary.json', 'r+', encoding='utf-8') as file:
            return load(file)

    @classmethod
    def get_users_diary(cls):
        with open('diary.json', 'r+', encoding='utf-8') as file:
            users = load(file)
            if users == {}:
                return {}
            cls_users = {}
            for diory in users.keys():
                cls_users[str(diory)] = []
                for diary_key in users[str(diory)].keys():
                    user = users[str(diory)][str(diary_key)]
                    cls_users[str(diory)].append(Diary(diary_key, user))
            return cls_users

    @classmethod
    def new_diary(cls, id, workout_set):
        users = Users_diary.get_users_diary_dict()
        user = users[str(id)]
        if len(user) > 5:
            old_date = datetime.datetime.now()
            old_dates = []
            for _ in user.keys():
                if datetime.datetime.now() - datetime.timedelta(days=7) > datetime.datetime(int(_[:4]), int(_[5:7]), int(_[8:10])):
                    old_dates.append(str(datetime.datetime(int(_[:4]), int(_[5:7]), int(_[8:10])).strftime("%Y-%m-%d")))
                elif old_date > datetime.datetime(int(_[:4]), int(_[5:7]), int(_[8:10])):
                    old_date = datetime.datetime(int(_[:4]), int(_[5:7]), int(_[8:10]))
            user.pop(str(old_date.strftime("%Y-%m-%d")))
            for __ in old_dates:
                user.pop(__)
        with open('diary.json', 'w') as file:
            data = {**users, str(id): {Diary(datetime.datetime.now().strftime("%Y-%m-%d"), workout_set).to_dict()["date"] : Diary(datetime.datetime.now().strftime("%Y-%m-%d"), workout_set).to_dict()["workout_set"], **user}}
            file.write(dumps(data))



class Workout():

    def __init__(self, title, level, gender, type, location, link, group, type_workout):
        self.title = title
        self.level = level
        self.gender = gender
        self.type = type
        self.location = location
        self.link = link
        self.group = group
        self.type_workout = type_workout

class Workouts():
    def __init__(self) -> None:
        pass

    @classmethod
    def workout_personal(cls, id, group, type_workout, count_workout=8):
        workouts = Workouts.get_workouts_dict()
        user = Users_characteristics.get_users_dict()[str(id)]
        level = user["level"]
        place = user["place"]
        if user["level"] == "Не указано":
            level = 1
        if user["gender"] == "Не указано":
            gender = "М/Ж"
        elif user["gender"] == "Мужской":
            gender = "М"
        elif user["gender"] == "Женский":
            gender = "Ж"
        if user["place"] == "Не указано":
            place = "Тренажерный зал, Спортивная площадка на улице, Дом"
        set_workouts_one = set()
        set_workouts_two = set()
        workout_keys = list(workouts.keys())
        random.shuffle(workout_keys)
        grp = "Разминка"
        for title in workout_keys:
            workout = workouts[title]
            if len(set_workouts_one) == count_workout-2:
                break
            elif len(set_workouts_two) >= 2:
                grp = group
            if all([workout["Уровень"] <= int(level), gender in workout["Пол"],\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if len(set_workouts_two) >= 2:
                    if not workout in set_workouts_one:
                        set_workouts_one.add(workout)
                else:
                    if not workout in set_workouts_two:
                        set_workouts_two.add(workout)
        return list(list(set_workouts_two) + list(set_workouts_one))

    @classmethod
    def workout_power(cls, id, group, type_workout, count_workout=8):
        workouts = Workouts.get_workouts_dict()
        users_d = Users_diary.get_users_diary_dict()
        old_workout_set = []
        if str(id) in users_d.keys():
            data = datetime.datetime.now() - datetime.timedelta(days=1)
            old_date = data.strftime("%Y-%m-%d")
            if str(old_date) in users_d[str(id)].keys():
                old_workout_set = users_d[str(id)][old_date]
        level = 1
        place = "Тренажерный Зал"
        set_workouts = []
        workout_keys = list(workouts.keys())
        random.shuffle(workout_keys)
        grp = "Разминка"
        for title in workout_keys:
            workout = workouts[title]
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
                    grp = group
                    break
        for title in workout_keys:
            workout = workouts[title]
            if len(set_workouts) == count_workout-1:
                grp = "Пресс"
                break
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
        for title in workout_keys:
            workout = workouts[title]
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
                    break
        return set_workouts

    @classmethod
    def workout_cardio(cls, id, type_workout):
        workouts = Workouts.get_workouts_dict()
        users_d = Users_diary.get_users_diary_dict()
        old_workout_set = []
        if str(id) in users_d.keys():
            data = datetime.datetime.now() - datetime.timedelta(days=1)
            old_date = data.strftime("%Y-%m-%d")
            if str(old_date) in users_d[str(id)].keys():
                old_workout_set = users_d[str(id)][old_date]
        level = 1
        place = "Тренажерный Зал"
        set_workouts = []
        workout_keys = list(workouts.keys())
        random.shuffle(workout_keys)
        grp = "Кардио"
        for title in workout_keys:
            workout = workouts[title]
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
                    grp = "Пресс"
                    break
        for title in workout_keys:
            workout = workouts[title]
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
                    break
        return set_workouts

    @classmethod
    def workout_func(cls, id, type_workout):
        workouts = Workouts.get_workouts_dict()
        users_d = Users_diary.get_users_diary_dict()
        old_workout_set = []
        if str(id) in users_d.keys():
            data = datetime.datetime.now() - datetime.timedelta(days=1)
            old_date = data.strftime("%Y-%m-%d")
            if str(old_date) in users_d[str(id)].keys():
                old_workout_set = users_d[str(id)][old_date]
        level = 1
        place = "Тренажерный Зал"
        set_workouts = []
        workout_keys = list(workouts.keys())
        random.shuffle(workout_keys)
        grp = "Разминка"
        for title in workout_keys:
            workout = workouts[title]
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
                    grp = "Функциональная"
                    break
        for title in workout_keys:
            workout = workouts[title]
            if all([workout["Уровень"] <= int(level),\
                    place in workout["Место"], workout["Группа мышц"] in grp,\
                    workout["Тип тренировки"] == type_workout]):
                workout = "<a href='{}'>{}</a>".format(workout["Описание"], title)
                if not workout in set_workouts and not workout in old_workout_set:
                    set_workouts.append(workout)
                if len(set_workouts) > 6:
                    break
        return set_workouts

class User_characteristics:

    def __init__(self, name, age="Не указано", height="Не указано", weight="Не указано", gender="Не указано", level="Не указано", task="Не указано", place="Не указано"):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.level = level
        self.task = task
        self.place = place

    def __str__(self) -> str:
        return "Имя: {}\
            \nВозраст: {}\
            \nРост: {}\
            \nВес: {}\
            \nПол: {}\
            \nУровень подготовки: {}\
            \nЦель тренировок: {}\
            \nМесто занятий: {}".format(self.name, self.age, self.height, self.weight, self.gender, self.level, self.task, self.place)

    def to_dict(self):
        return self.__dict__

class Users_characteristics:

    def __init__(self) -> None:
        pass

    @classmethod
    def get_users(cls):
        with open('users_characteristics.json', 'r+', encoding='utf-8') as file:
            users = load(file)
            if users == {}:
                return {}
            cls_users = {}
            for user_key in users.keys():
                user = users[user_key]
                cls_users[user_key] = User_characteristics(user["name"], user["age"], user["height"], user["weight"], user["gender"], user["level"], user["task"], user['place'])
            return cls_users

    @classmethod
    def get_users_dict(cls):
        with open('users_characteristics.json', 'r+', encoding='utf-8') as file:
            return load(file)

    @classmethod
    def new_user(cls, id, name):
        users = Users_characteristics.get_users_dict()
        with open('users_characteristics.json', 'w') as file:
            data = {**users, str(id): User_characteristics(name).to_dict()}
            file.write(dumps(data))

    @classmethod
    def change_characteristics(cls, id, characteristic, value):
        users = Users_characteristics.get_users_dict()
        with open('users_characteristics.json', 'w') as file:
            users[id][characteristic] = value
            file.write(dumps(users))


@dp.callback_query_handler(text='characteristics')
async def characteristic(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Изменить параметры", callback_data="change"))
    keyboard.add(InlineKeyboardMarkup(text="Главное меню", callback_data="start"))
    users = Users_characteristics.get_users()
    users_id = list(users.keys())
    if not str(call.from_user.id) in users_id:
        Users_characteristics.new_user(call.from_user.id, str(call.from_user.full_name))
        users = Users_characteristics.get_users()
    await call.message.answer(str(users[str(call.from_user.id)]), reply_markup=keyboard)

@dp.callback_query_handler(text='diary_workout')
async def characteristic(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Главное меню", callback_data="start"))
    users = Users_diary.get_users_diary()
    if users == {}:
        await call.message.answer("За последнею неделю вы не тренировались", reply_markup=keyboard)
    elif not str(call.from_user.id) in users.keys():
        await call.message.answer("За последнею неделю вы не тренировались", reply_markup=keyboard)
    else:
        await call.message.answer("\n\n".join([ str(_) for _ in users[str(call.from_user.id)]]), reply_markup=keyboard, disable_web_page_preview=True)    
        
@dp.callback_query_handler(text='change')
async def change(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Имя", callback_data="name"))
    keyboard.row(InlineKeyboardMarkup(text="Возраст", callback_data="age"), InlineKeyboardMarkup(text="Рост", callback_data="height"))
    keyboard.row(InlineKeyboardMarkup(text="Вес", callback_data="weight"), InlineKeyboardMarkup(text="Пол", callback_data="gender"))
    keyboard.row(InlineKeyboardMarkup(text="Уровень", callback_data="level"), InlineKeyboardMarkup(text="Цель тренировки", callback_data="task"))
    keyboard.add(InlineKeyboardMarkup(text="Место тренировки", callback_data="place"))
    keyboard.add(InlineKeyboardMarkup(text="Вернуться назад", callback_data="characteristics"))
    users = Users_characteristics.get_users()
    await call.message.answer(str(users[str(call.from_user.id)]), reply_markup=keyboard)


@dp.callback_query_handler(text="place")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(change_key=call)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Дом", callback_data="Дом"), InlineKeyboardMarkup(text="Тренажёрный зал", callback_data="Тренажерный Зал"))
    keyboard.add(InlineKeyboardMarkup(text="Спортивная площадка на улице", callback_data="Спортивная площадка на улице"))
    await call.message.answer("Выберите цель тренировки" , reply_markup=keyboard)


@dp.callback_query_handler(text="Дом")
@dp.callback_query_handler(text="Тренажерный Зал")
@dp.callback_query_handler(text="Спортивная площадка на улице")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    change_key = await state.get_data()
    change_key = change_key["change_key"]
    Users_characteristics.change_characteristics(str(call.from_user.id), change_key.data, call.data)
    await call.message.delete()
    await characteristic(change_key)


@dp.callback_query_handler(text="task")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(change_key=call)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardMarkup(text="Набрать силу", callback_data="Набрать силу"), InlineKeyboardMarkup(text="Сбросить вес", callback_data="Сбросить вес"))
    keyboard.add(InlineKeyboardMarkup(text="Поддерживать форму", callback_data="Поддерживать форму"))
    await call.message.answer("Выберите цель тренировки" , reply_markup=keyboard)


@dp.callback_query_handler(text="Набрать силу")
@dp.callback_query_handler(text="Сбросить вес")
@dp.callback_query_handler(text="Поддерживать форму")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    change_key = await state.get_data()
    change_key = change_key["change_key"]
    Users_characteristics.change_characteristics(str(call.from_user.id), change_key.data, call.data)
    await call.message.delete()
    await characteristic(change_key)


@dp.callback_query_handler(text="gender")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(change_key=call)
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardMarkup(text="Мужской", callback_data="Мужской"), InlineKeyboardMarkup(text="Женский", callback_data="Женский"))
    await call.message.answer("Выберите пол" , reply_markup=keyboard)


@dp.callback_query_handler(text="Мужской")
@dp.callback_query_handler(text="Женский")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    change_key = await state.get_data()
    change_key = change_key["change_key"]
    Users_characteristics.change_characteristics(str(call.from_user.id), change_key.data, call.data)
    await call.message.delete()
    await characteristic(change_key)


@dp.callback_query_handler(text="name")
@dp.callback_query_handler(text="age")
@dp.callback_query_handler(text="height")
@dp.callback_query_handler(text="weight")
@dp.callback_query_handler(text="level")
async def change_key(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(change_key=call)
    await Form.value.set()
    await call.message.answer("Введите значение")

@dp.message_handler(state=Form.value)
async def change_value(message: types.Message, state: FSMContext):
    change_key = await state.get_data()
    change_key = change_key["change_key"]
    await state.finish()
    if change_key.data == "name":
        if len(message.text) > 32:
            await message.answer("Имя не может быть больше 32 символов! \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
    elif change_key.data == "age":
        if not message.text.lstrip("+-").isdigit():
            await message.answer("Я не знаю такой метод счисления, это арабский? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
        elif int(message.text) < 0:
            await message.answer("Вы ещё не родились? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
        elif int(message.text) > 100:
            await message.answer("В таком возрасте принято уходить на покой. \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
    elif change_key.data == "height":
        if not message.text.lstrip("+-").isdigit():
            await message.answer("Я не знаю такой метод счисления, это арабский? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
        elif int(message.text) < 0:
            await message.answer("Как это понимать? Вы вростаете в землю? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
        elif int(message.text) > 272:
            await message.answer("Вы побили рекорд Гиннесса! Или нет? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
    elif change_key.data == "weight":
        if not message.text.lstrip("+-").isdigit():
            await message.answer("Я не знаю такой метод счисления, это арабский? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
        elif int(message.text) < 0:
            await message.answer("Вы чёрная дыра? \nВведите корректную информацию!")
            message_id = message.message_id+1
            await asyncio.sleep(2)
            await bot.delete_message(message.chat.id, message_id)
            await characteristic(change_key)
            raise asyncio.CancelledError
        elif int(message.text) > 150:
            if int(message.text) > 610:
                await message.answer("Вы побили рекорд Гиннесса! Или нет? \nВведите корректную информацию!")
                message_id = message.message_id+1
                await asyncio.sleep(2)
                await bot.delete_message(message.chat.id, message_id)
                await characteristic(change_key)
                raise asyncio.CancelledError
            else:
                await message.answer("Мы рекомендуем вам сбросить вес! \nЦель измененна на 'Сбросить вес'")
                Users_characteristics.change_characteristics(str(message.from_user.id), "task", "Сбросить вес")
                message_id = message.message_id+1
                await asyncio.sleep(2)
                await bot.delete_message(message.chat.id, message_id)
                raise asyncio.CancelledError
    Users_characteristics.change_characteristics(str(message.from_user.id), change_key.data, message.text)
    await bot.delete_message(message.chat.id, message.message_id-1)
    await bot.delete_message(message.chat.id, message.message_id)
    await characteristic(change_key)
    


@dp.message_handler()
@dp.message_handler(content_types=ContentType.ANY)
async def echo(message: types.Message):
    await message.reply("Давайте сделаем вид что этого никогда не было...")
    await asyncio.sleep(1)
    await bot.delete_message(message.chat.id, message.message_id+1)
    await bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)