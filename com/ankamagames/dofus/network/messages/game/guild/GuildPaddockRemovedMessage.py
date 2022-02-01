from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildPaddockRemovedMessage(INetworkMessage):
    protocolId = 9960
    paddockId:int
    
    
