from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    delayEndTime:int
    
    
