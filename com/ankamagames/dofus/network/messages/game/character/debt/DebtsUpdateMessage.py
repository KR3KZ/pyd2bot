from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation


class DebtsUpdateMessage(INetworkMessage):
    protocolId = 2524
    action:int
    debts:DebtInformation
    
    
