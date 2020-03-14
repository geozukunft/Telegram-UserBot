from userbot import (CMD_HELP)
from userbot.events import register
from userbot.utils import helpers


@register(outgoing=True, pattern="^\.i(nvite)?l(ink)?")
async def invitelink(event):
    """Command to get link creator, chatid and the random part of an invite link."""

    _, args = await helpers.get_args(event)
    link = args[0]
    link_creator, chatid, random_part = await helpers.resolve_invite_link(link)
    caption = "<b>INVITELINK INFO:</b> \n"
    caption += f"Creator ID: {link_creator} \n"
    caption += f"Chat ID: {chatid} \n"
    caption += f"Random ID: {random_part} \n"
    
    await event.reply(caption)






















CMD_HELP.update({
    "il ":".il\
   \nUsage:Check invite links BETA"
})
