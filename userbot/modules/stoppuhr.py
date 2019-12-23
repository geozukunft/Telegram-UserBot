import asyncio
from datetime import datetime as dt
import telethon
import re

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
    
    async for i in range(0,8600):
    #async for i in infinity():
        
        t_form = "%H:%M:%S"


        time = "["+ str(dt.now().strftime(t_form)) +"]"
        #print(time)
        
        #print(event.text)
        #print(re.match(r"(\[.*?\])",event.text))
        neuertext = re.sub(r"\[.*?\]", time, event.text, 0)
        #print(neuertext)
        try:
            await event.edit(neuertext)
            await asyncio.sleep(random.randint(10, 50))
        except telethon.errors.rpcerrorlist.MessageNotModifiedError:
            pass

        except:
            break
    
    endetext = re.sub(r"\[.*?\]", "[zeit leider abgelaufen :(]", event.text, 0)
    await event.edit(endetext)
        #dt.now().strftime(t_form)


