from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IdolSelectErrorMessage(INetworkMessage):
    protocolId = 4378
    reason:int
    idolId:int
    activate:bool
    party:bool
    
    
