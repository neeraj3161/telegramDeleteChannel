from telethon import TelegramClient
from telethon.tl.functions.messages import DeleteHistoryRequest

# Replace with your credentials
api_id =  0 # Your API ID (integer)
api_hash = ''  # Your API Hash

client = TelegramClient('session_name', api_id, api_hash)

async def delete_all_chats():
    await client.start()

    async for dialog in client.iter_dialogs():
        if not dialog.is_channel:  # Ensures it deletes chats (not channels)
            print(f"Deleting chat: {dialog.name} (ID: {dialog.id})")
            await client(DeleteHistoryRequest(peer=dialog.id,max_id=0, just_clear=False, revoke=True))

    print("✅ Successfully deleted all chats!")

with client:
    client.loop.run_until_complete(delete_all_chats())
