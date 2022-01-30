from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ArenaRanking(NetworkMessage):
    protocolId = 6311
    rank:int
    bestRank:int
    
    
