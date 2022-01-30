from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildModificationNameValidMessage(INetworkMessage):
    protocolId = 5982
    guildName:str
    
    
