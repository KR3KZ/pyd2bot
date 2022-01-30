from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AlignmentRankUpdateMessage(NetworkMessage):
    protocolId = 7764
    alignmentRank:int
    verbose:bool
    
