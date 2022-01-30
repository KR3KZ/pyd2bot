from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PurchasableDialogMessage(INetworkMessage):
    protocolId = 582
    purchasableId:int
    purchasableInstanceId:int
    price:int
    buyOrSell:bool
    secondHand:bool
    
    
