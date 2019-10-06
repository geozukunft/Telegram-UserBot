from userbot import CMD_HELP
from userbot.events import register
from bwb import bwb

import asyncio

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

import os
from dotenv import load_dotenv

load_dotenv("config.env")

TELEGRAM_ID_STRING = os.environ.get("TELEGRAM_ID", None)
TELEGRAM_ID = int(TELEGRAM_ID_STRING)

bwb = bwb.bwb(TELEGRAM_ID)


wrap_users = {
    't': 79316791,   # Tanner
    'j': 172033414,  # Jason
    'o': 358491576,  # Jonas
    'm': 964048273,  # Mini Eule
    'g': 234480941,  # Twit
    'v': 181585055,  # Viktor
}



@register(NewMessage(outgoing=True, pattern='!!+init'))
async def init(event):
    await event.respond('000000init ' + bwb.init())


@register(NewMessage(outgoing=True, pattern=r'!!+(e(?:enc)?)?w(?:rap)? (\S+) ([\s\S]+)'))
async def wrap(event):
    enc = event.pattern_match.group(1) is not None
    message = event.pattern_match.group(3)

    u = event.pattern_match.group(2).lower()
    if u.isdigit():
        u = int(u)
    else:
        u = wrap_users.get(u, None)

    await event.respond(bwb.wrap(message, target=u, enc=enc), reply_to=event.reply_to_msg_id)


@register(NewMessage())
async def hs(event):
    text = bwb.parse(event.raw_text)
    handshake_auth = False

    if text.startswith('000000'):
        pass
    elif bwb.check_auth(text, handshake=True):
        handshake_auth = True
    elif bwb.check_auth(text):
        auth = True
    else:
        return

    if ' ' in text:
        command, data = text[6:].split()
    else:
        command, data = text[6:], None

    if command == 'init' and data:
        await event.respond('000000handshake ' + bwb.handshake(data))
    elif command == 'handshake' and data:
        await event.respond(bwb.wrap('secret ' + bwb.secret(data), handshake=True))
    elif handshake_auth and command == 'secret' and data:
        bwb.set_secret(data)
        await event.respond(bwb.wrap('🤝'))
    elif auth:
        command = command.lower()
        if command == '🤝':
            await asyncio.sleep(1)
            await event.respond('🤝')
        elif command == 'ping':
            await event.reply('Pong!')
    elif auth and command == 'system':
            
            sysd = await event.respond('Doing some Magic Right now')
            await asyncio.sleep(2)
            try:
                neo = "neofetch --stdout"
                fetch = await asyncrunapp(
                    neo,
                    stdout=asyncPIPE,
                    stderr=asyncPIPE,
                )

                stdout, stderr = await fetch.communicate()
                result = str(stdout.decode().strip()) \
                    + str(stderr.decode().strip())

                await sysd.edit("`" + result + "`")
            except FileNotFoundError:
                await sysd.edit("`I fucked up installing neofetch`")
    elif auth and command == 'ping':
            await event.reply('Gurr!')