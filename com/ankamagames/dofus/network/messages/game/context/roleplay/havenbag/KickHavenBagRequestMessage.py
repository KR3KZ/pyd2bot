from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class KickHavenBagRequestMessage(NetworkMessage):
    protocolId = 188
    guestId:int
    
