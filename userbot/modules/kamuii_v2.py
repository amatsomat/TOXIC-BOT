# Ported By VICKY @VckyouuBitch
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
# Kalo Mau Ambil Jangan Hapus Credit Ya :)

import os
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY, CMD_HELP


@bot.on(geezbot_cmd(outgoing=True, pattern="kamuii(?: |$)(.*)"))
async def _(fry):
    await fry.edit("`Prosess, Mengaktifkan jurus tumor bolong...😜`")
    level = fry.pattern_match.group(2)
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await fry.edit("`Mohon Balas Di Sticker`")
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await fry.edit("`Gambar tidak di dukung`")
        return
    if reply_message.sender.bot:
        await fry.edit("`Mohon Balas Di Sticker`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    async with fry.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fry.reply("`Mohon Unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Forward"):
            await fry.edit("`Mohon Matikan Setelan Forward Privasi...`")
        else:
            downloaded_file_name = await fry.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await fry.client.send_file(
                fry.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await fry.client.delete_messages(conv.chat_id,
                                                 [msg.id, response.id])
            else:
                await fry.client.delete_messages(
                    conv.chat_id,
                    [msg.id, response.id, r.id, msg_level.id])
    await fry.delete()
    return os.remove(downloaded_file_name)
