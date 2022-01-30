from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightExternalInformations import FightExternalInformations


class MapRunningFightListMessage(NetworkMessage):
    protocolId = 1018
    fights:list[FightExternalInformations]
    
