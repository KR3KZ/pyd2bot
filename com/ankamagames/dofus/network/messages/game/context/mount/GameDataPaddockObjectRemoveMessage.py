from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameDataPaddockObjectRemoveMessage(NetworkMessage):
    protocolId = 7808
    cellId:int
    
