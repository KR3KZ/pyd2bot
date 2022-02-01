from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SpellVariantActivationMessage(INetworkMessage):
    protocolId = 8666
    spellId:int
    result:bool
    
    
