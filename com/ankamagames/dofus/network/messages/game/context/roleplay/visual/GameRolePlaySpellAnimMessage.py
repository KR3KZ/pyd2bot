from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlaySpellAnimMessage(INetworkMessage):
    protocolId = 8430
    casterId:int
    targetCellId:int
    spellId:int
    spellLevel:int
    
    
