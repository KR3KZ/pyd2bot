from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportHavenBagRequestMessage(NetworkMessage):
    protocolId = 5838
    guestId:int
    
    
