from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class OrnamentSelectedMessage(INetworkMessage):
    protocolId = 7637
    ornamentId:int
    
    
