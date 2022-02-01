from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SetEnablePVPRequestMessage(INetworkMessage):
    protocolId = 4228
    enable:bool
    
    
