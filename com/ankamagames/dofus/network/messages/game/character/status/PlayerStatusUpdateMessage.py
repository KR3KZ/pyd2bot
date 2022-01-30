from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusUpdateMessage(NetworkMessage):
    protocolId = 120
    accountId:int
    playerId:int
    status:PlayerStatus
    
    
