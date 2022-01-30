from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusUpdateMessage(INetworkMessage):
    protocolId = 120
    accountId:int
    playerId:int
    status:PlayerStatus
    
    
