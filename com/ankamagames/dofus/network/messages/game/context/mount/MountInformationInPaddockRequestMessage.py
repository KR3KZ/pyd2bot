from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountInformationInPaddockRequestMessage(INetworkMessage):
    protocolId = 6636
    mapRideId:int
    
    
