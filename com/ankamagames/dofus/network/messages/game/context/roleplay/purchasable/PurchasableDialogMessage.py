from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    protocolId = 582
    purchasableId:float
    purchasableInstanceId:int
    price:float
    
