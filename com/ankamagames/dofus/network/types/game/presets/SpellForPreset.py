from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SpellForPreset(INetworkMessage):
    protocolId = 7500
    spellId:int
    shortcuts:int
    
    
