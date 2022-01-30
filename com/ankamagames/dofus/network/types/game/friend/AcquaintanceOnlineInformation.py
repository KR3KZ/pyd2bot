from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class AcquaintanceOnlineInformation(AcquaintanceInformation):
    protocolId = 4750
    playerId:int
    playerName:str
    moodSmileyId:int
    status:PlayerStatus
    
    
