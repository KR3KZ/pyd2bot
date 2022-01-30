from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class RecycleResultMessage(NetworkMessage):
    protocolId = 2853
    nuggetsForPrism:int
    nuggetsForPlayer:int
    
    
