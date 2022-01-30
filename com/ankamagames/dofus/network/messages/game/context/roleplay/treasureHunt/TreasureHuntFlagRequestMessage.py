from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntFlagRequestMessage(INetworkMessage):
    protocolId = 9576
    questType:int
    index:int
    
    
