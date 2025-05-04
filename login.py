from telethon.sync import TelegramClient

api_id = 28321284
api_hash = '3eb69a2b41876a0872179667ebfb96ef'

client = TelegramClient('forward_session', api_id, api_hash)
client.start()  # This will prompt for your phone number and code
print("Login successful. Session file created.")
