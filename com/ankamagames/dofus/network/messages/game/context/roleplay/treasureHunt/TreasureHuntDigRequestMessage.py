from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntDigRequestMessage(INetworkMessage):
    protocolId = 6219
    questType:int
    
    
