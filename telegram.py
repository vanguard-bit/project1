from telethon.sync import TelegramClient, events
import extract_ip as extract_ip

api_id = ""
api_hash = ""

Severity = 0

with TelegramClient('ses', api_id, api_hash) as client:

    @client.on(events.NewMessage(pattern='(?i).*hi'))
    async def handler(event):
        global Severity
        if Severity % 10 == 0:
            await event.reply("1")
            extract_ip.extract(Severity)
        Severity += 1

    client.run_until_disconnected()
