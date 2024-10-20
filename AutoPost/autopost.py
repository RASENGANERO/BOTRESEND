from telethon import TelegramClient
from telethon.tl.types import PeerChannel

import os
import json

import pytz
from time import sleep
from datetime import datetime, time, timedelta


# API данные для подключения к аккаунту
api_id = 24040704
api_hash = "1105a5c42822e6a798b7e6a1e4a7bd2e"

# Время отправки сообщений
first_send_media = "09:00"
text_post = "12:00"
second_send_media = "21:00"

# Чат отправки
forum = PeerChannel(channel_id=-1001616500560)
forum2 = PeerChannel(channel_id=-1001451579619)
channel_id = PeerChannel(channel_id=-1001886667160)


# Ветки отправки
rep = 33349
rep2 = 51159


# Функция для вычисления
def is_work_time(start_time: str, end_time: str):
    now = pytz.timezone('Europe/Moscow').localize(datetime.now()).time()
    start = time.fromisoformat(start_time)
    end = time.fromisoformat(end_time)
    return any([now <= end, now >= start]) if not start < end else (start <= now <= end)


# Функция для вычисления времени для сна бота (сколько бот будет ждать рассылки)
def waiting_to_wake_up(start_time, end_time):
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    hours = datetime.strptime("00:00", "%H:%M")
    result = datetime.strftime(hours - (start - end), '%H:%M')
    asd = timedelta(hours=int(result[0] + result[1]), minutes=int(result[3] + result[4]))
    return round(asd.total_seconds())


# Подключение к аккаунту
with TelegramClient('evgeniy', api_id, api_hash, system_version='4.10.2') as client:
    async def send_media():
        # Получаем список файлов
        files = os.listdir("./media")
        try:
            photos = os.listdir(
                f"./media/{files[0]}")  # Используется files[0] для того, чтобы при вызове функции всегда отправлялся 1-ый файл
        except:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, "Закончились фотографии❗️❗️❗️")
            await client.send_message(admin2, "Закончились фотографии❗️❗️❗️")
            print(f"Закончились фотографии!!!")
            return


        # Создание пустого списка для заполнения его путями отправляемых фотографий
        media = []

        try:
            # Перебор фотографий в папке
            for i in photos:
                media.append(f"./media/{files[0]}/{i}")
        except Exception as e:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, f"⚠️ Ошибка перебора фото")
            sleep(5)
            await client.send_message(admin2, f"⚠️ Ошибка перебора фото\n{e}")
            print(f"Ошибка открытия фото: {e}")
            return

        # Отправка фотографий
        try:
            await client.send_file(forum, media, reply_to=rep)
            sleep(5)
            await client.send_file(forum2, media, reply_to=rep2)
            sleep(5)
            await client.send_file(channel_id, media)
        except Exception as e:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, f"⚠️ Ошибка отправки фото")
            sleep(5)
            await client.send_message(admin2, f"⚠️ Ошибка отправки фото\n{e}")

            print(f"Ошибка отправки фотографий: {e}")

        try:
            # Удаление отправленных фото для освобождения места
            for i in photos:
                os.remove(f"./media/{files[0]}/{i}")
            os.rmdir(f"./media/{files[0]}")
        except:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, "Закончились фотографии❗️❗️❗️")
            sleep(5)
            await client.send_message(admin2, "Закончились фотографии❗️❗️❗️")
            print(f"Закончились фотографии!!!")
            return


    async def send_text():
        try:
            try:
                # Передаю в переменную json с текстами сообщений
                with open("text.json", "r", encoding="utf-8") as file:
                    messages = json.load(file)
            except:
                # Передаю в переменную json с текстами сообщений
                with open("text.json") as file:
                    messages = json.load(file)
        except Exception as e:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, "⚠️ Ошибка открытия файла")
            sleep(5)
            await client.send_message(admin2, f"⚠️ Ошибка открытия файла\n{e}")
            print(f"Ошибка открытия файла (возможно закончились или из-за кодировки): {e}")
            return

        try:
            # Отправка поста с текстом
            await client.send_message(forum, messages["message"][0]["text"], reply_to=rep)
            sleep(5)
            await client.send_message(forum2, messages["message"][0]["text"], reply_to=rep2)
            sleep(5)
            await client.send_message(channel_id, messages["message"][0]["text"])
        except Exception as e:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, f"⚠️ Ошибка отправки текстового поста")
            sleep(5)
            await client.send_message(admin2, f"⚠️ Ошибка отправки текстового поста\n{e}")
            print("Закончились текстовые посты!")
            return

        try:
            # Удаление из json-a отправленного текста
            del messages["message"][0]
        except:
            admin = await client.get_entity("https://t.me/Eoblonski")
            admin2 = await client.get_entity("https://t.me/AOKochkin")
            await client.send_message(admin, "Закончились текстовые посты❗️❗️❗️")
            await client.send_message(admin2, "Закончились текстовые посты❗️❗️❗️")
            print("Закончились текстовые посты!")
            return

        # Запись json-a обратно в файл
        with open("text.json", "w") as file:
            json.dump(messages, file, ensure_ascii=False, indent=2)


    # Бесконечный цикл отправки сообщений через время
    while True:
        time_now = pytz.timezone('Europe/Moscow').localize(datetime.now()).strftime('%H:%M')
        sleep(waiting_to_wake_up(time_now, second_send_media))
        client.loop.run_until_complete(send_media())

        time_now = pytz.timezone('Europe/Moscow').localize(datetime.now()).strftime('%H:%M')
        sleep(waiting_to_wake_up(time_now, first_send_media))
        client.loop.run_until_complete(send_media())

        time_now = pytz.timezone('Europe/Moscow').localize(datetime.now()).strftime('%H:%M')
        sleep(waiting_to_wake_up(time_now, text_post))
        client.loop.run_until_complete(send_text())