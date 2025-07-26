import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import random
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message:Message):
    list = ['https://yandex-images.clstorage.net/96Uyv3j86/b63a54gIYK2/C3gDZho-5xkbvyZv6OybDp6ohhsvTtrsQsuB9SL6JAH_niWOtLHBaBdfOnUfXk_lkkenU9So8a1D6aMvJeeDch48EHfI-PIMynkzbegt24nJ-EJcOc_NqtJcljH0eSfA69CrBmisTvaPVSdr1Y2aptIHd1RRbWsj06vn97W_xHsCsU2n22yhXllooa5pLJsJjijKFLxHDmbFWF_0Yzw-1bEepA_kJwd3QZOopVZF02lQSz2Pk6zq4IKlrnB5swh4Cv-NZ5ogKBvaIGMiJqYeTYxqCV62B8Hoj5CYt6szvFV1GqxDZqkLNYacaitYS1vv3oI9itDsLqiDYu77uD8JN8G_we9UZmXRG60joyAlH8QHbQUb-QHPbwmVXrPif_AaPlMtjCCpQ_EHFiKilMVfJZFCcM3eamghAurmu324Sj6IPErqEO5oXJRt6utuYZnBRGgLHTRGB6hJ2tY4aXDz2TKW7Y9mZEV7x9wna9qK3uzeTX_F2eRp6Uii6Dg6NEfxAPuPIF-hLphb7mLrI-8eAsBoBhI6jcCqz9LfN-F49JL1H-aDIaSKuYXd4uoURxAm0UuxjpTkIqhFpyA-N_rLvs88iizfradaUmrsbWjmWYTAb0FV_QGNb8eZWH6vN_tdehuuxWalR3dAFSRr3kgX4ZvMew9Rai6iTmoj-P-0CP4Ff4EslGkmGN8m6GnqIJ8NzmDFHL5GDCzPWJX4brI-mPoRaoVh6Ad4CNbnL5QKl2gahLHNG26sIQ_qIXCyvkbxS35JZJit7B4RbC1lJ2caisSgxdf0BUTszdDev6F5fFTzn6LEYulEdcLSK6cSAh6s00e8xNSg5ylJIOY08rPAvsgzDuBa76zT3q7pIadk0YtLI8yYN4-HKEaSnLOrsDwaOpnpwmohgDhJm6VqH41coZdEdYzQZOXpSCXne7p7CTNP_YNskilvm15lIuNvI9IKwSmMV_COxC-DXZjwbo',
            'https://avatars.mds.yandex.net/i?id=3074a425cf41a9d08b667f11ec637593-5433422-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=1d578c6bae85f9b4167292efeaf57f7cb097fad7-5263409-images-thumbs&n=13']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message:Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message:Message):
    await message.answer('Искусственный интеллект (ИИ) — это комплекс технологических решений, который позволяет '
                         'машинам имитировать человеческое мышление, учиться на данных и принимать решения.')

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Приветики! Я бот!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
