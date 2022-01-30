from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusUpdateRequestMessage(NetworkMessage):
    protocolId = 1504
    status:PlayerStatus
    
    
