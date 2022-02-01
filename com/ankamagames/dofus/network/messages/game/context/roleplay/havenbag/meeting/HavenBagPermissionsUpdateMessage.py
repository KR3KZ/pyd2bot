from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagPermissionsUpdateMessage(INetworkMessage):
    protocolId = 3186
    permissions:int
    
    
