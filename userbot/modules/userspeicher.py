from telethon.tl.functions.channels import CreateChannelRequest
from userbot.events import register
import userbot



from_list = [206212245, 697983746, 358491576]


@register(incoming=True, from_users=from_list)
#@errors_handler
async def funcname(e):
    try:
        print("versuche Forward!")
        await e.forward_to("{}loggroup".format(e.from_id))

    except:
        createdPrivateChannel = await e.client(CreateChannelRequest("{}loggroup".format(e.from_id),"about",megagroup=False))
        await e.forward_to("{}loggroup".format(e.from_id))


