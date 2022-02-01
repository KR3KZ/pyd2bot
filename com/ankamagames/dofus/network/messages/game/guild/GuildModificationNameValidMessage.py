from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildModificationNameValidMessage(INetworkMessage):
    protocolId = 5982
    guildName:str
    
    
