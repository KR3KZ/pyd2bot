from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonKeyRingUpdateMessage(INetworkMessage):
    protocolId = 2874
    dungeonId:int
    available:bool
    
    
