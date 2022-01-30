from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DisplayNumericalValuePaddockMessage(NetworkMessage):
    protocolId = 5348
    rideId:int
    value:int
    type:int
    
    
