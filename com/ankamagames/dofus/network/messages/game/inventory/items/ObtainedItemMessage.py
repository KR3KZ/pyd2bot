from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObtainedItemMessage(INetworkMessage):
    protocolId = 4201
    genericId:int
    baseQuantity:int
    
    
