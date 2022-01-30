from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class GameContextActorInformations(GameContextActorPositionInformations):
    protocolId = 801
    look:EntityLook
    
    
