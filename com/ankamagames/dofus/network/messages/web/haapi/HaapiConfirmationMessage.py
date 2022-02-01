from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiConfirmationMessage(NetworkMessage):
    kamas:int
    amount:int
    rate:int
    action:int
    transaction:str
    
    
