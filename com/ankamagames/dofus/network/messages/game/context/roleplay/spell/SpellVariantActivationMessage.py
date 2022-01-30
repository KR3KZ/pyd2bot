from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SpellVariantActivationMessage(INetworkMessage):
    protocolId = 8666
    spellId:int
    result:bool
    
    
