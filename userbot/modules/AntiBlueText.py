import asyncio

from telethon.tl import types, functions

from userbot.events import register


@register(outgoing=True)
async def handler(event):
    found = False
    for i, ent in enumerate(event.entities or []):
        if isinstance(ent, types.MessageEntityBotCommand):
            found = True
            event.entities[i] = types.MessageEntityTextUrl(
                ent.offset+1, ent.length, 'tg://need_update_for_some_feature')

    if found:
        await asyncio.sleep(1)  # inter-dc issues lol
        try:
            await event.client(functions.messages.EditMessageRequest(
                await event.get_input_chat(),
                id=event.id,
                no_webpage=not event.web_preview,
                message="."+event.raw_text,
                entities=event.entities
            ))
        except:
            pass


