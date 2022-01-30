from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceVersatileInformations import AllianceVersatileInformations


class AllianceVersatileInfoListMessage(NetworkMessage):
    protocolId = 9853
    alliances:list[AllianceVersatileInformations]
    
