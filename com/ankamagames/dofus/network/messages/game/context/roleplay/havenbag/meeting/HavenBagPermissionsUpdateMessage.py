from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagPermissionsUpdateMessage(NetworkMessage):
    protocolId = 3186
    permissions:int
    
    
