from userbot import CMD_HELP
from userbot.events import register
from bwb.common import common

import asyncio

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE


class user(common):
    TELEGRAM_ID = 358491576

bwb = user()


@register(outgoing=True, pattern='!!+init')
async def init(event):
    await event.respond('000000init ' + bwb.init())

@register(outgoing=True, pattern='!!+(t(?:anner)?|j(?:ason)?|o(?:wl)?|me?|c(?:ast)?) (.+)$')
async def cast(event):
    u = event.pattern_match.group(1)[0].lower()

    if u == 't': u = 79316791
    elif u == 'j': u = 172033414
    elif u == 'o': u = 358491576
    elif u == 'm': u = 234480941
    else: u = None

    await event.respond(bwb.wrap(event.pattern_match.group(2), target=u), reply_to=event.reply_to_msg_id)

@register()
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
    elif auth and command == '🤝':
        await asyncio.sleep(1)
        await event.respond('🤝') 
    elif auth and command == 'system':
        await asyncio.sleep(1)
        sysd = await event.respond('🤝') 
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
