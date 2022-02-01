from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagDailyLoteryMessage(INetworkMessage):
    protocolId = 2198
    returnType:int
    gameActionId:str
    
    
