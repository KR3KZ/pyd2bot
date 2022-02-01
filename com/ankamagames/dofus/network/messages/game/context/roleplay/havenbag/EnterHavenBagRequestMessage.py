from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EnterHavenBagRequestMessage(INetworkMessage):
    protocolId = 8214
    havenBagOwner:int
    
    
