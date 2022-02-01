from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NumericWhoIsMessage(INetworkMessage):
    protocolId = 7592
    playerId:int
    accountId:int
    
    
