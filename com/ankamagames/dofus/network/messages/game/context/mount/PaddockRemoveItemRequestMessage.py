from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockRemoveItemRequestMessage(NetworkMessage):
    protocolId = 9863
    cellId:int
    
    
