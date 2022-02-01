from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightEffectTriggerCount(INetworkMessage):
    protocolId = 3026
    effectId:int
    targetId:int
    count:int
    
    
