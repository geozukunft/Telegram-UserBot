import asyncio

from userbot import CMD_HELP
from userbot.events import register


from telethon import events
from telethon.tl import types, functions

@register(outgoing=True)
async def handler(event):
    found = False
    for i, ent in enumerate(event.entities or []):
        if isinstance(ent, types.MessageEntityBotCommand):
            found = True
            event.entities[i] = types.MessageEntityTextUrl(
                ent.offset, ent.length, 'tg://need_update_for_some_feature')

    if found:
        await asyncio.sleep(1)  # inter-dc issues lol
        await event.edit(
            await event.get_input_chat(),
            id=event.id,
            no_webpage=not event.web_preview,
            message=event.raw_text,
            entities=event.entities
        )
