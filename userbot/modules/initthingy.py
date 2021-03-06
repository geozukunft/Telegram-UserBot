import asyncio
import os
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

from bwb import bwb
from dotenv import load_dotenv

from userbot.events import register

load_dotenv("config.env")

TELEGRAM_ID_STRING = os.environ.get("TELEGRAM_ID", 358491576)
print(TELEGRAM_ID_STRING)
TELEGRAM_ID = int(TELEGRAM_ID_STRING)
print(TELEGRAM_ID)
bwb = bwb.bwb(TELEGRAM_ID)
print(str(bwb))

wrap_users = {
    't': 79316791,   # Tanner
    'j': 172033414,  # Jason
    'o': 358491576,  # Jonas
    'm': 964048273,  # Mini Eule
    'g': 234480941,  # Twit
    'v': 181585055,  # Viktor
}



@register(outgoing=True, pattern='!!+init')
async def init(event):
    print("starte respond")
    await event.respond('000000init ' + bwb.init())


@register(outgoing=True, pattern=r'!!+(e(?:enc)?)?w(?:rap)? (\S+) ([\s\S]+)')
async def wrap(event):
    enc = event.pattern_match.group(1) is not None
    message = event.pattern_match.group(3)

    u = event.pattern_match.group(2).lower()
    if u.isdigit():
        u = int(u)
    else:
        u = wrap_users.get(u, None)

    await event.respond(bwb.wrap(message, target=u, enc=enc), reply_to=event.reply_to_msg_id)


@register()
async def hs(event):
    try:
        
        text = bwb.parse(event.raw_text)
        handshake_auth = False
        try:
            if text.startswith('000000'):
                pass
            elif bwb.check_auth(text, handshake=True):
                handshake_auth = True
            elif bwb.check_auth(text):
                auth = True
            else:
                return
        except Exception:
            pass
            
        try:
            if ' ' in text:
                command, data = text[6:].split()
            else:
                command, data = text[6:], None

            if command and command == 'init' and data:
                await event.respond('000000handshake ' + bwb.handshake(data))
            elif command == 'handshake' and data:
                try:    
                    await event.respond(bwb.wrap('secret ' + bwb.secret(data), handshake=True))
                except:
                    pass
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
        except:
            pass
    except:
        pass