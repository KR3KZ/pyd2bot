from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.AccountHouseInformations import AccountHouseInformations
    


class AccountHouseMessage(NetworkMessage):
    houses:list['AccountHouseInformations']
    

    def init(self, houses:list['AccountHouseInformations']):
        self.houses = houses
        
        super().__init__()
    
    