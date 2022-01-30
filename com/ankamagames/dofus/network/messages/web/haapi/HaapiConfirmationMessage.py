from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiConfirmationMessage(INetworkMessage):
    protocolId = 5733
    kamas:int
    amount:int
    rate:int
    action:int
    transaction:str
    
    
