from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AlignmentRankUpdateMessage(INetworkMessage):
    protocolId = 7764
    alignmentRank:int
    verbose:bool
    
    
