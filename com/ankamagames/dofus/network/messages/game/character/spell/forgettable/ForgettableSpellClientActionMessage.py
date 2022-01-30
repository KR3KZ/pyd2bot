from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ForgettableSpellClientActionMessage(INetworkMessage):
    protocolId = 6523
    spellId:int
    action:int
    
    
