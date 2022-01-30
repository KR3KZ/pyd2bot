from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountInformationInPaddockRequestMessage(NetworkMessage):
    protocolId = 6636
    mapRideId:int
    
    
