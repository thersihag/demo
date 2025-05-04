from telethon import TelegramClient, events

# Already authenticated session name (must be uploaded to project)
session_name = 'forward_session'

# Telegram API credentials
api_id = 28321284
api_hash = '3eb69a2b41876a0872179667ebfb96ef'

# Initialize client with existing session
client = TelegramClient(session_name, api_id, api_hash)

# Sender and receiver
source_chat = -1388551614             # Group/channel ID (sender)
target_chat = '@hisardemobot'         # Username or ID (receiver)

@client.on(events.NewMessage(chats=source_chat))
async def forward_handler(event):
    await client.send_message(target_chat, event.message)

print("✅ Forwarder is running. Listening for messages...")
client.start()                        # No input needed
client.run_until_disconnected()
