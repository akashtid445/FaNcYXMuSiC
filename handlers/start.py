# OxyXmusic (Telegram bot project )
# Copyright (C) 2021 RiZoeL

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
     await message.reply_sticker("CAACAgEAAxkBAAEKSWJgwGQMxYa9he0KQnk0DQiRXs8lFAACTgIAAlEpDTkIb4MnCr3Ohx8E")
     await message.reply_text(
        f"""⇝ 𝐻𝑒𝑙𝑙𝑜 {message.from_user.first_name}  𝙄 𝙘𝙖𝙣 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩𝙨 𝙤𝙛 𝙏𝙚𝙡𝙚𝙜𝙚𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨. 𝙄 𝙝𝙖𝙫𝙚 𝙖 𝙡𝙤𝙩 𝙤𝙛 𝙘𝙤𝙤𝙡 𝙛𝙚𝙖𝙩𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙬𝙞𝙡𝙡 𝙖𝙢𝙖𝙯𝙚 𝙮𝙤𝙪 ☆.\n\n⇝ 𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙢𝙚 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙜𝙧𝙤𝙪𝙥𝙨'𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩𝙨? 𝙋𝙡𝙚𝙖𝙨𝙚 𝙘𝙡𝙞𝙘𝙠 𝙩𝙝𝙚 "Ƈօʍʍɑղժs" 𝙗𝙪𝙩𝙩𝙤𝙣 𝙗𝙚𝙡𝙤𝙬 𝙩𝙤 𝙠𝙣𝙤𝙬 𝙝𝙤𝙬 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙪𝙨𝙚 𝙢𝙚.\n\n⇝ 𝙐𝙨𝙚 𝙩𝙝𝙚 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙗𝙚𝙡𝙤𝙬 𝙩𝙤 𝙠𝙣𝙤𝙬 𝙢𝙤𝙧𝙚 𝙖𝙗𝙤𝙪𝙩 𝙢𝙚 💔.\n\n⇝ 𝐎𝐑 𝐄𝐋𝐒𝐄 𝐇𝐀𝐕𝐈𝐍𝐆 𝐏𝐑𝐎𝐁𝐋𝐄𝐌 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 देसी ΝϴᏴᏆͲᎪ""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 cσммαη∂s 📜", url="https://telegra.ph/N%C3%B8b%CE%90-%EA%AA%8E-M%E0%B8%99%E0%BA%AEic-06-06-2")
                  ],[
                    InlineKeyboardButton(
                        "🔥Mץ OwŇeℝ🔥", url="https://t.me/DesiNobita"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❤️ σғғιcιαℓ gяσυρ ❤️", url="https://t.me/cartoons_007"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**➤ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥Mץ OwŇeℝ 🔥", url="https://t.me/DesiNobita")
                ]
            ]
        )
   )
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of Nø͢͢͢bΐ ꪎ M͢͢͢นຮic !
╔━━━━━━━━⊰✦⊱━━━━━━━━╗
/ply  - play audio or link you requested
/play  - play song you requested
/dplay  - play song you requested via deezer
/splay  - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song  - download songs you want quickly
/search  - search videos on youtube with details
/deezer  - download songs you want quickly via deezer
/saavn  - download songs you want quickly via saavn

•Admins only•
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
╚━━━━━━━━⊰✦⊱━━━━━━━━╝
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⊲ Assɪsᴛᴀɴᴛ ⊳", url="https://t.me/NoBiTa_vC_pLaYeR?startgroup=true"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔱 Ｏｗｎｅｒ 🔱", url="https://t.me/DesiNobita"
                    ),
                    InlineKeyboardButton(
                        "✙ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ✙", url="https://t.me/NoBi_vC_PlAyEr_RoBoT?startgroup=true"
                    )
                ]
            ]
        )
    )

    
