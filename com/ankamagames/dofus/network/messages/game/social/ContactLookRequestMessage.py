from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ContactLookRequestMessage(NetworkMessage):
    requestId:int
    contactType:int
    
    
