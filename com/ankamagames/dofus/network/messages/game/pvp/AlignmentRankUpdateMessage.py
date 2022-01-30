from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AlignmentRankUpdateMessage(INetworkMessage):
    protocolId = 7764
    alignmentRank:int
    verbose:bool
    
    
