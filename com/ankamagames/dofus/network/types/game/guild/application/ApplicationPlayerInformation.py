from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
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
    status:PlayerStatus
    
    
