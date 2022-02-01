from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightExternalInformations import FightExternalInformations


class MapRunningFightListMessage(NetworkMessage):
    fights:list[FightExternalInformations]
    
    
