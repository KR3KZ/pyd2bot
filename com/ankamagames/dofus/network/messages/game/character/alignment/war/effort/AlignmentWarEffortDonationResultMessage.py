from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AlignmentWarEffortDonationResultMessage(INetworkMessage):
    protocolId = 6010
    result:int
    
    
