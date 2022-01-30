from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation


class DebtsUpdateMessage(NetworkMessage):
    protocolId = 2524
    action:int
    debts:DebtInformation
    
    
