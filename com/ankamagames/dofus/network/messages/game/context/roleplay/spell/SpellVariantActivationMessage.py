from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SpellVariantActivationMessage(NetworkMessage):
    protocolId = 8666
    spellId:int
    result:bool
    
