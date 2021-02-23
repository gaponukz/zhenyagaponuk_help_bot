from aiogram.utils.executor import start_webhook
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

import asyncio, os
import aioschedule
import json
import logging

TOKEN = "1549669090:AAEtDBdzYf_le6Dvx_DRNiO2qtBOIeG9lAM"

WEBHOOK_HOST = 'https://zhenyagaponukhelpbot.herokuapp.com'
WEBHOOK_PATH = '/webhook/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.environ.get('PORT')

bot = Bot(token = '1632180424:AAHiioPQ0uCxSi-p4sQ5MoHtiEc0Gsiw3Dk')
bot_name = 'Zhenyagaponuk Bot'
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda callback: callback.data.startswith('market_parser'))
async def process_callback_button(callback_query: types.CallbackQuery):
    if 'olx' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id, 
            'https://static.olx.ua/static/olxua/naspersclassifieds-regional/olxeu-atlas-web-olxua/static/img/fb/fb-image_redesign.png?t=21-02-22', 
            caption =  "Olx parser (пример): http://shorturl.at/vxRX1\nЦена: 1800 гривен"
        )
    elif 'kufar' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id, 
            'https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco/b37788ff002955911102',
            caption =  "Kufar parser"
        )
    elif 'blocket' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://s3-eu-west-1.amazonaws.com/tpd/logos/46d2b2130000640005009a07/0x0.png',
            caption =  "Blocket parser (пример): http://shorturl.at/swAIV\nЦена: 2000 гривен"
        )
    elif 'allegrolokalnie' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id, 
            'https://img.wprost.pl/img/logo-allegro/fb/bf/7fb5e1198334dbb5b799a05b0f44.jpeg',
            caption =  "Allegrolokalnie parser (пример): http://shorturl.at/tvHV0\nЦена: 1700 гривен"
        )
    else:
        market_parser_buttons = types.InlineKeyboardMarkup()\
            .add(types.InlineKeyboardButton('Парсер olx.ua(pl, kz...)', callback_data = "market_parser olx"))\
            .add(types.InlineKeyboardButton('Парсер kufar.by', callback_data = "market_parser kufar"))\
            .add(types.InlineKeyboardButton('Парсер blocket.se', callback_data = "market_parser blocket"))\
            .add(types.InlineKeyboardButton('Парсер allegrolokalnie.pl', callback_data = "market_parser allegrolokalnie"))

        await bot.send_message(
            callback_query.from_user.id,
            "Нажмите для детальной информации о парсере.",
            reply_markup = market_parser_buttons
        )

@dp.callback_query_handler(lambda callback: callback.data.startswith('parsers'))
async def process_callback_button(callback_query: types.CallbackQuery):
    if 'instagram' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png',
            caption =  "Парсер всех данных с Instagram которые можно достать: публикаций по тегам/локациям, аудитории блогеров а также их анализ.\nПример сбора локаций: https://gaponukz.github.io/art_map/"
        )
    elif 'facebook' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://1000logos.net/wp-content/uploads/2016/11/Facebook-logo.png',
            caption =  "Парсер постов с пабликов Facebook\nПрмер: http://shorturl.at/jwQWZ\nЦена 1500 гривен."
        )
    elif 'youtube' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/YouTube_Logo.svg/1200px-YouTube_Logo.svg.png',
            caption =  "Парсер YouTube по ключевым словам.\nЦена 1600 гривен."
        )
    elif 'telegram' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png',
            caption =  "Парсер сообщений Telegram. Цена: 1500 гривен.\nПарсер каналов/чатов по ключам. Цена: 1800 гривен."
        )
    elif 'mywed' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://mywed.com/images/mywed-logo/vertical-black.png',
            caption =  "Пример: https://shorturl.at/koxVY\nЦена: 1600 гривен."
        )
    elif 'gov' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://www.cvk.gov.ua/wp-content/themes/cvk/assets/images/gerb_cvk.gif',
            caption =  "Пример: http://shorturl.at/wCT58\nЦена: 1800 гривен."
        )
    else:
        parsers_buttons = types.InlineKeyboardMarkup()\
            .add(types.InlineKeyboardButton('Парсер Instagram', callback_data = "parsers instagram"))\
            .add(types.InlineKeyboardButton('Парсер Facebook', callback_data = "parsers facebook"))\
            .add(types.InlineKeyboardButton('Парсер YouTube', callback_data = "parsers youtube"))\
            .add(types.InlineKeyboardButton('Парсер Telegram', callback_data = "parsers telegram"))\
            .add(types.InlineKeyboardButton('Парсер mywed.com', callback_data = "parsers mywed"))\
            .add(types.InlineKeyboardButton('Парсер cvk.gov.ua', callback_data = "parsers gov"))

        await bot.send_message(
            callback_query.from_user.id,
            "Нажмите для детальной информации о парсере.",
            reply_markup = parsers_buttons
        )

@dp.callback_query_handler(lambda callback: callback.data.startswith('telegram_soft'))
async def process_callback_button(callback_query: types.CallbackQuery):
    if 'inviter' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telegram_X_2019_Logo.svg/600px-Telegram_X_2019_Logo.svg.png',
            caption = "Программа которая из указаных чатов парсит только активную аудиторию(недавно с сити и что-то писали в чат) и медленно добавляет её у ваш канал/чат.\nЦена: 1600 гривен."
        )
    elif 'mailing' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telegram_X_2019_Logo.svg/600px-Telegram_X_2019_Logo.svg.png',
            caption = "Программа которая из указаных чатов парсит только активную аудиторию(недавно с сити и что-то писали в чат) и медленно  рассылает ваше сообщение им.\nЦена: 1600 гривен."
        )
    elif 'resend' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telegram_X_2019_Logo.svg/600px-Telegram_X_2019_Logo.svg.png',
            caption = "Программа которая парсит все новые посты с указанных вами источников у ваш канал. Имеется много настроек: указывать ли источник, удалять ссылки или @usernames в тексте, приватные или публичные источники...\nЦена: от 1800 гривен."
        )
    elif 'search' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telegram_X_2019_Logo.svg/600px-Telegram_X_2019_Logo.svg.png',
            caption = "Парсер выдачи результатов Telegram search. По ключам с вашего аккаунта ищет чаты/каналы и результат сохраняет в Excel.\nПример: http://shorturl.at/pAG12\nЦена: 1500 гривен."
        )
    elif 'delete' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telegram_X_2019_Logo.svg/600px-Telegram_X_2019_Logo.svg.png',
            caption = "Программа позволит удалить сообщения с диапазоном дат с чатов Telegram.\nВсе сообщения логируются и сохраняются.\nЦена: 1400 гривен."
        )
    elif 'aud_parser' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telegram_X_2019_Logo.svg/600px-Telegram_X_2019_Logo.svg.png',
            caption = "Программа предоставит Excel файл с аккаунтами аудитории чата которого вы укажете."
        )
    else:
        telegram_soft_buttons = types.InlineKeyboardMarkup()\
            .add(types.InlineKeyboardButton('Инвайтер', callback_data = "telegram_soft inviter"))\
            .add(types.InlineKeyboardButton('Рассылка', callback_data = "telegram_soft mailing"))\
            .add(types.InlineKeyboardButton('Граббер постов с каналов', callback_data = "telegram_soft resend"))\
            .add(types.InlineKeyboardButton('Парсер поиска выдачи(чатов/каналов)', callback_data = "telegram_soft search"))\
            .add(types.InlineKeyboardButton('Удаление сообщений', callback_data = "telegram_soft delete"))\
            .add(types.InlineKeyboardButton('Парсер аудитории чатов', callback_data = "telegram_soft aud_parser"))
        
        await bot.send_message(
            callback_query.from_user.id,
            "Нажмите для детальной информации о софте.",
            reply_markup=telegram_soft_buttons
        )

@dp.callback_query_handler(lambda callback: callback.data.startswith('telegram_bots'))
async def process_callback_button(callback_query: types.CallbackQuery):
    if 'me' in callback_query.data:
        await bot.send_message(
            callback_query.from_user.id,
            'It is me!'
        )
    elif 'instagram' in callback_query.data:
        await bot.send_photo(
            callback_query.from_user.id,
            'https://content.freelancehunt.com/snippet/99287/91b2d/1209821/1EE19CEF-6AEC-4315-BA43-11BA7E7E89E8.png',
            caption =  "Бот, который выдаст топ 10 постов за лайками/комментариями из кнопкой Show more для следующих постов.\nЦена: 3000 гривен."
        )
    else:
        telegram_bots_buttons = types.InlineKeyboardMarkup()\
            .add(types.InlineKeyboardButton('Zhenyagaponuk Bot', callback_data = "telegram_bots me"))\
            .add(types.InlineKeyboardButton('Instagram Sorting Bot', callback_data = "telegram_bots instagram"))
        
        await bot.send_message(
            callback_query.from_user.id,
            "Нажмите для детальной информации о боте.",
            reply_markup=telegram_bots_buttons
        )

@dp.message_handler(commands = ['start'])
async def start_bot(message: types.Message):
    hello_buttons = types.InlineKeyboardMarkup()\
        .add(types.InlineKeyboardButton('Парсеры маркетплейсов', callback_data = "market_parser"))\
        .add(types.InlineKeyboardButton('Другие парсеры', callback_data = "parsers"))\
        .add(types.InlineKeyboardButton('Софт для Telegram', callback_data = "telegram_soft"))\
        .add(types.InlineKeyboardButton('Боты для Telegram', callback_data = "telegram_bots"))\

    await bot.send_message(
        message.from_user.id,
        f'Вас приветствует {bot_name}!\nВы наверно хотели заказать что-то в Жени или хотите узнать чем может вам он помочь?\nМой автор уже писал:', 
        reply_markup = hello_buttons
    )

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # asyncio.create_task(sheduler())

async def on_shutdown(dp):
    pass

if __name__ == '__main__':
    start_webhook(
        dispatcher = dp,
        webhook_path = WEBHOOK_PATH,
        on_startup = on_startup,
        on_shutdown = on_shutdown,
        host = WEBAPP_HOST,
        port = WEBAPP_PORT
    )
