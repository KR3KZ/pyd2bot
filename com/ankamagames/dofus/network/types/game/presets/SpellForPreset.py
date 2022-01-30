from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SpellForPreset(NetworkMessage):
    protocolId = 7500
    spellId:int
    shortcuts:int
    
    
