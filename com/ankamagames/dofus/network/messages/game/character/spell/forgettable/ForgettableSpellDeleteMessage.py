from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ForgettableSpellDeleteMessage(INetworkMessage):
    protocolId = 9143
    reason:int
    spells:int
    
    
