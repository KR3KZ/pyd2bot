from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


class GuildPaddockBoughtMessage(NetworkMessage):
    protocolId = 6217
    paddockInfo:PaddockContentInformations
    
