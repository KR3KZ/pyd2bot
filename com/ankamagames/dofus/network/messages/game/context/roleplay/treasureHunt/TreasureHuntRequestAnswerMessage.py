from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntRequestAnswerMessage(INetworkMessage):
    protocolId = 1019
    questType:int
    result:int
    
    
