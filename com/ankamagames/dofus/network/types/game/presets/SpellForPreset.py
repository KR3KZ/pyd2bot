from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellForPreset(NetworkMessage):
    spellId:int
    shortcuts:list[int]
    
    
