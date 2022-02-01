from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellDeleteMessage(NetworkMessage):
    reason:int
    spells:list[int]
    
    
