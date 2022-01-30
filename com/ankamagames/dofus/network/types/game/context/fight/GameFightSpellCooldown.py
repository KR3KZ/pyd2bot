from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightSpellCooldown(NetworkMessage):
    protocolId = 5389
    spellId:int
    cooldown:int
    
