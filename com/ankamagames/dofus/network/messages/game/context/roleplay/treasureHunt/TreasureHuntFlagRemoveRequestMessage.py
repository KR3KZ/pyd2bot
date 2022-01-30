from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntFlagRemoveRequestMessage(INetworkMessage):
    protocolId = 6823
    questType:int
    index:int
    
    
