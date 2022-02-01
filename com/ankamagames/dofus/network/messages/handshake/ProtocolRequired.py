from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ProtocolRequired(INetworkMessage):
    protocolId = 5716
    version:str
    
    
