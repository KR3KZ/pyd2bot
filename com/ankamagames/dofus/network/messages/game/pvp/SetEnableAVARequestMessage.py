from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SetEnableAVARequestMessage(INetworkMessage):
    protocolId = 3626
    enable:bool
    
    
