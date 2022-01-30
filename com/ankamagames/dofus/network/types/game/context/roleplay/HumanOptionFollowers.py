from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from com.ankamagames.dofus.network.types.game.look.IndexedEntityLook import IndexedEntityLook


class HumanOptionFollowers(HumanOption):
    protocolId = 77
    followingCharactersLook:IndexedEntityLook
    
