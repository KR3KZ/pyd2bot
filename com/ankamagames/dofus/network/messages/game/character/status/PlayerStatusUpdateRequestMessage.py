from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusUpdateRequestMessage(NetworkMessage):
    status:PlayerStatus
    
    
