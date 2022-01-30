from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntFinishedMessage(INetworkMessage):
    protocolId = 5016
    questType:int
    
    
