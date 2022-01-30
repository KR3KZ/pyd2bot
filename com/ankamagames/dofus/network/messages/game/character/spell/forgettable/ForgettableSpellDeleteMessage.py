from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellDeleteMessage(NetworkMessage):
    protocolId = 9143
    reason:int
    spells:int
    
    
