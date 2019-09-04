from telethon.tl.functions.channels import CreateChannelRequest
from userbot.events import register, errors_handler






@register(incoming=True, from_users=206212245)
#@errors_handler
async def funcname(e):
    try:
        await e.forward_to("{}loggroup".format(e.from_id))
    except:
        createdPrivateChannel = await e.client(CreateChannelRequest("{}loggroup".format(e.from_id),"about",megagroup=False))
        await e.forward_to("{}loggroup".format(e.from_id))

@register(incoming=True, from_users=697983746)
#@errors_handler
async def funcname(e):
    try:
        await e.forward_to("{}loggroup".format(e.from_id))
    except:
        createdPrivateChannel = await e.client(CreateChannelRequest("{}loggroup".format(e.from_id),"about",megagroup=False))
        await e.forward_to("{}loggroup".format(e.from_id))
