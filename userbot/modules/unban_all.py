# Port By @VckyouuBitch From GeezProjects
# Copyright © 2021 Geez-Projects
from telethon.tl.types import (
    ChannelParticipantsKicked,
)

from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez
from userbot import CMD_HELP


@bot.on(geezbot_cmd(outgoing=True, pattern="unban(all)\s?(.)?"))
async def _(event):
    await event.edit("`Sedang Mencari List Banning.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit("`Sukses Menghapus List Banning`")


CMD_HELP.update(
    {
        "unban_all": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{geez}unban all`\
    \n↳ : Membatalkan semua Ban Di Anggota Grup."
    }
)
