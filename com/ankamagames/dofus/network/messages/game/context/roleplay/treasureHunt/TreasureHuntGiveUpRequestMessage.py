from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntGiveUpRequestMessage(INetworkMessage):
    protocolId = 2962
    questType:int
    
    
