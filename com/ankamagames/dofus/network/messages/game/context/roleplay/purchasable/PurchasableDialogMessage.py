from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    protocolId = 582
    purchasableId:int
    purchasableInstanceId:int
    price:int
    
