from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlaySpellAnimMessage(INetworkMessage):
    protocolId = 8430
    casterId:int
    targetCellId:int
    spellId:int
    spellLevel:int
    
    
