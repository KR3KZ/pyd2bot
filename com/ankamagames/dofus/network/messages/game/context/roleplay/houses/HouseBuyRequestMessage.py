from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseBuyRequestMessage(INetworkMessage):
    protocolId = 4286
    proposedPrice:int
    
    
