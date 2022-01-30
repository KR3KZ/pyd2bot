from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AtlasPointsInformations import AtlasPointsInformations


class AtlasPointInformationsMessage(INetworkMessage):
    protocolId = 6676
    type:AtlasPointsInformations
    
    
