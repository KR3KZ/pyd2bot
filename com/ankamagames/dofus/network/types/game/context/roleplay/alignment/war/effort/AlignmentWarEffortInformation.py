from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortInformation(NetworkMessage):
    protocolId = 3356
    alignmentSide:int
    alignmentWarEffort:int
    
    
