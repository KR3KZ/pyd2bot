from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockSellBuyDialogMessage(NetworkMessage):
    protocolId = 7880
    bsell:bool
    ownerId:int
    price:int
    
    
