from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildSpellUpgradeRequestMessage(INetworkMessage):
    protocolId = 8207
    spellId:int
    
    
