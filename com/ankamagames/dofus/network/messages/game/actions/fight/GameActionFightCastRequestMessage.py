from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightCastRequestMessage(NetworkMessage):
    spellId:int
    cellId:int
    
    
