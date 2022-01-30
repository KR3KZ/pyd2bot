from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class PartyIdol(Idol):
    protocolId = 563
    ownersIds:list[float]
    
