from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightEffectTriggerCount(NetworkMessage):
    effectId:int
    targetId:int
    count:int
    
    
