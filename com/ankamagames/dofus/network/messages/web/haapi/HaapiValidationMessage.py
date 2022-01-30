from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiValidationMessage(INetworkMessage):
    protocolId = 8710
    action:int
    code:int
    
    
