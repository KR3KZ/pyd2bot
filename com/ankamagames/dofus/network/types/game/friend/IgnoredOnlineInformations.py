from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IgnoredOnlineInformations(IgnoredInformations):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    

    def init(self, playerId:int, playerName:str, breed:int, sex:bool, accountId:int, accountTag:'AccountTagInformation'):
        self.playerId = playerId
        self.playerName = playerName
        self.breed = breed
        self.sex = sex
        
        super().__init__(accountId, accountTag)
    
    