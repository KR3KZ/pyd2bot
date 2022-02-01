from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameContextReadyMessage(INetworkMessage):
    protocolId = 912
    mapId:int
    
    
