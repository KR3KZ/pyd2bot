from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SpellVariantActivationRequestMessage(NetworkMessage):
    protocolId = 4887
    spellId:int
    
    
