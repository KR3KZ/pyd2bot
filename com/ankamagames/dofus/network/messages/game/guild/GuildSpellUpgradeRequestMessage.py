from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildSpellUpgradeRequestMessage(INetworkMessage):
    protocolId = 8207
    spellId:int
    
    
