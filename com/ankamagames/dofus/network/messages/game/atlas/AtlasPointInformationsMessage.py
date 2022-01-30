from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AtlasPointsInformations import AtlasPointsInformations


class AtlasPointInformationsMessage(NetworkMessage):
    protocolId = 6676
    type:AtlasPointsInformations
    
