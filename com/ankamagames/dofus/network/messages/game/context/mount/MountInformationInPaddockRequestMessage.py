from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountInformationInPaddockRequestMessage(INetworkMessage):
    protocolId = 6636
    mapRideId:int
    
    
