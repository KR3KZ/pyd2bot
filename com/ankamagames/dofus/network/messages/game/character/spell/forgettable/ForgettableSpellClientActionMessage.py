from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellClientActionMessage(NetworkMessage):
    spellId:int
    action:int
    
    
