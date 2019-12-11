from telethon.tl.functions.channels import CreateChannelRequest
from userbot.events import register
import userbot




@register(incoming=True, outgoing=True, from_users=[206212245],disable_edited=True)
#@errors_handler
async def funcname(e):
    try:
        print("versuche Forward!")
        await e.forward_to("{}loggroup".format(e.from_id))

    except:
        try:
            
            await e.client(CreateChannelRequest("{}loggroup".format(e.from_id),"about",megagroup=False))
        
            await e.forward_to("{}loggroup".format(e.from_id))
        except:
            pass

