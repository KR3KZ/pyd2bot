from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DisplayNumericalValuePaddockMessage(INetworkMessage):
    protocolId = 5348
    rideId:int
    value:int
    type:int
    
    
