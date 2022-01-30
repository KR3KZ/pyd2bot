from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class ApplicationPlayerInformation(NetworkMessage):
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
    
    
