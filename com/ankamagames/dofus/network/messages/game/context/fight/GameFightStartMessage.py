from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class GameFightStartMessage(NetworkMessage):
    protocolId = 5357
    idols:Idol
    
