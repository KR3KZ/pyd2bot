from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShowCellRequestMessage(NetworkMessage):
    protocolId = 4305
    cellId:int
    
    
