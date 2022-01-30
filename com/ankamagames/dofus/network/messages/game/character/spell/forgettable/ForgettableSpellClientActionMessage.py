from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellClientActionMessage(NetworkMessage):
    protocolId = 6523
    spellId:int
    action:int
    
    
