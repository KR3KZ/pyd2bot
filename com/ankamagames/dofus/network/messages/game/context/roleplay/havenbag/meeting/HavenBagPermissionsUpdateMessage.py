from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagPermissionsUpdateMessage(INetworkMessage):
    protocolId = 3186
    permissions:int
    
    
