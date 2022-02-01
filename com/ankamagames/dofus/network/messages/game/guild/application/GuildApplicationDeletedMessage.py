from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildApplicationDeletedMessage(INetworkMessage):
    protocolId = 5546
    deleted:bool
    
    
