from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class GameFightStartMessage(INetworkMessage):
    protocolId = 5357
    idols:Idol
    
    