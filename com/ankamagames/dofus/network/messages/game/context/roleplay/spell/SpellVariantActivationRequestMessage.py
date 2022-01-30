from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SpellVariantActivationRequestMessage(INetworkMessage):
    protocolId = 4887
    spellId:int
    
    
