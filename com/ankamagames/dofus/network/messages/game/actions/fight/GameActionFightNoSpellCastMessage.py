from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameActionFightNoSpellCastMessage(NetworkMessage):
    protocolId = 8111
    spellLevelId:int
    
    
