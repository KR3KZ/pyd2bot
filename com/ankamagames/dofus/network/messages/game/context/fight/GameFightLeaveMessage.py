from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightLeaveMessage(INetworkMessage):
    protocolId = 4663
    charId:int
    
    
