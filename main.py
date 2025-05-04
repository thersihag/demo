from telethon import TelegramClient, events

# Telegram API credentials
api_id = 28321284
api_hash = '3eb69a2b41876a0872179667ebfb96ef'

# Session name
client = TelegramClient('forward_session', api_id, api_hash)

# Source and destination
source_chat = -1388551614           # Source: sender ID (a Telegram group/channel ID)
target_chat = '@hisardemobot'       # Destination: receiver username or chat ID

@client.on(events.NewMessage(chats=source_chat))
async def forward_handler(event):
    await client.send_message(target_chat, event.message)

print("Listening for new messages...")
client.start()
client.run_until_disconnected()
