from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonPartyFinderRegisterRequestMessage(INetworkMessage):
    protocolId = 2723
    dungeonIds:int
    
    
