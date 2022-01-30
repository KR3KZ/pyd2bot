from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChangeHavenBagRoomRequestMessage(NetworkMessage):
    protocolId = 7038
    roomId:int
    
    
