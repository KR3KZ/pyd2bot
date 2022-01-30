from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildSpellUpgradeRequestMessage(NetworkMessage):
    protocolId = 8207
    spellId:int
    
