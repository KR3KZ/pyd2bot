from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class OrnamentLostMessage(INetworkMessage):
    protocolId = 94
    ornamentId:int
    
    
