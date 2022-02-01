from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation


class PrismsInfoValidMessage(INetworkMessage):
    protocolId = 9294
    fights:PrismFightersInformation
    
    
