from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ContactLookErrorMessage(INetworkMessage):
    protocolId = 9873
    requestId:int
    
    
