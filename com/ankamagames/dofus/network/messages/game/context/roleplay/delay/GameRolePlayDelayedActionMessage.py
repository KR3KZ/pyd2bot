from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayDelayedActionMessage(INetworkMessage):
    protocolId = 1161
    delayedCharacterId:int
    delayTypeId:int
    delayEndTime:int
    
    
