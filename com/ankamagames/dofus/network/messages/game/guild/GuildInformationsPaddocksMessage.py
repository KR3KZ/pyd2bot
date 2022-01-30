from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


class GuildInformationsPaddocksMessage(INetworkMessage):
    protocolId = 178
    nbPaddockMax:int
    paddocksInformations:PaddockContentInformations
    
    
