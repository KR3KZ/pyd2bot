from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntGiveUpRequestMessage(NetworkMessage):
    protocolId = 2962
    questType:int
    
    
