from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightSpellCooldown(NetworkMessage):
    spellId:int
    cooldown:int
    
    
