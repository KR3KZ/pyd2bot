from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class IdolFightPreparationUpdateMessage(NetworkMessage):
    protocolId = 7338
    idolSource:int
    idols:list[Idol]
    
