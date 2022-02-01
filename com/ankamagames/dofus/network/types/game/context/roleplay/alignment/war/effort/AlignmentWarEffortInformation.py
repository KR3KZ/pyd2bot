from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AlignmentWarEffortInformation(INetworkMessage):
    protocolId = 3356
    alignmentSide:int
    alignmentWarEffort:int
    
    
