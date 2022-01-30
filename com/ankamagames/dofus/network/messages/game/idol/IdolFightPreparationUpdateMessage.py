from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class IdolFightPreparationUpdateMessage(INetworkMessage):
    protocolId = 7338
    idolSource:int
    idols:Idol
    
    
