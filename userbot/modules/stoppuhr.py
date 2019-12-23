import asyncio
from datetime import datetime as dt

import random

from userbot import CMD_HELP
from userbot.events import register

from telethon import events
from telethon.tl import types, functions

async def infinity():
    while True:
        yield


@register(outgoing=True)
async def handler(event):
    if not '[time]' in event.text:
        return
    
    async for i in infinity():
        
        t_form = "%H:%M:%S"



        neuertext = event.text.replace(r"\[.*\]",f"dt.now().strftime(t_form)")


        await event.edit(neuertext)
        await asyncio.sleep(random.randint(3, 10))

        #dt.now().strftime(t_form)

