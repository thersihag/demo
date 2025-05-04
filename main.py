from telethon import TelegramClient, events

# Session name and Telegram API credentials
api_id = 28321284
api_hash = '3eb69a2b41876a0872179667ebfb96ef'
session_name = 'forward_session'  # This must exist already

# Initialize client with existing session file
client = TelegramClient(session_name, api_id, api_hash)

# Source and target chats
source_chat = -1388551614              # Source: your group/channel ID
target_chat = '@hisardemobot'          # Target: bot or user/channel

@client.on(events.NewMessage(chats=source_chat))
async def forward_handler(event):
    await client.send_message(target_chat, event.message)

print("✅ Auto-forwarder is running. Waiting for new messages...")
client.start()  # Will not ask for input — uses session
client.run_until_disconnected()
