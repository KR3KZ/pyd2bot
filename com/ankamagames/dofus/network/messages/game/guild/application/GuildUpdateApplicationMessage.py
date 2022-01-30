from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildUpdateApplicationMessage(INetworkMessage):
    protocolId = 6940
    applyText:str
    guildId:int
    
    
