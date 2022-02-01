from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameActionFightNoSpellCastMessage(INetworkMessage):
    protocolId = 8111
    spellLevelId:int
    
    
