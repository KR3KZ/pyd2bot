from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class WarnOnPermaDeathMessage(INetworkMessage):
    protocolId = 9760
    enable:bool
    
    
