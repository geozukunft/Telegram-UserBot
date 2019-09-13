from telethon.tl.functions.channels import CreateChannelRequest
from userbot.events import register, errors_handler
import userbot






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


@register(outgoing=True)
#@errors_handler
async def funcname(e):

    ich = await e.client.get_me()
    ich_id  = ich.id
    if e.from_id == ich_id:
        try:
            await e.forward_to("{}loggroup".format(e.from_id))
        except:
            createdPrivateChannel = await e.client(CreateChannelRequest("{}loggroup".format(e.from_id),"about",megagroup=False))
            await e.forward_to("{}loggroup".format(e.from_id))

