from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusUpdateRequestMessage(INetworkMessage):
    protocolId = 1504
    status:PlayerStatus
    
    
