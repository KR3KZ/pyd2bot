from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightExternalInformations import FightExternalInformations


class MapRunningFightListMessage(INetworkMessage):
    protocolId = 1018
    fights:FightExternalInformations
    
    
