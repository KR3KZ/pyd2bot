from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagPermissionsUpdateRequestMessage(INetworkMessage):
    protocolId = 2106
    permissions:int
    
    
