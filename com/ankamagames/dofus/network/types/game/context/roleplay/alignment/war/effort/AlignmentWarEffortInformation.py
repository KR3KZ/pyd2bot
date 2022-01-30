from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AlignmentWarEffortInformation(INetworkMessage):
    protocolId = 3356
    alignmentSide:int
    alignmentWarEffort:int
    
    
