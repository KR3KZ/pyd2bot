from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildVersatileInformations(INetworkMessage):
    protocolId = 4170
    guildId:int
    leaderId:int
    guildLevel:int
    nbMembers:int
    
    
