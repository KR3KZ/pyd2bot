from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SpellVariantActivationRequestMessage(INetworkMessage):
    protocolId = 4887
    spellId:int
    
    
