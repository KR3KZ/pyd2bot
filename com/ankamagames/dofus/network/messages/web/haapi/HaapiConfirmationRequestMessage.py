from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationRequestMessage(NetworkMessage):
    protocolId = 5599
    kamas:int
    ogrines:int
    rate:int
    action:int
    
