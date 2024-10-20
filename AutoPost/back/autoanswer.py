from telethon import TelegramClient, events


# API данные для подключения к аккаунту
api_id = 25649641
api_hash = "d251d50d7a38842fa4efca07e8ae100d"

client = TelegramClient('andrey', api_id, api_hash, system_version='4.10.2')
client.start()


@client.on(events.NewMessage(chats=[1616500560, 1451579619], blacklist_chats=True))
async def resend_message(event):
    user = await event.get_input_sender()
    try:
        await client.send_message(user, "Это бот для рассылки.\nДля связи с Евгением перейдите по ссылке: \nhttps://t.me/Eoblonski")
    except:



client.run_until_disconnected()