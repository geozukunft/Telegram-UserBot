# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """
from asyncio import sleep

from userbot import (CMD_HELP)
from userbot.events import register

chatlist = []


@register(incoming=True)
async def fischer(handler):
    global chatlist
    if handler.chat_id in chatlist:
        if handler.message.mentioned:
            await sleep(0.5)
            await handler.reply("/fish")
            await handler.client.send_read_acknowledge(handler.chat_id,clear_mentions=True)
            

@register(outgoing=True, pattern="^\.startfisch")
async def startfischer(handler):
    global chatlist
    chatlist.append(handler.chat_id)
    await handler.edit("sollte getan sein")



@register(outgoing=True, pattern="^\.stopfisch")
async def startfischer(handler):
    global chatlist
    chatlist.remove(handler.chat_id)
    await handler.edit("sollte getan sein")


@register(outgoing=True, pattern="^\.notstopp")
async def startfischer(handler):
    global chatlist
    chatlist.clear()
    await handler.edit("sollte getan sein")



CMD_HELP.update({
    "startfisch":" Startet Fisching",
    "stopfisch":"Stoppt fisching im chat",
    "notstop":"stoppt fisching in allen chats"
})
