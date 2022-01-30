from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagPermissionsUpdateRequestMessage(NetworkMessage):
    protocolId = 2106
    permissions:int
    
    
