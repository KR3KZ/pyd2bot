from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ForgettableSpellDeleteMessage(INetworkMessage):
    protocolId = 9143
    reason:int
    spells:int
    
    
