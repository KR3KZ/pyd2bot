from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ArenaRanking(INetworkMessage):
    protocolId = 6311
    rank:int
    bestRank:int
    
    
