from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildVersatileInformations(INetworkMessage):
    protocolId = 4170
    guildId:int
    leaderId:int
    guildLevel:int
    nbMembers:int
    
    
