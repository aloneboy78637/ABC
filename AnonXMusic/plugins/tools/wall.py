from pyrogram import Client, filters
import requests
from pyrogram.types import Message
from io import BytesIO
from AnonXMusic import app


def get_random_picture():
    response = requests.get('https://source.unsplash.com/random')
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        return None  

@app.on_message(filters.command("rp"))
def pic(client, message):
    random_pic = get_random_picture()
    if random_pic:
        message.reply_photo(random_pic)
    else:
        message.reply("✦ sᴛᴏʀʏ, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ɢᴇᴛ ᴀ ʀᴀɴᴅᴏᴍ ᴘɪᴄᴛᴜʀᴇ ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ.")

@app.on_message(filters.command("pic"))
def pic_command(client, message: Message):
    # Extract the name from the command
    try:
        name = message.command[1]
    except IndexError:
        client.send_message(message.chat.id, "⬤ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ ➥ /pic command.")
        return

   
    unsplash_url = f"https://source.unsplash.com/500x500/?{name}"

    try:
        response = requests.get(unsplash_url)
        if response.status_code == 200:
            client.send_photo(message.chat.id, photo=unsplash_url, caption=f"❖ ʜᴇʀᴇ's ᴀ ᴘɪᴄᴛᴜʀᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ➥ {name}." )
        else:
            client.send_message(message.chat.id, "⬤ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ɪᴍᴀɢᴇ.")
    except requests.RequestException as e:
        client.send_message(message.chat.id, f"⬤ ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ➥ {str(e)}")        
