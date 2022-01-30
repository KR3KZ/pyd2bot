from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightEffectTriggerCount(NetworkMessage):
    protocolId = 3026
    effectId:int
    targetId:int
    count:int
    
    
