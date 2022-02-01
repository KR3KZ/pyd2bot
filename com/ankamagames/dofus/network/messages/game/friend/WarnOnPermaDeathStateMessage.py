from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class WarnOnPermaDeathStateMessage(INetworkMessage):
    protocolId = 8629
    enable:bool
    
    
