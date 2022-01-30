from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagDailyLoteryMessage(INetworkMessage):
    protocolId = 2198
    returnType:int
    gameActionId:str
    
    
