from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiValidationMessage(NetworkMessage):
    protocolId = 8710
    action:int
    code:int
    
    
