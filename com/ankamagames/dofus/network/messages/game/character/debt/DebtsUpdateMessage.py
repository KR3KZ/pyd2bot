from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation


@dataclass
class DebtsUpdateMessage(NetworkMessage):
    action:int
    debts:list[DebtInformation]
    
    
    def __post_init__(self):
        super().__init__()
    