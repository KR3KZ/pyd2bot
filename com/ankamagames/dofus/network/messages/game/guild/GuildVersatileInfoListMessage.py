from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations


class GuildVersatileInfoListMessage(NetworkMessage):
    protocolId = 211
    guilds:GuildVersatileInformations
    
