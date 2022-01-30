from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonPartyFinderRegisterSuccessMessage(INetworkMessage):
    protocolId = 2385
    dungeonIds:int
    
    
