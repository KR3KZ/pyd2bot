from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SpellForPreset(INetworkMessage):
    protocolId = 7500
    spellId:int
    shortcuts:int
    
    
