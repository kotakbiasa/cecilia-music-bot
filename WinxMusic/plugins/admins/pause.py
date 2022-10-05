#
# Copyright (C) 2021-2022 by mrootx@Github, < https://github.com/gabrielmaialva33 >.
#
# This file is part of < https://github.com/gabrielmaialva33/WinxMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/gabrielmaialva33/WinxMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from WinxMusic import app
from WinxMusic.core.call import Winx
from WinxMusic.utils.database import is_music_playing, music_off
from WinxMusic.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Winx.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )
