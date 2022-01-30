from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationRequestMessage(NetworkMessage):
    protocolId = 5599
    kamas:float
    ogrines:float
    rate:int
    action:int
    
