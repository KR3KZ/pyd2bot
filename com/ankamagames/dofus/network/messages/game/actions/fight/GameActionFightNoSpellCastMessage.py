from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameActionFightNoSpellCastMessage(INetworkMessage):
    protocolId = 8111
    spellLevelId:int
    
    
