from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AcquaintanceOnlineInformation(AcquaintanceInformation):
    playerId:int
    playerName:str
    moodSmileyId:int
    status:'PlayerStatus'
    

    def init(self, playerId:int, playerName:str, moodSmileyId:int, status:'PlayerStatus', playerState:int, accountId:int, accountTag:'AccountTagInformation'):
        self.playerId = playerId
        self.playerName = playerName
        self.moodSmileyId = moodSmileyId
        self.status = status
        
        super().__init__(playerState, accountId, accountTag)
    
    