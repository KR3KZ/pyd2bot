from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightSpellCooldown(INetworkMessage):
    protocolId = 5389
    spellId:int
    cooldown:int
    
    
