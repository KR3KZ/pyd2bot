from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlaySpellAnimMessage(NetworkMessage):
    protocolId = 8430
    casterId:float
    targetCellId:int
    spellId:int
    spellLevel:int
    
