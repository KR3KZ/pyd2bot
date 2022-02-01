from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


class GuildInformationsPaddocksMessage(NetworkMessage):
    nbPaddockMax:int
    paddocksInformations:list[PaddockContentInformations]
    
    
