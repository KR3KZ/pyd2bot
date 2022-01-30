from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class RecycleResultMessage(INetworkMessage):
    protocolId = 2853
    nuggetsForPrism:int
    nuggetsForPlayer:int
    
    
