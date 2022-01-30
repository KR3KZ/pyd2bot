from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationMessage(NetworkMessage):
    protocolId = 5733
    kamas:float
    amount:float
    rate:int
    action:int
    transaction:str
    
