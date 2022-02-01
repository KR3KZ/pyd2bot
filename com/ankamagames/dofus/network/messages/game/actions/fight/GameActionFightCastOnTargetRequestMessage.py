from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightCastOnTargetRequestMessage(NetworkMessage):
    spellId:int
    targetId:int
    
    
