from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagDailyLoteryMessage(NetworkMessage):
    protocolId = 2198
    returnType:int
    gameActionId:str
    
    
