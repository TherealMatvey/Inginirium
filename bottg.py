import asyncio
import logging
from logging.config import ConvertingTuple
import sys
from os import getenv

import random
import sqlite3
import cv2
import numpy as np
import matplotlib.pyplot as plt

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters.command import Command, CommandStart
from aiogram.types import FSInputFile, Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, LinkPreviewOptions


connection = sqlite3.connect('bot_database(att0).db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER
)
''')


TOKEN_API = "7692404557:AAFoiQuJ0dtJLOaMpU_bwl2SvXt8GHvAYCI"


user = {'in_dialogue': False}
button_event = {'active': False}
always = {'working': True}

bot = Bot(TOKEN_API)
dp = Dispatcher()


HELP_COMMAND = """
/buttons - Кнопки
/dialogue - Диалог
/cancel - Выйти из диалога


Бота сделал Хазиев Матвей, 15 лет
"""

DIALOGUE_COMMAND = ('<b>Вы начали диалог с ботом.</b>\n'
                    '<u>Чтобы выйти из диалога, напишите команду</u> <u>/cancel</u>\n'
                    'Задайте ему один из этих вопросов:\n\n'
                    '<i>Какая сегодня погода?</i>\n'
                    '<i>Что можно сегодня поесть?</i>\n'
                    '<i>Расскажи анекдот</i>')
                    


list_answer1 = ['Хорошая', 'Сегодня прохладно', 'Сегодня тепло', 'Погода отличная!']
list_answer2 = ['Борщ с хлебом и макароны с сосисками', 'Яйцо, пожаренное на хлебе', 'Банан, яблоко, апельсин', 'Гречневая крупа с гуляшом']
list_answer3 = ["""Если у вас закончилась мазь от зуда,
                    — Не спешите выбрасывать тюбик.
                    Его уголком очень удобно чесаться.""",
                """Почему у тебя такой печальный вид?
                    — Жена собралась на курорт.
                    И ты что за нее беспокоишься?
                    — Нет, но если на моем лице не будет грусти, она ни за что не поедет.""", 
                """В полицию пришла заплаканная женщина:
                    — Найдите моего мужа, он исчез.
                    Когда это произошло?
                    — Неделю назад.
                    Но почему вы только сейчас об этом заявляете?
                    — У него сегодня зарплата.""", 
                """Когда уже электронная почта, будет посылки принимать?"""]

 


@dp.message(Command('help'))
async def help_command(message: types.Message):
    #Ответ
    await message.reply(text = HELP_COMMAND)

@dp.message(CommandStart())
async def start_command(message: types.Message):
    #Ответ
    await message.delete()
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])

    red = (0, 255, 0)
    mat = [[(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
           [(red), (0, 0, 255), (0, 0, 255), (0, 0, 255), (red), (0, 0, 255), (red),       (0, 0, 255), (0, 0, 255), (0, 0, 255), (red),       (0, 0, 255), (red), (red),       (red),       (0, 0, 255), (0, 0, 255), (red), (red), (red)],
           [(red), (red),       (0, 0, 255), (red),       (red), (0, 0, 255), (red),       (0, 0, 255), (0, 0, 255), (0, 0, 255), (red),       (0, 0, 255), (red), (0, 0, 255), (0, 0, 255), (red),       (0, 0, 255), (red), (0, 0, 255), (0, 0, 255)],
           [(red), (0, 0, 255), (red),       (0, 0, 255), (red), (0, 0, 255), (red),       (0, 0, 255), (0, 0, 255), (0, 0, 255), (red),       (0, 0, 255), (red), (red),       (red),       (0, 0, 255), (0, 0, 255), (red), (red), (0, 0, 255)],
           [(red), (0, 0, 255), (0, 0, 255), (0, 0, 255), (red), (0, 0, 255), (red),       (0, 0, 255), (0, 0, 255), (0, 0, 255), (red),       (0, 0, 255), (red), (0, 0, 255), (red),       (0, 0, 255), (0, 0, 255), (red), (0, 0, 255), (0, 0, 255)],
           [(red), (0, 0, 255), (0, 0, 255), (0, 0, 255), (red), (0, 0, 255), (0, 0, 255), (red),       (red),       (red),       (0, 0, 255), (0, 0, 255), (red), (0, 0, 255), (0, 0, 255), (red),       (0, 0, 255), (red), (0, 0, 255), (0, 0, 255)],
           [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],]
    arr = np.array(mat)
    plt.imshow(arr, interpolation='none')
    plt.savefig("name.jpg")
    await message.answer_photo(
    FSInputFile("name.jpg"),
    caption = '🔷<i>Добро пожаловать в наш телеграмм бот!</i>\n\n'
                              '🔸<i><b>Тут есть несколько интересных вещей!</b></i>\n\n'
                              '<span class = "tg-spoiler">Удачи!❤</span>',
                        parse_mode='HTML')
    await message.answer(text = '<u>Напишите команду</u> <u>/help</u>, <u>чтобы узнать больше о командах бота</u>',
                         parse_mode='HTML')
    print(user['in_dialogue'])

    cursor.execute('INSERT INTO Users (username, surname, age) VALUES (?, ?, ?)', (message.from_user.full_name, "a", 0))
    connection.commit()
    await message.answer(message.from_user.full_name)


@dp.message(Command(commands='users'))
async def users_list_command(message: Message):
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    await message.answer(str(users))

@dp.message(Command(commands='dialogue'))
async def dialogue_command(message: Message):
    if user['in_dialogue'] == False:
        await message.answer(text = DIALOGUE_COMMAND, parse_mode='HTML')
        user['in_dialogue'] = True
        print(user['in_dialogue'])
    else:
        await message.answer(text = "Вы уже находитесь в диалоге!")

@dp.message(F.text == 'Какая сегодня погода?')
async def answer_1(message: Message):
        print(user['in_dialogue'])
        if user['in_dialogue'] == True:
            await message.answer(list_answer1[random.randrange(0, 4)])

@dp.message(F.text == 'Что можно сегодня поесть?')
async def answer_1(message: Message):
        print(user['in_dialogue'])
        if user['in_dialogue'] == True:
            await message.answer(list_answer2[random.randrange(0, 4)])

@dp.message(F.text == 'Расскажи анекдот')
async def answer_1(message: Message):
        print(user['in_dialogue'])
        if user['in_dialogue'] == True:
            await message.answer(list_answer3[random.randrange(0, 4)])

@dp.message(Command(commands='cancel'))
async def cancel_command(message: Message):
    if user['in_dialogue'] == True:
        user['in_dialogue'] = False
        await message.answer(text = "Вы вышли из диалога.")
        print(user['in_dialogue'])
    else:
        await message.answer(text = "Вы не находитесь в диалоге.")
        
@dp.message()
async def no_answer(message: Message):
    if user['in_dialogue'] == True:
        await message.answer(text = """Вы находитесь в диалоге!
Напишите команду /cancel чтобы выйти 
или задайте один из вопросов.""")
    else:
        pass


@dp.message(Command(commands = 'game'))
async def cmd_random(message: types.Message):
   b1 = InlineKeyboardButton(
        text='Больше',
        callback_data='Bigger')

   b2 = InlineKeyboardButton(
        text='Меньше',
        callback_data='Smaller')
    
   keyboard2 = InlineKeyboardMarkup(
        inline_keyboard=[[b1, b2]])
   if always['working'] == True:
        await message.answer(
            f'Ваше число больше {78}?',
            reply_markup=keyboard2
        )
        await message.delete()

#@dp.message(Command(commands = 'button'))
#async def button_command(message: types.Message):
#    button_event['active'] = True
#    kb = [
#        [
#            types.KeyboardButton(text = "Кнопка1"),
#            types.KeyboardButton(text = "Кнопка2")
#        ],
#        [types.KeyboardButton(text = "Кнопка3")]
#    ]
#    keyboard = types.ReplyKeyboardMarkup(keyboard = kb, resize_keyboard = True, input_field_placeholder = "Я могу менять текст даже тут!")
    #Ответ
#    await message.delete()
#    await message.answer("Какую кнопку выберешь?", reply_markup = keyboard)

#@dp.message(F.text == "Кнопка1")
#async def number_one(message: types.Message):
#    if button_event['active'] == True:
#        await message.answer("Она ничего не делает...")
#        await message.delete()

#@dp.message(F.text == "Кнопка2")
#async def number_two(message: types.Message):
#    if button_event['active'] == True:
#        await message.answer("Всё получилось!")
#        await message.delete()

#@dp.message(F.text == "Кнопка3")
#async def number_three(message: types.Message):
#    if button_event['active'] == True:
#        await message.answer("Эта кнопка шире других!")
#        await message.delete()

#@dp.message()
#async def no_number(message: types.Message):
#    if button_event['active'] == True:
#        button_event['active'] = False

#--------------------------------------------------------------------

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


#@dp.message(Command(commands='link'))
#async def link_command(message: Message):
#    link1 = LinkPreviewOptions(
#        url = "Youtube.com",
#        prefer_small_media = True,
#        show_above_text = True)
#    await message.answer("jj", link_preview_options=link1)


#@dp.message(Command(commands = 'showimage'))
#async def balance_command(message: types.Message):
    #Ответ
    # Отправка файла из файловой системы
#    image_from_pc = FSInputFile(r"C:\Users\DELL\Documents\Discord.png")
#    result = await message.answer_photo(
#        image_from_pc,
#        caption = "Легендарное изображение"
#    )
    #await message.reply(str(b))

#@dp.message(F.new_chat_members)
#async def somebody_added(message: Message):
#    for user in message.new_chat_members:
#        await message.reply(f"Привет, {user.full_name}")

#@dp.message(F.photo)
#async def download_photo(message: types.Message, bot: Bot):
#    await bot.download(
#        message.photo[-1],
#        destination=f"{message.photo[-1].file_id}.jpg"
#    )
#    src = cv2.imread(f"{message.photo[-1].file_id}.jpg")
#    image = cv2.resize(src, None, fx = 0.8, fy = 0.8, interpolation=cv2.INTER_CUBIC)
#    dst = cv2.blur(image, (1, 15))
#    cv2.imwrite(f"{message.photo[-1].file_id}.jpg", dst)
#
#    await message.answer_photo(
#        FSInputFile(f"{message.photo[-1].file_id}.jpg"),
#        caption = "Изображение изи файла на компьютере")
   
#@dp.message(Command(commands='fonts'))
#async def fonts_command(message: Message):
    #Ответ
#    if always['working'] == True:
#        await message.answer(
#            text = 'Сейчас я вам покажу разные виды текста:\n\n'
#                '<b>Жирный</b>\n'
#                '<i>Наклонный</i>\n'
#                '<u>Подчёркнутый</u>\n'
#                '<span class = "tg-spoiler">Спойлер</span>\n\n'
#                'Чтобы посмотреть доступные команды - введи команду /help',
#            parse_mode='HTML')
