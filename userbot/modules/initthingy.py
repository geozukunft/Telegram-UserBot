from userbot import CMD_HELP
from userbot.events import register








from bwb.common import common
class user(common):
 TELEGRAM_ID = 234480941
bwb = user()

from bot.events import register
import asyncio

@register(outgoing=True, pattern='!!+init')
async def init(z):
 await z.respond('000000init ' + bwb.init())

@register(outgoing=True, pattern='!!+(t|m|c) (.+)$')
async def jt(z):
 u = z.pattern_match.group(1).lower()
 if u == 't': u = 79316791
 elif u == 'm': u = 234480941
 else: u = None

 await z.respond(bwb.wrap(z.pattern_match.group(2), target=u), reply_to=z.reply_to_msg_id)

@register()
async def hs(z):
 text = bwb.parse(z.raw_text)
 hs_au = False
 if text.startswith('000000'):
  pass
 elif bwb.check_auth(text, handshake=True):
  hs_au = True
 elif bwb.check_auth(text):
  au = True
 else:
  return

 if ' ' in text:
  command, data = text[6:].split()
 else:
  command, data = text[6:], None

 if command == 'init' and data:
  await z.respond('000000handshake ' + bwb.handshake(data))
 elif command == 'handshake' and data:
  await z.respond(bwb.wrap('secret ' + bwb.secret(data), handshake=True))
 elif hs_au and command == 'secret' and data:
  bwb.set_secret(data)
  await z.respond(bwb.wrap('🤝'))
 elif au and command == '🤝':
  await asyncio.sleep(1)
  await z.respond('🤝') 