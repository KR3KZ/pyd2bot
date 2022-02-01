from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class ApplicationPlayerInformation(INetworkMessage):
    protocolId = 3872
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    accountId:int
    accountTag:str
    accountNickname:str
    status:PlayerStatus
    
    
