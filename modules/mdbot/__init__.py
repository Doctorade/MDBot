from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.model import Group, Member

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

from . import MDBot

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def setu(app: Ariadne, group: Group, member: Member, message: MessageChain):
    order = str(message)
    qq = str(member.id)
    if len(order) >= 3:
        if order[0:3] == '/md':
            await app.sendMessage(
                group,
                MessageChain(MDBot.mdbot(str(qq), order)),
            )
