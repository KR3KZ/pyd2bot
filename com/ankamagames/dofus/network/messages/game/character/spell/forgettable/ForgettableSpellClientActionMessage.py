from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ForgettableSpellClientActionMessage(INetworkMessage):
    protocolId = 6523
    spellId:int
    action:int
    
    
