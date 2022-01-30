from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameFightEntityInformation(GameFightFighterInformations):
    protocolId = 5544
    entityModelId:int
    level:int
    masterId:int
    
