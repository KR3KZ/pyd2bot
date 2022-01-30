from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockSellBuyDialogMessage(INetworkMessage):
    protocolId = 7880
    bsell:bool
    ownerId:int
    price:int
    
    
