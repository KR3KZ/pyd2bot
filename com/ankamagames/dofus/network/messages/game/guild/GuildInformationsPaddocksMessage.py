from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


class GuildInformationsPaddocksMessage(NetworkMessage):
    protocolId = 178
    nbPaddockMax:int
    paddocksInformations:PaddockContentInformations
    
