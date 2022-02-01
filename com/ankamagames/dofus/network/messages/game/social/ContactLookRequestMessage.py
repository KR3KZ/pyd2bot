from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ContactLookRequestMessage(INetworkMessage):
    protocolId = 9165
    requestId:int
    contactType:int
    
    
