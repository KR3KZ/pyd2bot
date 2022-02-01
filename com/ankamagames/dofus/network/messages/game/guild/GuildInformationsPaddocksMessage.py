from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


class GuildInformationsPaddocksMessage(INetworkMessage):
    protocolId = 178
    nbPaddockMax:int
    paddocksInformations:PaddockContentInformations
    
    
