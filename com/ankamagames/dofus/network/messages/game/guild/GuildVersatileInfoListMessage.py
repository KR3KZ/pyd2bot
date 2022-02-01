from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations


class GuildVersatileInfoListMessage(NetworkMessage):
    guilds:list[GuildVersatileInformations]
    
    
