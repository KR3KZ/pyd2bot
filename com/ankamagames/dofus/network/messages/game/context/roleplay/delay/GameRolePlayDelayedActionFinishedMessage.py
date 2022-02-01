from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionFinishedMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    
    
