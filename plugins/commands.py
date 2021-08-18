#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config

START_IMG="https://telegra.ph/file/2a35fca576aa49de77c98.jpg"
ABS="Developer"
APPER="shamilhabeeb"
OWNER="Owner"
GITCLONE="github.com/shamilhabeebnelli/song-bot"
B2="telegram.dog/shamilnelli"
BUTTON1="📜 Source Code 📜"

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=START_IMG, caption="Hi ⁪⁬⁮ {},\nIam A Simple Mp3 Downloader Bot,\n\nSend me Any Songs name, I can help you with uploading that to TG".format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(BUTTON1, url=GITCLONE)
                 ],[
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/shamilhabeeb"),
                    InlineKeyboardButton(ABS, url=B2)
            ]
          ]
        ),
        reply_to_message_id=message.message_id
    )
