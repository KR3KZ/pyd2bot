from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagPermissionsUpdateRequestMessage(INetworkMessage):
    protocolId = 2106
    permissions:int
    
    
