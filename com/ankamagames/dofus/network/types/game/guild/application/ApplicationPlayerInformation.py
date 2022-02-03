from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class ApplicationPlayerInformation(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    accountId:int
    accountTag:str
    accountNickname:str
    status:'PlayerStatus'
    

    def init(self, playerId:int, playerName:str, breed:int, sex:bool, level:int, accountId:int, accountTag:str, accountNickname:str, status:'PlayerStatus'):
        self.playerId = playerId
        self.playerName = playerName
        self.breed = breed
        self.sex = sex
        self.level = level
        self.accountId = accountId
        self.accountTag = accountTag
        self.accountNickname = accountNickname
        self.status = status
        
        super().__init__()
    
    