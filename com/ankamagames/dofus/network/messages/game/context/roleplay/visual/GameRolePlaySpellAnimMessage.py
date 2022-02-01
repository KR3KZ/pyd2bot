from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlaySpellAnimMessage(NetworkMessage):
    casterId:int
    targetCellId:int
    spellId:int
    spellLevel:int
    
    
