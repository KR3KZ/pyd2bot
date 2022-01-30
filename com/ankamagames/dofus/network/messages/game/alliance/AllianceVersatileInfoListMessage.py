from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceVersatileInformations import AllianceVersatileInformations


class AllianceVersatileInfoListMessage(INetworkMessage):
    protocolId = 9853
    alliances:AllianceVersatileInformations
    
    
