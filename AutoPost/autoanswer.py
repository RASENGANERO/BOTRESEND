from telethon import TelegramClient, events


# API данные для подключения к аккаунту
api_id = 24040704
api_hash = "1105a5c42822e6a798b7e6a1e4a7bd2e"

client = TelegramClient('autoanswer', api_id, api_hash, system_version='4.10.2')
client.start()


@client.on(events.NewMessage(chats=[1616500560, 1451579619], blacklist_chats=True))
async def resend_message(event):
    user = await event.get_input_sender()
    await client.send_message(user, "Это бот для рассылки.\nДля связи с Евгением перейдите по ссылке: \nhttps://t.me/Eoblonski")


client.run_until_disconnected()