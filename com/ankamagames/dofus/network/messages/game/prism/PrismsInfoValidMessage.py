from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation


class PrismsInfoValidMessage(NetworkMessage):
    fights:list[PrismFightersInformation]
    
    
