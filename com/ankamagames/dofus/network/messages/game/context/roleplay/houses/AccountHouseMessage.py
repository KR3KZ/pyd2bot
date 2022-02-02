from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.AccountHouseInformations import AccountHouseInformations


@dataclass
class AccountHouseMessage(NetworkMessage):
    houses:list[AccountHouseInformations]
    
    
    def __post_init__(self):
        super().__init__()
    