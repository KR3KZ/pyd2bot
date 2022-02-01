from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceVersatileInformations import AllianceVersatileInformations


class AllianceVersatileInfoListMessage(NetworkMessage):
    alliances:list[AllianceVersatileInformations]
    
    
