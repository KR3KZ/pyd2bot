from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayDelayedActionFinishedMessage(INetworkMessage):
    protocolId = 6062
    delayedCharacterId:int
    delayTypeId:int
    
    
