from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildModificationStartedMessage(INetworkMessage):
    protocolId = 310
    canChangeName:bool
    canChangeEmblem:bool
    
    
